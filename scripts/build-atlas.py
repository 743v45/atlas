#!/usr/bin/env python3
"""atlas 门户封面(生成物,禁止手改)。

封面是窄页——只回答「这是什么地方、去哪」:大标题 + 一句话 + 五馆卡片。
错题集没有独立视图页:跨馆警示两区(落选/腐烂)宿主在 mistakes 馆索引,
由 mistakes/scripts/build-index.py 直读邻馆 meta 生成(A11)——内容不搬家,原地链接。

用法:python3 scripts/build-atlas.py(在五馆各自 build 之后跑)
样式:atlas/shared/render.py 的 BASE_CSS
"""

import html
import importlib.util
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("render", ROOT / "shared" / "render.py")
_render = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_render)
BASE_CSS = _render.BASE_CSS

esc = html.escape

# 五馆卡片:馆印单字 + 全名 + 一句话 + 索引路径 + 计数 glob(馆印文字承载识别,与各馆判词章同语系)
HALLS = [
    ("选", "pick · 选型对比决策库", "选什么——域 → 类别 → 条目,有据报告 + 决策矩阵",
     "pick/index.html", "pick", "*/*/meta.json", "条目"),
    ("做", "apprentice · AI 学徒笔记库", "怎么做——结论馆,收录即定案,课从真实对话长出来",
     "apprentice/index.html", "apprentice", "*/*/meta.json", "课"),
    ("摔", "mistakes · 错题集", "怎么摔的——经过 / 根因 / 修正,索引页附落选 / 腐烂警示区",
     "mistakes/index.html", "mistakes", "*/meta.json", "条"),
    ("想", "spark · 奇想录", "想去但还没走的 Z——低摩擦苗圃,毕业制流向各馆",
     "spark/index.html", "spark", "*/meta.json", "条念头"),
    ("问", "asked · 问答馆", "是什么、为什么——师父讲的地形,自洽且可溯",
     "asked/index.html", "asked", "*/meta.json", "篇"),
]

ATLAS_CSS = """
  /* ── 封面:窄页,只回答「这是什么地方、去哪」 ── */
  .cover-head { margin: .7rem 0 2.6rem; }
  .cover-head h1 { font-size: 2.8rem; letter-spacing: .06em; margin: 0 0 .6rem; }
  .cover-head .lead { color: var(--muted); font-size: 1rem; margin: 0 0 .8rem; max-width: 40em; }
  .cover-head .meta { color: var(--muted); font-size: .78rem; font-family: var(--font-mono); }
  .cover-head .meta a { font-family: var(--font-body); }
  .halls { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: .8rem; }
  .hall {
    display: flex; gap: .8rem; align-items: flex-start; text-decoration: none; color: var(--text);
    background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: .9rem 1rem;
  }
  .hall:hover { border-color: var(--link); }
  .hall-body { min-width: 0; }
  .hall h2 { margin: 0 0 .25rem; font-size: 1.06rem; }
  .hall .desc { color: var(--muted); font-size: .82rem; line-height: 1.55; }
  .hall .figures { font-family: var(--font-mono); font-size: .75rem; color: var(--link); margin-top: .5rem; }
  /* 馆印:五馆各答一问的单字(文字承载识别,色只作强调) */
  .sigil {
    flex-shrink: 0; display: inline-flex; align-items: center; justify-content: center;
    width: 34px; height: 34px; border: 1.5px solid var(--text); border-radius: 50%;
    color: var(--text); font-family: var(--font-display); font-size: 16px; line-height: 1;
    margin-top: .1rem;
  }
  .hall:hover .sigil { border-color: var(--link); color: var(--link); }
  @media (max-width: 720px) {
    .cover-head h1 { font-size: 2rem; }
    body { padding: 1.1rem .8rem 2.5rem; }
  }
"""


def collect_counts():
    """五馆条目计数(只数 meta,不解析内容——封面只需要数字)。"""
    return {lib: sum(1 for _ in (ROOT / lib / "items").glob(pat))
            for _sigil, _name, _desc, _href, lib, pat, _unit in HALLS}


def render_index(counts):
    """封面:标题 + 五馆卡片。错题集的跨馆警示区住 mistakes 馆索引,不在此展开(见 A11)。"""
    today = date.today().isoformat()
    cards = "\n".join(
        f"""    <a class="hall" href="{href}">
      <span class="sigil" aria-hidden="true">{sigil}</span>
      <div class="hall-body">
        <h2>{esc(name)}</h2>
        <div class="desc">{esc(desc)}</div>
        <div class="figures">{counts[lib]} {unit}</div>
      </div>
    </a>"""
        for sigil, name, desc, href, lib, _pat, unit in HALLS
    )
    body = f"""  <div class="cover-head">
    <h1>atlas</h1>
    <p class="lead">地图集:馆是图上的区域,错题集是警示图层——走过的路会重新起雾,所以边走边画。</p>
    <div class="meta"><a href="PHILOSOPHY.md">设计理念</a> · <a href="README.md">README</a> · 内容不搬家,原地链接</div>
  </div>
  <div class="halls">
{cards}
  </div>"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>atlas · 馆群封面</title>
<style>{BASE_CSS}{ATLAS_CSS}</style>
</head>
<body>
<main>
{body}
  <footer>生成于 {today} · <code>python3 scripts/build-atlas.py</code>(五馆 build 之后跑)· 本页为生成物,禁止手改</footer>
</main>
</body>
</html>
"""


def main():
    counts = collect_counts()
    (ROOT / "index.html").write_text(render_index(counts), encoding="utf-8")
    detail = " · ".join(f"{lib} {counts[lib]}" for _s, _n, _d, _h, lib, _p, _u in HALLS)
    print(f"✅ 门户封面已生成:index.html | {detail}")


if __name__ == "__main__":
    main()
