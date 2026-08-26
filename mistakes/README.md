# mistakes — 错题集

翻车的档案馆:一次真实翻车 = 一条错题(经过 / 根因 / 修正),可追溯出处。**单一事实源**——apprentice 各课的「翻车记录」小节只留一行摘要 + 链接到这里,根因与修正的完整档案只住本馆。

失败比成功教学价值高;`recurring`(同一根因又犯)是本馆的最高警示——翻车不可怕,可怕的是翻得毫无新意。

**记录规则见 [RULES.md](RULES.md),写任何错题前先读它。**

## 结构

```
mistakes/
├── README.md / RULES.md / CLAUDE.md
├── index.html           # 错题索引(生成物,禁止手改)
├── scripts/build-index.py   # 校验门禁 + 渲染(引擎在 atlas/shared/)
├── template/            # 新错题模板(meta.json + mistake.md)
└── items/<错题>/{meta.json, mistake.md, mistake.html}   # 单层,暂不分类
```

## 快速上手

```bash
mkdir -p items/<错题>
cp template/meta.json template/mistake.md items/<错题>/
# … 记录,遵守 RULES.md …
python3 scripts/build-index.py
```
