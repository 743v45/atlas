# AdsPower

> **TL;DR**：商业指纹浏览器（多账号矩阵场景标配）：本地 REST API 启动 Profile 返回 debug 端口供 Selenium/Playwright 接管；中文与性价比占优；个人 Agent 开发一般用不上。

- **结论**：hold（观望——场景外，非能力否定）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 桌面端商业指纹浏览器 + 本地 REST API | [1][2] |
| 定价 | 订阅制，有免费档（以官网 2026-08-27 页面为准） | [2] |
| API 模式 | `GET local.adspower.net:50325/api/v1/browser/start?user_id=X` → 返回 `data.ws.puppeteer`（WebSocket）或 `debug_port` | [1] |

## 为什么（场景外）

- **接入模式成熟**（官方文档，2026-08-27 查证）：Selenium 用 `debuggerAddress="127.0.0.1:<debug_port>"`；Playwright 用 `chromium.connect_over_cdp(ws_url)`；社区有 awesome-adspower-automation 集成指南 [1][3]。
- **定位**：多账号矩阵运营（电商、社媒）场景的性价比之选，中文本地化好；与 Multilogin 功能高度同质（Bright 2026 对比：平局，Multilogin 系统需求略优）[4]。
- **hold 理由**：商业指纹库 + 付费订阅 + 桌面端，面向的是「账号矩阵运营」而非「Agent 驱动浏览器」——个人 Agent 开发者用开源路线（Patchright/Camoufox/Donut）即可。

## 对比

见 `../comparison.md` 路线 C。与 [Multilogin](../multilogin/report.md) 二选一：性价比/中文 → AdsPower；指纹口碑/自研引擎 → Multilogin。

## 风险与注意

- Python Playwright 需走 CDP 端点接入（`connect_over_cdp`），官方文档以 JS Playwright 为主（社区反馈，2026-08-27 查证）[3]。
- 多账号矩阵灰色运营有法律与封号风险，见横评「合规边界」。

## 来源

1. AdsPower Local API – Open Browser — https://localapi-doc-en.adspower.com/docs/FFMFMf（官方文档，查证 2026-08-27）
2. AdsPower Local API 总览 — https://www.adspower.com/local-api/（访问 2026-08-27）
3. awesome-adspower-automation — https://github.com/pencil20388-eng/awesome-adspower-automation
4. 2026 年 AdsPower 与 Multilogin 对比 — bright.cn（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录；场景外，多账号矩阵场景可复评 |
