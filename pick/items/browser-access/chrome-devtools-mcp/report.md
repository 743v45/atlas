# Chrome DevTools MCP

> **TL;DR**：Google 官方、直连活跃 Chrome 实例，performance trace / insight / 网络瀑布 / console 能力独占——前端调试与性能场景无可替代；代价是 schema 最重（≈18k token）。

- **结论**：adopt（推荐——限定调试/性能场景）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐49,750，MCP 榜第一（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-26（日更） | [1] |
| 许可证 | Apache-2.0 | [1] |
| schema 成本 | ≈18,000 token 常驻（2025-11 公开基准，主流 MCP 里最重） | [2] |

## 为什么选

- **独占能力**：performance trace、insight 分析、网络请求瀑布、console 消息——前端调试/性能场景无可替代 [1]。
- **直连活跃实例**：连接你开着的 Chrome（通过 DevTools 协议），不是新起无痕会话——「看正在发生的」是它区别于 Playwright MCP 的形态差异。
- **生态验证**：MCP 生态 star 榜第一（49.7k，gh 2026-08-27），Google 官方出品，日更。

## 对比

与 [Playwright MCP](../playwright-mcp/report.md)：调试/性能/网络 → 本项；跨浏览器测试 → 对方。schema 本项更重（18k vs 13.7k），换来 trace/网络独占 [2]。见 `../comparison.md`。

## 风险与注意

- schema 最重：单会话任务不划算，重调试场景才值回票价。
- Chromium 系限定（Firefox/WebKit 场景无解）。

## 来源

1. chrome-devtools-mcp — https://github.com/ChromeDevTools/chrome-devtools-mcp（gh 一手数据 2026-08-27）
2. Chrome DevTools MCP vs Playwright MCP: A Practical Comparison — trackingplan.com（2026，引用 2025-11 公开基准）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录；限定调试/性能场景 |
