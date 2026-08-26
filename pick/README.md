# pick — 选型对比决策库

帮选任何东西——软件工具、表现形式、方案。宽表对比 + 属性矩阵 + 决策矩阵 + 有据报告，索引页聚合导航，各类条目独立目录存放。报告要求**有理有据**——论断有来源、数据有日期；元信息与索引由脚本自动关联，永不分叉。

**记录规则见 [RULES.md](RULES.md)，写任何报告前先读它。**

## 结构

```
tlrt/
├── README.md            # 本文件
├── RULES.md             # 记录规则（核心）
├── index.html           # 索引页（生成物，禁止手改）
├── scripts/
│   ├── build-index.py   # 聚合 meta + 渲染全部 HTML（索引/报告/横评）
│   └── refresh-stats.py # gh 一手数据 → meta.stats（star/push/license）
├── template/            # 新报告模板（meta.json + report.md）
├── items/               # 各类条目：items/<类别>/<条目>/{meta.json, report.md, report.html}
│   └── <类别>/          #   类别级：_meta.json + decision.json（可选决策矩阵）+ comparison.md → comparison.html
└── decks/               # Slidev 演示，只链接报告不复制结论
```

## 快速上手

新建一份报告：

```bash
mkdir -p items/<类别>/<条目>
cp template/meta.json template/report.md items/<类别>/<条目>/
# … 调研写作，遵守 RULES.md 第 3 节 …
python3 scripts/build-index.py   # 校验 + 渲染全部页面
```

日常查看：浏览器打开 `index.html`，卡片点击进入渲染后的报告页（带面包屑与上下篇导航）。

数据保鲜（建议周期性执行）：

```bash
python3 scripts/refresh-stats.py       # gh 刷新 star/push/license → meta.stats
python3 scripts/build-index.py         # 重建页面（stale 标记基于 collected_at）
```

## 唯一事实来源

- 条目元信息与一手数据快照只存于 `items/<类别>/<条目>/meta.json`（`stats` 由 refresh-stats.py 维护）
- 所有 HTML（`index.html`、各 `report.html`、`comparison.html`）完全由脚本生成——改 meta 或 md 后重新跑 build，不要手改
- 横评的「GitHub 活跃度速查」表从 meta.stats 自动生成（md 里写 `<!--gen:activity-table-->` 占位）
- 脚本会做校验门禁（必填字段、来源非空、verdict 合法、日期格式、正文 star 与 stats 一致性），不过门禁的报告进不了索引
