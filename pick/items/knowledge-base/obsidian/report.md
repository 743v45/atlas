# Obsidian

> **TL;DR**：被 pick 为 taevasidian 的阅读器层：本地纯 Markdown、[[双链]] 是文件层面机制、反链/图谱为核心功能——只当阅读器用（随时可换），不做写入通道；2026 年官方 CLI 与 agent skills 落地，这一架构方向获官方背书。

- **结论**：adopt（推荐——限定阅读器角色）
- **核实日期**：2026-08-27（官网定价/路线图/CLI 文档当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 桌面 / 移动阅读器 + 编辑器 | [1] |
| 许可与价格 | 本体免费无限制、无需注册；Commercial $50/人/年**可选**（「Obsidian is now free for work」）；Sync $4/人/月（年付，$5 月付）；Publish $8/站/月（年付）（2026-08-27 官网查询） | [1] |
| 版本线 | 1.9（2025-08-18 公测版）引入 Bases 核心插件 → 1.10 Bases API → 1.12（2026 年中）官方 CLI → 1.13（2026-07）；2026 路线图已落地 Airtable 导入（2026-08）、iOS Share Sheet（2026-07）等 | [2][3][4] |
| 开源参考 | 本体闭源；官方帮助库 obsidianmd/obsidian-help ⭐1,893、push 2026-08-25（gh 2026-08-27 采集，仅作维护活跃参考） | [5] |

## 为什么选

- **不锁格式、不建数据库**：打开同一目录即可，纯 Markdown 文件——这是它胜出的根本 [6]。
- **双链是文件层机制**：`[[wiki链接]]` + 反链面板 / 图谱为核心功能不靠插件；双链只写一次，反链自动算 [6]。
- **Bases 不破坏纯文本形态**：数据库视图（表格/卡片）由 `.base` 文件 + 笔记 YAML 属性驱动，「所有数据仍由本地 Markdown 文件与 YAML 属性承载」（官方 1.9 发布说明）——表里如一的本地优先 [3]。
- **生态最大**：插件层（Dataview 等）可加不强求；2026-05 上线新社区目录与自动审核，插件上架缩短至 24 小时内（kepano，2026-05-12）[2][7]。
- **角色边界**（架构核心保险）：Obsidian 只是阅读器，Claude Code 是写入口——阅读器随时可换、数据零迁移 [6]。

## 2026 年的关键变化：官方拥抱 agent

- **官方 agent skills**：CEO kepano 2026-01 发布 [obsidian-skills](https://github.com/kepano/obsidian-skills)（MIT，⭐47,329，gh 2026-08-27 采集），教 Claude Code / Codex / OpenCode 等 agent 使用 Obsidian 风格 Markdown、Bases、JSON Canvas 与 Obsidian CLI [4]。
- **官方 CLI**：1.12 起 101 条命令可程序化操作 vault（含 bases 命令组），Catalyst 早享首发 [4]。
- **Headless 同步客户端**：2026-02 路线图落地，CLI 下无桌面端同步 vault（obsidianmd/obsidian-headless，gh 2026-08-27 采集确认存在）[2]。
- 含义：本选型「Claude Code 写文件、Obsidian 只读」的分工，从民间用法变成了官方支持的方向——阅读器层的长期风险显著下降。

## 对比

vs Logseq / 思源 / Trilium / Outline / Notion：见 `../comparison.md`。核心分野是**数据形态**（纯 Markdown vs 应用自管数据库）与 **AI 写入通道**。

## 风险与注意

- 官方同步收费且未采用——同步走自建（git / SynologyDrive），有踩坑（见 [markdown-git-vault](../markdown-git-vault/report.md)）。
- 商业闭源软件：本体免费 + 商业许可可选的现行政策（2026-08-27 查询）缓解了成本风险，但闭源演进方向仍不可控——这正是「只当阅读器、随时可换」保险存在的原因。
- CLI / agent skills 为 2026 新能力，接口仍在快速迭代（early access 起步），生产使用需盯版本（待验证：CLI 正式版覆盖面）。

## 来源

1. Obsidian Pricing — https://obsidian.md/pricing（访问 2026-08-27）
2. Obsidian Roadmap — https://obsidian.md/roadmap（访问 2026-08-27）
3. Obsidian 1.9.0 / 1.9.10 Changelog — https://obsidian.md/changelog/2025-08-18-desktop-v1.9.10（访问 2026-08-27）
4. kepano/obsidian-skills — https://github.com/kepano/obsidian-skills（gh 2026-08-27 采集）；Obsidian CLI — https://help.obsidian.md/cli 与 https://artemxtech.substack.com/p/obsidian-cli-changed-how-my-agent（访问 2026-08-27）
5. obsidianmd/obsidian-help — https://github.com/obsidianmd/obsidian-help（gh 2026-08-27 采集）
6. Claude 会话 be457b46（2026-08-25）——14+9 问设计树遍历与落地执行记录
7. kepano on X（Obsidian Community 发布）— https://x.com/kepano/status/2054287387199754246（2026-05-12，访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（历史会话提取） |
| 2026-08-27 | adopt | 高强度调研修订：核实 2026 定价（商业许可可选化）、Bases 版本线、官方 CLI 与 agent skills；TL;DR 同步更新 |
