#!/usr/bin/env python3
"""yawyd 馆群门户 + 错题集索引(生成物,禁止手改)。

错题集 = 跨馆负知识聚合——内容不搬家,原地链接(单一事实源):
- 翻车:apprentice 各课「## 翻车记录」小节的表格行
- 落选:pick verdict=hold 的条目
- 腐烂警示:两馆超 180 天未验证/未采集的条目,及 apprentice status=outdated

用法:python3 scripts/build-atlas.py(在 pick / apprentice 各自 build 之后跑)
样式:借 apprentice 的 BASE_CSS(共享层;shared/ 抽取后换 import 路径——见 README 迁移留档)
"""

import html
import importlib.util
import json
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STALE_DAYS = 180  # 与两馆一致

_spec = importlib.util.spec_from_file_location("app_build", ROOT / "apprentice/scripts/build-index.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
BASE_CSS = _mod.BASE_CSS

esc = html.escape


def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def days_since(d):
    try:
        return (date.today() - datetime.strptime(d, "%Y-%m-%d").date()).days
    except (TypeError, ValueError):
        return None


def iter_items(lib):
    for meta_path in sorted((ROOT / lib / "items").glob("*/*/meta.json")):
        rel = meta_path.parent.relative_to(ROOT).as_posix()
        yield rel, load_json(meta_path)


def mistakes_rows(lesson_md):
    """抽「## 翻车记录」小节的表格数据行(跳过表头与分隔行),补齐三列。"""
    sec = re.search(r"^## 翻车记录\s*$(.*?)(?=^## |\Z)", lesson_md, re.M | re.S)
    if not sec:
        return []
    rows = []
    for line in sec.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|[\s:|-]+\|?$", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or cells[0] == "日期":
            continue
        cells = cells[:3] + [""] * (3 - len(cells))
        rows.append(cells)
    return rows


def collect():
    """扫两馆 meta + 翻车小节,返回门户数据。"""
    holds, mistakes, rotten = [], [], []
    pick_count = app_count = 0

    for rel, meta in iter_items("pick"):
        pick_count += 1
        if meta.get("verdict") == "hold":
            holds.append((rel, meta))
            continue  # 落选不再重复进腐烂区
        stats = meta.get("stats") or {}
        base = stats.get("collected_at") or meta.get("verified")
        d = days_since(base)
        if d is not None and d > STALE_DAYS:
            rotten.append(("pick", rel, meta.get("name", ""), "待复核", d))

    for rel, meta in iter_items("apprentice"):
        app_count += 1
        lesson = (ROOT / rel / "lesson.md").read_text(encoding="utf-8")
        for cells in mistakes_rows(lesson):
            mistakes.append((rel, meta.get("name", ""), cells))
        if meta.get("status") == "outdated":
            rotten.append(("apprentice", rel, meta.get("name", ""), "过期", None))
        else:
            d = days_since(meta.get("verified"))
            if d is not None and d > STALE_DAYS:
                rotten.append(("apprentice", rel, meta.get("name", ""), "待重验", d))

    return {"pick_count": pick_count, "app_count": app_count,
            "holds": holds, "mistakes": mistakes, "rotten": rotten}


ATLAS_CSS = """
  .masthead { display: flex; align-items: baseline; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.2rem; }
  .masthead .sub { color: var(--muted); font-size: .92rem; }
  .halls { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: .9rem; margin-bottom: 2.2rem; }
  .hall {
    display: block; text-decoration: none; color: var(--text);
    background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: .9rem 1.1rem;
  }
  .hall:hover { border-color: var(--link); }
  .hall h2 { margin: 0 0 .25rem; font-size: 1.15rem; }
  .hall .desc { color: var(--muted); font-size: .85rem; }
  .hall .figures { font-family: var(--font-mono); font-size: .78rem; color: var(--link); margin-top: .4rem; }
  h2.zone { font-size: 1.3rem; margin: 2rem 0 .6rem; }
  .zone .note { color: var(--muted); font-size: .8rem; margin: 0 0 .5rem; font-family: var(--font-body); }
  table { table-layout: fixed; }
  td, th { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  td.wrap { white-space: normal; overflow: visible; }
  .muted { color: var(--muted); font-size: .8rem; }
  .empty-zone { color: var(--muted); font-size: .88rem; padding: .3rem 0 1rem; }
"""


def _table(headers, rows_html, widths=None):
    cols = "".join(f'<th style="width:{w}">{h}</th>' for h, w in zip(headers, widths or [""] * len(headers)))
    return f'<table><thead><tr>{cols}</tr></thead><tbody>{rows_html}</tbody></table>'


def render(data):
    today = date.today().isoformat()

    halls = f"""  <div class="halls">
    <a class="hall" href="pick/index.html">
      <h2>pick · 选型对比决策库</h2>
      <div class="desc">选什么——域 → 类别 → 条目,有据报告 + 决策矩阵</div>
      <div class="figures">{data['pick_count']} 条目</div>
    </a>
    <a class="hall" href="apprentice/index.html">
      <h2>apprentice · AI 学徒笔记库</h2>
      <div class="desc">怎么问——结论馆,收录即定案,课从真实对话长出来</div>
      <div class="figures">{data['app_count']} 课</div>
    </a>
  </div>"""

    # ── 错题集 · 翻车 ──
    if data["mistakes"]:
        rows = "".join(
            f'<tr><td class="muted">{esc(c[0])}</td><td class="wrap">{esc(c[1])}</td><td class="wrap">{esc(c[2])}</td>'
            f'<td><a href="{rel}/lesson.html">{esc(name)}</a></td></tr>'
            for rel, name, c in data["mistakes"]
        )
        mistakes_html = _table(["日期", "翻车", "修正", "课"], rows, ["7rem", "auto", "auto", "9rem"])
    else:
        mistakes_html = '<p class="empty-zone">暂无翻车记录。</p>'

    # ── 错题集 · 落选 ──
    if data["holds"]:
        rows = "".join(
            f'<tr><td><a href="{rel}/report.html">{esc(m.get("name", ""))}</a></td>'
            f'<td class="muted">{esc(rel.split("/")[1])}</td><td class="wrap">{esc(m.get("summary", ""))}</td></tr>'
            for rel, m in data["holds"]
        )
        holds_html = _table(["条目", "类别", "一句话结论"], rows, ["9rem", "7rem", "auto"])
    else:
        holds_html = '<p class="empty-zone">暂无落选条目——被毙的方案会带着理由住在 pick 的决策树里。</p>'

    # ── 错题集 · 腐烂警示 ──
    if data["rotten"]:
        rows = "".join(
            f'<tr><td class="muted">{esc(lib)}</td><td><a href="{rel}/{ "report.html" if lib == "pick" else "lesson.html"}">{esc(name)}</a></td>'
            f'<td>{esc(tag)}</td><td class="muted">{f"{d} 天" if d else "—"}</td></tr>'
            for lib, rel, name, tag, d in data["rotten"]
        )
        rotten_html = _table(["馆", "条目", "状态", "距今"], rows, ["7rem", "auto", "5rem", "5rem"])
    else:
        rotten_html = '<p class="empty-zone">全部在保鲜期内。</p>'

    body = f"""{halls}
  <h2 class="zone">错题集 · 翻车</h2>
  <p class="note">来自 apprentice 各课的「翻车记录」——失败比成功教学价值高。原地链接,单一事实源。</p>
{mistakes_html}
  <h2 class="zone">错题集 · 落选</h2>
  <p class="note">pick 里 verdict=hold 的条目——被毙的方案与理由。</p>
{holds_html}
  <h2 class="zone">错题集 · 腐烂警示</h2>
  <p class="note">两馆超 {STALE_DAYS} 天未验证/未采集的条目与已过期(outdated)的课——知识在腐烂的地方,先看这里。</p>
{rotten_html}"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>yawyd · 馆群门户</title>
<style>{BASE_CSS}{ATLAS_CSS}</style>
</head>
<body>
<main>
  <div class="masthead">
    <h1>yawyd</h1>
    <span class="sub">馆群门户 · 一个仓一个站 · 内容不搬家,原地链接</span>
  </div>
{body}
  <footer>生成于 {today} · <code>python3 scripts/build-atlas.py</code>(两馆 build 之后跑)· 本页为生成物,禁止手改</footer>
</main>
</body>
</html>
"""


def main():
    data = collect()
    (ROOT / "index.html").write_text(render(data), encoding="utf-8")
    print(
        f"✅ 门户+错题集已生成:馆 pick {data['pick_count']} 条 / apprentice {data['app_count']} 课 · "
        f"翻车 {len(data['mistakes'])} · 落选 {len(data['holds'])} · 腐烂 {len(data['rotten'])}"
    )


if __name__ == "__main__":
    main()
