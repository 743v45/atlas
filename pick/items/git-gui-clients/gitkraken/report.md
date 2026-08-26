# GitKraken

> **TL;DR**：颜值与团队协作向：免费版仅本地+公开仓库，付费 $6.99/人/月起且偏重，个人用户不推荐，跨平台团队协作再考虑。

- **结论**：hold 观望
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 版本号未公开于定价页（GitKraken Desktop 持续迭代，产品线已扩至 CLI/GitLens/Insights） | [1] |
| 许可证 | freemium 商业：Free（仅本地仓库+公开远端）、Pro $6.99/席/月（年付）、Advanced $9.99、Business $19.99、Enterprise 定制 | [1] |
| 仓库 | 无公开仓库 | — |
| 维护活跃度 | 产品化程度最高的厂商之一（桌面+CLI+IDE 插件+AI 全家桶）；官网常年挂促销（当前 40%–50% off，2026-08-27） | [1] |

## 为什么 hold（不推荐个人新采用）

1. **免费档对个人开发者近乎不可用**：仅本地仓库与公开远端，私有仓库直接锁（2026-08-27 定价页口径）[1]——多数人的真实仓库都是私有的。
2. **付费起步价是本类别订阅线最贵一档**：Pro $6.99/席/月（年付口径，另有首席位 $4.59 促销价）[1]，三年 ≈ $250，超过 Fork 终身价 4 倍。
3. **性能包袱有官方自认**：GitKraken 官方帮助中心维护着「Improve GitKraken Desktop Performance」专页，专门处理「大或复杂仓库上的缓慢/无响应」（页面更新于 2026-03）[2]；dev.to 2025 横评同样把 GitKraken 列入 monorepo 吃力组 [3]。
4. **产品方向转向平台化**：定价页重心已是 GitLens/CLI/Insights/AI credits 的全家桶 [1]，单机 GUI 用户为其平台野心买单的意味明显。

## 什么场景重新考虑（hold 的例外口）

- 团队统一采购 + 需要 Linux + 深度 Jira/GitLab/Azure DevOps 集成 + 好看的协作看板时，它是跨平台团队档的最成熟选项（2026-07-28 会话结论亦然 [5]）。

## 对比

vs SmartGit：同跨平台订阅，SmartGit 有非商业免费且 $5/人/月起，GitKraken 颜值与分支图更强 [1][4]。个人轻快需求被 Fork/GitFox 全面覆盖。逐维度对比见 `../comparison.md`。

## 风险与注意

- 定价页动态表单 + 常年促销（当前 40%/50% off 倒计时），实际成交价波动大，采购前以 checkout 为准 [1]。
- Electron 架构带来的内存占用与大仓库卡顿是长期社区议题 [2][3]。

## 来源

1. GitKraken Pricing（层级价格与免费档限制，访问 2026-08-27） — https://www.gitkraken.com/pricing
2. GitKraken Help: Improve GitKraken Desktop Performance（更新 2026-03） — https://help.gitkraken.com/notifications/desktop-performance/ （访问 2026-08-27）
3. dev.to: Best Git GUI Clients in 2025 — https://dev.to/_d7eb1c1703182e3ce1782/best-git-gui-clients-in-2025-gitkraken-sourcetree-fork-and-more-compared-4gjd （访问 2026-08-27）
4. Bytestack: Top 4 UI Git Clients Compared — https://getpi.bytestack.ai/blog/4-gui-git （访问 2026-08-27）
5. 用户 2026-07-28 Claude 会话（参考价 $5–9/席/月，本轮已核出确切价）— 本地会话记录

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录（原因：免费档私有仓库锁定 + 订阅贵 + 大仓库性能包袱） |
