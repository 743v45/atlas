# opencode-telegram-bot

> **TL;DR**：保活与推送全场最强（TG 通道），命令面完整；但代码全过 Telegram 云端是合规雷，diff 体验灾难——只当通知器，不当遥控器。

- **结论**：hold 观望
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/grinev/opencode-telegram-bot | — |
| 维护活跃度 | pushed 2026-09-13，⭐1,159（gh 2026-09-17） | [1] |
| 命令面 | /status /new /abort /sessions /projects /worktree /messages /revert /fork /task | [2] |

## 为什么不选（hold 理由）

- **代码资产出本机**：项目上下文、交互过程全部经 Telegram 云端存储转发——个人项目勉强，公司代码合规禁区 [2][3]。
- **diff 体验灾难**：TG 消息形态无法承载红绿 diff，大改动刷屏 [3]。
- Bot token + user ID + OpenCode Basic Auth 全是敏感凭据，bot 账号被盗 = 远程命令入口；Docker 部署下 /open /ls /attach 等功能不可用（网络命名空间限制）[2]。

## 为什么仍值得记录

- **推送/保活天花板**：TG 后台常驻网络是全场最稳的通知通道，「任务完成/中断提醒」场景无可替代；/task 支持预定任务，/revert /fork 支持从历史分叉重试 [2]。
- 定位应是 **OpenCode 的通知器/轻遥控**，与原生 App 客户端（dzianisv）组合使用而非替代 [2][3]。

## 风险与注意

- 若用：限定允许的 Telegram 用户 ID、最小权限 token、Agent 跑在隔离目录/容器、留操作日志 [2]。

## 来源

1. GitHub 仓库 — https://github.com/grinev/opencode-telegram-bot（gh 2026-09-17：MIT、⭐1,159、pushed 2026-09-13）
2. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17）
3. 口碑调研报告 A — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md（2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | hold | 首次记录：通知器价值真实，遥控器定位不成立 |
