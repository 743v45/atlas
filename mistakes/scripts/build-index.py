#!/usr/bin/env python3
"""聚合 items/ 下所有错题的 meta.json,校验后生成全部 HTML(均为生成物,禁止手改):

- index.html                    错题索引(状态过滤 + 类型搜索 + 表头排序)
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
ITEMS_DIR = ROOT / "items"
OUTPUT = ROOT / "index.html"

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
    return mistakes, errors, warnings


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


def render_index(mistakes):
    today = date.today().isoformat()
    rows = "\n".join(render_row(m) for m in mistakes) or '<tr><td colspan="4">还没有错题——要么你走得很稳,要么你还没开始记。</td></tr>'
    chips = "".join(
        f'<button class="chip" data-status="{key}" style="--chip-c:{color}">{label}</button>'
        for key, (label, _seal, color) in STATUS.items()
    )
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
  <table class="idx-table">
    <thead><tr>
      <th data-sort="name" tabindex="0">错题</th><th data-sort="date" class="num" tabindex="0">日期</th>
      <th>类型</th><th data-sort="status" tabindex="0">状态</th>
    </tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物,禁止手改</footer>
</main>
<script>
  // 文本过滤 + status chips + 表头排序(点击切换升降序)
  const STATUS_ORDER = {json.dumps({k: i for i, k in enumerate(STATUS)})};
  const input = document.getElementById('filter');
  let statusF = 'all';
  const chips = [...document.querySelectorAll('.chip')];

  function applyFilter() {{
    document.querySelectorAll('tbody tr').forEach(tr => {{
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
    OUTPUT.write_text(render_index(mistakes), encoding="utf-8")
    print(f"✅ 已生成 {len(mistakes) + 1} 个页面(index + {len(mistakes)} 条错题)")


if __name__ == "__main__":
    main()
