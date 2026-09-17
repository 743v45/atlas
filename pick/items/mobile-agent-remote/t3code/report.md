# T3 Code

> **TL;DR**：多 CLI 统一控制面里讨论度最高（Theo 团队），但 token 消耗 3~5x 放大 bug（#7338）+ 官方自认极早期，等磨稳再看。

- **结论**：hold 观望
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/pingdotgg/t3code | — |
| 维护活跃度 | pushed 2026-09-16，⭐22,865（gh 2026-09-17） | [1] |
| 端 | iOS / Android / Web / Electron 桌面 | [1][2] |
| 包装对象 | Claude Code / Codex / Cursor CLI / OpenCode / Grok Build 等 | [1][2] |

## 为什么不选（hold 理由）

- **账单雷**：issue #7338「[Bug]: Extremely high usage」——配合 Claude Code 时 API token 消耗比原生高 3~5 倍的用户报告；对 BYO Key 用户是真金白银的损失 [2][3]。
- **官方自认极早期**：README 明写 "We are very very early… Expect bugs"、"(mostly) not accepting contributions"——不接受社区 PR 的快速迭代项目 [1][3]。
- **版本回归史**：0.0.28 引入断连（用户回退 0.0.27，「since .28 it became unusable」，2026-07-12）；某机器断网时持续重连会冻结本机全部线程的报告 [3]。
- 模型由底层 CLI 订阅决定，不是统一 BYO 池 [3]。

## 对比

- 讨论度第一、包装广度第一，但成熟度垫底——「观望与尝鲜首选」是两份口碑报告一致的定位 [3]。

## 风险与注意

- alpha 期 issue 密度极高，生产依赖前等：#7338 修复确认 + 稳定版发布 + 接受外部 PR [2][3]。

## 来源

1. GitHub 仓库 — https://github.com/pingdotgg/t3code（gh 2026-09-17：MIT、⭐22863、pushed 2026-09-16）
2. Issue #7338 — https://github.com/pingdotgg/t3code/issues/7338（已复核存在）
3. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | hold | 首次记录：token 放大 bug + alpha，半年后重估 |
