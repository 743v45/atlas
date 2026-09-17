# OpenCode Mobile (doza62)

> **TL;DR**：iOS 侧功能最全的 OpenCode 客户端（Face ID/Haptic/原生 Git），但 2026-02-25 后停更半年 + 作者自认 beta 重连问题，iOS 用户暂无可靠 BYO 客户端。

- **结论**：hold 观望
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/doza62/opencode-mobile | — |
| 维护活跃度 | **pushed 2026-02-25，⭐271（gh 2026-09-17）——半年未更新** | [1] |
| 端 | iOS / Android / Web（React Native） | [1][2] |

## 为什么不选（hold 理由）

- **停更半年**：gh API 直查最后 push 2026-02-25。此类贴上游 `opencode serve` API 的薄客户端，上游一变就失配，半年不动是硬风险 [1]。
- **作者自认 beta 且问题具体**：2026-03 作者称 "finally working (still beta quality)"；已知问题含权限请求截断、会话状态不自动刷新、重连时键盘隐藏 [2]。
- **iOS 重连顽疾**：App Store 用户反馈后台回切白屏断连、需冷启动重连（聚合口碑 [3]）。
- 部分版本无法渲染多选一审批题，任务后台静默卡死——审批闭环断裂（聚合口碑，待验证 [3]）。

## 对比

- vs dzianisv（Android adopt）：同生态同架构，但维护节奏差一档（8 月 vs 2 月）[1][2]。
- iOS 侧现状：doza62 停更、Shahfarzane 停更（2026-01-15）、KKCode/FlyCode 样本极少——**iOS 的 BYO 路线暂无可靠选项**，这是本类别当前最大空白 [2]。

## 风险与注意

- 若仍要在 iOS 试 BYO：doza62 仍是功能最全候选，需接受「停更 + beta」双重前提，并自备 Tailscale/隧道 [2][3]。
- 复活信号（重新 push、跟进上游 API 版本声明）出现时重估 [1]。

## 来源

1. GitHub 仓库 — https://github.com/doza62/opencode-mobile（gh 2026-09-17：MIT、⭐271、pushed 2026-02-25）
2. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17，作者 beta 自述）
3. 口碑调研报告 A — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md（2026-09-17，App Store 重连吐槽）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | hold | 首次记录：功能最全但停更半年压死 |
