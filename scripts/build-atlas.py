#!/usr/bin/env python3
"""atlas 门户封面 + 错题集视图(生成物,禁止手改)。

两个产物,**内容不搬家,原地链接**(单一事实源):

- index.html  封面:馆导航 + 错题集入口(窄页——只回答「这是什么地方、去哪」)
- views.html  错题集视图(跨馆负知识聚合,三区):
  - 翻车:mistakes 馆全部条目(根因一行摘要 + 链接,按日期倒序)
  - 落选:pick verdict=hold 的条目(默认折叠,展开才看,按 push 倒序)
  - 腐烂警示:pick / apprentice 超 180 天未验证/未采集的条目,及 apprentice status=outdated(按腐烂天数倒序)

错题集是**视图维度**不是内容馆(有门禁的才是馆,见 PHILOSOPHY.md §5)——
它只是各馆已有内容的跨库复用,故住在门户子页,不建内容馆、不双头维护。

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


def item_push(meta):
    """条目的一手日期:stats.pushed_at(gh 最后 push)。无 stats(商业闭源等)返回空串。"""
    return ((meta.get("stats") or {}).get("pushed_at") or "")


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
    """扫五馆 meta,返回门户数据(三区均已按默认日期倒序,见下)。"""
    holds, mistakes, rotten = [], [], []
    pick_count = app_count = mistake_count = 0

    for rel, meta in iter_items("pick"):
        pick_count += 1
        if meta.get("verdict") == "hold":
            holds.append((rel, meta, item_push(meta)))
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

    # ── 默认排序(口径见 atlas/DESIGN-TREE.md A10:入口页一律日期倒序) ──
    # 翻车:错题日期倒序(最近摔的在上);同日按错题名,输出可复现。
    mistakes.sort(key=lambda t: t[1].get("name", ""))
    mistakes.sort(key=lambda t: t[1].get("date", ""), reverse=True)
    # 落选:pick 的一手日期是 push(updated/verified 在类别内全同,无区分度);
    # 无 push 的条目无日期可比 → 固定沉底,不混进倒序里。
    holds.sort(key=lambda t: t[1].get("name", ""))
    holds.sort(key=lambda t: t[2], reverse=True)
    holds.sort(key=lambda t: t[2] == "")
    # 腐烂警示:越烂越靠前(距今天数降序;outdated 无天数按最烂处理 → 排最前)。
    rotten.sort(key=lambda t: t[2])
    rotten.sort(key=lambda t: t[4] if t[4] is not None else 10**6, reverse=True)

    return {"pick_count": pick_count, "app_count": app_count, "mistake_count": mistake_count,
            "spark_count": spark_count, "asked_count": asked_count,
            "holds": holds, "mistakes": mistakes, "rotten": rotten}


ATLAS_CSS = """
  /* ── 封面:窄页,只回答「这是什么地方、去哪」 ── */
  .cover-head { margin: .7rem 0 2.6rem; }
  .cover-head h1 { font-size: 2.8rem; letter-spacing: .06em; margin: 0 0 .6rem; }
  .cover-head .lead { color: var(--muted); font-size: 1rem; margin: 0 0 .8rem; max-width: 40em; }
  .cover-head .meta { color: var(--muted); font-size: .78rem; font-family: var(--font-mono); }
  .cover-head .meta a { font-family: var(--font-body); }
  .halls { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: .8rem; margin: 0 0 .8rem; }
  .hall {
    display: flex; gap: .8rem; align-items: flex-start; text-decoration: none; color: var(--text);
    background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: .9rem 1rem;
  }
  .hall:hover { border-color: var(--link); }
  .hall-body { min-width: 0; }
  .hall h2 { margin: 0 0 .25rem; font-size: 1.06rem; }
  .hall .desc { color: var(--muted); font-size: .82rem; line-height: 1.55; }
  .hall .figures { font-family: var(--font-mono); font-size: .75rem; color: var(--link); margin-top: .5rem; }
  /* 错题集入口:是跨馆视图不是第六馆,故刻意不长成馆卡片(细条,视觉层级低于五馆) */
  .views-entry {
    display: flex; align-items: baseline; gap: .6rem; flex-wrap: wrap;
    text-decoration: none; color: var(--muted); font-size: .84rem;
    border-top: 1px dashed var(--border); padding: .65rem .1rem 0;
  }
  .views-entry:hover { color: var(--link); }
  .views-entry b { color: var(--text); font-weight: 600; }
  .views-entry:hover b { color: var(--link); }
  .views-entry .figures { margin-left: auto; font-family: var(--font-mono); font-size: .74rem; }
  /* 馆印:五馆各答一问的单字(文字承载识别,与五馆判词章同语系;色只作强调) */
  .sigil {
    flex-shrink: 0; display: inline-flex; align-items: center; justify-content: center;
    width: 34px; height: 34px; border: 1.5px solid var(--text); border-radius: 50%;
    color: var(--text); font-family: var(--font-display); font-size: 16px; line-height: 1;
    margin-top: .1rem;
  }
  .hall:hover .sigil { border-color: var(--link); color: var(--link); }
  /* ── 错题集视图:三区共用 ── */
  h2.zone { font-size: 1.34rem; margin: 2.4rem 0 .5rem; }
  h2.zone:first-of-type { margin-top: 1.4rem; }
  .zone-note { color: var(--muted); font-size: .82rem; margin: 0 0 .6rem; }
  table { table-layout: fixed; }
  td, th { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  td.wrap { white-space: normal; overflow: visible; }
  td.num { font-variant-numeric: tabular-nums; font-family: var(--font-mono); font-size: .78rem; white-space: nowrap; }
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
  .report-nav { display: flex; gap: .9rem; flex-wrap: wrap; align-items: center; font-size: .84rem; color: var(--muted); margin-bottom: 1.2rem; }
  @media (max-width: 720px) {
    .cover-head h1 { font-size: 2rem; }
    body { padding: 1.1rem .8rem 2.5rem; }
  }
"""


def _table(headers, rows_html, widths=None):
    cols = "".join(f'<th style="width:{w}">{h}</th>' for h, w in zip(headers, widths or [""] * len(headers)))
    return f'<table><thead><tr>{cols}</tr></thead><tbody>{rows_html}</tbody></table>'


def _page(title, css, body, today):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>{BASE_CSS}{css}</style>
</head>
<body>
<main>
{body}
  <footer>生成于 {today} · <code>python3 scripts/build-atlas.py</code>(五馆 build 之后跑)· 本页为生成物,禁止手改</footer>
</main>
</body>
</html>
"""


def render_index(data):
    """封面:标题 + 五馆卡片 + 错题集入口(细条,不抢馆卡片位)。错题集不在此展开(见 views.html)。"""
    today = date.today().isoformat()
    body = f"""  <div class="cover-head">
    <h1>atlas</h1>
    <p class="lead">地图集:馆是图上的区域,错题集是警示图层——走过的路会重新起雾,所以边走边画。</p>
    <div class="meta"><a href="PHILOSOPHY.md">设计理念</a> · <a href="README.md">README</a> · 内容不搬家,原地链接</div>
  </div>
  <div class="halls">
    <a class="hall" href="pick/index.html">
      <span class="sigil" aria-hidden="true">选</span>
      <div class="hall-body">
        <h2>pick · 选型对比决策库</h2>
        <div class="desc">选什么——域 → 类别 → 条目,有据报告 + 决策矩阵</div>
        <div class="figures">{data['pick_count']} 条目</div>
      </div>
    </a>
    <a class="hall" href="apprentice/index.html">
      <span class="sigil" aria-hidden="true">做</span>
      <div class="hall-body">
        <h2>apprentice · AI 学徒笔记库</h2>
        <div class="desc">怎么做——结论馆,收录即定案,课从真实对话长出来</div>
        <div class="figures">{data['app_count']} 课</div>
      </div>
    </a>
    <a class="hall" href="mistakes/index.html">
      <span class="sigil" aria-hidden="true">摔</span>
      <div class="hall-body">
        <h2>mistakes · 错题集</h2>
        <div class="desc">怎么摔的——经过 / 根因 / 修正,单一事实源</div>
        <div class="figures">{data['mistake_count']} 条</div>
      </div>
    </a>
    <a class="hall" href="spark/index.html">
      <span class="sigil" aria-hidden="true">想</span>
      <div class="hall-body">
        <h2>spark · 奇想录</h2>
        <div class="desc">想去但还没走的 Z——低摩擦苗圃,毕业制流向各馆</div>
        <div class="figures">{data['spark_count']} 条念头</div>
      </div>
    </a>
    <a class="hall" href="asked/index.html">
      <span class="sigil" aria-hidden="true">问</span>
      <div class="hall-body">
        <h2>asked · 问答馆</h2>
        <div class="desc">是什么、为什么——师父讲的地形,自洽且可溯</div>
        <div class="figures">{data['asked_count']} 篇</div>
      </div>
    </a>
  </div>
  <a class="views-entry" href="views.html">
    <b>错题集视图 →</b>
    <span>跨馆负知识聚合:翻车 / 落选 / 腐烂警示</span>
    <span class="figures">{len(data['mistakes'])} 翻车 · {len(data['holds'])} 落选 · {len(data['rotten'])} 腐烂</span>
  </a>"""
    return _page("atlas · 馆群封面", ATLAS_CSS, body, today)


def render_views(data):
    """错题集视图:三区(翻车按日期倒序 / 落选按 push 倒序 / 腐烂按天数倒序)。"""
    today = date.today().isoformat()

    # ── 翻车(来自 mistakes 馆,根因摘要直读) ──
    if data["mistakes"]:
        rows = "".join(
            f'<tr><td class="num muted">{esc(m.get("date", ""))}</td>'
            f'<td><a href="{rel}/mistake.html">{esc(m.get("name", ""))}</a></td>'
            f'<td class="muted">{esc("、".join(m.get("tags", [])))}</td>'
            f'<td class="wrap">{esc(digest)}</td></tr>'
            for rel, m, digest in data["mistakes"]
        )
        mistakes_html = _table(["日期", "错题", "类型", "根因"], rows, ["6rem", "13rem", "8rem", "auto"])
    else:
        mistakes_html = '<p class="empty-zone">还没有错题——要么走得很稳,要么还没开始记。</p>'

    # ── 落选(默认折叠) ──
    if data["holds"]:
        rows = "".join(
            f'<tr><td><a href="{rel}/report.html">{esc(m.get("name", ""))}</a></td>'
            f'<td class="muted">{esc(rel.split("/")[2])}</td>'
            f'<td class="num muted">{esc(push or "—")}</td>'
            f'<td class="wrap">{esc(m.get("summary", ""))}</td></tr>'
            for rel, m, push in data["holds"]
        )
        holds_inner = _table(["条目", "类别", "push", "一句话结论"], rows, ["9rem", "7rem", "5rem", "auto"])
        holds_html = (
            f'<details class="fold"><summary>展开 {len(data["holds"])} 条落选'
            f'(verdict=hold,被毙的方案与理由——不常看,收着)</summary>{holds_inner}</details>'
        )
    else:
        holds_html = '<p class="empty-zone">暂无落选条目——被毙的方案会带着理由住在 pick 的决策树里。</p>'

    # ── 腐烂警示 ──
    if data["rotten"]:
        rows = "".join(
            f'<tr><td class="muted">{esc(lib)}</td><td><a href="{rel}/{ "report.html" if lib == "pick" else "lesson.html"}">{esc(name)}</a></td>'
            f'<td>{esc(tag)}</td><td class="num muted">{f"{d} 天" if d else "—"}</td></tr>'
            for lib, rel, name, tag, d in data["rotten"]
        )
        rotten_html = _table(["馆", "条目", "状态", "距今"], rows, ["7rem", "auto", "5rem", "5rem"])
    else:
        rotten_html = '<p class="empty-zone">全部在保鲜期内。</p>'

    body = f"""  <nav class="report-nav" style="font-size:.84rem;color:var(--muted);margin-bottom:1.2rem">
    <a href="index.html">← atlas</a>
  </nav>
  <div class="cover-head">
    <h1>错题集</h1>
    <p class="lead">跨馆负知识聚合:失败比成功教学价值高——最近摔的跤、被毙的方案、正在腐烂的知识。</p>
    <div class="meta">{len(data['mistakes'])} 翻车 · {len(data['holds'])} 落选 · {len(data['rotten'])} 腐烂 · 各馆内容不搬家,原地链接</div>
  </div>
  <h2 class="zone">翻车</h2>
  <p class="zone-note">来自 mistakes 馆——按日期倒序(最近摔的在上),根因一行直读,详情点入。</p>
{mistakes_html}
  <h2 class="zone">落选</h2>
  <p class="zone-note">pick 里 verdict=hold 的条目——按 push 倒序,无 push 的沉底。默认折叠,不常看的知识不占视野。</p>
{holds_html}
  <h2 class="zone">腐烂警示</h2>
  <p class="zone-note">两馆超 {STALE_DAYS} 天未验证/未采集的条目与已过期(outdated)的课——按距今倒序,烂得最久的在最上。</p>
{rotten_html}"""
    return _page("atlas · 错题集视图", ATLAS_CSS, body, today)


def main():
    data = collect()
    (ROOT / "index.html").write_text(render_index(data), encoding="utf-8")
    (ROOT / "views.html").write_text(render_views(data), encoding="utf-8")
    print(
        f"✅ 门户已生成:封面 index.html + 错题集 views.html | "
        f"pick {data['pick_count']} · apprentice {data['app_count']} · mistakes {data['mistake_count']} · "
        f"spark {data['spark_count']} · asked {data['asked_count']} | "
        f"翻车 {len(data['mistakes'])} · 落选 {len(data['holds'])}(折叠) · 腐烂 {len(data['rotten'])}"
    )


if __name__ == "__main__":
    main()
