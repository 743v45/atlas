#!/usr/bin/env python3
"""聚合 items/ 下所有错题的 meta.json,校验后生成全部 HTML(均为生成物,禁止手改):

- index.html                    错题集主页:错题索引(状态过滤 + 类型搜索 + 表头排序)
                                + 跨馆警示两区(落选/腐烂,直读邻馆 meta,见 A11)
- items/<错题>/mistake.html      渲染 mistake.md,带面包屑与上下篇导航

校验门禁(RULES.md 第 4 节):
- 必填字段缺失:name / date / source / tags / status
- status 不在枚举内;日期不是 YYYY-MM-DD;tags 必须非空数组
- mistake.md 缺「## 经过」「## 根因」「## 修正」任一小节 → 不进索引(没有根因的错题不算错题)
- related 路径不存在 → 不许指向不存在的关联
- 任何错误 → 打印全部问题并退出码 1
"""

import html
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ATLAS = ROOT.parent  # atlas 根:跨馆警示区直读邻馆 meta——是源文件非生成物,无构建顺序耦合(A11)
ITEMS_DIR = ROOT / "items"
OUTPUT = ROOT / "index.html"
STALE_DAYS = 180  # 与 pick/apprentice 两馆一致

# ============================================================
# 引擎共享层(atlas/shared/render.py)
# ============================================================
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("render", Path(__file__).resolve().parent.parent.parent / "shared" / "render.py")
_render = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_render)
render_inline = _render.render_inline
render_markdown = _render.render_markdown
BASE_CSS = _render.BASE_CSS

# status 枚举 → (中文显示, 判词单字, 状态色)。
# recurring 是本馆最高警示:同一根因又犯——翻车不可怕,翻得毫无新意才可怕。
STATUS = {
    "fixed": ("已修正", "修", "#0ca30c"),
    "recurring": ("复发", "犯", "#d03b3b"),
}
REQUIRED_FIELDS = ["name", "date", "source", "tags", "status"]
REQUIRED_SECTIONS = ("## 经过", "## 根因", "## 修正")

# ============================================================
# 数据收集与校验
# ============================================================

def parse_date(value, where, errors):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        errors.append(f"{where}: 日期 {value!r} 不是 YYYY-MM-DD")
        return None


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_mistake(meta, where):
    errors = []
    for field in REQUIRED_FIELDS:
        if not meta.get(field):
            errors.append(f"{where}: 必填字段 {field} 缺失或为空")
    if meta.get("status") and meta.get("status") not in STATUS:
        errors.append(f"{where}: status {meta['status']!r} 不在 {sorted(STATUS)} 内")
    tags = meta.get("tags")
    if tags is not None and (not isinstance(tags, list) or not tags):
        errors.append(f"{where}: tags 必须是非空数组")
    if meta.get("date"):
        parse_date(meta["date"], f"{where} date", errors)
    rel = meta.get("related")
    if rel is not None:
        if not isinstance(rel, list):
            errors.append(f"{where}: related 必须是数组")
        else:
            for r in rel:
                p = Path(r)
                if not p.is_absolute():
                    p = ROOT / p
                if not p.exists():
                    errors.append(f"{where}: related 路径不存在:{r}(不许指向不存在的关联)")
    return errors


def check_sections(md_text, where, errors):
    for sec in REQUIRED_SECTIONS:
        if sec not in md_text:
            errors.append(f"{where}: mistake.md 缺「{sec}」小节(没有根因的错题不算错题)")


def collect():
    """扫描 items/<错题>/(单层),返回 (mistakes, errors, warnings)。"""
    mistakes, errors, warnings = [], [], []
    if not ITEMS_DIR.is_dir():
        return mistakes, errors, warnings
    for d in sorted(p for p in ITEMS_DIR.iterdir() if p.is_dir()):
        meta_path = d / "meta.json"
        where = d.relative_to(ROOT).as_posix()
        if not meta_path.exists():
            warnings.append(f"{where}: 缺少 meta.json(未写入索引)")
            continue
        if not (d / "mistake.md").exists():
            warnings.append(f"{where}: 缺少 mistake.md")
            continue
        try:
            meta = load_json(meta_path)
        except json.JSONDecodeError as e:
            errors.append(f"{where}: JSON 解析失败 {e}")
            continue
        m_errors = validate_mistake(meta, where)
        errors.extend(m_errors)
        if m_errors:
            continue
        md = (d / "mistake.md").read_text(encoding="utf-8")
        check_sections(md, where, errors)
        mistakes.append({"dir": d, "meta": meta, "md": md})
    # 默认日期倒序（入口统一排序见 atlas/DESIGN-TREE.md A10）：
    # 先按目录名升序定次级键，再按 date 倒序——稳定排序，同日错题保持目录序，输出可复现。
    # 索引表行序与详情页上下篇导航同源此列表，故排序必须在此层做，两处才自洽。
    mistakes.sort(key=lambda m: m["dir"].name)
    mistakes.sort(key=lambda m: m["meta"]["date"], reverse=True)
    return mistakes, errors, warnings


def days_since(d):
    try:
        return (date.today() - datetime.strptime(d, "%Y-%m-%d").date()).days
    except (TypeError, ValueError):
        return None


def collect_zones():
    """跨馆警示两区数据(内容不搬家,原地链接,宿主从门户迁入本馆索引见 A11):

    - 落选:pick verdict=hold 的条目(带类别与 push 日期)
    - 腐烂:pick 超 STALE_DAYS 未采集/未验证,apprentice 超 STALE_DAYS 未验证或 outdated
    """
    holds, rotten = [], []
    for meta_path in sorted((ATLAS / "pick" / "items").glob("*/*/meta.json")):
        meta = load_json(meta_path)
        if meta.get("verdict") == "hold":
            push = (meta.get("stats") or {}).get("pushed_at") or ""
            holds.append((meta_path.parent, meta, push))
            continue
        stats = meta.get("stats") or {}
        base = stats.get("collected_at") or meta.get("verified")
        d = days_since(base)
        if d is not None and d > STALE_DAYS:
            rotten.append(("pick", meta_path.parent, meta.get("name", ""), "待复核", d))
    for meta_path in sorted((ATLAS / "apprentice" / "items").glob("*/*/meta.json")):
        meta = load_json(meta_path)
        if meta.get("status") == "outdated":
            rotten.append(("apprentice", meta_path.parent, meta.get("name", ""), "过期", None))
        else:
            d = days_since(meta.get("verified"))
            if d is not None and d > STALE_DAYS:
                rotten.append(("apprentice", meta_path.parent, meta.get("name", ""), "待重验", d))

    # 排序口径同 DESIGN-TREE A10/A11:稳定双重排序,目录名升序定次级键,输出可复现。
    # 落选:push 倒序,无 push(商业闭源等)无日期可比 → 固定沉底,不混进倒序。
    holds.sort(key=lambda t: t[1].get("name", ""))
    holds.sort(key=lambda t: t[2], reverse=True)
    holds.sort(key=lambda t: t[2] == "")
    # 腐烂:越烂越靠前(距今天数降序;outdated 无天数按最烂处理 → 排最前)。
    rotten.sort(key=lambda t: t[2])
    rotten.sort(key=lambda t: t[4] if t[4] is not None else 10**6, reverse=True)
    return holds, rotten


# ============================================================
# 页面渲染
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
  .idx-table { display: table; table-layout: fixed; }
  .idx-table th {
    font-size: .73rem; color: var(--muted); font-weight: 500; text-align: left; font-family: var(--font-body);
    cursor: pointer; user-select: none; white-space: nowrap;
  }
  .idx-table th:focus-visible { outline-offset: -2px; }
  .idx-table th.sorted-asc::after { content: " ↑"; color: var(--link); }
  .idx-table th.sorted-desc::after { content: " ↓"; color: var(--link); }
  .idx-table td { border-bottom: 1px solid var(--border); font-size: .84rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .idx-table td:first-child { width: 13rem; }
  .idx-table td.mx { color: var(--muted); }
  .idx-table td.num, .idx-table th.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; font-family: var(--font-mono); font-size: .78rem; }
  .idx-table tbody tr:hover td { background: color-mix(in srgb, var(--link) 5%, transparent); }
  .idx-table .mistake-name { font-weight: 600; }
  .empty { text-align: center; color: var(--muted); padding: 4rem 0; }
  /* ── 跨馆警示两区(A11:宿主从门户 views.html 迁入本馆索引;非本馆门禁内容,只聚合+原地链接) ── */
  h2.zone { font-size: 1.3rem; margin: 2.6rem 0 .4rem; }
  .zone-note { color: var(--muted); font-size: .82rem; margin: 0 0 .6rem; }
  .empty-zone { color: var(--muted); font-size: .88rem; padding: .3rem 0 1rem; }
  details.fold { margin-bottom: 1rem; }
  details.fold > summary {
    cursor: pointer; color: var(--muted); font-size: .88rem; padding: .35rem 0;
    user-select: none; list-style: none;
  }
  details.fold > summary::before { content: "▸ "; }
  details.fold[open] > summary::before { content: "▾ "; }
  details.fold > summary:hover { color: var(--link); }
  @media (max-width: 720px) { .idx-table { min-width: 560px; } .category { overflow-x: auto; } }
"""

DETAIL_CSS = """
  .mistake-nav {
    display: flex; gap: .9rem; flex-wrap: wrap; align-items: center;
    font-size: .84rem; color: var(--muted); margin-bottom: 1rem; font-family: var(--font-body);
  }
  .mistake-nav .sep { color: var(--border); }
  article {
    background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 1.25rem 1.45rem; position: relative;
  }
  article > .seal-big { position: absolute; top: 1rem; right: 1.2rem; }
"""


def badge(status):
    label, seal, color = STATUS[status]
    return f'<span class="seal" style="--vb:{color}" title="{label}"><i></i>{seal}</span>'


def seal_big(status):
    label, seal, color = STATUS[status]
    return f'<span class="seal seal-big" style="--vb:{color}" title="{label}"><i></i>{seal}</span>'


def render_row(m):
    meta = m["meta"]
    rel = m["dir"].relative_to(ROOT).as_posix()
    tags = "、".join(meta.get("tags", []))
    search = " ".join([meta.get("name", ""), tags, meta.get("source", "")])
    return f"""      <tr data-status="{meta['status']}" data-date="{html.escape(meta.get('date', ''))}" data-name="{html.escape(meta['name'])}"
          data-search="{html.escape(search.lower())}">
        <td class="mistake-name"><a href="{html.escape(rel)}/mistake.html" title="{html.escape(meta.get('source', ''))}">{html.escape(meta['name'])}</a></td>
        <td class="num">{html.escape(meta.get('date', ''))}</td>
        <td class="mx">{html.escape(tags)}</td>
        <td>{badge(meta['status'])}</td>
      </tr>"""


def _rel_link(item_dir, page):
    """邻馆条目页相对本索引(mistakes/index.html,深度 1)的链接:../pick/items/.../report.html。"""
    return f"../{item_dir.relative_to(ATLAS).as_posix()}/{page}"


def render_zone_holds(holds):
    """落选区:pick verdict=hold,默认折叠——不常看的知识不占视野(A5 取舍,随 A11 迁入)。"""
    note = "来自 pick 馆——verdict=hold 的条目:被毙的方案与理由。按 push 倒序,无 push 沉底;内容不搬家,原地链接。"
    if not holds:
        body = '<p class="empty-zone">暂无落选条目——被毙的方案带着理由住在 pick 的决策树里。</p>'
    else:
        rows = "".join(
            f"\n      <tr><td><a href=\"{_rel_link(d, 'report.html')}\">{html.escape(meta.get('name', ''))}</a></td>"
            f'<td class="mx">{html.escape(d.relative_to(ATLAS).as_posix().split("/")[2])}</td>'
            f'<td class="num">{html.escape(push or "—")}</td>'
            f'<td class="mx">{html.escape(meta.get("summary", ""))}</td></tr>'
            for d, meta, push in holds
        )
        table = ('  <table class="idx-table">\n    <thead><tr>'
                 '<th>条目</th><th>类别</th><th class="num">push</th><th>一句话结论</th>'
                 f'</tr></thead>\n    <tbody>{rows}\n    </tbody>\n  </table>')
        body = f'  <details class="fold"><summary>展开 {len(holds)} 条落选(不常看,收着)</summary>\n{table}\n  </details>'
    return f'  <h2 class="zone">落选</h2>\n  <p class="zone-note">{note}</p>\n{body}'


def render_zone_rotten(rotten):
    """腐烂警示区:两馆超期/outdated,越烂越靠前。"""
    note = f"来自 pick · apprentice 两馆——超 {STALE_DAYS} 天未验证/未采集,或已过期(outdated)。按距今倒序,烂得最久的在最上。"
    if not rotten:
        body = '<p class="empty-zone">全部在保鲜期内。</p>'
    else:
        rows = "".join(
            f'\n      <tr><td class="mx">{html.escape(lib)}</td>'
            f'<td><a href="{_rel_link(d, "report.html" if lib == "pick" else "lesson.html")}">{html.escape(name)}</a></td>'
            f'<td>{html.escape(tag)}</td>'
            f'<td class="num">{f"{days} 天" if days is not None else "—"}</td></tr>'
            for lib, d, name, tag, days in rotten
        )
        body = ('  <table class="idx-table">\n    <thead><tr>'
                '<th>馆</th><th>条目</th><th>状态</th><th class="num">距今</th>'
                f'</tr></thead>\n    <tbody>{rows}\n    </tbody>\n  </table>')
    return f'  <h2 class="zone">腐烂警示</h2>\n  <p class="zone-note">{note}</p>\n{body}'


def render_index(mistakes, holds, rotten):
    today = date.today().isoformat()
    rows = "\n".join(render_row(m) for m in mistakes) or '<tr><td colspan="4">还没有错题——要么你走得很稳,要么你还没开始记。</td></tr>'
    chips = "".join(
        f'<button class="chip" data-status="{key}" style="--chip-c:{color}">{label}</button>'
        for key, (label, _seal, color) in STATUS.items()
    )
    zones = render_zone_holds(holds) + "\n" + render_zone_rotten(rotten)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>mistakes · 错题集索引</title>
<style>{BASE_CSS}{INDEX_CSS}</style>
</head>
<body>
<main>
  <div class="masthead">
    <h1>mistakes</h1>
    <span class="sub">错题集 · <a href="RULES.md">RULES.md</a> · <a href="../index.html">← atlas</a></span>
    <span class="figures">{len(mistakes)} 条</span>
  </div>
  <input id="filter" type="search" placeholder="按错题名 / 类型 / 出处搜索…" autocomplete="off">
  <div class="chips">
    <button class="chip active" data-status="all">全部</button>
    {chips}
  </div>
  <table class="idx-table" id="main-table">
    <thead><tr>
      <th data-sort="name" tabindex="0">错题</th><th data-sort="date" class="num sorted-desc" tabindex="0">日期</th>
      <th>类型</th><th data-sort="status" tabindex="0">状态</th>
    </tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
{zones}
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物,禁止手改</footer>
</main>
<script>
  // 文本过滤 + status chips + 表头排序(点击切换升降序)。
  // 过滤只作用于主表(#main-table)——跨馆警示两区不参与搜索/状态过滤(A11)
  const STATUS_ORDER = {json.dumps({k: i for i, k in enumerate(STATUS)})};
  const input = document.getElementById('filter');
  let statusF = 'all';
  const chips = [...document.querySelectorAll('.chip')];

  function applyFilter() {{
    document.querySelectorAll('#main-table tbody tr').forEach(tr => {{
      const q = input.value.trim().toLowerCase();
      const hitText = !q || tr.dataset.search.includes(q);
      const hitStatus = statusF === 'all' || tr.dataset.status === statusF;
      tr.classList.toggle('hidden', !(hitText && hitStatus));
    }});
  }}
  input.addEventListener('input', applyFilter);
  chips.forEach(ch => ch.addEventListener('click', () => {{
    chips.forEach(c => c.classList.remove('active'));
    ch.classList.add('active');
    statusF = ch.dataset.status;
    applyFilter();
  }}));

  document.querySelectorAll('.idx-table th[data-sort]').forEach(th => {{
    th.addEventListener('click', () => {{
      const tbody = th.closest('table').querySelector('tbody');
      const key = th.dataset.sort;
      const asc = !th.classList.contains('sorted-asc');
      th.closest('table').querySelectorAll('th').forEach(t => t.classList.remove('sorted-asc', 'sorted-desc'));
      th.classList.add(asc ? 'sorted-asc' : 'sorted-desc');
      [...tbody.querySelectorAll('tr')].sort((a, b) => {{
        let va = a.dataset[key] ?? '', vb = b.dataset[key] ?? '';
        if (key === 'status') return ((STATUS_ORDER[va] ?? 9) - (STATUS_ORDER[vb] ?? 9)) * (asc ? 1 : -1);
        return String(va).localeCompare(String(vb), 'zh') * (asc ? 1 : -1);
      }}).forEach(tr => tbody.appendChild(tr));
    }});
  }});
</script>
</body>
</html>
"""


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
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物,禁止手改 · 源文件见同目录 .md</footer>
</main>
</body>
</html>
"""


def render_mistake_page(m, prev, nxt, today):
    meta = m["meta"]
    nav = ['<a href="../../index.html">← 索引</a>', f'<a href="../../../index.html">← atlas</a>']
    if prev:
        nav.append(f'<a href="../{prev["dir"].name}/mistake.html">← {html.escape(prev["meta"]["name"])}</a>')
    if nxt:
        nav.append(f'<a href="../{nxt["dir"].name}/mistake.html">{html.escape(nxt["meta"]["name"])} →</a>')
    nav_html = '<span class="sep">·</span>'.join(nav)
    body = f"""  <nav class="mistake-nav">{nav_html}</nav>
  <article>
  {seal_big(meta['status'])}
{render_markdown(m['md'])}
  </article>"""
    return _page(f"{meta['name']} · mistakes", DETAIL_CSS, body, today)


def main():
    mistakes, errors, warnings = collect()
    holds, rotten = collect_zones()
    for w in warnings:
        print(f"⚠️  {w}")
    if errors:
        print("\n❌ 校验未通过,索引未更新:")
        for e in errors:
            print(f"   {e}")
        print("\n参见 RULES.md 第 2、4 节。")
        sys.exit(1)

    today = date.today().isoformat()
    import json as _json
    for idx, m in enumerate(mistakes):
        prev = mistakes[idx - 1] if idx > 0 else None
        nxt = mistakes[idx + 1] if idx + 1 < len(mistakes) else None
        page = render_mistake_page(m, prev, nxt, today)
        (m["dir"] / "mistake.html").write_text(page, encoding="utf-8")
    OUTPUT.write_text(render_index(mistakes, holds, rotten), encoding="utf-8")
    print(f"✅ 已生成 {len(mistakes) + 1} 个页面(index + {len(mistakes)} 条错题)"
          f"| 落选 {len(holds)}(折叠) · 腐烂 {len(rotten)}")


if __name__ == "__main__":
    main()
