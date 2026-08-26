# Spec Kit（GitHub）

> **TL;DR**：spec-driven 开发的事实标准：GitHub 官方开源（⭐131,657k，MIT，2026-08-21 发布 1.0.0），constitution→specify→plan→tasks→implement→converge 把 PRD 变成 agent 可执行流程、30+ agent 通用；适合「PRD 主要给 AI 消费」的 repo 工作流，人类协作评审弱于文档平台。

- **结论**：trial（试用——在非关键路径的 repo 内工作流先跑通）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v1.0.0（2026-08-21 发布，项目满一年） | [1][2] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/github/spec-kit | [1] |
| 维护活跃度 | ⭐131,657、最近 push 2026-08-26（gh 2026-08-27 采集）；GitHub 官方维护 | [1] |
| 形态 | specify CLI + 项目内 slash 命令，兼容 30+ AI coding agent（CLI 与 IDE 均） | [1] |

## 为什么试用

- **spec-driven 是 2025-2026 最大的新范式，spec-kit 是其事实标准**：把「PRD 是给 AI 的输入」制度化——specifications 不再是写完即弃的脚手架，而是可执行、直接产出实现的一等公民（README「Specifications become executable」，gh 2026-08-27）[1]。GitHub 官方出品 + ⭐131,657k，是该流派体量与背书最强的开源实现。
- **流程完整且可收敛**：`/speckit-constitution`（项目原则，一次性）→ `/speckit-specify`（写 spec）→ `/speckit-plan` → `/speckit-tasks` → `/speckit-implement` → `/speckit-converge`（实现与 spec 对齐校验，重复至 Converged）[1]；另有 opt-in 的 bug 修复流（assess→fix→test）与 idea 评估流 [1]。
- **agent 中立**：不锁 coding agent——Copilot / Claude Code / Cursor 等 30+ 集成（`specify integration list`）[1]。对已用 Claude Code 的团队，引入的是流程纪律而非新供应商。
- **产物是 repo 内 Markdown**：spec 即版本控制资产，agent 全文检索零摩擦——正好补上飞书/Notion「agent 检索不顺手」的短板（见 [feishu-docs-base](../feishu-docs-base/report.md)）。

## 对比

- 与 Kiro：同流派（spec→design→tasks），Kiro 绑定自家 IDE 与 credits 计费、EARS 句式更严；spec-kit 开源、装进你现有的 agent——见 [kiro](../kiro/report.md)。
- 与 OpenSpec（观察名单）：OpenSpec 主打轻量、brownfield 友好（⭐131,657k，MIT，gh 2026-08-27）[3]，spec-kit 流程更重更全。

## 风险与注意

- **不是协作文档平台**：人类评审走 git PR，评论/@/审批、富文本、原型嵌入都没有——「给人读的 PRD」仍需飞书/Notion 承载，两套并行有同步成本。
- **1.0.0 ≠ 冻结**：维护者明说 1.0 只是个数字，价值从稳定性转向可适应性（manorrock 2026-08-21）[2]——流程与命令面仍会演进，升级预期要留。
- **对非开发读者不友好**：spec 面向 engineering，业务方/老板阅读体验远不如文档平台（推导自形态 [1]）。

## 来源

1. github/spec-kit README 与仓库数据 — https://github.com/github/spec-kit（gh 2026-08-27 采集）
2. Spec Kit Turns One — and Ships 1.0.0 — 维护者博客 2026-08-21，https://www.manorrock.com/blog/2026/08/21/spec_kit_turns_one.html
3. Fission-AI/OpenSpec 仓库数据 — gh 2026-08-27 采集，https://github.com/Fission-AI/OpenSpec

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录（2026 新增条目：spec-driven 范式） |
