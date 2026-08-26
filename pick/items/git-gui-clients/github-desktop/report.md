# GitHub Desktop

> **TL;DR**：官方免费入门款：界面最简洁但功能基础、Electron 在大仓库吃力，适合 GitHub 重度用户轻量使用。

- **结论**：trial 试用
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | release-3.6.4（2026-08-13 发布） | [2] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/desktop/desktop | — |
| 维护活跃度 | ⭐ 21,792（gh 采集 2026-08-27）；最近 push 2026-08-26（当日仍活跃）；GitHub 官方团队维护 | [1] |

## 为什么选（作为入门/轻量试用）

1. **开源 + 官方 + 维护极稳**：MIT 许可，GitHub 亲儿子，2026-08-26 仍在 push、8 月中刚发 3.6.4（gh 2026-08-27）[1][2]。不存在 bus factor 问题。
2. **上手成本全场最低**：Rockstar Developer University 2026 评测定位其为「初学者之选」[4]；界面简洁度是所有候选中公认第一梯队（2026-07-28 会话结论同）[5]。
3. **对 GitHub 工作流有原生加成**：PR/Issue 关联、GitHub 登录集成开箱即用（官网功能口径）。

## 为什么不是 adopt

1. **功能面明显窄**：交互式 rebase、高级历史搜索、多 profile 等能力缺失或弱于 Fork/Tower/SmartGit（2026-07-28 会话：「功能较基础」[5]；第三方横评同样将其归入入门档 [4]）。
2. **Electron 架构 + 大仓库吃力**：dev.to 2025 横评把 GitHub Desktop 列入「monorepo 上会吃力的 Electron 系」一组 [3]。
3. **平台覆盖窄于跨平台竞品**：仅 macOS/Windows，无 Linux 官方支持（与 GitKraken/SmartGit/Sublime Merge 相比）[1]。

## 对比

与 Sourcetree 同为免费双雄：更简洁更快上手 vs 更全功能；与付费项（Fork）相比省了 $59.99 但功能与性能均有差距。逐维度对比见 `../comparison.md`。

## 风险与注意

- 深度 Git 用户会较快触顶（无行级暂存的精细化程度不及 Sublime Merge，无 lazygit 的键位效率）。
- 大 monorepo 仓库慎用（性能证据见 [3]）。

## 来源

1. GitHub: desktop/desktop — https://github.com/desktop/desktop （gh 采集 2026-08-27）
2. GitHub Desktop Releases（release-3.6.4, 2026-08-13） — https://github.com/desktop/desktop/releases （gh 采集 2026-08-27）
3. dev.to: Best Git GUI Clients in 2025 — https://dev.to/_d7eb1c1703182e3ce1782/best-git-gui-clients-in-2025-gitkraken-sourcetree-fork-and-more-compared-4gjd （访问 2026-08-27）
4. Rockstar Developer University: 11 Best Git Clients for Developers in 2026 — https://rockstardeveloperuniversity.com/best-git-clients-for-developers （访问 2026-08-27）
5. 用户 2026-07-28 Claude 会话（Sourcetree 同类调研）— 本地会话记录

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录 |
