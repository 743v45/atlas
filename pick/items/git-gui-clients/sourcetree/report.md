# Sourcetree

> **TL;DR**：免费且功能全的参照系：Atlassian 出品但更新偏慢、大仓库卡顿报告多，已在用可继续，新装建议先试 Fork。

- **结论**：trial 试用
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | Mac 4.2.19（2026-07-30 构建）/ Win 3.4.31（2026-03 前后） | [1] |
| 许可证 | 免费闭源（Atlassian 专有） | [2] |
| 仓库 | 无公开仓库 | — |
| 维护活跃度 | 2026 年 Mac 版发版记录：01-11、02-21、06-04、07-30，共 4 个小版本，以修复为主（如 4.2.17 仅为修 release notes 格式 + Bitbucket API 替换） | [1][2] |

## 为什么不直接 adopt（但值得试用）

1. **免费 + 功能全，仍是「免费全功能」的参照系**：分支管理、Hg 支持（Mac）、PR 集成、内置冲突处理一应俱全 [3]。用户 2026-07-28 会话结论：已在用且免费，没必要强换 [5]。
2. **更新节奏明显放缓**：2026 年前 8 个月仅 4 个 minor 版本且多为 breakfix（含一次纯粹修 release notes 格式）[2]；对照 GitHub Desktop（2026-08-13 发 3.6.4）与 lazygit（2026-08-12 发 v0.64.1）的高频节奏，Sourcetree 处于「维护态」而非「进化态」。
3. **大仓库性能是公认短板**：Bytestack 2026 横评明确记录「部分用户报告 Sourcetree 在大仓库上变慢」[3]；dev.to 2025 横评也把 SourceTree 列入 monorepo 吃力一组 [4]。
4. **试用期定位**：新用户装它零成本、能完整体验全功能 GUI 工作流；若嫌卡或想要更轻快，升级路径就是 Fork（$59.99 买断）[5]。

## 对比

免费三杰中：功能全但慢（Sourcetree）、快而简（GitHub Desktop）、终端流（lazygit）。付费线（Fork/Sublime Merge）在性能与打磨上全面胜出。逐维度对比见 `../comparison.md`。

## 风险与注意

- 安装需 Atlassian 账号注册（历史行为，2026-08 未复测，待验证）。
- 与 Atlassian 生态（Bitbucket/Jira）绑定最深，非该生态用户感知不到额外好处。
- macOS 版要求 10.15+ [2]。

## 来源

1. Sourcetree Download Archives（版本与构建日期） — https://www.sourcetreeapp.com/download-archives （访问 2026-08-27）
2. Sourcetree Release Notes — https://product-downloads.atlassian.com/sourcetree/GUI/ReleaseNotes.html （访问 2026-08-27）
3. Bytestack: Sourcetree, GitKraken, GitHub Desktop, and Fork Compared — https://getpi.bytestack.ai/blog/4-gui-git （访问 2026-08-27）
4. dev.to: Best Git GUI Clients in 2025 — https://dev.to/_d7eb1c1703182e3ce1782/best-git-gui-clients-in-2025-gitkraken-sourcetree-fork-and-more-compared-4gjd （访问 2026-08-27）
5. 用户 2026-07-28 Claude 会话（Sourcetree 同类调研）— 本地会话记录

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录（承接 2026-07-28 会话「免费首选，但嫌卡换 Fork」结论） |
