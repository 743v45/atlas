# mcp-chrome

> **TL;DR**：接管现有 Chrome 会话（登录态/cookie/tab 全在）的代表方案，Webfuse 2026 榜单唯一推荐；但 push 停在 2026-01-06、放缓 7 个月，同类需求 Chrome DevTools MCP / Claude in Chrome 更活跃。

- **结论**：hold（观望）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐12,352（gh 采集 2026-08-27） | [1] |
| 最后 push | **2026-01-06**（放缓 7 个月） | [1] |
| 许可证 | MIT | [1] |
| 同类已死项 | BrowserMCP/mcp ⭐12,352，push 停 2025-04-24（勿选） | [1] |

## 为什么（曾经）选

- **接管现有会话**：连接用户现有的本地 Chrome——登录态、cookie、tab 全在，适合「让 Agent 用我的身份干活」；与 Playwright MCP 的 fresh session 模式互补（Webfuse 2026 榜单将其列为该场景唯一推荐）。

## 为什么现在 hold

- **节奏放缓**：star 过线但最后 push 2026-01-06（gh 2026-08-27 观测），7 个月无提交——又一条「star 是存量、push 是生命体征」的实例。
- **同类更活跃**：[Chrome DevTools MCP](../chrome-devtools-mcp/report.md)（直连活跃实例）与 [Claude in Chrome](../claude-in-chrome/report.md)（官方扩展）覆盖同一诉求且在日更。

## 对比

见 `../comparison.md`。若恢复活跃可复评为 trial。

## 来源

1. mcp-chrome / BrowserMCP — https://github.com/hangwin/mcp-chrome、https://github.com/BrowserMCP/mcp（gh 一手数据 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录；维护放缓 + 能力被更活跃项覆盖 |
