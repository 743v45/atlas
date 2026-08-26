# browser-use

> **TL;DR**：最星标的开源 AI 浏览器 Agent 框架（⭐110,825、日更、MIT）：DOM 重构 + 交互元素标注喂给 LLM，WebVoyager 89.1%；自托管或云，可作执行引擎嵌入。

- **结论**：adopt（推荐——自治层）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐110,825（gh 采集 2026-08-27），AI 浏览器 Agent 顶流 | [1] |
| 最后 push | 2026-08-26（日更） | [1] |
| 许可证 | MIT | [1] |
| 基准 | WebVoyager 89.1%（AIMultiple 2026 引述） | [2] |

## 为什么选

- **自治层代表**：LLM 规划 + 浏览器执行；把混乱 DOM 重构、标注交互元素后喂给 LLM——这是它 WebVoyager 89.1% 的方法论 [2]。
- **架构清晰**：`Agent` 编排层 / `Browser` 会话层 / `Tools` 扩展层三层模型；可作为执行引擎嵌入自研工作流，而非只能整只使用 [1][2]。
- **部署灵活**：Python 库自托管或用其云；MCP server 是它的通道之一（见横评观察名单）。

## 对比

「通道 / 原语 / 自治」三层里的自治层——给目标它自己跑。与 [Stagehand](../stagehand/report.md)（原语层）互补而非竞争。见 `../comparison.md`。

## 风险与注意

- 自治 = 不确定性：关键业务流程要加校验与护栏。
- LLM 成本与延迟随步数增长。

## 来源

1. browser-use — https://github.com/browser-use/browser-use（gh 一手数据 2026-08-27）
2. Best 30+ Open Source Web Agents in 2026 — aimultiple.com（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录 |
