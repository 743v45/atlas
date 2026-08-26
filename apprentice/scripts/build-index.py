#!/usr/bin/env python3
"""聚合 items/ 下所有课的 meta.json,校验后生成全部 HTML(均为生成物,禁止手改):

- index.html                        索引页(status 过滤 + 症状搜索 + 表头排序)
- items/<类别>/<课>/lesson.html      渲染 lesson.md,带面包屑与上下篇导航

用法:python3 scripts/build-index.py

校验门禁(RULES.md 第 6 节)——「强制优于记忆」:规则写成代码,不认自觉:
- 必填字段缺失:name / question / status / date / verified / model / symptoms / source
- status 不在枚举内;日期不是 YYYY-MM-DD;symptoms 必须非空数组
- lesson.md 缺「## 验证」或「## 翻车记录」小节 → 不进索引(没有验证段的课不算走通过)
- artifacts 路径不存在 → 图纸不许指向不存在的公路
- 任何错误 → 打印全部问题并退出码 1
- 单类别课数超 CAT_WARN → 仅预警(warn,结构判据提醒拆类别)
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

# status 枚举 → (中文显示, 判词单字, 状态色)。
# 课收录即定案(库是结论馆,不是草稿箱):走出结论、验证通过才建课;
# 唯一的后续变迁是失效(模型换代)→ outdated。
# 色值取自 dataviz 参考色板的 status palette(语义:good/critical),
# 判词章 = 色环 + 单字——文字承载识别,色环只是强调,永不只靠颜色传义。
STATUS = {
    "settled": ("定案", "定", "#0ca30c"),
    "outdated": ("过期", "旧", "#d03b3b"),
}
GAN = "甲乙丙丁戊己庚辛壬癸"  # 类别档案编号:天干(第 11 类起退回数字)
REQUIRED_FIELDS = ["name", "question", "status", "date", "verified", "model", "symptoms", "source"]
STALE_DAYS = 180  # 最后验证超过此天数 → 标「待重验」(模型换代快,课的时效比数据更短)
CAT_WARN = 9  # 单类别课数超过 → 拆类别预警(RULES 第 1 节结构判据:横向拆,不加深层级)

# ============================================================
# Markdown 子集渲染器(零依赖;与 pick 共享的引擎层,见 scripts/ORIGIN.md)
# 覆盖 lesson.md 模板的封闭语法:标题 / 段落 / GFM 表格 / 有无序列表 /
# 引用块 / 围栏代码 / 水平线 / 行内(粗体、代码、链接、裸 URL)/ HTML 行透传
# ============================================================

def render_inline(text):
    """行内渲染：先抽出行内代码占位 → 转义 → 粗体/链接/裸URL → 还原代码。"""
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    # 裸 URL 自动成链（跳过已生成的 href="/文本后的 URL；字符类限 ASCII，避免吞掉全角括号等中文标点）
    text = re.sub(r"(?<![\"'>=])(https?://[A-Za-z0-9._~:/?#\[\]@!$&+*,;=%-]+)", r'<a href="\1">\1</a>', text)

    def unstash(m):
        return f"<code>{html.escape(codes[int(m.group(1))], quote=False)}</code>"

    text = re.sub("\x00(\\d+)\x00", unstash, text)
    return text


def _table_cell_align(spec):
    spec = spec.strip()
    if spec.startswith(":") and spec.endswith(":"):
        return "center"
    if spec.endswith(":"):
        return "right"
    return "left"


def render_markdown(md_text):
    """行级状态机，把 markdown 子集渲染为 HTML 片段。"""
    lines = md_text.splitlines()
    out, i, n = [], 0, len(lines)
    while i < n:
        s = lines[i].strip()
        # 围栏代码块
        if s.startswith("```"):
            lang = s[3:].strip()
            buf = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # 跳过收尾 ```
            code = html.escape("\n".join(buf), quote=False)
            out.append(f'<pre><code class="lang-{html.escape(lang)}">{code}</code></pre>')
            continue
        # 空行
        if not s:
            i += 1
            continue
        # 水平线
        if re.fullmatch(r"-{3,}", s):
            out.append("<hr>")
            i += 1
            continue
        # 标题
        m = re.match(r"(#{1,4})\s+(.*)", s)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{render_inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        # 引用块
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{render_inline(' '.join(b for b in buf if b))}</blockquote>")
            continue
        # GFM 表格
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            aligns = [_table_cell_align(c) for c in lines[i + 1].strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "".join(
                f'<th style="text-align:{a}">{render_inline(h)}</th>' for h, a in zip(header, aligns)
            )
            tbody = "".join(
                "<tr>"
                + "".join(f'<td style="text-align:{a}">{render_inline(c)}</td>' for c, a in zip(r, aligns))
                + "</tr>"
                for r in rows
            )
            out.append(f"<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>")
            continue
        # 无序列表
        if re.match(r"[-*]\s+", s):
            items = []
            while i < n and re.match(r"[-*]\s+", lines[i].strip()):
                items.append(f"<li>{render_inline(re.sub(r'^[-*]\s+', '', lines[i].strip()))}</li>")
                i += 1
            out.append(f"<ul>{''.join(items)}</ul>")
            continue
        # 有序列表
        if re.match(r"\d+\.\s+", s):
            items = []
            while i < n and re.match(r"\d+\.\s+", lines[i].strip()):
                items.append(f"<li>{render_inline(re.sub(r'^\d+\.\s+', '', lines[i].strip()))}</li>")
                i += 1
            out.append(f"<ol>{''.join(items)}</ol>")
            continue
        # HTML 行透传（模板/手工 HTML 片段）
        if s.startswith("<"):
            out.append(line := lines[i])
            i += 1
            continue
        # 段落：合并连续普通行
        buf = [s]
        i += 1
        while i < n:
            nx = lines[i].strip()
            if (
                not nx
                or nx.startswith(("#", "|", ">", "```", "<", "-", "*"))
                or re.match(r"\d+\.\s+", nx)
                or re.fullmatch(r"-{3,}", nx)
            ):
                break
            buf.append(nx)
            i += 1
        out.append(f"<p>{render_inline(' '.join(buf))}</p>")
    return "\n".join(out)


# ============================================================
# 数据收集与校验
# ============================================================

def parse_date(value, where, errors):
    """严格解析 YYYY-MM-DD,失败则记入 errors 返回 None。"""
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        errors.append(f"{where}: 日期 {value!r} 不是 YYYY-MM-DD")
        return None


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_lesson(meta, where):
    """校验单课 meta,返回 errors。"""
    errors = []
    for field in REQUIRED_FIELDS:
        if not meta.get(field):
            errors.append(f"{where}: 必填字段 {field} 缺失或为空")
    if meta.get("status") and meta.get("status") not in STATUS:
        errors.append(f"{where}: status {meta['status']!r} 不在 {sorted(STATUS)} 内")
    sym = meta.get("symptoms")
    if sym is not None and (not isinstance(sym, list) or not sym):
        errors.append(f"{where}: symptoms 必须是非空数组")
    for f_name in ("date", "verified"):
        if meta.get(f_name):
            parse_date(meta[f_name], f"{where} {f_name}", errors)
    arts = meta.get("artifacts")
    if arts is not None:
        if not isinstance(arts, list):
            errors.append(f"{where}: artifacts 必须是数组")
        else:
            for art in arts:
                if not isinstance(art, str) or not art:
                    errors.append(f"{where}: artifacts 元素必须是非空字符串")
                    continue
                p = Path(art)
                if not p.is_absolute():
                    p = ROOT / p
                if not p.exists():
                    errors.append(f"{where}: artifacts 路径不存在:{art}(图纸不许指向不存在的公路)")
    return errors


def check_lesson_sections(md_text, where, errors):
    """课的必填小节(RULES.md 第 3 节):缺验证段或翻车记录 → 不进索引。"""
    for sec in ("## 验证", "## 翻车记录"):
        if sec not in md_text:
            errors.append(f"{where}: lesson.md 缺「{sec}」小节(没有验证段的课不进索引)")


def collect():
    """扫描 items/<类别>/<课>/,返回 (categories, errors, warnings)。"""
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
            warnings.append(f"类别 {cat_dir.name}/ 缺少 _meta.json(用目录名兜底显示)")

        lessons = []
        for lesson_dir in sorted(p for p in cat_dir.iterdir() if p.is_dir()):
            meta_path = lesson_dir / "meta.json"
            where = lesson_dir.relative_to(ROOT).as_posix()
            if not meta_path.exists():
                warnings.append(f"{where}: 缺少 meta.json(未写入索引)")
                continue
            if not (lesson_dir / "lesson.md").exists():
                warnings.append(f"{where}: 缺少 lesson.md")
                continue
            try:
                meta = load_json(meta_path)
            except json.JSONDecodeError as e:
                errors.append(f"{where}: JSON 解析失败 {e}")
                continue
            lesson_errors = validate_lesson(meta, where)
            errors.extend(lesson_errors)
            if lesson_errors:
                continue  # 校验不过的课不进索引

            lesson_md = (lesson_dir / "lesson.md").read_text(encoding="utf-8")
            check_lesson_sections(lesson_md, where, errors)

            try:
                base = datetime.strptime(meta["verified"], "%Y-%m-%d").date()
            except (KeyError, ValueError):
                base = None
            lessons.append({
                "dir": lesson_dir,
                "meta": meta,
                "lesson_md": lesson_md,
                "stale": base is not None and (date.today() - base).days > STALE_DAYS,
            })

        categories.append({
            "slug": cat_dir.name,
            "dir": cat_dir,
            "name": cat_meta.get("name", cat_dir.name),
            "description": cat_meta.get("description", ""),
            "order": cat_meta.get("order", 999),
            "lessons": lessons,
        })
        if len(lessons) > CAT_WARN:
            warnings.append(
                f"类别 {cat_dir.name}: {len(lessons)} 课,超 {CAT_WARN}——按结构判据横向拆类别,不加深层级(RULES 第 1 节)"
            )

    categories.sort(key=lambda c: (c["order"], c["name"]))
    return categories, errors, warnings


# ============================================================
# 页面渲染(共享样式,file:// 零依赖;BASE_CSS 与 pick 共享,见 scripts/ORIGIN.md)
# ============================================================

BASE_CSS = """
  :root {
    --bg: #f7f7f4; --card: #fffdf9; --text: #1d2430; --muted: #5d6570; --border: #e4e3de;
    --link: #3157a6; --accent: #b07d10; --danger: #d03b3b;
    --font-display: "Songti SC", "STSong", "Noto Serif CJK SC", serif;
    --font-body: -apple-system, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #16181b; --card: #1d2024; --text: #e8e6e1; --muted: #9aa0a8; --border: #2c2f34;
      --link: #7a9ce0; --accent: #d29922; --danger: #e05252;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 1.6rem 1.25rem 3rem; background: var(--bg); color: var(--text);
    font: 15px/1.68 var(--font-body);
  }
  main { max-width: 1040px; margin: 0 auto; }
  a { color: var(--link); }
  :focus-visible { outline: 2px solid var(--link); outline-offset: 2px; }
  code { background: var(--card); border: 1px solid var(--border); border-radius: 4px; padding: 0 .25em; font-size: .86em; font-family: var(--font-mono); }
  pre { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: .7rem .9rem; overflow-x: auto; }
  pre code { border: none; background: none; padding: 0; }
  table { border-collapse: collapse; width: 100%; margin: .6rem 0; }
  th, td { border: 1px solid var(--border); padding: .28rem .55rem; font-size: .88rem; }
  th { background: var(--card); }
  blockquote {
    margin: .8rem 0; padding: .45rem 1rem; border-left: 3px solid var(--link);
    background: color-mix(in srgb, var(--link) 4%, transparent);
  }
  h1, h2, h3 { font-family: var(--font-display); font-weight: 600; }
  h1 { font-size: 1.7rem; letter-spacing: .02em; margin: 0 0 .2rem; }
  h2 { font-size: 1.22rem; margin-top: 1.7rem; } h3 { font-size: 1.02rem; margin-top: 1.3rem; }
  footer {
    margin-top: 2.6rem; color: var(--muted); font-size: .78rem; text-align: center;
    border-top: 1px solid var(--border); padding-top: .9rem;
  }
  .hidden { display: none !important; }
  .seal {
    display: inline-flex; align-items: center; justify-content: center;
    width: 22px; height: 22px; border: 1.5px solid var(--vb); border-radius: 50%;
    color: var(--vb); font-family: var(--font-display); font-size: 12.5px; line-height: 1;
    flex-shrink: 0; text-decoration: none;
  }
  .seal i { display: none; }
  .seal-big {
    width: 46px; height: 46px; font-size: 22px; border-width: 2px;
    transform: rotate(-6deg); opacity: .92;
  }
"""

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
  .idx-table { display: table; table-layout: fixed; }
  .idx-table th {
    font-size: .73rem; color: var(--muted); font-weight: 500; text-align: left; font-family: var(--font-body);
    cursor: pointer; user-select: none; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .idx-table th:focus-visible { outline-offset: -2px; }
  .idx-table th.sorted-asc::after { content: " ↑"; color: var(--link); }
  .idx-table th.sorted-desc::after { content: " ↓"; color: var(--link); }
  .idx-table td { border-bottom: 1px solid var(--border); font-size: .82rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .idx-table td:first-child { width: 11rem; }
  .idx-table td.num, .idx-table th.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; font-family: var(--font-mono); font-size: .78rem; }
  .idx-table td.mx { color: var(--muted); }
  .idx-table td.stale { color: var(--danger); }
  .idx-table tbody tr:hover td { background: color-mix(in srgb, var(--link) 5%, transparent); }
  .idx-table .lesson-name { font-weight: 600; }
  .empty { text-align: center; color: var(--muted); padding: 4rem 0; }
  @media (max-width: 720px) {
    body { padding: 1rem .7rem 2.5rem; }
    .category { overflow-x: auto; }
    .category h2 { font-size: 1.12rem; }
    .masthead .figures { display: none; }
    .idx-table { min-width: 640px; }
  }
"""

LESSON_CSS = """
  .lesson-nav {
    display: flex; gap: .9rem; flex-wrap: wrap; align-items: center;
    font-size: .84rem; color: var(--muted); margin-bottom: 1rem; font-family: var(--font-body);
  }
  .lesson-nav .sep { color: var(--border); }
  article {
    background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 1.25rem 1.45rem; position: relative;
  }
  article > .seal-big { position: absolute; top: 1rem; right: 1.2rem; }
"""


def badge(status):
    """判词章(小):索引宽表用——色环描边 + 单字,title 带全称。"""
    label, seal, color = STATUS[status]
    return f'<span class="seal" style="--vb:{color}" title="{label}"><i></i>{seal}</span>'


def seal_big(status):
    """判词章(大):课页 TL;DR 处盖章——色环 + 单字 + 微旋转。"""
    label, seal, color = STATUS[status]
    return f'<span class="seal seal-big" style="--vb:{color}" title="{label}"><i></i>{seal}</span>'


def render_row(lesson):
    """渲染单课行(索引宽表:课 | 问题 | 症状 | 状态 | 验证 | 模型)。

    所有插值都经 html.escape;verified 超 STALE_DAYS 天标红(待重验)。
    """
    m, stale = lesson["meta"], lesson["stale"]
    rel = lesson["dir"].relative_to(ROOT).as_posix()
    symptoms = "、".join(m.get("symptoms", []))
    v_attrs = f' class="num stale" title="待重验:超 {STALE_DAYS} 天未验证"' if stale else ' class="num"'
    search = " ".join([m.get("name", ""), m.get("question", ""), m.get("model", "")] + m.get("symptoms", []))
    return f"""      <tr data-status="{m['status']}" data-verified="{html.escape(m.get('verified', ''))}" data-name="{html.escape(m['name'])}"
          data-search="{html.escape(search.lower())}">
        <td class="lesson-name"><a href="{html.escape(rel)}/lesson.html" title="{html.escape(m.get('question', ''))}">{html.escape(m['name'])}</a></td>
        <td>{html.escape(m.get('question', ''))}</td>
        <td class="mx">{html.escape(symptoms)}</td>
        <td>{badge(m['status'])}</td>
        <td{v_attrs}>{html.escape(m.get('verified', ''))}</td>
        <td class="mx">{html.escape(m.get('model', ''))}</td>
      </tr>"""


def render_index(categories):
    """渲染索引页 index.html:每类别一张宽表(症状搜索 + status chips + 表头排序)。"""
    total = sum(len(c["lessons"]) for c in categories)
    today = date.today().isoformat()

    sections = []
    for ci, c in enumerate(categories):
        gan = GAN[ci] if ci < len(GAN) else str(ci + 1)
        rows = "\n".join(render_row(l) for l in c["lessons"]) or '<tr><td colspan="6" class="sum">该类别暂无课。</td></tr>'
        sections.append(f"""  <section class="category" data-search="{html.escape(c['name'].lower())}">
    <h2><span class="gan" aria-hidden="true">{gan}</span>{html.escape(c['name'])}</h2>
    <table class="idx-table">
      <thead><tr>
        <th data-sort="name" tabindex="0">课</th><th data-sort="question" tabindex="0">问题</th>
        <th>症状</th><th data-sort="status" tabindex="0">状态</th>
        <th data-sort="verified" class="num" tabindex="0">验证</th><th>模型</th>
      </tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
  </section>""")

    body = "\n".join(sections) or """  <section class="empty">
    <p>还没有任何课。</p>
    <p>按 <code>RULES.md</code> 新建:<code>items/&lt;类别&gt;/&lt;课&gt;/</code>,从 <code>template/</code> 复制模板开始。</p>
  </section>"""

    chips = "".join(
        f'<button class="chip" data-status="{key}" style="--chip-c:{color}">{label}</button>'
        for key, (label, _seal, color) in STATUS.items()
    )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>apprentice · 学徒笔记索引</title>
<style>{BASE_CSS}{INDEX_CSS}</style>
</head>
<body>
<main>
  <div class="masthead">
    <h1>apprentice</h1>
    <span class="sub">AI 学徒笔记库 · <a href="RULES.md">RULES.md</a></span>
    <span class="figures">{len(categories)} 类 · {total} 课</span>
  </div>
  <input id="filter" type="search" placeholder="按课名 / 问题 / 症状搜索…" autocomplete="off">
  <div class="chips">
    <button class="chip active" data-status="all">全部</button>
    {chips}
  </div>
{body}
  <footer>生成于 {today} · <code>python3 scripts/build-index.py</code> · 本页为生成物,禁止手改 · 红=待重验</footer>
</main>
<script>
  // 文本过滤(含症状反查)+ status chips + 表头排序(类别内,点击切换升降序)
  const STATUS_ORDER = {json.dumps({k: i for i, k in enumerate(STATUS)})};
  const input = document.getElementById('filter');
  let statusF = 'all';
  const chips = [...document.querySelectorAll('.chip')];

  function applyFilter() {{
    document.querySelectorAll('.category').forEach(sec => {{
      let visible = 0;
      sec.querySelectorAll('tbody tr').forEach(tr => {{
        const q = input.value.trim().toLowerCase();
        const hitText = !q || tr.dataset.search.includes(q) || sec.dataset.search.includes(q);
        const hitStatus = statusF === 'all' || tr.dataset.status === statusF;
        const hit = hitText && hitStatus;
        tr.classList.toggle('hidden', !hit);
        if (hit) visible++;
      }});
      sec.classList.toggle('hidden', visible === 0);
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
      const table = th.closest('table');
      const tbody = table.querySelector('tbody');
      const key = th.dataset.sort;
      const asc = !th.classList.contains('sorted-asc');
      table.querySelectorAll('th').forEach(t => t.classList.remove('sorted-asc', 'sorted-desc'));
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


def render_lesson_page(cat, lesson, prev, nxt, today):
    """渲染单课的 lesson.html(面包屑 + 上下篇 + 正文)。"""
    m = lesson["meta"]
    nav = ['<a href="../../../index.html">← 索引</a>', f'<span>{html.escape(cat["name"])}</span>']
    if prev:
        nav.append(f'<a href="../{prev["dir"].name}/lesson.html">← {html.escape(prev["meta"]["name"])}</a>')
    if nxt:
        nav.append(f'<a href="../{nxt["dir"].name}/lesson.html">{html.escape(nxt["meta"]["name"])} →</a>')
    nav_html = '<span class="sep">·</span>'.join(nav)
    body = f"""  <nav class="lesson-nav">{nav_html}</nav>
  <article>
  {seal_big(m['status'])}
{render_markdown(lesson['lesson_md'])}
  </article>"""
    return _page(f"{m['name']} · apprentice", LESSON_CSS, body, today)


# ============================================================
# 主流程
# ============================================================

def main():
    categories, errors, warnings = collect()

    for w in warnings:
        print(f"⚠️  {w}")
    if errors:
        print("\n❌ 校验未通过,索引未更新:")
        for e in errors:
            print(f"   {e}")
        print("\n参见 RULES.md 第 2、3、6 节。")
        sys.exit(1)

    today = date.today().isoformat()
    generated = 0

    # 1) 各课 lesson.html(类别内上下篇导航)
    for cat in categories:
        for idx, lesson in enumerate(cat["lessons"]):
            prev = cat["lessons"][idx - 1] if idx > 0 else None
            nxt = cat["lessons"][idx + 1] if idx + 1 < len(cat["lessons"]) else None
            page = render_lesson_page(cat, lesson, prev, nxt, today)
            (lesson["dir"] / "lesson.html").write_text(page, encoding="utf-8")
            generated += 1

    # 2) 索引页
    OUTPUT.write_text(render_index(categories), encoding="utf-8")
    generated += 1

    total = sum(len(c["lessons"]) for c in categories)
    print(f"✅ 已生成 {generated} 个页面(index + {total} 课),共 {len(categories)} 个类别 / {total} 课")


if __name__ == "__main__":
    main()
