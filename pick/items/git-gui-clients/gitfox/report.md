# GitFox

> **TL;DR**：macOS 原生新秀：SwiftUI 编写、Fork 级功能对齐，€60/年订阅；v4.x 迭代快但生态年轻，值得观察再上车。

- **结论**：assess 评估
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | App Store 显示 4.1.4 (11140)（2026-04-29）；官网首页仍标 4.0.0（首页版本号滞后） | [3][1] |
| 许可证 | 闭源（Pro 订阅：€60/年 含 VAT，或 €8/月；Team €144/年/2 席；30 天全功能试用免卡） | [2] |
| 仓库 | 无公开仓库 | — |
| 维护活跃度 | 2026 年内 4.1.x 持续修复（Quick Look、线程池泄漏等）；Homebrew cask 上架分发 | [3][1] |

## 为什么进入候选（而非直接推荐）

1. **真·macOS 原生，正中用户平台**：SwiftUI 全量编写、无 Electron，diff/stage/分支/冲突全覆盖（官网口径，2026-08-27）[1]。对 darwin 用户是本类别唯一的现代原生实现。
2. **社区口碑对齐 Fork**：作者在 r/macapps 发布时称「与 Fork 功能对等」（Reddit，2025-08 前后）[4]；早期定价约 €32 一次性，现行官网已是 €60/年订阅（2026-08-27 查询）[2]——定价模型变过一次，是观察点而非减分项本身。
3. **迭代速度快**：一年多从 1.x 到 4.1.4，App Store 更新记录密集（含内存泄漏、线程池耗尽这类深水区修复）[3]。
4. **不确定项尚多，故 assess**：大仓库性能无独立评测（官方与 Reddit 均未覆盖）；订阅制下长期持有成本高于 Fork 买断（€60/年 vs $59.99 一次）；单人/小团队产品，bus factor 与 Fork 同级但历史更短（待验证）。

## 对比

vs Fork：同为轻快 mac 客户端，Fork $59.99 买断 + 10 年口碑 vs GitFox €60/年 + 原生 SwiftUI 新鲜感；vs Tower：都无 Linux，GitFox 更轻更快但功能深度不及。逐维度对比见 `../comparison.md`。

## 风险与注意

- 大仓库表现「待验证」——无第三方数据，本条是它卡在 assess 的主因。
- 订阅定价（€60/年 ≈ $65-70/年，含 VAT 口径）两年即超过 Fork 终身价。
- 仅 macOS；Windows 用户排除。

## 来源

1. Gitfox 官网（版本 4.0.0、原生宣传、brew cask） — https://www.gitfox.app （访问 2026-08-27）
2. Gitfox Plans（€60/年、€8/月、Team €144/年 2 席，Paddle 结算） — https://www.gitfox.app/plans （访问 2026-08-27）
3. App Store: Gitfox 版本记录（4.1.4, 2026-04-29） — https://apps.apple.com/app/gitfox （访问 2026-08-27）
4. Reddit r/macapps: 作者发布帖（feature parity to Fork、早期 ~€32 定价） — https://www.reddit.com/r/macapps/comments/1munkvg/after_months_of_development_ive_completed_a （访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | assess | 首次记录（2026-07-28 会话未覆盖，本轮新增候选） |
