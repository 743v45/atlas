#!/usr/bin/env python3
"""全仓断链 + 模板残留断言（五馆 + 门户全站，防新馆裸奔）。

各馆自带 check.py 只守自家产物；本脚本在 atlas 仓根跑，把整个仓当一个站点：
- 断链：全仓 .html 的 <a href> / <link href> 与 .md 的 [文本](路径) 相对链接，
  逐一断言目标存在（跳过 http(s)://、mailto:、data:、tel: 与纯 # 锚点；
  带 #锚 / ?查询 的取文件部分；md 剥代码块与行内代码后提取，防示例误报）。
- 模板残留：全仓 .html 与 .md 中未替换的 {{word}} 占位（各馆 template/ 目录下的
  模板文件本身豁免——那里 {{}} 是合法语法；检测前剥 pre/code 与代码块，
  正文教学示例不算残留）。
- 渲染器单源（承继 apprentice/scripts/check-drift.sh，反向断言见各馆 ORIGIN.md）：
  五馆 build-index.py 与 scripts/build-atlas.py 内不得复活本地渲染器副本
  （def render_inline / 非 _render 来源的 BASE_CSS 定义）——
  渲染器与样式只住 atlas/shared/render.py，别名的正确写法是 BASE_CSS = _render.BASE_CSS。
- 任一断链/残留/副本 → 打印「来源文件 → 目标」清单，退出码 1。

用法：python3 scripts/check-all.py
排除：.git*（含 .git.archived-mono）、__pycache__、node_modules、dist（decks 构建产物）。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXTERNAL = ("http://", "https://", "mailto:", "data:", "tel:", "//", "${")
HREF_RE = re.compile(r"""<(?:a|link)\b[^>]*?\bhref=(?:"([^"]+)"|'([^']+)')""", re.IGNORECASE)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
PLACEHOLDER_RE = re.compile(r"\{\{[\w一-鿿][\w一-鿿 ]*\}\}")
# 本地渲染器副本复活迹象：本地定义 render_inline / 非 _render 来源的 BASE_CSS
# （正确接入是 BASE_CSS = _render.BASE_CSS；原 shell 版未排除别名行，字面移植会全量误报）
LOCAL_RENDER_RE = re.compile(r"^(?:def render_inline|BASE_CSS = (?!_render\.))", re.MULTILINE)
RENDER_SOURCES = [
    "pick/scripts/build-index.py", "apprentice/scripts/build-index.py",
    "mistakes/scripts/build-index.py", "spark/scripts/build-index.py",
    "asked/scripts/build-index.py", "scripts/build-atlas.py",
]


SKIP_PARTS = {".git", "__pycache__", "node_modules", "dist"}  # .git 前缀另查；dist = decks 构建产物


def iter_files(*exts):
    """全仓收集，排除 .git*（含 .git.archived-mono 旧仓残留）、__pycache__、
    node_modules 与 dist（pick/decks 的 Slidev 依赖与构建产物，非站点内容）。"""
    for p in sorted(ROOT.rglob("*")):
        if p.suffix not in exts or not p.is_file():
            continue
        parts = p.relative_to(ROOT).parts
        if any(part.startswith(".git") or part in SKIP_PARTS for part in parts):
            continue
        yield p


def strip_html_code(text):
    return re.sub(r"<(?:pre|code)\b.*?</(?:pre|code)>", "", text, flags=re.DOTALL | re.IGNORECASE)


def strip_md_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


def broken_link(src, href):
    """相对链接可解析则返回 None，否则返回问题描述。"""
    href = href.strip()
    if not href or href.startswith(EXTERNAL) or href.startswith("#"):
        return None
    path_part = href.split("#", 1)[0].split("?", 1)[0]
    if not path_part:
        return None
    target = (src.parent / path_part).resolve()
    if not target.exists():
        return f"{src.relative_to(ROOT)} → {href}"
    return None


def main():
    broken, leftover = [], []

    # ---------- 1) 断链：html href + md 相对链接 ----------
    for p in iter_files(".html"):
        text = p.read_text(encoding="utf-8", errors="replace")
        for groups in HREF_RE.findall(text):
            for href in groups:
                if not href:
                    continue
                msg = broken_link(p, href)
                if msg:
                    broken.append(msg)
    for p in iter_files(".md"):
        text = strip_md_code(p.read_text(encoding="utf-8", errors="replace"))
        for href in MD_LINK_RE.findall(text):
            msg = broken_link(p, href)
            if msg:
                broken.append(msg)

    # ---------- 2) 模板残留：未替换的 {{word}}（template/ 模板本身豁免） ----------
    for p in iter_files(".html", ".md"):
        if "template" in p.relative_to(ROOT).parts:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        text = strip_html_code(text) if p.suffix == ".html" else strip_md_code(text)
        m = PLACEHOLDER_RE.search(text)
        if m:
            leftover.append(f"{p.relative_to(ROOT)} → 未替换占位 {m.group(0)}")

    # ---------- 3) 渲染器单源（承继 apprentice/scripts/check-drift.sh） ----------
    drift = []
    for rel in RENDER_SOURCES:
        p = ROOT / rel
        if not p.exists():
            continue
        if LOCAL_RENDER_RE.search(p.read_text(encoding="utf-8", errors="replace")):
            drift.append(f"{rel} → 本地渲染器副本复活，删除副本接 atlas/shared/render.py")

    # ---------- 汇总 ----------
    if broken:
        print(f"\n❌ {len(broken)} 处断链：")
        for line in broken:
            print(f"   {line}")
    if leftover:
        print(f"\n❌ {len(leftover)} 处模板残留：")
        for line in leftover:
            print(f"   {line}")
    if drift:
        print(f"\n❌ {len(drift)} 处渲染器副本（引擎单源违规）：")
        for line in drift:
            print(f"   {line}")
    if broken or leftover or drift:
        sys.exit(1)
    print("✅ 全仓断链 + 模板残留 + 渲染器单源断言全部通过")


if __name__ == "__main__":
    main()
