# pick — 选型对比决策库

选型对比决策库：索引 HTML（生成物）+ 各类条目独立目录——选软件工具、选表现形式、选方案，任何要「从中挑一个」的东西（`items/<类别>/<条目>/{meta.json, report.md}`）。

## 必守规则

- **写任何报告前先读 [RULES.md](RULES.md)**——目录命名、meta 字段、写作规范、横评规则都在里面。
- **数据时间是硬规则**：所有数据必须显式标注观测时间（star 注采集日期、评测注评测方与年份、价格注查询日期）。无时间戳的数据视为无效——过期数据比没有数据更危险。
- **原始数据留档（raw/）**：采集即留档到 `raw/<今日日期>/{gh,web,sessions}/`，不指望二次获取（star 会变、网页会消失、会话会被清理）——gh 通道由 refresh-stats 自动落盘；**派调研 subagent 时 prompt 必须含此条款**（RULES 第 9 节）。
- **所有 HTML 均为生成物，禁止手改**（`index.html`、`domains/*.html`、各目录 `report.html` / `comparison.html`）：本地三连 `refresh-stats → build-index → check`——`check.py` 是防漂移断言（链接/模板残留/产物新鲜度），CI 部署前必跑。meta.stats 勿手改（gh 自动维护）。
- 报告要**有理有据**：结论先行，关键论断必有 `[n]` 编号引用；不确定标「待验证」。
- **横评必须有属性对比矩阵**（条目并排成列、维度成行）+ 可选决策矩阵（`decision.json` 权重评分，注记「维度外风险以 verdict 为准」）；不能只有「场景→名字」的推荐表。
- **三层结构**：界（`domains.json` 的 `kingdoms`，已启用，域 >9 时必有）→ 域 → 类别 → 条目；新类别必须归属一个域；分层判据（类别 >30 拆分、独立 meta 才立条目）见 RULES 第 1 节。
- **两级设计树，同步变更**：项目架构决策进根目录 `DESIGN-TREE.md`（架构变更当日加节点）；每个类别一棵 `items/<类别>/decision-tree.md`（根问题/分叉/理由/落选节点，叶子 `- 叶：[名](slug/) verdict`）——build 会校验叶子与 meta verdict 一致，改 verdict/加条目必须同步树（RULES.md 第 7 节）。
- Slidev 演示放 `decks/<主题>/`，只链接报告、不复制结论。

## 部署与协作

- **push 即部署**：push 到 atlas 的 main → 根 CI 统一构建五馆（含 pick 本地三连的断言）→ deploy 到 https://743v45.github.io/atlas/pick/ （断言失败阻止上线）；生成物 HTML 一并入库。
- **调研 subagent 派单模板**：读 RULES → 挖历史会话（提取脚本导出到 `raw/`）→ gh/WebSearch 高强度调研（原始数据落 `raw/`）→ 写全套（条目/横评/决策矩阵/设计树）→ 只动自己类别目录、**禁跑 build**（并行会互相覆盖，主会话统一三连）；并行 ≤6 个防 429 限流，撞了错峰唤醒。
