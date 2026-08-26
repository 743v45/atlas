#!/usr/bin/env python3
"""聚合 items/ 下所有念头的 meta.json,校验后生成全部 HTML(均为生成物,禁止手改):

- index.html                  念头索引(状态过滤 + 搜索 + 排序)
- items/<念头>/spark.html      渲染 spark.md,带面包屑与上下篇

校验门禁(RULES.md 第 4 节)——刻意只有三条硬规则,其余从宽:
- 必填字段:name / date / status
- status 不在枚举内;date 不是 YYYY-MM-DD
- status=graduated 时 graduated_to 必填且路径存在(毕业必须留真实去向)
- md 无必填小节——低摩擦是本馆的核心功能
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

# status 枚举 → (中文显示, 判词单字, 状态色)。毕业制:终态三选一。
STATUS = {
    "idea": ("灵感", "念", "#fab219"),
    "snoozed": ("搁置", "搁", "#898781"),
    "graduated": ("毕业", "毕", "#0ca30c"),
    "dropped": ("放弃", "弃", "#d03b3b"),
}
REQUIRED_FIELDS = ["name", "date", "status"]

# ============================================================
# 数据收集与校验
# ============================================================

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_spark(meta, where):
    errors = []
    for field in REQUIRED_FIELDS:
        if not meta.get(field):
            errors.append(f"{where}: 必填字段 {field} 缺失或为空")
    if meta.get("status") and meta["status"] not in STATUS:
        errors.append(f"{where}: status {meta['status']!r} 不在 {sorted(STATUS)} 内")
    if meta.get("date"):
        try:
            datetime.strptime(meta["date"], "%Y-%m-%d")
        except ValueError:
            errors.append(f"{where}: 日期 {meta['date']!r} 不是 YYYY-MM-DD")
    if meta.get("status") == "graduated":
        dest = meta.get("graduated_to")
        if not dest:
            errors.append(f"{where}: 毕业必须填 graduated_to(去向,毕业不留指向 = 图纸断链)")
        else:
            p = Path(dest)
            if not p.is_absolute():
                p = ROOT / p
            if not p.exists():
                errors.append(f"{where}: graduated_to 路径不存在:{dest}(不许指向没修成的路)")
    return errors


def collect():
    sparks, errors, warnings = [], [], []
    if not ITEMS_DIR.is_dir():
        return sparks, errors, warnings
    for d in sorted(p for p in ITEMS_DIR.iterdir() if p.is_dir()):
        meta_path = d / "meta.json"
        where = d.relative_to(ROOT).as_posix()
        if not meta_path.exists():
            warnings.append(f"{where}: 缺少 meta.json(未写入索引)")
            continue
        md_path = d / "spark.md"
        if not md_path.exists():
            warnings.append(f"{where}: 缺少 spark.md")
            continue
        try:
            meta = load_json(meta_path)
        except json.JSONDecodeError as e:
            errors.append(f"{where}: JSON 解析失败 {e}")
            continue
        s_errors = validate_spark(meta, where)
        errors.extend(s_errors)
        if s_errors:
            continue
        sparks.append({"dir": d, "meta": meta, "md": md_path.read_text(encoding="utf-8")})
    return sparks, errors, warnings


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
  .idx-table td:first-child { width: auto; }
  .idx-table td.mx { color: var(--muted); }
  .idx-table td.num, .idx-table th.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; font-family: var(--font-mono); font-size: .78rem; }
  .idx-table tbody tr:hover td { background: color-mix(in srgb, var(--link) 5%, transparent); }
  .idx-table .spark-name { font-weight: 600; }
  .idx-table .dest { font-size: .76rem; }
  .empty { text-align: center; color: var(--muted); padding: 4rem 0; }
  @media (max-width: 720px) { .idx-table { min-width: 560px; } .wrap-x { overflow-x: auto; } }
"""

DETAIL_CSS = """
  .spark-nav {
    display: flex; gap: .9rem; flex-wrap: wrap; align-items: center;
    font-size: .84rem; color: var(--muted); margin-bottom: 1rem; font-family: var(--font-body);
  }
  .spark-nav .sep { color: var(--border); }
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


def render_row(s):
    meta = s["meta"]
    rel = s["dir"].relative_to(ROOT).as_posix()
    tags = "、".join(meta.get("tags") or [])
    dest = meta.get("graduated_to") or ""
    search = " ".join([meta.get("name", ""), tags])
    return f"""      <tr data-status="{meta['status']}" data-date="{html.escape(meta.get('date', ''))}" data-name="{html.escape(meta['name'])}"
          data-search="{html.escape(search.lower())}">
        <td class="spark-name"><a href="{html.escape(rel)}/spark.html">{html.escape(meta['name'])}</a></td>
        <td class="num">{html.escape(meta.get('date', ''))}</td>
        <td class="mx">{html.escape(tags)}</td>
        <td>{badge(meta['status'])}</td>
        <td class="mx dest">{html.escape(dest)}</td>
      </tr>"""


def render_index(sparks):
    today = date.today().isoformat()
    rows = "\n".join(render_row(s) for s in sparks) or '<tr><td colspan="5">苗圃还空着。</td></tr>'
    chips = "".join(
        f'<button class="chip" data-status="{key}" style="--chip-c:{color}">{label}</button>'
        for key, (label, _seal, color) in STATUS.items()
    )
    import json as _json
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>spark · 奇想录索引</title>
<style>{BASE_CSS}{INDEX_CSS}</style>
</head>
<body>
<main>
  <div class="masthead">
    <h1>spark</h1>
    <span class="sub">奇想录 · <a href="RULES.md">RULES.md</a> · <a href="../index.html">← atlas</a></span>
    <span class="figures">{len(sparks)} 条念头</span>
  </div>
  <input id="filter" type="search" placeholder="按念头 / 标签搜索…" autocomplete="off">
  <div class="chips">
    <button class="chip active" data-status="all">全部</button>
    {chips}
  </div>
  <div class="wrap-x">
  <table class="idx-table">
    <thead><tr>
      <th data-sort="name" tabindex="0">念头</th><th data-sort="date" class="num" tabindex="0">日期</th>
      <th>标签</th><th data-sort="status" tabindex="0">状态</th><th>去向</th>
    </tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
  </div>
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物,禁止手改 · 想到重复的点子先查这里</footer>
</main>
<script>
  // 文本过滤 + status chips + 表头排序(点击切换升降序)
  const STATUS_ORDER = {_json.dumps({k: i for i, k in enumerate(STATUS)})};
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


def render_spark_page(s, prev, nxt, today):
    meta = s["meta"]
    nav = ['<a href="../index.html">← 索引</a>', '<a href="../../index.html">← atlas</a>']
    if prev:
        nav.append(f'<a href="../{prev["dir"].name}/spark.html">← {html.escape(prev["meta"]["name"])}</a>')
    if nxt:
        nav.append(f'<a href="../{nxt["dir"].name}/spark.html">{html.escape(nxt["meta"]["name"])} →</a>')
    nav_html = '<span class="sep">·</span>'.join(nav)
    body = f"""  <nav class="spark-nav">{nav_html}</nav>
  <article>
  {seal_big(meta['status'])}
{render_markdown(s['md'])}
  </article>"""
    return _page(f"{meta['name']} · spark", DETAIL_CSS, body, today)


def main():
    sparks, errors, warnings = collect()
    for w in warnings:
        print(f"⚠️  {w}")
    if errors:
        print("\n❌ 校验未通过,索引未更新:")
        for e in errors:
            print(f"   {e}")
        print("\n参见 RULES.md 第 2、4 节。")
        sys.exit(1)

    today = date.today().isoformat()
    for idx, s in enumerate(sparks):
        prev = sparks[idx - 1] if idx > 0 else None
        nxt = sparks[idx + 1] if idx + 1 < len(sparks) else None
        page = render_spark_page(s, prev, nxt, today)
        (s["dir"] / "spark.html").write_text(page, encoding="utf-8")
    OUTPUT.write_text(render_index(sparks), encoding="utf-8")
    print(f"✅ 已生成 {len(sparks) + 1} 个页面(index + {len(sparks)} 条念头)")


if __name__ == "__main__":
    main()
