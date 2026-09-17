# Zedra

> **TL;DR**：技术上最有含金量：Rust+GPUI 120fps + Iroh QUIC 纯 P2P 零中继；但官方自认早期 breaking changes，中文输入法有适配问题，先评估再动。

- **结论**：assess 评估
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/tanlethanh/zedra（报告 B 称迁至 deltaqdev/zedra，gh API 显示 canonical 名仍为 tanlethanh/zedra，迁移说法待验证） | [1] |
| 维护活跃度 | pushed 2026-09-15，⭐223（gh 2026-09-17） | [1] |
| 端 | iOS / Android 客户端 + macOS/Linux/Windows daemon | [1][2] |
| 技术栈 | Rust + GPUI（Zed 引擎）+ Iroh（QUIC/UDP） | [1][2] |

## 为什么关注

- **信任模型全场最优**：出站优先 QUIC/UDP P2P 直连，无需公网 IP 与端口转发；官方 README 称凭证不离开设备、TLS 1.3 端到端 [1][2]。
- **性能天花板**：GPUI GPU 渲染，HN/Reddit 好评「20 万行代码库滑动如丝」；真原生编辑器 + 全功能终端，非网页套壳 [3][4]。
- 切网/短休眠后无感重连（QUIC 特性）[4]。

## 为什么只是 assess

- **官方自认早期**：README 明写 "Zedra is early… bugs, rough edges, and breaking changes should be expected"；完整零信任安全模型是 "near future"——安全宣称与成熟度不一致 [1][2]。
- **中文输入法适配瑕疵**：GPUI 移动端 IME 有吞字/无法选词的用户反馈（聚合口碑，对中文用户是一票否决级风险，待自测）[4]。
- 对称 NAT/CGNAT 环境回退 relay——家庭网络下并非始终直连 [2]。
- 声量小（⭐223）、无独立审计、Android beta 分发 [2]。

## 对比

- vs CC Pocket：同为「不信任中继」路线，Zedra 用 P2P 彻底消灭中继，CC Pocket 用本机 Bridge + Tailscale；后者成熟度更高 [2]。

## 风险与注意

- 「迁移到 deltaqdev/zedra」说法未证实，引用仓库地址时以 GitHub API canonical 名为准 [1]。
- 仓库迁移/早期项目 breaking changes 风险：不作为关键会话唯一入口 [2]。

## 来源

1. GitHub 仓库 — https://github.com/tanlethanh/zedra（gh 2026-09-17：MIT、⭐223、pushed 2026-09-15）
2. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17）
3. HN 讨论 — https://news.ycombinator.com/item?id=48420833（Show HN，2026 年中）
4. 口碑调研报告 A — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md（2026-09-17，GPUI 性能口碑与中文输入法问题）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | assess | 首次记录：技术路线最优，等 IME 适配与稳定化 |
