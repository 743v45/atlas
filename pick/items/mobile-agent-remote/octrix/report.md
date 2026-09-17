# Octrix

> **TL;DR**：国产模型（DeepSeek/Kimi）手机遥控的空白位填充者，V2EX 圈内好评；但仓库无 LICENSE 文件与「全栈开源」宣称矛盾，样本少，先评估。

- **结论**：assess 评估
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | **无 LICENSE 文件**（gh API license=null，2026-09-17）——与 V2EX 主帖「全栈开源」宣称矛盾 | [1][2] |
| 仓库 | https://github.com/andforce/octrix | — |
| 维护活跃度 | pushed 2026-09-11，⭐117（gh 2026-09-17） | [1] |
| 端 | iOS / iPadOS / Mac（Apple Silicon） | [2][3] |

## 为什么关注

- **填补真实空白**：V2EX 主帖（2026-02-03）作者指出国产模型接入类 Codex CLI 后没有官方手机入口，Octrix 的聊天式遥控由此产生价值 [2]。
- 桥接十余款 CLI，对 DeepSeek/Kimi 等国产模型场景针对性最强；扫码配对（Host + Relay）；语音输入 [2][3]。
- V2EX 圈内口碑：「UI 克制、无恶心付费策略」（聚合口碑 [3]）。

## 为什么只是 assess

- **license 缺失是硬伤**：无 LICENSE 文件意味着默认版权保留，fork/自托管/二次分发的合法性存疑——「开源」宣称待作者补文件后才能采信 [1]。
- 口碑样本高度集中于 V2EX，国际社区几乎无声量；中继架构的安全、数据留存无公开审计 [2]。
- iOS 后台限制下长会话 20 分钟未交互偶发断连（聚合口碑，待验证 [3]）。

## 对比

- 国产模型 + iOS + 免费 + App 四条件目前无替代者；KKCode/FlyCode 样本更少（见 decision-tree 落选节点）[2]。

## 风险与注意

- 使用前自行审计中继代码与数据流；「全栈开源」在 LICENSE 补齐前按「源码可见」理解，不是法律意义上的开源 [1]。

## 来源

1. GitHub 仓库 — https://github.com/andforce/octrix（gh 2026-09-17：license=null、⭐117、pushed 2026-09-11）
2. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17，V2EX 主帖 2026-02-03）
3. 口碑调研报告 A — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md（2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | assess | 首次记录：空白位价值真实，LICENSE 缺失压住 verdict |
