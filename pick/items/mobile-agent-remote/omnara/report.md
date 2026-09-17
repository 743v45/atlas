# Omnara

> **TL;DR**：云托管开箱即用第一：零网络配置、审批策略引擎 + Watch 联动；代码默认过其云端是隐私代价，「停更」传言已证伪（2026-09 仍活跃）。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/omnara-ai/omnara | — |
| 维护活跃度 | pushed 2026-09-16，⭐2,852（gh 2026-09-17） | [1] |
| 端 | iOS App / Web dashboard / 终端（`pip install omnara`） | [1][2] |
| 背景 | YC S25 | [3] |

## 为什么选（作为 trial）

- **免运维首选**：Managed Cloud 一键用，无需公网 IP/隧道/自建；手机断连重连率低，网络平滑度属第一梯队（云基建支撑）[2][3]。
- **审批做成策略引擎**：高危 tool 动作多级拦截 + 手机推送；Apple Watch 联动 [2][3]。
- **「停更」传言证伪**：调研报告 B 依第三方索引判断 2025-09 后停更——gh API 直查 pushed_at=2026-09-16，项目活跃，回到现役候选 [1]。

## 为什么不是 adopt

- **默认架构代码过第三方云**：会话数据流经其托管服务器；开源版可自托管 VPC，但多数用户冲云版去，隐私口碑弱于 Happy/Paseo/CC Pocket [2][3]。
- 模型面窄：主要同步 Claude Code 会话，非跨 Agent 通用工作区；依赖终端/PTY，Windows 需 WSL（issue #72 `termios` 缺失，2025-08）[3]。
- 免费额度有限，商业化转化推得较紧（聚合口碑，待验证 [3]）。

## 对比

- vs Catnip（落选节点）：同为「本机不在场」路线，Omnara 自带云与账号体系，Catnip 绑 GitHub Codespaces [3]。
- vs Happy：Omnara 赢在免配置与 Watch；Happy 赢在 E2EE 与语音 [3]。

## 风险与注意

- 云版使用前确认代码/会话出本机的边界是否可接受；敏感仓库走自托管部署 [2][3]。

## 来源

1. GitHub 仓库 — https://github.com/omnara-ai/omnara（gh 2026-09-17：Apache-2.0、⭐2,852、pushed 2026-09-16）
2. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17，停更说法证伪记录在案）
3. 口碑调研报告 A — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md（2026-09-17）
4. 官网 — https://www.omnara.com

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：修正「停更」误判；隐私架构决定其上限 |
