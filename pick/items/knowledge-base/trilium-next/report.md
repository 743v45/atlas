# Trilium / TriliumNext

> **TL;DR**：自托管 Web 多端访问、Docker 部署好——但数据非纯 Markdown、AI 写入通道弱；2025-06 fork 仓库归档、项目并回原名 Trilium（原 zadam/trilium 仓库，2026-08 仍活跃发版）；多端 Web 访问刚需时才值得评。

- **结论**：assess（评估——需求不符）
- **核实日期**：2026-08-27（gh 一手数据当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 自托管 Web 笔记（Docker），层级树 + 克隆 | [1][2] |
| 许可 | AGPL-3.0 | [1] |
| 维护活跃度 | TriliumNext/Trilium ⭐37,599、push 2026-08-26；v0.105.0 发布 2026-08-19（发布者 eliandoran）（gh 2026-08-27 采集） | [1] |
| 项目沿革 | 原作 zadam 2024-01 转维护模式 → 社区 fork TriliumNext/Notes（⭐37,599，**2025-06-24 归档**）→ 项目承接原仓库更名：TriliumNext/Trilium（即原 zadam/trilium，「TriliumNext Notes will become Trilium Notes」官方讨论 #5867） | [1][3][4] |

## 为什么（未 pick）

- **唯一亮点是 Web 多端**：桌面使用为主的场景没有优势（2026-08-25 会话结论）[2]。
- **数据库形态**：文档树存自管数据库（非纯 Markdown），AI 工具链通用性差、写入通道弱（第三方 MCP server 存在但非官方主线，gh 2026-08-27 检索：triliumnext-mcp 两家 ⭐37,599/67）[2][5]。
- **沿革风险已消解但需重认识**：旧「TriliumNext/Notes」仓库归档 ≠ 项目死亡——是并回原名与主仓库的整合动作，主线在 TriliumNext/Trilium 持续活跃（月度发版，2026-08-19 v0.105.0）[1][3][4]。

## 对比

见 `../comparison.md`。多端 Web 访问 + 自托管 + 深层级知识库场景的候选；与思源同为数据库形态、但 AI 转向远不如思源激进。

## 风险与注意

- 数据库形态锁定，迁出依赖导出功能。
- 项目治理刚经历「fork → 并回原名」的整合，文档站与仓库仍在过渡（docs 仓库归档重建中，gh 2026-08-27 观测）[4]。
- 官方同步走自建 sync server（Docker），第三方托管可选 [1]。

## 来源

1. TriliumNext/Trilium — https://github.com/TriliumNext/Trilium（gh 2026-08-27 采集：⭐37,599、push 2026-08-26、AGPL-3.0、v0.105.0 于 2026-08-19 由 eliandoran 发布；README 含功能清单）
2. Claude 会话 be457b46（2026-08-25）
3. TriliumNext/Notes（fork 旧仓库）— https://github.com/TriliumNext/Notes（gh 2026-08-27 采集：archived、push 2025-06-24、⭐37,599）
4. TriliumNext Notes will become Trilium Notes — https://github.com/orgs/TriliumNext/discussions/5867（访问 2026-08-27）；How TriliumNext Revitalized an Abandoned Open Source Project — https://dosu.dev/customers/how-triliumnext-revitalized-an-abandoned-open-source-project-with-dosus-help（访问 2026-08-27）
5. triliumnext-mcp（社区 MCP server）— https://github.com/perfectra1n/triliumnext-mcp 与 https://github.com/tan-yong-sheng/triliumnext-mcp（gh 2026-08-27 采集：⭐37,599/67、push 2026-08-26/2026-03-24）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | assess | 首次记录（历史会话提取） |
| 2026-08-27 | assess | 高强度调研修订：更正项目沿革（fork 归档实为并回原名 TriliumNext/Trilium，主线活跃）；条目名与 repo 同步更正 |
