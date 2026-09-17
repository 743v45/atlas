# CC Pocket

> **TL;DR**：小而美的 Claude/Codex 手机遥控桥：审批流与目录锁死做得最规矩，Tailscale 直连不碰云；短板是社区样本少、只覆盖两家族 CLI。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/K9i-0/ccpocket | — |
| 维护活跃度 | pushed 2026-09-15，⭐1,069（gh 2026-09-17） | [1] |
| 技术栈 | Flutter（iOS/Android）+ 桌面 Bridge Server | [1][2] |

## 为什么选（作为 trial）

- **安全工程最规矩**：`BRIDGE_ALLOWED_DIRS` 锁死 Agent 可访问目录；API Key 存 iOS Keychain / Android Keystore；`BRIDGE_API_KEY` 验证连接；SECURITY.md 独立成文 [1][2]。
- **连接路径清晰可自托管**：QR / mDNS / 手工 ws/wss / Tailscale 四种配对，官方给 Tailscale `ws://host:8765` 完整指南；代码留本机，无云中继依赖 [1][2]。
- **审批流好评集中**：一键允许/拒绝高危操作，被对比文评为「上手极简度与审批流」单项胜出 [3]。

## 对比

- 与 Happy 同为 Claude/Codex 桥接，但 Happy 走官方中继（可自托管），CC Pocket 天然本机 Bridge——对中继信任敏感时选它 [2][3]。
- 与 Paseo 比：无跨 Agent 编排，纯会话镜像；换来的是配置面小得多 [3]。

## 风险与注意

- **社区样本少**：Reddit 零活动、HN 仅 2026-03 Show HN，无长测口碑，稳定结论只能自测 [3]。
- 原生 wss 直连时手机休眠唤醒易断连需重扫 QR；本机休眠则连接全断——Tailscale + 防休眠是标配 [3]。
- Claude OAuth 需 `BRIDGE_ALLOW_CLAUDE_OAUTH=1` 手动开启，默认关 [3]。
- Windows/Linux Bridge 为实验性 [3]。

## 来源

1. GitHub 仓库 — https://github.com/K9i-0/ccpocket（gh 2026-09-17：MIT、⭐1,069、pushed 2026-09-15）
2. 安全文档 — https://github.com/K9i-0/ccpocket/blob/main/SECURITY.md
3. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17，关键论断经 GitHub API 复核）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：架构干净但缺独立长测口碑 |
