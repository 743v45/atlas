# Markdown + Git 仓库工作流

> **TL;DR**：被实际 pick 的方案：纯 Markdown + Git 仓库 + agent CLI（Claude Code）直写 + INDEX 索引驱动——AI 共建的本质是 AI 对存储层的原生访问权，本地纯文本是唯一没有中间商的形态。

- **结论**：adopt（推荐——已生产落地）
- **核实日期**：2026-08-27（自 2026-08-20/25 两次会话提取，2026-08-27 高强度调研复核）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 方案（非产品）：Git 仓库 + CLAUDE.md 规则 + INDEX.md 索引 + 原子化笔记 | [1] |
| 落地实例 | taevasidian：272 篇 md、重名 0、孤儿链接 0、三通道备份；仓库 2026-08-26 仍有推送（gh 2026-08-27 采集） | [2] |
| 调研时间 | 2026-08-20（选型）、2026-08-25（落地）、2026-08-27（复核） | [1][2][3] |

## 为什么选

- **原生访问权**：AI 对文件系统读写 / 搜索 / 批量重构无门槛；Notion 类走 API 批量读写很慢，共建体验差 [1]。
- **共建历史可回溯**：Git 天然记录「人和 AI 各自改了什么」[1]。
- **token 效率**：索引驱动（会话开始只读 INDEX、按需读文件），比全量塞库或 RAG 黑盒高效；千条以内 ripgrep 就够，RAG 被否（黑盒检索、token 效率低）[1]。
- **维护机制**（taevasidian 实例）：AI 写入自动织 `[[链接]]`（反链由阅读器自动算）+ 定期审计（AI 合并重复 / 归档过时 / 补链接）[2]。

## 2026 年的行业验证

这套「agent 直接操作本地 Markdown 仓库」的架构在 2026 年获得了**官方级背书**，不再是民间 hack：

- Obsidian CEO（kepano）2026-01 发布官方 agent skills 仓库（obsidian-markdown / obsidian-bases / obsidian-cli 等，MIT，⭐0，gh 2026-08-27 采集），明确定位「教你的 agent 使用 Obsidian CLI 与开放格式（Markdown、Bases、JSON Canvas）」[3]。
- Obsidian 1.12（2026 年中）内置官方 CLI（101 条命令，初为 Catalyst 早享），程序化操作 vault 成为官方能力 [4]。
- 第三方综述将「笔记即 agent 上下文」（notes as agent context）列为 2026 年笔记赛道的**新竞争轴线**：Bear 2.8 带 CLI + MCP server、新秀 ZenNotes MCP 原生（Ry Walker Research 2026）[5]。
- 连数据库型选手也在跟进：思源 v3.8.0（2026-08）内置 MCP 与智能体，仓库描述改为「让人与智能体在此协作」（gh 2026-08-27 采集）[6]。

即：2026 年全行业向「AI 直写存储层」收敛，本方案 2026-08 就已生产验证，属于提前踩中了方向。

## 对比

与「Obsidian 单独用」的区别：Obsidian 只是这个方案之上的**阅读器层**（见 [Obsidian](../obsidian/report.md)），随时可换、数据零迁移——这是架构核心保险 [2]。完整属性对比见 `../comparison.md`。

## 风险与注意

- 纯手工（无产品功能）：搜索 / 图谱 / 同步全靠自建组合（git + SynologyDrive）。
- 踩坑实录：SynologyDrive 会吃掉 `.git` 空目录（发生两次），解法已记入 taevasidian 库宪法 [2]。
- taevasidian 为私有仓库（⭐0），其经验对外部读者无直接可复制性——复制的是**架构**而非仓库本身（gh 2026-08-27 采集确认存在与活跃）。

## 来源

1. Claude 会话 99faa8a0（2026-08-20）「个人知识库，和 ai 共建，用什么工具管理」——选型推理
2. Claude 会话 be457b46（2026-08-25）——落地执行记录；远端 https://github.com/743v45/taevasidian（gh 2026-08-27 采集：pushed 2026-08-26）
3. kepano/obsidian-skills — https://github.com/kepano/obsidian-skills（gh 2026-08-27 采集：⭐0、MIT、创建 2026-01-02；README 定位原文）
4. OpenClaw + Obsidian CLI（Obsidian 1.12 CLI 101 命令）— https://artemxtech.substack.com/p/obsidian-cli-changed-how-my-agent（访问 2026-08-27）；官方文档 https://help.obsidian.md/cli（访问 2026-08-27）
5. Minimalist Markdown Note Apps — https://rywalker.com/research/minimalist-markdown-mac-notes（Ry Walker Research 2026，访问 2026-08-27）
6. 思源笔记 v3.8.0 发布帖（内置 MCP 和 Agent）— https://ld246.com/tag/siyuan/good（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（自历史会话提取，方案已生产验证） |
| 2026-08-27 | adopt | 高强度调研修订：补 2026 行业验证节（官方 CLI/skills/竞品 MCP 化）与 gh 采集数据 |
