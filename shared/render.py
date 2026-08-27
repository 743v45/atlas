"""atlas 共享引擎层——Markdown 渲染器 + 基础样式。

2026-08-27 第三馆(mistakes)触发抽取(触发条件见 apprentice/scripts/ORIGIN.md):
自 apprentice 的 build-index.py 上提,与 pick 的对账副本合并为这一份。
此后五馆与门户(build-atlas)统一 import 本文件,
各馆 build 内不得再出现本地渲染器副本(scripts/check-all.py 单源断言看守)。

覆盖模板的封闭语法:标题 / 段落 / GFM 表格 / 有无序列表 /
引用块 / 围栏代码 / 水平线 / 行内(粗体、代码、链接、裸 URL)/ HTML 行透传
"""

import html
import re


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
