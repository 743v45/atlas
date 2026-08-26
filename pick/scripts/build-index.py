#!/usr/bin/env python3
"""聚合 items/ 下所有 meta.json，校验后生成全部 HTML（均为生成物，禁止手改）：

- index.html                       索引页（verdict 过滤 + 按 updated 排序）
- items/<类别>/<条目>/report.html   渲染 report.md，带面包屑与上下篇导航
- items/<类别>/comparison.html      渲染 comparison.md，<!--gen:activity-table--> 处
                                    自动注入从 meta.stats 生成的活跃度表

用法：python3 scripts/build-index.py
数据刷新：python3 scripts/refresh-stats.py（gh 一手数据 → meta.stats）

校验门禁（RULES.md 第 6 节）：
- 必填字段缺失：name / verdict / summary / updated / verified / sources
- sources 为空列表；verdict 不在枚举内；日期不是 YYYY-MM-DD
- 任何错误 → 打印全部问题并退出码 1
- 正文 ⭐ 数与 meta.stats.stars 不一致 → 仅警告（warn，观察期）
"""

import html
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEMS_DIR = ROOT / "items"
OUTPUT = ROOT / "index.html"

# verdict 枚举 → (中文显示, 判词单字, 状态色)。
# 色值取自 dataviz 参考色板的 status palette（语义：good/warning/neutral/critical），
# 判词章 = 色环 + 单字——文字承载识别，色环只是强调，永不只靠颜色传义。
VERDICTS = {
    "adopt": ("推荐", "荐", "#0ca30c"),
    "trial": ("试用", "试", "#fab219"),
    "assess": ("评估", "评", "#898781"),
    "hold": ("观望", "观", "#d03b3b"),
}
GAN = "甲乙丙丁戊己庚辛壬癸"  # 类别档案编号：天干（第 11 类起退回数字）
REQUIRED_FIELDS = ["name", "verdict", "summary", "updated", "verified", "sources"]
STALE_DAYS = 180  # 数据采集/核实超过此天数 → 标「待复核」

# ============================================================
# 引擎共享层(上提至 atlas/shared/render.py;第三馆触发抽取,见 apprentice/scripts/ORIGIN.md)
# ============================================================
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("render", Path(__file__).resolve().parent.parent.parent / "shared" / "render.py")
_render = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_render)
render_inline = _render.render_inline
render_markdown = _render.render_markdown
BASE_CSS = _render.BASE_CSS
# ============================================================
# 数据收集与校验
# ============================================================

def parse_date(value, where, errors):
    """严格解析 YYYY-MM-DD，失败则记入 errors 返回 None。"""
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        errors.append(f"{where}: 日期 {value!r} 不是 YYYY-MM-DD")
        return None


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_tool(meta, where):
    """校验单个工具 meta，返回 (errors, warnings)。"""
    errors, warnings = [], []
    for field in REQUIRED_FIELDS:
        if not meta.get(field):
            errors.append(f"{where}: 必填字段 {field} 缺失或为空")
    if meta.get("verdict") and meta.get("verdict") not in VERDICTS:
        errors.append(f"{where}: verdict {meta['verdict']!r} 不在 {sorted(VERDICTS)} 内")
    if meta.get("sources") is not None and not isinstance(meta.get("sources"), list):
        errors.append(f"{where}: sources 必须是数组")
    for f_name in ("updated", "verified"):
        if meta.get(f_name):
            parse_date(meta[f_name], f"{where} {f_name}", errors)
    stats = meta.get("stats")
    if stats is not None:
        if not isinstance(stats, dict):
            errors.append(f"{where}: stats 必须是对象")
        elif stats.get("collected_at"):
            parse_date(stats["collected_at"], f"{where} stats.collected_at", errors)
    return errors, warnings


def stale_base_date(meta):
    """时效基准日：优先 stats.collected_at（数据采集），否则 verified（人工核实）。"""
    stats = meta.get("stats") or {}
    base = stats.get("collected_at") or meta.get("verified")
    if not base:
        return None
    try:
        return datetime.strptime(base, "%Y-%m-%d").date()
    except ValueError:
        return None


def load_decision(cat_dir, errors):
    """加载类别决策矩阵 decision.json（可选），结构见 RULES.md 第 5 节。"""
    dec_path = cat_dir / "decision.json"
    if not dec_path.exists():
        return {}
    try:
        return load_json(dec_path)
    except json.JSONDecodeError as e:
        errors.append(f"{dec_path.relative_to(ROOT)}: JSON 解析失败 {e}")
        return {}


def check_decision_tree(cat, warnings):
    """类别设计树叶子校验（RULES.md 第 7 节）：树上 verdict 与 meta 一致、条目全部入树。"""
    tree_path = cat["dir"] / "decision-tree.md"
    if not tree_path.exists():
        warnings.append(f"类别 {cat['slug']}: 缺少 decision-tree.md（设计树，RULES.md 第 7 节）")
        return
    txt = tree_path.read_text(encoding="utf-8")
    txt = re.sub(r"`[^`]+`", "", txt)  # 剥掉行内代码 span（格式说明示例不是真叶子）
    leaves = re.findall(r"\[([^\]]+)\]\(([^/)]+)/\)\s*`?(\w+)`?", txt)
    meta_map = {t["dir"].name: t["meta"]["verdict"] for t in cat["tools"]}
    for name, slug, verdict in leaves:
        if slug not in meta_map:
            warnings.append(f"{cat['slug']}/decision-tree.md: 叶子 {slug} 不存在于条目")
        elif meta_map[slug] != verdict:
            warnings.append(
                f"{cat['slug']}/decision-tree.md: {slug} 树上 {verdict} ≠ meta {meta_map[slug]}，请同步（RULES 第 7 节）"
            )
    tree_slugs = {s for _, s, _ in leaves}
    for slug in meta_map:
        if slug not in tree_slugs:
            warnings.append(f"{cat['slug']}/decision-tree.md: 条目 {slug} 未入树，请补叶子")


def check_star_consistency(meta, md_text, where, warnings):
    """正文 ⭐ 数与 meta.stats.stars 一致性（warn 不 fail）。"""
    stats = meta.get("stats") or {}
    stars = stats.get("stars")
    if stars is None:
        return
    found = set(re.findall(r"⭐\s*([\d,]+)", md_text))
    if found and f"{stars:,}" not in found:
        warnings.append(f"{where}: 正文 star {sorted(found)} 与 meta.stats.stars={stars:,} 不一致，请同步")


def collect():
    """扫描 items/<类别>/<条目>/，返回 (categories, errors, warnings)。"""
    categories, errors, warnings = [], [], []
    if not ITEMS_DIR.is_dir():
        return categories, errors, warnings

    for cat_dir in sorted(p for p in ITEMS_DIR.iterdir() if p.is_dir()):
        cat_meta_path = cat_dir / "_meta.json"
        cat_meta = {}
        if cat_meta_path.exists():
            try:
                cat_meta = load_json(cat_meta_path)
            except json.JSONDecodeError as e:
                errors.append(f"{cat_meta_path.relative_to(ROOT)}: JSON 解析失败 {e}")
        else:
            warnings.append(f"类别 {cat_dir.name}/ 缺少 _meta.json（用目录名兜底显示）")

        tools = []
        for tool_dir in sorted(p for p in cat_dir.iterdir() if p.is_dir()):
            meta_path = tool_dir / "meta.json"
            where = tool_dir.relative_to(ROOT).as_posix()
            if not meta_path.exists():
                warnings.append(f"{where}: 缺少 meta.json（未写入索引）")
                continue
            if not (tool_dir / "report.md").exists():
                warnings.append(f"{where}: 缺少 report.md")
            try:
                meta = load_json(meta_path)
            except json.JSONDecodeError as e:
                errors.append(f"{where}: JSON 解析失败 {e}")
                continue
            tool_errors, _ = validate_tool(meta, where)
            errors.extend(tool_errors)
            if tool_errors:
                continue  # 校验不过的工具不进索引

            report_md = ""
            report_path = tool_dir / "report.md"
            if report_path.exists():
                report_md = report_path.read_text(encoding="utf-8")
                check_star_consistency(meta, report_md, where, warnings)

            base = stale_base_date(meta)
            tools.append({
                "dir": tool_dir,
                "meta": meta,
                "report_md": report_md,
                "stale": base is not None and (date.today() - base).days > STALE_DAYS,
            })

        categories.append({
            "slug": cat_dir.name,
            "dir": cat_dir,
            "name": cat_meta.get("name", cat_dir.name),
            "description": cat_meta.get("description", ""),
            "order": cat_meta.get("order", 999),
            "columns": cat_meta.get("columns", []),
            "decision": load_decision(cat_dir, errors),
            "comparison": (cat_dir / "comparison.md").exists(),
            "tools": tools,
        })

    categories.sort(key=lambda c: (c["order"], c["name"]))
    return categories, errors, warnings


# ============================================================
# 活跃度表生成（从 meta.stats，注入 comparison 的占位标记处）
# ============================================================

def gen_activity_md(cat):
    """类别内所有带 stats 的工具 → markdown 活跃度表（star 降序）。"""
    rows = []
    collected = set()
    for t in cat["tools"]:
        st = t["meta"].get("stats") or {}
        if not st.get("stars") and not st.get("pushed_at"):
            continue
        slug = t["dir"].name
        name = t["meta"]["name"]
        stars = st.get("stars")
        stars_txt = f"⭐{stars:,}" if isinstance(stars, int) else "—"
        repo = st.get("source_repo", "")
        repo_md = f"[{repo}](https://github.com/{repo})" if repo else "—"
        rows.append((stars if isinstance(stars, int) else -1,
                     f"| [{name}]({slug}/report.md) | {repo_md} | {stars_txt} | {st.get('pushed_at', '—')} | {st.get('license', '—')} |"))
        if st.get("collected_at"):
            collected.add(st["collected_at"])
    rows.sort(key=lambda r: -r[0])
    lines = ["| 项目 | 仓库 | star | 最后 push | license |", "|---|---|---|---|---|"]
    lines += [r[1] for r in rows]
    note = ""
    if collected:
        note = f"\n\n*star / push 为 gh 一手快照，采集 {', '.join(sorted(collected))}；无 stats 的项（商业闭源等）不列。*"
    return "\n".join(lines) + note


# ============================================================
# 页面渲染（共享样式，file:// 零依赖）
# ============================================================


INDEX_CSS = """
  .masthead { display: flex; align-items: baseline; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem; }
  .masthead .sub { color: var(--muted); font-size: .92rem; }
  .masthead .figures { margin-left: auto; font-family: var(--font-mono); font-size: .8rem; color: var(--muted); }
  #filter {
    width: 100%; padding: .5rem .8rem; margin-bottom: .6rem; font-size: .95rem; font-family: var(--font-body);
    border: 1px solid var(--border); border-radius: 8px; background: var(--card); color: var(--text);
  }
  .chips { display: flex; gap: .4rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
  .chip {
    padding: .1rem .7rem; border-radius: 999px; border: 1px solid var(--border);
    background: var(--card); color: var(--muted); cursor: pointer; font-size: .8rem; font-family: var(--font-body);
  }
  .chip.active { color: var(--chip-c); border-color: var(--chip-c); font-weight: 600; }
  .category { margin-bottom: 2.1rem; animation: drawer .4s ease both; }
  .category:nth-child(1) { animation-delay: .02s } .category:nth-child(2) { animation-delay: .07s }
  .category:nth-child(3) { animation-delay: .12s } .category:nth-child(4) { animation-delay: .17s }
  @keyframes drawer { from { opacity: 0; transform: translateY(7px) } to { opacity: 1; transform: none } }
  @media (prefers-reduced-motion: reduce) { .category { animation: none } }
  .category h2 { font-size: 1.32rem; margin: 0 0 .5rem; display: flex; align-items: center; gap: .65rem; }
  .gan {
    display: inline-flex; align-items: center; justify-content: center;
    width: 1.75em; height: 1.75em; border: 1.5px solid var(--text); border-radius: 5px;
    font-size: .82em; font-family: var(--font-display); line-height: 1; flex-shrink: 0;
  }
  .cmp { font-size: .8rem; font-weight: normal; margin-left: auto; font-family: var(--font-body); }
  .idx-table { display: table; table-layout: fixed; }
  .idx-table th {
    font-size: .73rem; color: var(--muted); font-weight: 500; text-align: left; font-family: var(--font-body);
    cursor: pointer; user-select: none; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .idx-table th:focus-visible { outline-offset: -2px; }
  .idx-table th.sorted-asc::after { content: " ↑"; color: var(--link); }
  .idx-table th.sorted-desc::after { content: " ↓"; color: var(--link); }
  .idx-table td { border-bottom: 1px solid var(--border); font-size: .82rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .idx-table td:first-child { width: 7.5rem; }
  .idx-table td.num, .idx-table th.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; font-family: var(--font-mono); font-size: .78rem; }
  .idx-table td.mx { color: var(--muted); }
  .idx-table td.warn { color: var(--accent); }
  .idx-table tbody tr:hover td { background: color-mix(in srgb, var(--link) 5%, transparent); }
  .idx-table .tool-name { font-weight: 600; }
  .push-stale { color: var(--danger); }
  .collected-note { color: var(--muted); font-size: .75rem; margin-top: .3rem; font-family: var(--font-mono); }
  .empty { text-align: center; color: var(--muted); padding: 4rem 0; }
  /* 域列表（顶层索引）与域页 */
  .domain {
    margin-bottom: 1.3rem; padding: 1rem 1.2rem; background: var(--card);
    border: 1px solid var(--border); border-radius: 12px;
  }
  .domain h2 { margin: 0 0 .35rem; display: flex; align-items: center; gap: .65rem; font-size: 1.3rem; }
  .domain h2 a { color: inherit; text-decoration: none; }
  .domain h2 a:hover { color: var(--link); }
  .domain .figures { margin-left: auto; font-family: var(--font-mono); font-size: .78rem; color: var(--muted); font-weight: 400; }
  .domain-desc { margin: .1rem 0 .7rem; color: var(--muted); font-size: .9rem; font-family: var(--font-body); }
  .cat-chips { display: flex; gap: .5rem; flex-wrap: wrap; }
  .cat-chip {
    display: inline-flex; align-items: baseline; gap: .4rem; padding: .18rem .8rem;
    border: 1px solid var(--border); border-radius: 999px; background: var(--bg);
    text-decoration: none; color: var(--text); font-size: .85rem; font-family: var(--font-body);
  }
  .cat-chip:hover { border-color: var(--link); color: var(--link); }
  .cat-chip span { color: var(--muted); font-family: var(--font-mono); font-size: .72rem; }
  .cat-count { font-size: .74rem; color: var(--muted); font-weight: 400; font-family: var(--font-mono); }
  .kingdom-name {
    font-size: 1.05rem; color: var(--muted); font-weight: 600; margin: 1.6rem 0 .6rem;
    border-bottom: 1px dashed var(--border); padding-bottom: .3rem;
  }
  .omni-wrap { position: relative; margin-bottom: 1.4rem; }
  #omni {
    width: 100%; padding: .55rem .9rem; font-size: .98rem; font-family: var(--font-body);
    border: 1px solid var(--border); border-radius: 9px; background: var(--card); color: var(--text);
  }
  .omni-results {
    position: absolute; top: calc(100% + 4px); left: 0; right: 0; z-index: 10;
    background: var(--card); border: 1px solid var(--border); border-radius: 9px;
    box-shadow: 0 6px 20px rgba(0,0,0,.10); overflow: hidden;
  }
  .omni-results a, .omni-none {
    display: flex; align-items: baseline; gap: .6rem; padding: .45rem .9rem;
    text-decoration: none; color: var(--text); font-size: .88rem; font-family: var(--font-body);
  }
  .omni-results a:hover { background: color-mix(in srgb, var(--link) 6%, transparent); }
  .omni-results b { font-weight: 600; }
  .omni-v { font-size: .74rem; color: var(--muted); }
  .omni-d { margin-left: auto; font-size: .76rem; color: var(--muted); font-family: var(--font-mono); }
  @media (max-width: 720px) {
    body { padding: 1rem .7rem 2.5rem; }
    .category { overflow-x: auto; }
    .category h2 { font-size: 1.12rem; }
    .masthead .figures { display: none; }
    .idx-table { min-width: 640px; }
  }
"""

REPORT_CSS = """
  .report-nav {
    display: flex; gap: .9rem; flex-wrap: wrap; align-items: center;
    font-size: .84rem; color: var(--muted); margin-bottom: 1rem; font-family: var(--font-body);
  }
  .report-nav .sep { color: var(--border); }
  article {
    background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 1.25rem 1.45rem; position: relative;
  }
  article > .seal-big { position: absolute; top: 1rem; right: 1.2rem; }
"""





def badge(verdict):
    """判词章（小）：索引宽表用——色环描边 + 单字，title 带全称。"""
    label, seal, color = VERDICTS[verdict]
    return f'<span class="seal" style="--vb:{color}" title="{label}"><i></i>{seal}</span>'


def seal_big(verdict):
    """判词章（大）：报告页 TL;DR 处盖章——色环 + 单字 + 微旋转。"""
    label, seal, color = VERDICTS[verdict]
    return f'<span class="seal seal-big" style="--vb:{color}" title="{label}"><i></i>{seal}</span>'


def fmt_star(n):
    """star 缩写：1,234 → 1.2k。"""
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def fmt_push(d):
    """同年省年份（08-26），跨年全显（2025-07-05）。"""
    if not d:
        return "—"
    return d[5:] if d[:4] == str(date.today().year) else d


def render_row(tool, columns, base_prefix=""):
    """渲染单个工具行（索引宽表：工具 | 结论 | <类别维度列> | star | push）。

    所有插值都经 html.escape；⚠ 结尾的维度值（如 AGPL 传染提醒）琥珀色高亮。
    """
    m, stale = tool["meta"], tool["stale"]
    rel = tool["dir"].relative_to(ROOT).as_posix()
    stats = m.get("stats") or {}
    # base_prefix：域页（domains/*.html）需要 ../ 回根；条目链接必须带前缀，否则解析成 /domains/items/…（404）
    matrix = m.get("matrix") or {}
    stars = stats.get("stars")
    stars_txt = fmt_star(stars) if isinstance(stars, int) else "—"
    pushed = stats.get("pushed_at", "")
    push_old = False
    if pushed:
        try:
            push_old = (date.today() - datetime.strptime(pushed, "%Y-%m-%d").date()).days > STALE_DAYS
        except ValueError:
            pass
    push_cls = ' class="num push-stale"' if push_old else ' class="num"'
    push_html = f'<td{push_cls}>{html.escape(fmt_push(pushed))}</td>'

    matrix_tds = []
    for col in columns:
        val = matrix.get(col, "—")
        cls = ' class="mx warn"' if "⚠" in val else ' class="mx"'
        matrix_tds.append(f'<td{cls}>{html.escape(val)}</td>')

    tags = " ".join(m.get("tags", []))
    return f"""      <tr data-verdict="{m['verdict']}" data-stars="{stars if isinstance(stars, int) else -1}"
          data-push="{pushed}" data-name="{html.escape(m['name'])}"
          data-search="{html.escape(' '.join([m['name'], m['summary'], tags]).lower())}">
        <td class="tool-name"><a href="{base_prefix}{html.escape(rel)}/report.html" title="{html.escape(m['summary'])}">{html.escape(m['name'])}</a></td>
        <td>{badge(m['verdict'])}</td>
        {''.join(matrix_tds)}
        <td class="num">{stars_txt}</td>
        {push_html}
      </tr>"""


def render_category_sections(cats, base_prefix=""):
    """渲染若干类别的宽表 section（域页复用）。base_prefix 为域内相对路径前缀（items/ 或空）。"""
    sections = []
    for c in cats:
        cmp_html = ""
        if c["comparison"]:
            cmp_html = f'<a class="cmp" href="{base_prefix}items/{html.escape(c["slug"])}/comparison.html">横评 →</a>'
        rows = "\n".join(render_row(t, c["columns"], base_prefix=base_prefix) for t in c["tools"]) or f'<tr><td colspan="{2 + len(c["columns"]) + 2}" class="sum">该类别暂无条目报告。</td></tr>'
        collected = sorted({(t["meta"].get("stats") or {}).get("collected_at") for t in c["tools"]} - {None})
        note = f'<p class="collected-note">star / push 为 gh 快照，采集 {", ".join(collected)}；红色 push 表示停滞超 {STALE_DAYS} 天；条目名悬停看一句话结论。</p>' if collected else ""
        dim_ths = "".join(f'<th>{html.escape(col)}</th>' for col in c["columns"])
        sections.append(f"""  <section class="category" id="{c['slug']}" data-search="{html.escape(c['name'].lower())}">
    <h2>{html.escape(c['name'])} <span class="cat-count">{len(c['tools'])} 条</span> {cmp_html}</h2>
    <table class="idx-table">
      <thead><tr>
        <th data-sort="name" tabindex="0">条目</th><th data-sort="verdict" tabindex="0">结论</th>
        {dim_ths}
        <th data-sort="stars" class="num" tabindex="0">star</th><th data-sort="push" class="num" tabindex="0">push</th>
      </tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
    {note}
  </section>""")
    return "\n".join(sections)


TABLE_JS = """
  // 文本过滤 + verdict chips + 表头排序（类别内，点击切换升降序）
  const VERDICT_ORDER = %(verdict_order)s;
  const input = document.getElementById('filter');
  let verdictF = 'all';
  const chips = [...document.querySelectorAll('.chip')];

  function applyFilter() {
    document.querySelectorAll('.category').forEach(sec => {
      let visible = 0;
      sec.querySelectorAll('tbody tr').forEach(tr => {
        const q = input.value.trim().toLowerCase();
        const hitText = !q || tr.dataset.search.includes(q) || sec.dataset.search.includes(q);
        const hitVerdict = verdictF === 'all' || tr.dataset.verdict === verdictF;
        const hit = hitText && hitVerdict;
        tr.classList.toggle('hidden', !hit);
        if (hit) visible++;
      });
      sec.classList.toggle('hidden', visible === 0);
    });
  }
  input.addEventListener('input', applyFilter);
  chips.forEach(ch => ch.addEventListener('click', () => {
    chips.forEach(c => c.classList.remove('active'));
    ch.classList.add('active');
    verdictF = ch.dataset.verdict;
    applyFilter();
  }));

  document.querySelectorAll('.idx-table th[data-sort]').forEach(th => {
    th.addEventListener('click', () => {
      const table = th.closest('table');
      const tbody = table.querySelector('tbody');
      const key = th.dataset.sort;
      const asc = !th.classList.contains('sorted-asc');
      table.querySelectorAll('th').forEach(t => t.classList.remove('sorted-asc', 'sorted-desc'));
      th.classList.add(asc ? 'sorted-asc' : 'sorted-desc');
      [...tbody.querySelectorAll('tr')].sort((a, b) => {
        let va = a.dataset[key], vb = b.dataset[key];
        if (key === 'stars') return (Number(va) - Number(vb)) * (asc ? 1 : -1);
        if (key === 'verdict') return ((VERDICT_ORDER[va] ?? 9) - (VERDICT_ORDER[vb] ?? 9)) * (asc ? 1 : -1);
        if (key === 'push') return String(va).localeCompare(String(vb)) * (asc ? 1 : -1);
        return va.localeCompare(vb, 'zh') * (asc ? 1 : -1);
      }).forEach(tr => tbody.appendChild(tr));
    });
  });
""" % {"verdict_order": json.dumps({k: i for i, k in enumerate(VERDICTS)})}


def render_domain_list(categories, domains):
    """顶层索引：域列表（短页）；声明了 kingdoms 时按界分组；含全站搜索。"""
    total = sum(len(c["tools"]) for c in categories)
    today = date.today().isoformat()
    kingdoms = []
    seen_k = set()
    for d in domains:
        k = d.get("kingdom")
        if k and k["slug"] not in seen_k:
            seen_k.add(k["slug"])
            kingdoms.append(k)

    def domain_card(d):
        gan = ""
        di = [i for i, x in enumerate(domains) if x["slug"] == d["slug"]][0]
        gan = GAN[di] if di < len(GAN) else str(di + 1)
        cats = [c for c in categories if c["slug"] in d.get("categories", [])]
        n_items = sum(len(c["tools"]) for c in cats)
        cat_chips = "".join(
            f'<a class="cat-chip" href="domains/{d["slug"]}.html#{c["slug"]}">{html.escape(c["name"])}<span>{len(c["tools"])}</span></a>'
            for c in cats
        )
        return f"""    <section class="domain">
    <h2><span class="gan" aria-hidden="true">{gan}</span><a href="domains/{d['slug']}.html">{html.escape(d['name'])}</a><span class="figures">{len(cats)} 类 · {n_items} 条</span></h2>
    <p class="domain-desc">{html.escape(d['description'])}</p>
    <div class="cat-chips">{cat_chips}</div>
  </section>"""

    if kingdoms:
        groups = []
        unkingdomed = [d for d in domains if not d.get("kingdom")]
        for k in kingdoms:
            cards = "".join(domain_card(d) for d in domains if d.get("kingdom") and d["kingdom"]["slug"] == k["slug"])
            groups.append(f"""  <section class="kingdom" id="k-{k['slug']}">
    <h2 class="kingdom-name">{html.escape(k['name'])}</h2>
{cards}
  </section>""")
        if unkingdomed:
            groups.append("".join(domain_card(d) for d in unkingdomed))
        body = "\n".join(groups)
    else:
        body = "\n".join(domain_card(d) for d in domains)

    # 全站搜索索引（条目级轻量数据，膨胀到千条也仅几十 KB）
    search_idx = []
    for d in domains:
        for c in categories:
            if c["slug"] in d.get("categories", []):
                for t in c["tools"]:
                    search_idx.append({
                        "n": t["meta"]["name"],
                        "v": t["meta"]["verdict"],
                        "d": f"{d['name']} / {c['name']}",
                        "h": f"items/{c['slug']}/{t['dir'].name}/report.html",
                    })

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>pick · 选型对比索引</title>
<style>{BASE_CSS}{INDEX_CSS}</style>
</head>
<body>
<main>
  <div class="masthead">
    <h1>pick</h1>
    <span class="sub">选型对比决策库 · <a href="RULES.md">RULES.md</a></span>
    <span class="figures">{len(kingdoms) and f"{len(kingdoms)} 界 · " or ""}{len(domains)} 域 · {len(categories)} 类 · {total} 条</span>
  </div>
  <div class="omni-wrap">
    <input id="omni" type="search" placeholder="全站搜索：条目 / 类别 / 域…" autocomplete="off" aria-label="全站搜索">
    <div id="omni-results" class="omni-results hidden"></div>
  </div>
{body}
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物，禁止手改</footer>
</main>
<script>
  const IDX = {json.dumps(search_idx, ensure_ascii=False)};
  const LABEL = {json.dumps({k: v[0] for k, v in VERDICTS.items()}, ensure_ascii=False)};
  const omni = document.getElementById('omni');
  const box = document.getElementById('omni-results');
  omni.addEventListener('input', () => {{
    const q = omni.value.trim().toLowerCase();
    if (!q) {{ box.classList.add('hidden'); box.innerHTML = ''; return; }}
    const hits = IDX.filter(x => x.n.toLowerCase().includes(q) || x.d.toLowerCase().includes(q)).slice(0, 12);
    box.innerHTML = hits.length
      ? hits.map(x => `<a href="${{x.h}}"><b>${{x.n}}</b><span class="omni-v">${{LABEL[x.v] || ''}}</span><span class="omni-d">${{x.d}}</span></a>`).join('')
      : '<span class="omni-none">无匹配</span>';
    box.classList.remove('hidden');
  }});
  omni.addEventListener('keydown', e => {{
    if (e.key === 'Escape') {{ omni.value = ''; box.classList.add('hidden'); }}
    if (e.key === 'Enter') {{ const first = box.querySelector('a'); if (first) location.href = first.getAttribute('href'); }}
  }});
  document.addEventListener('click', e => {{
    if (!e.target.closest('.omni-wrap')) {{ box.classList.add('hidden'); }}
  }});
</script>
</body>
</html>
"""


def render_domain_page(d, cats, today):
    """域聚合页：域内各类别宽表 + 过滤/排序。"""
    chips = "".join(
        f'<button class="chip" data-verdict="{key}" style="--chip-c:{color}">{label}</button>'
        for key, (label, _seal, color) in VERDICTS.items()
    )
    n_items = sum(len(c["tools"]) for c in cats)
    body = f"""  <nav class="report-nav"><a href="../index.html">← 索引</a><span class="sep">·</span><span>{html.escape(d['name'])}</span><span class="sep">·</span><span>{len(cats)} 类 {n_items} 条</span></nav>
  <div class="masthead">
    <h1>{html.escape(d['name'])}</h1>
    <span class="sub">{html.escape(d['description'])}</span>
  </div>
  <input id="filter" type="search" placeholder="按名称 / 结论 / 标签过滤…" autocomplete="off">
  <div class="chips">
    <button class="chip active" data-verdict="all">全部</button>
    {chips}
  </div>
{render_category_sections(cats, base_prefix="../")}
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物，禁止手改</footer>"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(d['name'])} · pick</title>
<style>{BASE_CSS}{INDEX_CSS}</style>
</head>
<body>
<main>
{body}
</main>
<script>{TABLE_JS}</script>
</body>
</html>
"""


def gen_decision_md(cat):
    """类别决策矩阵（加权）：维度权重 ×1–5 评分 → 加权总分，降序。

    决策矩阵只覆盖所列维度；维度外的风险（如维护断层史）以各条目 verdict 为准——
    这条注记必须随表输出，避免「矩阵满分但 verdict 谨慎」被误读为矛盾。
    """
    dec = cat.get("decision") or {}
    weights = dec.get("weights") or {}
    scores = dec.get("scores") or {}
    if not weights or not scores:
        return "（本类别暂无决策矩阵，可在类别目录新建 decision.json，见 RULES.md 第 5 节。）"
    dims = list(weights)
    max_total = sum(weights.values()) * 5
    entries = []
    for t in cat["tools"]:
        slug = t["dir"].name
        s = scores.get(slug)
        if not s:
            continue
        total = sum(weights[d] * s.get(d, 0) for d in dims)
        entries.append((total, slug, t["meta"]["name"], s))
    entries.sort(key=lambda e: (-e[0], e[2]))
    header = "| 条目 | " + " | ".join(f"{d}（w={weights[d]}）" for d in dims) + " | 加权总分 |"
    sep = "|---" * (len(dims) + 2) + "|"
    rows = [
        f"| [{name}]({slug}/report.md) | " + " | ".join(str(s.get(d, "—")) for d in dims) + f" | **{total}** / {max_total} |"
        for total, slug, name, s in entries
    ]
    updated = dec.get("updated", "—")
    note = (
        f"\n\n*权重与评分均为 1–5；评于 {updated}；评分依据见各条目报告。"
        f"决策矩阵只覆盖所列维度，维度外的风险（如维护断层史）以各条目 verdict 为准。*"
    )
    return "\n".join([header, sep] + rows) + note


def _page(title, css, body_html, today):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{BASE_CSS}{css}</style>
</head>
<body>
<main>
{body_html}
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物，禁止手改 · 源文件见同目录 .md</footer>
</main>
</body>
</html>
"""


def render_report_page(cat, tool, prev, nxt, today, domain=None):
    """渲染单个工具的 report.html（面包屑 + 上下篇 + 正文）。"""
    m = tool["meta"]
    nav = [f'<a href="../../../index.html">← 索引</a>']
    if domain:
        nav.append(f'<a href="../../../domains/{domain["slug"]}.html">{html.escape(domain["name"])}</a>')
    nav.append(f'<span>{html.escape(cat["name"])}</span>')
    if cat["comparison"]:
        nav.append('<a href="../comparison.html">类别横评</a>')
    if prev:
        nav.append(f'<a href="../{prev["dir"].name}/report.html">← {html.escape(prev["meta"]["name"])}</a>')
    if nxt:
        nav.append(f'<a href="../{nxt["dir"].name}/report.html">{html.escape(nxt["meta"]["name"])} →</a>')
    nav_html = '<span class="sep">·</span>'.join(nav)
    body = f"""  <nav class="report-nav">{nav_html}</nav>
  <article>
  {seal_big(m['verdict'])}
{render_markdown(tool['report_md'])}
  </article>"""
    return _page(f"{m['name']} · pick", REPORT_CSS, body, today)


def render_comparison_page(cat, today, domain=None):
    """渲染类别横评 comparison.html，占位标记处注入 meta 生成的活跃度表。"""
    md = (cat["dir"] / "comparison.md").read_text(encoding="utf-8")
    md = md.replace("<!--gen:activity-table-->", gen_activity_md(cat))
    md = md.replace("<!--gen:decision-matrix-->", gen_decision_md(cat))
    nav = [f'<a href="../../index.html">← 索引</a>']
    if domain:
        nav.append(f'<a href="../../domains/{domain["slug"]}.html">{html.escape(domain["name"])}</a>')
    nav.append(f'<span>{html.escape(cat["name"])} · 横评</span>')
    nav_html = '<span class="sep">·</span>'.join(nav)
    body = f"""  <nav class="report-nav">{nav_html}</nav>
  <article>
{render_markdown(md)}
  </article>"""
    return _page(f"{cat['name']} 横评 · pick", REPORT_CSS, body, today)


# ============================================================
# 主流程
# ============================================================

def load_domains(categories, errors):
    """加载根级 domains.json（域聚合层），校验：类别全覆盖、无未知类别。"""
    path = ROOT / "domains.json"
    if not path.exists():
        return []
    try:
        raw = load_json(path)
    except json.JSONDecodeError as e:
        errors.append(f"domains.json: JSON 解析失败 {e}")
        return []
    domains = raw.get("domains", [])
    kingdoms = raw.get("kingdoms", [])
    known = {c["slug"] for c in categories}
    covered = set()
    for d in domains:
        for slug in d.get("categories", []):
            if slug not in known:
                errors.append(f"domains.json: 域 {d.get('slug')} 引用了未知类别 {slug}")
            covered.add(slug)
    for slug in sorted(known - covered):
        errors.append(f"domains.json: 类别 {slug} 未归属任何域（请补进某个 domain 的 categories）")
    # 界（kingdoms）：声明后所有域必须归属且仅归一个界
    k_of_domain = {}
    for k in kingdoms:
        for dslug in k.get("domains", []):
            if dslug not in {d["slug"] for d in domains}:
                errors.append(f"domains.json: 界 {k.get('slug')} 引用了未知域 {dslug}")
            elif dslug in k_of_domain:
                errors.append(f"domains.json: 域 {dslug} 归属了多个界")
            else:
                k_of_domain[dslug] = k
    for d in domains:
        if kingdoms and d["slug"] not in k_of_domain:
            errors.append(f"domains.json: 已声明界但域 {d['slug']} 未归属任何界")
    for d in domains:
        d["kingdom"] = k_of_domain.get(d["slug"])
    return domains


def main():
    categories, errors, warnings = collect()
    for cat in categories:
        check_decision_tree(cat, warnings)
    domains = load_domains(categories, errors)
    cat_domain = {slug: d for d in domains for slug in d.get("categories", [])}
    # 膨胀预警门禁（RULES.md 第 1 节分层判据）
    for c in categories:
        if len(c["tools"]) > 30:
            warnings.append(f"类别 {c['slug']} 已 {len(c['tools'])} 条（>30）：建议横向拆分（并系拆分）而非加深")
    if len(domains) > 9:
        warnings.append(f"已有 {len(domains)} 个域（>9）：建议在 domains.json 声明 kingdoms 启用界分组")

    for w in warnings:
        print(f"⚠️  {w}")
    if errors:
        print("\n❌ 校验未通过，索引未更新：")
        for e in errors:
            print(f"   {e}")
        print("\n参见 RULES.md 第 2、6 节。")
        sys.exit(1)

    today = date.today().isoformat()
    generated = 0

    # 1) 各工具 report.html（面包屑带域层）
    for cat in categories:
        domain = cat_domain.get(cat["slug"])
        for idx, tool in enumerate(cat["tools"]):
            prev = cat["tools"][idx - 1] if idx > 0 else None
            nxt = cat["tools"][idx + 1] if idx + 1 < len(cat["tools"]) else None
            page = render_report_page(cat, tool, prev, nxt, today, domain=domain)
            (tool["dir"] / "report.html").write_text(page, encoding="utf-8")
            generated += 1

    # 2) 各类别 comparison.html
    for cat in categories:
        if cat["comparison"]:
            page = render_comparison_page(cat, today, domain=cat_domain.get(cat["slug"]))
            (cat["dir"] / "comparison.html").write_text(page, encoding="utf-8")
            generated += 1

    # 3) 域聚合页
    domains_dir = ROOT / "domains"
    domains_dir.mkdir(exist_ok=True)
    for d in domains:
        cats = [c for c in categories if c["slug"] in d.get("categories", [])]
        (domains_dir / f"{d['slug']}.html").write_text(render_domain_page(d, cats, today), encoding="utf-8")
        generated += 1

    # 4) 顶层索引（域列表）
    OUTPUT.write_text(render_domain_list(categories, domains), encoding="utf-8")
    generated += 1

    total = sum(len(c["tools"]) for c in categories)
    print(f"✅ 已生成 {generated} 个页面（索引 + {len(domains)} 域页 + {total} 份报告 + 横评），共 {len(domains)} 域 / {len(categories)} 类 / {total} 条")


if __name__ == "__main__":
    main()
