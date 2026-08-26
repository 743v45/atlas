# Steel Browser

> **TL;DR**：把浏览器 API 做成开源基础设施、可自托管，自托管云浏览器首选之一；AIMultiple 2026 速度分 99 但功能分 45，功能面弱于商业云。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐7,543（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-25 | [1] |
| 许可证 | Apache-2.0 | [1] |
| 备注 | repo 已从 `steel-dev/steel` 改名 `steel-dev/steel-browser`（2026 年内） | [1] |

## 为什么选

- **开源基础设施**：浏览器 API 本体开源、可自托管，API / Python / Node SDK 控制会话舰队（APIScout 2026：对 agent builder 的开放性是主要卖点）[2]。
- **速度**：AIMultiple 2026 速度分 99（功能分 45，见风险）[3]。

## 对比

- 与 Browserbase：Steel 开源可自托管 vs Browserbase 托管省心（APIScout 2026 对比定位）[2]。
- AIMultiple 2026 综合 72，低于 Bright Data 97 / BrowserAI 87 / Anchor 82，高于 Hyperbrowser 62 [3]。
- 完整矩阵见 `../comparison.md`。

## 风险与注意

- 功能分 45（AIMultiple 2026）：观测/反检测等能力面弱于商业云 [3]。
- repo 改名史说明项目在快速演进，接口稳定性需盯 changelog。

## 来源

1. steel-browser — https://github.com/steel-dev/steel-browser（gh 一手数据 2026-08-27）
2. Browserbase vs Steel vs Hyperbrowser — apiscout.dev（2026 评测）
3. Remote Browsers: Web Infra for AI Agents Compared — aimultiple.com（2026 评测）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录 |
