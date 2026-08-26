# Browserbase

> **TL;DR**：托管浏览器会话的事实「安全默认」：内置 Stealth 代理与会话管理，团队生产最省心；按量付费的外部依赖，选型取决于预算与数据边界。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 云 API（商业闭源），本地零安装 | [1] |
| 关联开源 | stagehand ⭐24,066 / mcp-server-browserbase ⭐24,066（gh 2026-08-27） | [2] |
| 定价 | 按量付费（查询日期 2026-08-27，以官网为准） | [1] |

## 为什么选

- **业界安全默认**：适合不想自研浏览器运维的团队，内置 Stealth 代理与会话管理（APIScout 2026 评测定位）[3]。
- **生态复合**：官方 MCP server + Stagehand SDK 打通「云会话 × Agent 原语」全链路；与反检测需求天然复合（Stealth 内置）[2]。
- **头部活跃**：三家头部云浏览器（Browserbase/Steel/Browserless）之一，2026 年竞争烈度高 [3][4]。

## 对比

AIMultiple 2026 综合分：**Bright Data 97 > BrowserAI 87 > Anchor 82 > Steel 72 > Hyperbrowser 62**（Browserbase 未列分，但 APIScout 2026 将其列为 safest default）[3][4]。完整云平台矩阵见 `../comparison.md`。

## 风险与注意

- 按量计费的外部依赖：成本随任务量线性增长，预算敏感场景先算账。
- 数据出域：敏感数据场景注意合规边界。
- 厂商锁定：会话/Stealth/观测能力绑定其平台。

## 来源

1. Browserbase — https://www.browserbase.com（访问 2026-08-27）
2. stagehand / mcp-server-browserbase — https://github.com/browserbase/stagehand、https://github.com/browserbase/mcp-server-browserbase（gh 一手数据 2026-08-27）
3. Browserbase vs Steel vs Hyperbrowser: Browser Infrastructure 2026 — apiscout.dev（2026 评测）
4. Remote Browsers: Web Infra for AI Agents Compared — aimultiple.com（2026 评测）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录；云依赖未实测付费生产，不升 adopt |
