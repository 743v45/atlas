# Camoufox

> **TL;DR**：引擎级改造 Firefox（C++ 源码层伪造指纹），指纹一致性理论最强；2025 年有约一年维护断层、2026-08 已恢复日更，README 警告未撤，选它要盯紧维护公告。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐11,450（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-26（日更节奏） | [1] |
| 许可证 | MPL-2.0 | [1] |
| 形态 | 定制 Firefox 浏览器 + Python 库（Playwright API 驱动） | [1][2] |

## 为什么选

- **原理**：编译期修改 Firefox C++ 源码，`navigator`、WebGL、screen、fonts、WebRTC 等所有指纹在引擎实现层拦截伪造，借鉴 Tor / Arkenfox / CreepJS 研究 [1][2]。
- **一致性优势**：指纹从引擎层「长」出来，天然自洽——JS 注入式伪装（老 playwright-stealth 路线）只改表层属性，容易自相矛盾 [2]。
- **注入隔离**：Playwright 的注入操作（如 `window.__playwright__binding__`）被移到页面外的独立作用域，页面探测不到 [2]。

## 对比

补丁派（Patchright/nodriver）修 Chromium 痕迹、迁移成本低；Camoufox 引擎派一致性最强但要接受 Firefox 引擎差异。见 `../comparison.md`。

## 风险与注意

- **维护断层史**：README 官方警告——作者个人原因曾有约一年维护断层，基础 Firefox 版本老化 + 新发现指纹不一致问题导致对抗性能下滑（2025 年状态描述）[1]。
- **当前状态**（gh 2026-08-27）：push 2026-08-26，已恢复日更；但 README 警告未撤，建议持续盯指纹一致性公告。
- Firefox 引擎：个别对 Chromium 行为有依赖的站点兼容性需自测。

## 来源

1. Camoufox — https://github.com/daijro/camoufox（gh 一手数据 2026-08-27；README 状态警告为 2025 年内容）
2. Stealth Overview — https://camoufox.com（访问 2026-08-27）
3. The 6 best Patchright alternatives in 2026 — roundproxies.com（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录；断层已恢复但警告未撤，不升 adopt |
