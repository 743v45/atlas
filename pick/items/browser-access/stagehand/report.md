# Stagehand

> **TL;DR**：Browserbase 官方开源的 AI 浏览器 SDK：act / extract / observe 三原语抽象页面操作，介于「裸通道」与「全自治 Agent」之间的原语层代表；⭐24,066、日更。

- **结论**：adopt（推荐）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐24,066（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-26（日更） | [1] |
| 许可证 | MIT | [1] |
| 语言 | TypeScript / Python SDK，底层跑 Playwright | [1] |

## 为什么选

- **三原语抽象**：`act`（自然语言执行）/ `extract`（结构化抽取）/ `observe`（列出可操作元素）——自研 Agent 想要页面级原语而非逐元素点击时选它 [1]。
- **填补中间层**：选型框架的第三层——通道（MCP/CLI，Agent 自己看页面）、**原语（Stagehand，代码里调 act/extract）**、自治（browser-use，给目标它自己跑）；三者是抽象层级而非竞争关系，大型系统常三层叠用。
- **生产形态现成**：配 Browserbase 云即成生产部署（自研自托管亦可，底层 Playwright）。

## 对比

见 `../comparison.md`「通道 / 原语 / 自治」三层表。

## 风险与注意

- 自然语言原语的确定性弱于显式选择器——关键流程建议 `observe` + 校验。
- 依赖底层 Playwright 的能力边界。

## 来源

1. stagehand — https://github.com/browserbase/stagehand（gh 一手数据 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录；此前调研最大遗漏项，本次补齐 |
