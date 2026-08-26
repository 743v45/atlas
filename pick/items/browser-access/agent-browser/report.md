# agent-browser

> **TL;DR**：Vercel 出品的 Rust CLI，AI Agent 浏览器自动化的 CLI 路线领跑者（⭐41,376、日更）；`@e2` 元素引用语法 + 官方 skill 一键装进 Claude Code 等 8 个 Agent，装完即用。

- **结论**：adopt（推荐）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐41,376（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-26（日更） | [1] |
| 许可证 | Apache-2.0 | [1] |
| 语言/安装 | Rust；npm / brew / cargo 三通道 | [1] |
| 控制协议 | CDP | [2] |

## 为什么选

- **CLI 路线领跑**：评测文章里的「12k+ stars」是旧数据，gh 2026-08-27 实测 ⭐41,376——增长极快，也是「评测数据会过期」的实例 [1]。
- **token 经济学**：零常驻 schema（skill 按需加载）；`@e2` 元素引用语法压缩快照，长任务成本远低于 MCP 路线（对比见 `../comparison.md` token 成本表）。
- **生态一等公民**：官方 skill 一键装进 Claude Code、Codex、Cursor、Gemini CLI、Copilot、Goose、OpenCode、Windsurf（`npx skills add vercel-labs/agent-browser`），skill 从仓库动态拉取保持更新 [1]。
- **命令面完整**：`open/click/fill/extract/snapshot/screenshot` + `agent-browser chat "自然语言指令"`（单发/REPL，可 `--model`）[2]。
- **云地组合**：本地 CLI + 云端浏览器（Scrapfly/Browserless 均有官方对接指南）渐成模式 [3]。

## 对比

- 与 Playwright CLI：同构思路（state 存磁盘、引用元素），agent-browser 通用性更广（不绑 Playwright 生态）[2]。
- 与 MCP 路线：token 成本占优，见 `../comparison.md`。

## 风险与注意

- Vercel Labs 出品，带实验性质；迭代快意味着接口可能变。
- CDP 路线的底层限制（同源限制见知识库 Chrome 调试端口笔记）。

## 来源

1. agent-browser — https://github.com/vercel-labs/agent-browser（gh 一手数据 2026-08-27）
2. Code-First Agents – Browser CLI with agent-browser — bitbasti.com（2026）
3. Vercel Agent Browser + Cloud Browser Integration — scrapfly.io（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录 |
