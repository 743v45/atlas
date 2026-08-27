#!/usr/bin/env python3
"""atlas 门户 + 错题集视图(生成物,禁止手改)。

门户 = 地图集封面:馆导航 + 跨馆负知识聚合——**内容不搬家,原地链接**(单一事实源):
- 翻车:mistakes 馆全部条目(根因一行摘要 + 链接)
- 落选:pick verdict=hold 的条目(默认折叠,展开才看)
- 腐烂警示:pick / apprentice 超 180 天未验证/未采集的条目,及 apprentice status=outdated

用法:python3 scripts/build-atlas.py(在五馆各自 build 之后跑)
样式:atlas/shared/render.py 的 BASE_CSS
"""

import html
import importlib.util
import json
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STALE_DAYS = 180  # 与两馆一致

_spec = importlib.util.spec_from_file_location("render", ROOT / "shared" / "render.py")
_render = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_render)
BASE_CSS = _render.BASE_CSS

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


def root_cause_digest(md_text, limit=90):
    """根因小节第一行文本摘要(去 markdown 语法,截断)。"""
    sec = re.search(r"^## 根因\s*$(.*?)(?=^## |\Z)", md_text, re.M | re.S)
    if not sec:
        return ""
    line = next((l.strip() for l in sec.group(1).splitlines() if l.strip()), "")
    line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", line)
    line = re.sub(r"[*`]", "", line)
    return line[: limit - 1] + "…" if len(line) > limit else line


def collect():
    """扫五馆 meta,返回门户数据。"""
    holds, mistakes, rotten = [], [], []
    pick_count = app_count = mistake_count = 0

    for rel, meta in iter_items("pick"):
        pick_count += 1
        if meta.get("verdict") == "hold":
            holds.append((rel, meta))
            continue
        stats = meta.get("stats") or {}
        base = stats.get("collected_at") or meta.get("verified")
        d = days_since(base)
        if d is not None and d > STALE_DAYS:
            rotten.append(("pick", rel, meta.get("name", ""), "待复核", d))

    for rel, meta in iter_items("apprentice"):
        app_count += 1
        if meta.get("status") == "outdated":
            rotten.append(("apprentice", rel, meta.get("name", ""), "过期", None))
        else:
            d = days_since(meta.get("verified"))
            if d is not None and d > STALE_DAYS:
                rotten.append(("apprentice", rel, meta.get("name", ""), "待重验", d))

    for d_ in sorted((ROOT / "mistakes" / "items").glob("*/meta.json")):
        mistake_count += 1
        meta = load_json(d_)
        rel = d_.parent.relative_to(ROOT).as_posix()
        md = (d_.parent / "mistake.md").read_text(encoding="utf-8")
        mistakes.append((rel, meta, root_cause_digest(md)))

    spark_count = sum(1 for _ in (ROOT / "spark" / "items").glob("*/meta.json"))
    asked_count = sum(1 for _ in (ROOT / "asked" / "items").glob("*/meta.json"))

    return {"pick_count": pick_count, "app_count": app_count, "mistake_count": mistake_count,
            "spark_count": spark_count, "asked_count": asked_count,
            "holds": holds, "mistakes": mistakes, "rotten": rotten}


ATLAS_CSS = """
  .masthead { display: flex; align-items: baseline; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.2rem; }
  .masthead .sub { color: var(--muted); font-size: .92rem; }
  .halls { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: .9rem; margin-bottom: 2.2rem; }
  .hall {
    display: block; text-decoration: none; color: var(--text);
    background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: .9rem 1.1rem;
  }
  .hall:hover { border-color: var(--link); }
  .hall h2 { margin: 0 0 .25rem; font-size: 1.12rem; }
  .hall .desc { color: var(--muted); font-size: .84rem; }
  .hall .figures { font-family: var(--font-mono); font-size: .78rem; color: var(--link); margin-top: .4rem; }
  h2.zone { font-size: 1.3rem; margin: 2rem 0 .6rem; }
  .zone .note { color: var(--muted); font-size: .8rem; margin: 0 0 .5rem; font-family: var(--font-body); }
  table { table-layout: fixed; }
  td, th { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  td.wrap { white-space: normal; overflow: visible; }
  .muted { color: var(--muted); font-size: .8rem; }
  .empty-zone { color: var(--muted); font-size: .88rem; padding: .3rem 0 1rem; }
  details.fold { margin-bottom: 1rem; }
  details.fold > summary {
    cursor: pointer; color: var(--muted); font-size: .88rem; padding: .35rem 0;
    user-select: none; list-style: none;
  }
  details.fold > summary::before { content: "▸ "; }
  details.fold[open] > summary::before { content: "▾ "; }
  details.fold > summary:hover { color: var(--link); }
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
      <div class="desc">怎么做——结论馆,收录即定案,课从真实对话长出来</div>
      <div class="figures">{data['app_count']} 课</div>
    </a>
    <a class="hall" href="mistakes/index.html">
      <h2>mistakes · 错题集</h2>
      <div class="desc">怎么摔的——经过 / 根因 / 修正,单一事实源</div>
      <div class="figures">{data['mistake_count']} 条</div>
    </a>
    <a class="hall" href="spark/index.html">
      <h2>spark · 奇想录</h2>
      <div class="desc">想去但还没走的 Z——低摩擦苗圃,毕业制流向各馆</div>
      <div class="figures">{data['spark_count']} 条念头</div>
    </a>
    <a class="hall" href="asked/index.html">
      <h2>asked · 问答馆</h2>
      <div class="desc">是什么、为什么——师父讲的地形,自洽且可溯</div>
      <div class="figures">{data['asked_count']} 篇</div>
    </a>
  </div>"""

    # ── 错题集 · 翻车(来自 mistakes 馆,根因摘要直读) ──
    if data["mistakes"]:
        rows = "".join(
            f'<tr><td class="muted">{esc(m.get("date", ""))}</td>'
            f'<td><a href="{rel}/mistake.html">{esc(m.get("name", ""))}</a></td>'
            f'<td class="muted">{esc("、".join(m.get("tags", [])))}</td>'
            f'<td class="wrap">{esc(digest)}</td></tr>'
            for rel, m, digest in data["mistakes"]
        )
        mistakes_html = _table(["日期", "错题", "类型", "根因"], rows, ["6rem", "13rem", "8rem", "auto"])
    else:
        mistakes_html = '<p class="empty-zone">还没有错题——要么走得很稳,要么还没开始记。</p>'

    # ── 错题集 · 落选(默认折叠) ──
    if data["holds"]:
        rows = "".join(
            f'<tr><td><a href="{rel}/report.html">{esc(m.get("name", ""))}</a></td>'
            f'<td class="muted">{esc(rel.split("/")[2])}</td><td class="wrap">{esc(m.get("summary", ""))}</td></tr>'
            for rel, m in data["holds"]
        )
        holds_inner = _table(["条目", "类别", "一句话结论"], rows, ["9rem", "7rem", "auto"])
        holds_html = (
            f'<details class="fold"><summary>展开 {len(data["holds"])} 条落选'
            f'(verdict=hold,被毙的方案与理由——不常看,收着)</summary>{holds_inner}</details>'
        )
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
  <p class="note">来自 mistakes 馆——根因一行直读,详情点入。失败比成功教学价值高。</p>
{mistakes_html}
  <h2 class="zone">错题集 · 落选</h2>
  <p class="note">pick 里 verdict=hold 的条目。默认折叠——不常看的知识不占视野,要时点开。</p>
{holds_html}
  <h2 class="zone">错题集 · 腐烂警示</h2>
  <p class="note">两馆超 {STALE_DAYS} 天未验证/未采集的条目与已过期(outdated)的课——知识在腐烂的地方,先看这里。</p>
{rotten_html}"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>atlas · 馆群门户</title>
<style>{BASE_CSS}{ATLAS_CSS}</style>
</head>
<body>
<main>
  <div class="masthead">
    <h1>atlas</h1>
    <span class="sub">馆群门户 · <a href="PHILOSOPHY.md">设计理念</a> · 内容不搬家,原地链接</span>
  </div>
{body}
  <footer>生成于 {today} · <code>python3 scripts/build-atlas.py</code>(五馆 build 之后跑)· 本页为生成物,禁止手改</footer>
</main>
</body>
</html>
"""


def main():
    data = collect()
    (ROOT / "index.html").write_text(render(data), encoding="utf-8")
    print(
        f"✅ 门户已生成:pick {data['pick_count']} · apprentice {data['app_count']} · mistakes {data['mistake_count']} · "
        f"spark {data['spark_count']} · asked {data['asked_count']} | "
        f"翻车 {len(data['mistakes'])} · 落选 {len(data['holds'])}(折叠) · 腐烂 {len(data['rotten'])}"
    )


if __name__ == "__main__":
    main()
