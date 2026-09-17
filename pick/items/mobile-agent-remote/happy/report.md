# Happy

> **TL;DR**：Claude/Codex 手机遥控的高频默认：E2EE + 语音独门，跨设备续接体验最好；但 2026-01 的 Codex 移动审批失灵 issue 证明核心闭环仍会断裂。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/slopus/happy | — |
| 维护活跃度 | pushed 2026-09-16，⭐23,805（gh 2026-09-17） | [1] |
| 端 | iOS / Android / Web 原生 | [1][5] |

## 为什么选（作为 trial）

- **赛道内声量第一的默认候选**：多份调研把 Happy 列为 Claude/Codex 双代理 + BYOK + 推送审批的高频首选；`happy claude` / `happy codex` 直接接管本地会话转 remote 模式，键盘一键切回桌面 [5]。
- **E2EE + 语音是独门组合**：全链路端到端加密、可自托管 relay；语音派活场景（散步/通勤下发任务）口碑最好 [5][6]。
- **把审批和通知做成了产品**：权限请求/完成/错误推送、手机追加指令、会话跨设备续接 [5]。

## 为什么不是 adopt

- **Codex 移动审批闭环断裂史**：#503「Mobile app unable to approve Happy Codex commands」与 #489「确认/拒绝按钮无响应」（均 2026-01，现 closed）直接击穿遥控器的核心价值——审批不可靠时退化为只读进度窗 [2][4]。
- 跨设备会话保持有 bug 史：#496 手机切 Windows 端新建了会话而非恢复（closed）[3]。
- 无独立安全审计；存在 slopus/happy 与 rootux/happy 两个相近仓库、happy-coder 旧包名，迁移期有混淆风险 [5]。
- 模型锁定 Claude/Codex 两家族，不满足「任意 BYO 模型」需求 [5]。

## 对比

- vs Paseo：Happy 专精 Claude/Codex 体验与推送；Paseo 赢在异构编排但复杂度高、订阅额度有折损（见 paseo 条目）[5]。
- vs CC Pocket：Happy 走 E2E 中继开箱即用；CC Pocket 本机 Bridge 无中继但需自配 Tailscale。

## 风险与注意

- 低网速下 E2E relay 握手延迟；网络切换偶发 Machine 从列表消失（待验证，来自聚合口碑 [5]）。
- 本机 CLI 所在机器必须保持运行，合盖即断——合盖续跑需云工作区路线 [5]。

## 来源

1. GitHub 仓库 — https://github.com/slopus/happy（gh 2026-09-17：MIT、⭐23,805、pushed 2026-09-16）
2. Issue #489 — https://github.com/slopus/happy/issues/489（2026-01-28，已复核存在，closed）
3. Issue #496 — https://github.com/slopus/happy/issues/496（2026-01-30，已复核存在，closed）
4. Issue #503 — https://github.com/slopus/happy/issues/503（2026-01-31，已复核存在，closed）
5. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17）
6. 官网 — https://happy.engineering

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：体验默认项，但审批闭环 bug 史 + 模型锁定使其不满足 BYO 硬条件 |
