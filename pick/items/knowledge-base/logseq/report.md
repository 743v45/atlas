# Logseq

> **TL;DR**：开源大纲式双链笔记，本地文件形态、AI 可直写——次选；2.0（2026-07 beta）转向 SQLite 数据库版、文件版 OG 并行维护，页面阅读型知识库场景仍弱于 Obsidian。

- **结论**：assess（评估——备选）
- **核实日期**：2026-08-27（gh 一手数据 + 官方公告当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 大纲式（outliner）本地笔记 | [1][2] |
| 许可 | AGPL-3.0 开源 | [2] |
| 维护活跃度 | ⭐44,642、push 2026-08-26；近期发布 2.0.1（2026-07-13，DB 版 beta）、nightly（2026-08-26）（gh 2026-08-27 采集） | [2] |
| 版本分裂 | 2.0 = 数据库版（SQLite）beta；文件版现称 Logseq OG（Markdown），官方表态两者长期并行、目标功能对齐（2026 公告） | [3][4] |

## 为什么（未 pick）

- **数据形态（OG 模式）达标**：本地纯 Markdown 文件，AI 友好度与 vault 方案同源 [2]。
- **场景错位**：大纲 / 日记流为主的使用范式，与用户「页面阅读为主 + 全文搜索辅助」的主用法不符（2026-08-25 会话结论）[2]。
- **2.0 的数据库转向添变数**：主线开发重心移向 SQLite 数据库版（Datalog 查询、高级查询能力），文件版 OG 并行维护——若选 Logseq 做 AI 直写，需明确锁 OG 模式；社区对 2.0 beta 的稳定性亦有保留（HN 2026-07 讨论：「多年停滞后的改贩是数据库」）[3][4]。

## 对比

见 `../comparison.md`。它是 Obsidian 的开源替代候选（在意开源协议时首选）；数据形态上 OG/2.0 双轨是它与 Obsidian（纯 md 一条道）的关键差异。

## 风险与注意

- AGPL-3.0（对个人使用无影响）。
- 2.0 双轨并行：功能不对齐期 OG 模式可能沦为二等公民（官方称长期支持，待验证）[3]。
- 953 个 open issues（gh 2026-08-27 采集），历史质量口碑一般（HN 2026-07：「buggy mess」评价并存）[2][4]。

## 来源

1. Logseq — https://logseq.com（访问 2026-08-27）
2. logseq/logseq — https://github.com/logseq/logseq（gh 2026-08-27 采集：⭐44,642、push 2026-08-26、AGPL-3.0、2.0.1 发布 2026-07-13）
3. Big update: Logseq is splitting into two versions — https://logseq.io/p/e3YDyX5AYr（官方公告，访问 2026-08-27）；Why the database version and how it's going — https://discuss.logseq.com/t/why-the-database-version-and-how-its-going/26744（访问 2026-08-27）
4. Logseq 2.0 Beta (DB version) is here — https://news.ycombinator.com/item?id=48896229（HN 2026-07，访问 2026-08-27）；Logseq OG (markdown) vs Logseq (DB:sqlite) — https://discuss.logseq.com/t/logseq-og-markdown-vs-logseq-db-sqlite/34608（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | assess | 首次记录（历史会话提取） |
| 2026-08-27 | assess | 高强度调研修订：补 gh 活跃度、2.0 数据库版转向与 OG/2.0 双轨事实 |
