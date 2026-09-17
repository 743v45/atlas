# Paseo

> **TL;DR**：多 Agent 异构编排第一：/paseo-handoff 跨 harness 交棒 + 零遥测自托管；代价是配置复杂度、license 文件非标准、走订阅时额度折损。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0（license 文件带自定义版权头，GitHub 识别为 NOASSERTION；正文为 Apache-2.0，gh 2026-09-17 解码确认） | [1] |
| 仓库 | https://github.com/getpaseo/paseo | — |
| 维护活跃度 | pushed 2026-09-16，⭐17,468（gh 2026-09-17） | [1] |
| 端 | iOS / Android / Web / CLI / 桌面 | [1][3] |
| 支持 harness | Claude Code / Codex / Copilot / OpenCode / Pi 等 | [1][3] |

## 为什么选（作为 trial）

- **异构编排能力独一档**：本地 daemon 调度多个 CLI，`/paseo-handoff` 让 Claude 规划、Codex 执行跨 harness 交棒；`/paseo-committee` 多 Agent 评审；worktree 并行隔离——四方对比中「跨模型调度」单项公认完胜 [3][4]。
- **隐私主张干净**：零遥测、无强制登录、本地 daemon + TCP/Tailscale 直连或可选 E2E relay [1][3]。
- **App Store 中文好评真实可查**：「非常好用，直连的速度快」（2026-05-31）、「移动CC天花板」（2026-04-15）[2]。
- **修复节奏扎实**：v0.1.65（2026-05-03）系统性修 daemon 断线、relay 重连循环、崩溃日志缺失、Apple Silicon 错装 Intel 包 CPU 100% 等 [3]。

## 为什么不是 adopt

- **Anthropic 订阅额度折损**：社区引维护者回应称 Paseo 内走 Claude Code 订阅会消耗不同 credit 池，「实际使用可能只剩一部分额度」——订阅党账单雷 [3]。
- **复杂度天然高**：daemon + 多 harness + relay 概念面大，只想手机批准单个 Claude 任务时是过度设计 [3]。
- 早期稳定性缺口有痕迹：「always ask 权限选项崩溃」（App Store 2026-05-16）；v0.1.65 修复项反向证明此前不稳 [2][3]。
- license 文件非标准 SPDX（虽正文 Apache-2.0），企业合规场景需自行确认 [1]。

## 对比

- vs Happy：Paseo 是编排层，Happy 是体验层；单 Claude/Codex 用户选 Happy 更轻 [3]。
- vs Vibe Kanban：Paseo 保留完整审批闭环与流式输出；Vibe Kanban 是任务队列粒度（见其条目）[3]。

## 风险与注意

- 并行 4+ Agent 时 daemon 有并发冲突崩溃报告（待验证，聚合口碑 [3]）。
- 本机 daemon 机器必须常开；合盖即断 [3]。

## 来源

1. GitHub 仓库 + LICENSE 解码 — https://github.com/getpaseo/paseo（gh 2026-09-17：⭐17,468、pushed 2026-09-16）
2. App Store 评论页 — https://apps.apple.com/cn/app/paseo-remote-coding-agents/id6758887924（评论 2026-04 至 2026-06）
3. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17，issue/release 经 GitHub API 复核）
4. 口碑调研报告 A — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md（2026-09-17，/paseo-handoff 编排叙事）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：编排第一但额度折损 + 复杂度限制其作为默认 |
