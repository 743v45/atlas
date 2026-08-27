#!/usr/bin/env python3
"""聚合 items/ 下所有问答的 meta.json,校验后生成全部 HTML(均为生成物,禁止手改):

- index.html                  问答索引(搜索 + 表头排序)
- items/<条目>/answer.html     渲染 answer.md,带面包屑与上下篇导航

校验门禁(RULES.md 第 4 节)——知识要准确可溯:
- 必填字段缺失:name / date / source / tags
- date 不是 YYYY-MM-DD;tags 必须非空数组
- source 路径不存在 → 知识必须可溯,先归档再建条
- answer.md 缺 TL;DR → 不自洽的条目不算自洽存档
- 任何错误 → 打印全部问题并退出码 1
"""

import html
import json
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
render_markdown = _render.render_markdown
BASE_CSS = _render.BASE_CSS

REQUIRED_FIELDS = ["name", "date", "source", "tags"]

# ============================================================
# 数据收集与校验
# ============================================================

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_entry(meta, where):
    errors = []
    for field in REQUIRED_FIELDS:
        if not meta.get(field):
            errors.append(f"{where}: 必填字段 {field} 缺失或为空")
    if meta.get("date"):
        try:
            datetime.strptime(meta["date"], "%Y-%m-%d")
        except ValueError:
            errors.append(f"{where}: 日期 {meta['date']!r} 不是 YYYY-MM-DD")
    tags = meta.get("tags")
    if tags is not None and (not isinstance(tags, list) or not tags):
        errors.append(f"{where}: tags 必须是非空数组")
    src = meta.get("source")
    if src and not (ROOT.parent / src).exists():
        errors.append(f"{where}: source 路径不存在:{src}(知识要可溯——先归档到 atlas/conversations/ 再建条)")
    return errors


def check_self_contained(md_text, where, errors):
    if "TL;DR" not in md_text:
        errors.append(f"{where}: answer.md 缺 TL;DR(不自洽的条目不算存档)")


def collect():
    entries, errors, warnings = [], [], []
    if not ITEMS_DIR.is_dir():
        return entries, errors, warnings
    for d in sorted(p for p in ITEMS_DIR.iterdir() if p.is_dir()):
        meta_path = d / "meta.json"
        where = d.relative_to(ROOT).as_posix()
        if not meta_path.exists():
            warnings.append(f"{where}: 缺少 meta.json(未写入索引)")
            continue
        md_path = d / "answer.md"
        if not md_path.exists():
            warnings.append(f"{where}: 缺少 answer.md")
            continue
        try:
            meta = load_json(meta_path)
        except json.JSONDecodeError as e:
            errors.append(f"{where}: JSON 解析失败 {e}")
            continue
        e_errors = validate_entry(meta, where)
        errors.extend(e_errors)
        if e_errors:
            continue
        md = md_path.read_text(encoding="utf-8")
        check_self_contained(md, where, errors)
        entries.append({"dir": d, "meta": meta, "md": md})
    return entries, errors, warnings


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
  .idx-table { display: table; table-layout: fixed; }
  .idx-table th {
    font-size: .73rem; color: var(--muted); font-weight: 500; text-align: left; font-family: var(--font-body);
    cursor: pointer; user-select: none; white-space: nowrap;
  }
  .idx-table th:focus-visible { outline-offset: -2px; }
  .idx-table th.sorted-asc::after { content: " ↑"; color: var(--link); }
  .idx-table th.sorted-desc::after { content: " ↓"; color: var(--link); }
  .idx-table td { border-bottom: 1px solid var(--border); font-size: .84rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .idx-table td:first-child { width: auto; }
  .idx-table td.mx { color: var(--muted); }
  .idx-table td.num, .idx-table th.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; font-family: var(--font-mono); font-size: .78rem; }
  .idx-table tbody tr:hover td { background: color-mix(in srgb, var(--link) 5%, transparent); }
  .idx-table .entry-name { font-weight: 600; }
  .idx-table .src { font-size: .74rem; }
  .empty { text-align: center; color: var(--muted); padding: 4rem 0; }
  @media (max-width: 720px) { .idx-table { min-width: 560px; } .wrap-x { overflow-x: auto; } }
"""

DETAIL_CSS = """
  .entry-nav {
    display: flex; gap: .9rem; flex-wrap: wrap; align-items: center;
    font-size: .84rem; color: var(--muted); margin-bottom: 1rem; font-family: var(--font-body);
  }
  .entry-nav .sep { color: var(--border); }
  article {
    background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 1.25rem 1.45rem;
  }
"""


def render_row(e):
    meta = e["meta"]
    rel = e["dir"].relative_to(ROOT).as_posix()
    tags = "、".join(meta.get("tags", []))
    search = " ".join([meta.get("name", ""), tags])
    return f"""      <tr data-date="{html.escape(meta.get('date', ''))}" data-name="{html.escape(meta['name'])}"
          data-search="{html.escape(search.lower())}">
        <td class="entry-name"><a href="{html.escape(rel)}/answer.html">{html.escape(meta['name'])}</a></td>
        <td class="num">{html.escape(meta.get('date', ''))}</td>
        <td class="mx">{html.escape(tags)}</td>
        <td class="mx src">{html.escape(meta.get('source', ''))}</td>
      </tr>"""


def render_index(entries):
    today = date.today().isoformat()
    rows = "\n".join(render_row(e) for e in entries) or '<tr><td colspan="4">书架还空着。</td></tr>'
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>asked · 问答馆索引</title>
<style>{BASE_CSS}{INDEX_CSS}</style>
</head>
<body>
<main>
  <div class="masthead">
    <h1>asked</h1>
    <span class="sub">问答馆 · <a href="RULES.md">RULES.md</a> · <a href="../index.html">← atlas</a></span>
    <span class="figures">{len(entries)} 篇</span>
  </div>
  <input id="filter" type="search" placeholder="按问题 / 标签搜索…" autocomplete="off">
  <div class="wrap-x">
  <table class="idx-table">
    <thead><tr>
      <th data-sort="name" tabindex="0">问题</th><th data-sort="date" class="num" tabindex="0">日期</th>
      <th>标签</th><th>出处</th>
    </tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
  </div>
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物,禁止手改 · 我问、AI 长答、值得留存</footer>
</main>
<script>
  const input = document.getElementById('filter');
  input.addEventListener('input', () => {{
    const q = input.value.trim().toLowerCase();
    document.querySelectorAll('tbody tr').forEach(tr => {{
      tr.classList.toggle('hidden', q && !tr.dataset.search.includes(q));
    }});
  }});
  document.querySelectorAll('.idx-table th[data-sort]').forEach(th => {{
    th.addEventListener('click', () => {{
      const tbody = th.closest('table').querySelector('tbody');
      const key = th.dataset.sort;
      const asc = !th.classList.contains('sorted-asc');
      th.closest('table').querySelectorAll('th').forEach(t => t.classList.remove('sorted-asc', 'sorted-desc'));
      th.classList.add(asc ? 'sorted-asc' : 'sorted-desc');
      [...tbody.querySelectorAll('tr')].sort((a, b) =>
        String(a.dataset[key] ?? '').localeCompare(String(b.dataset[key] ?? ''), 'zh') * (asc ? 1 : -1)
      ).forEach(tr => tbody.appendChild(tr));
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


def render_entry_page(e, prev, nxt, today):
    meta = e["meta"]
    nav = ['<a href="../../index.html">← 索引</a>', '<a href="../../../index.html">← atlas</a>']
    if prev:
        nav.append(f'<a href="../{prev["dir"].name}/answer.html">← {html.escape(prev["meta"]["name"])}</a>')
    if nxt:
        nav.append(f'<a href="../{nxt["dir"].name}/answer.html">{html.escape(nxt["meta"]["name"])} →</a>')
    nav_html = '<span class="sep">·</span>'.join(nav)
    body = f"""  <nav class="entry-nav">{nav_html}</nav>
  <article>
{render_markdown(e['md'])}
  </article>"""
    return _page(f"{meta['name']} · asked", DETAIL_CSS, body, today)


def main():
    entries, errors, warnings = collect()
    for w in warnings:
        print(f"⚠️  {w}")
    if errors:
        print("\n❌ 校验未通过,索引未更新:")
        for e in errors:
            print(f"   {e}")
        print("\n参见 RULES.md 第 2、4 节。")
        sys.exit(1)

    today = date.today().isoformat()
    for idx, e in enumerate(entries):
        prev = entries[idx - 1] if idx > 0 else None
        nxt = entries[idx + 1] if idx + 1 < len(entries) else None
        page = render_entry_page(e, prev, nxt, today)
        (e["dir"] / "answer.html").write_text(page, encoding="utf-8")
    OUTPUT.write_text(render_index(entries), encoding="utf-8")
    print(f"✅ 已生成 {len(entries) + 1} 个页面(index + {len(entries)} 篇问答)")


if __name__ == "__main__":
    main()
