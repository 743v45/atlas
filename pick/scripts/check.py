#!/usr/bin/env python3
"""渲染产物断言（防漂移测试）——build 之后跑，检查生成 HTML 的正确性。

用法：python3 scripts/build-index.py && python3 scripts/check.py

覆盖三类回归（都真实发生过）：
1. 链接完整性：爬所有 html 的相对 href，逐一断言目标文件存在
   （2026-08-27 域页 404 回归：/domains/items/… 双重前缀）
2. 模板残留：f-string/%% 未替换的占位（{{xxx}} 残迹）与空关键区
   （2026-08-27 TABLE_JS 双花括号语法错回归）
3. 源与产物脱节：任何 html 早于任何源文件（md/json）的 mtime → 忘了重建
   （用户报「索引没更新」的一类根源）
4. 关键内容：每页判词章/figures/锚点齐全
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_FILES = [ROOT / "index.html", *sorted((ROOT / "domains").glob("*.html")),
              *sorted((ROOT / "items").glob("*/*/*.html")), *sorted((ROOT / "items").glob("*/ *.html"))]
HTML_FILES = [f for f in HTML_FILES if f.exists()]

failures = []


def fail(msg):
    failures.append(msg)


# ---------- 1) 链接完整性 ----------
checked = 0
for page in HTML_FILES:
    base = page.parent
    text = page.read_text(encoding="utf-8")
    for href in re.findall(r'(?:href|src)="([^"]+)"', text):
        if href.startswith(("http", "#", "mailto:", "data:", "${")) or href.endswith((".css", ".js")):
            continue
        target = (base / href.split("#")[0]).resolve()
        checked += 1
        if href.split("#")[0] and not target.exists():
            fail(f"链接断链: {page.relative_to(ROOT)} → {href}")

# ---------- 2) 模板残留与关键内容 ----------
for page in HTML_FILES:
    text = page.read_text(encoding="utf-8")
    # f-string/%% 未替换的典型残迹（生成页不该出现成对花括号占位）
    if re.search(r"\{\{?\w+\}\}?[^\w]", text.replace("{{", "")) and "{{" in text:
        fail(f"模板残留: {page.relative_to(ROOT)} 含未替换的 {{…}}")
    if page.name == "report.html":
        if 'class="seal' not in text:
            fail(f"判词章缺失: {page.relative_to(ROOT)}")
        if "<blockquote>" not in text:
            fail(f"TL;DR 引用块缺失: {page.relative_to(ROOT)}")
    if page.name == "index.html":
        for must in ('class="domain"', 'id="omni"'):
            if must not in text:
                fail(f"索引关键区缺失: {must}")
        # figures 与实际条目数一致
        m = re.search(r'(\d+) 条</span>', text)
        n_meta = len(list((ROOT / "items").glob("*/*/meta.json")))
        if m and int(m.group(1)) != n_meta:
            fail(f"索引条目数 {m.group(1)} ≠ 实际 {n_meta}")

# ---------- 3) 源与产物脱节 ----------
newest_src = 0.0
for src in list((ROOT / "items").rglob("*.md")) + list((ROOT / "items").rglob("*.json")) \
        + [ROOT / "domains.json", ROOT / "scripts" / "build-index.py"]:
    newest_src = max(newest_src, src.stat().st_mtime)
oldest_html = min(f.stat().st_mtime for f in HTML_FILES)
if oldest_html < newest_src:
    fail("产物过期：源文件比某些 html 新——改完源忘了 python3 scripts/build-index.py")

# ---------- 汇总 ----------
print(f"检查 {len(HTML_FILES)} 个页面 / {checked} 个链接")
if failures:
    print(f"\n❌ {len(failures)} 处失败：")
    for f_ in failures[:30]:
        print(f"   {f_}")
    sys.exit(1)
print("✅ 产物断言全部通过")
