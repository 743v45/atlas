# Claude in Chrome

> **TL;DR**：Anthropic 官方 Chrome 扩展（side panel + Chrome debugger API）：让 Claude 直接操作你正在用的浏览器——同 profile、同登录态、同 tab；适合日常开发调试，不适合无人值守批量。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | Chrome Web Store 扩展（side panel 交互） | [1] |
| 驱动 | Chrome 低层 `debugger` API（DevTools 同款接口） | [1] |
| 出品 | Anthropic 官方 | [1] |

## 为什么选

- **零迁移的「接管」**：操作你正在用的浏览器——同 profile、同登录态、同 tab；日常开发/调试中让 Claude 直接看着页面干活（ Lalatendu 2026 综述将其列入务实组合的「日常开发调试」位）[2]。
- **路线独特性**：与 ChatGPT Atlas（AI 整浏览器）相对——「浏览器交给 AI」vs「AI 装进浏览器」，前者保留你的全部使用上下文 [1]。

## 对比

与 [mcp-chrome](../mcp-chrome/report.md)：同样接管现有会话；本项官方出品、随 Claude 生态更新。见 `../comparison.md`。

## 风险与注意

- 扩展形态：不适合无人值守/批量任务（那是 CLI/云路线的事）。
- 绑定 Claude 生态；能力边界受 Chrome 扩展 API 限制。

## 来源

1. Claude in Chrome vs ChatGPT Atlas: Extension vs Full Browser — usecarly.com（2026）
2. Playwright MCP vs Claude in Chrome — lalatenduswain.medium.com（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录；场景限定日常调试 |
