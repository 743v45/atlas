# Multilogin

> **TL;DR**：商业指纹浏览器口碑领先者：自研 Mimic/Stealthfox 引擎、指纹技术行业标杆，€29/mo 起；官方 Playwright/Puppeteer/Selenium automation 文档齐全；多账号矩阵商业场景才需要。

- **结论**：hold（观望——场景外，非能力否定）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 桌面端商业指纹浏览器 + Multilogin X API | [2] |
| 定价 | €29/mo 起（ProxyHorizon 2026 评测口径） | [3] |
| 引擎 | 自研 Mimic（Chromium 系）/ Stealthfox（Firefox 系） | [3] |
| 官方自动化文档 | Playwright / Puppeteer / Selenium 示例齐全（2026-08-27 查证） | [1][2] |

## 为什么（场景外）

- **指纹口碑领先**：行业评测普遍认为其自研引擎指纹技术最扎实（ProxyHorizon 2026 评 4.5/5）[3]。
- **接入模式与 AdsPower 同构**：API 认证 → 启动 Mimic Profile → 拿 CDP 端点（`ws://...`）→ `chromium.connectOverCDP()`（官方文档）[1]；官方 GitHub 还有 automation SDK（profile farming、cookie 导入等脚本）[4]。
- **hold 理由**：与 AdsPower 相同——面向多账号矩阵商业运营，非 Agent 开发者刚需。

## 对比

见 `../comparison.md` 路线 C。与 [AdsPower](../adspower/report.md)：Multilogin 指纹口碑/系统需求略优，AdsPower 性价比/中文本地化更好（Bright 2026 对比：总体平局）。

## 风险与注意

- 商业订阅 + 指纹浏览器合规责任由使用者承担（见横评「合规边界」）。

## 来源

1. Playwright automation example — https://multilogin.com/help/en_US/playwright-automation-example（官方文档，查证 2026-08-27）
2. Multilogin X API beginner's guide — https://multilogin.com/help/en_US/multilogin-x-api-beginners-guide
3. The 8 Best Anti-Detect Browsers for AI Agents in 2026 — proxyhorizon.com（2026）
4. Multilogin X Automation SDK — https://github.com/multilogin-automation

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录；场景外，多账号矩阵场景可复评 |
