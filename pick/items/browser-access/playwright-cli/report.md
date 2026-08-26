# Playwright CLI

> **TL;DR**：微软 2026 年初为 AI coding agent 发布的官方 CLI（`@playwright/cli`）：浏览器 state 存磁盘不进上下文，官方定位为 Playwright MCP 的 token 高效演进方向；发布尚新，生态待观察。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 发布 | 2026 年初（monorepo：microsoft/playwright ⭐95,168，gh 2026-08-27） | [1] |
| 许可证 | Apache-2.0 | [1] |
| 包名 | `@playwright/cli`（npm） | [2] |

## 为什么选

- **token 杀手锏**：浏览器状态存磁盘、只回传紧凑引用，常驻 schema 成本 ≈0（对比 Playwright MCP ≈13.7k、DevTools MCP ≈18k，2025-11 公开基准）[3]。
- **官方方向**：微软 2026 年明确把重心从 Playwright MCP 向 CLI 迁移（Kualitatem 2026：「Playwright MCP is Shifting to Playwright CLI」）[4]——押注它与微软路线图一致。
- **工作流**：`playwright-cli open --headed` → `snapshot` 拿元素引用 → 后续操作引用元素（与 agent-browser 的 `@e2` 思路同构）[2]。
- **零学习成本**：已用 Playwright 生态的团队直接上手。

## 对比

与 [agent-browser](../agent-browser/report.md)：思路同构；Playwright CLI 绑 Playwright 生态（对存量用户是优势），agent-browser 面向所有 CLI Agent。token 对比表见 `../comparison.md`。

## 风险与注意

- 发布仅半年余（2026 年初），API 稳定性与社区沉淀待观察。
- 迁移期内 Playwright MCP 仍在维护——不是二选一，按任务形态分层用。

## 来源

1. playwright monorepo — https://github.com/microsoft/playwright（gh 一手数据 2026-08-27）
2. Playwright CLI: The Token-Efficient Alternative to Playwright MCP — testcollab.com（2026）
3. Chrome DevTools MCP vs Playwright MCP — trackingplan.com（引用 2025-11 公开基准）
4. Playwright MCP is Shifting to Playwright CLI — kualitatem.com（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录；官方方向明确但太新，不升 adopt |
