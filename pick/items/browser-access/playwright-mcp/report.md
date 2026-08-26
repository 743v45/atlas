# Playwright MCP

> **TL;DR**：微软官方 MCP、唯一成熟的跨引擎选项（Chromium/Firefox/WebKit），a11y 快照驱动；但 schema ≈13.7k 常驻、多步任务运行时成本反超，且微软投入正向 CLI 迁移。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐36,494（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-21 | [1] |
| 许可证 | Apache-2.0 | [1] |
| schema 成本 | ≈13,700 token 常驻（2025-11 公开基准） | [2] |

## 为什么选

- **跨引擎独占**：Chromium / Firefox / WebKit 三引擎，MCP 生态里唯一成熟选项；跨浏览器测试场景的默认选。
- **a11y 快照驱动**：基于无障碍树而非截图/DOM 全量，token 相对友好；支持 fresh session 与持久 profile [1]。

## 成本与去向

- **初始轻、运行重**：schema 13.7k 比 DevTools MCP 的 18k 轻，但 Trackingplan 2026 实测**多步 journey 的运行时成本反超**（逐工具往返累积）[2]。
- **官方重心迁移**：微软 2026 明示投入转向 [Playwright CLI](../playwright-cli/report.md)；MCP 仍在维护，但新能力先看 CLI。

## 对比

与 [Chrome DevTools MCP](../chrome-devtools-mcp/report.md)：跨引擎测试选本项，调试/性能/网络选对方。完整对比见 `../comparison.md`。

## 风险与注意

- 长任务 token 成本高——多步场景优先 CLI 路线。
- 关注微软路线图：MCP 与 CLI 的功能差会随时间拉大。

## 来源

1. playwright-mcp — https://github.com/microsoft/playwright-mcp（gh 一手数据 2026-08-27）
2. Chrome DevTools MCP vs Playwright MCP: A Practical Comparison — trackingplan.com（2026，引用 2025-11 公开基准）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录；能力稳但官方重心已向 CLI 迁移 |
