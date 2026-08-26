# nodriver

> **TL;DR**：undetected-chromedriver 官方继任者：WebSocket 直连系统 Chrome、无中间层痕迹，直面 Cloudflare 的 Python 默认选择；维护放缓，备选社区 fork zendriver。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐4,698（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-05-13（节奏放缓） | [1] |
| 许可证 | AGPL-3.0 | [1] |
| 形态 | Python async 驱动库 | [1] |
| 前作 | undetected-chromedriver ⭐4,698，push 停在 2025-07-05（已死，勿选） | [3] |
| 社区 fork | zendriver ⭐4,698，push 2026-08-16（活跃） | [2] |

## 为什么选

- **原理**：通过 WebSocket 直连系统 Chrome 的 DevTools 端口——控制平面里没有 Playwright shim、没有 `Runtime.enable` 调用序列、没有中间件 [4]。
- **定位**：直面 Cloudflare / Imperva / hCaptcha 场景的 Python 默认选择（Scrapfly 2026 评测结论）[5]。
- **AI 接入**：纯 Python API，与 browser-use 等框架组合方便。
- **血统**：undetected-chromedriver 作者 ultrafunkamsterdam 的官方续作 [1]。

## 对比

见 `../comparison.md`。与 Patchright 互为补丁派两条路：nodriver 无中间层直连（Python），Patchright 修补 Playwright（Node/Python 双栈）。

## 风险与注意

- **维护放缓**：最后 push 2026-05-13（gh 2026-08-27 观测）；停摆时切 fork zendriver（AGPL-3.0，push 2026-08-16 活跃）[1][2]。
- **AGPL-3.0**：网络服务场景有传染性，商用注意合规。
- 单作者项目，巴士系数低。

## 来源

1. nodriver — https://github.com/ultrafunkamsterdam/nodriver（gh 一手数据 2026-08-27）
2. zendriver — https://github.com/cdpdriver/zendriver（gh 一手数据 2026-08-27）
3. undetected-chromedriver — https://github.com/ultrafunkamsterdam/undetected-chromedriver（gh 一手数据 2026-08-27）
4. Anti-Detect Browser Benchmark 2026 — ianlpaterson.com（2026 评测）
5. Best Stealth Browsers for Web Scraping in 2026 — scrapfly.io（2026 评测）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录；维护放缓故 adopt 降 trial |
