# Fork

> **TL;DR**：买断制里体验最好：$59.99 一次付费终身用，轻快稳定，macOS 重度终端用户的首选 GUI 辅助。

- **结论**：adopt 推荐
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | Mac 2.66.7 / Win 2.16.1（官网 CDN 下载链接观察，2026-08-27） | [1] |
| 许可证 | 闭源（专有软件，$59.99 一次性买断，评估版免费无时限） | [1] |
| 仓库 | 无公开仓库（独立开发者 Dan Pristupov） | — |
| 维护活跃度 | 两个平台持续发版（2026-08-27 观察到的当前版本号较新）；无公开 changelog 仓库，节奏只能从版本号推断 | [1] |

## 为什么选

1. **买断制 + 不限时免费评估，在订阅浪潮里独树一帜**：官网明示 $59.99、free evaluation（2026-08-27 查询），无订阅、无功能墙试用 [1]。7 月底会话与 8 月底复核价格一致，无波动。
2. **第三方评测一致点名「最均衡」**：Rockstar Developer University 2026 年评测结论「Fork 是多数开发者的最佳 Git 客户端——快、专注、staging/历史/rebase/blame/冲突工具全而不 bury 基础操作」[3]；Tower 官方横评（2026）也称其「非常能打、界面干净、藏了不少高级功能（多作者 profile 等）」[2]——竞争对手拿它当参照系本身就是背书。
3. **性能与场景匹配**：2025 年 dev.to 横评把 Fork 列入「能优雅处理大仓库」一组（对照：GitKraken/SourceTree/GitHub Desktop 在 monorepo 上吃力）[4]。对把 GUI 当辅助、主力在终端的用户，Fork 的轻快恰好是核心诉求。
4. **Reddit 社区口碑长期稳定**：r/git 2025 年「你用什么 Git 客户端」讨论中 Fork 是付费项里被点名最多的推荐 [5]。

## 对比

与免费方案（Sourcetree/GitHub Desktop）相比贵 $59.99 但换来性能与交互打磨；与 Sublime Merge（$99 买断）相比更便宜、更「常规 GUI」，Sublime 胜在极致性能与行级操作；与 Tower（$69/年 起）相比一次付费 vs 年年付。逐维度对比见 `../comparison.md`。

## 风险与注意

- 闭源、单人维护的独立软件：bus factor 风险客观存在；但自 2016 年 Beta 起持续运营 10 年（Reddit 早期推广帖可佐证 longevity [5]），2026 年仍在发版 [1]。
- 自带捆绑 Git、历史上未提供切换系统 Git 的选项（Reddit 用户抱怨，2019 年讨论；当前版本是否已支持待验证）[5]。
- 无 Linux 版；macOS/Windows 双平台 [1]。

## 来源

1. Fork 官网（版本与价格） — https://fork.dev （访问 2026-08-27）
2. Tower Blog: Best Git Client - for Mac and Windows in 2026 — https://www.git-tower.com/blog/best-git-client （访问 2026-08-27）
3. Rockstar Developer University: 11 Best Git Clients for Developers in 2026 — https://rockstardeveloperuniversity.com/best-git-clients-for-developers （访问 2026-08-27）
4. dev.to: Best Git GUI Clients in 2025: GitKraken, SourceTree, Fork, and More Compared — https://dev.to/_d7eb1c1703182e3ce1782/best-git-gui-clients-in-2025-gitkraken-sourcetree-fork-and-more-compared-4gjd （访问 2026-08-27）
5. Reddit r/git: What git client do you use (2025) — https://www.reddit.com/r/git/comments/1inut0b/what_git_client_do_you_use （访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（承接 2026-07-28 会话结论：付费首选 Fork） |
