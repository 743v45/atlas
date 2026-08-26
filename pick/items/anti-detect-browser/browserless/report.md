# Browserless

> **TL;DR**：老牌 headless 浏览器基础设施：BaaS v2 / BrowserQL / REST 多 API、可 Docker 自托管；自托管路线的稳健备选，反检测不是主打。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐13,635（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-25 | [1] |
| 许可证 | NOASSERTION（自定义，商用前读条款） | [1] |
| 形态 | 云 API + Docker 自托管 | [1] |

## 为什么选

- **老牌 + 多 API**：BaaS v2 / BrowserQL / REST 多入口，自托管故事清晰（2026 调研口径）[1]。
- **与 CLI 组合**：agent-browser 官方对接指南将本地 CLI + 云端浏览器作为组合模式（Scrapfly 2026 文档）[2]。

## 对比

自托管云浏览器二选一：Steel（Apache-2.0、功能分 45）vs Browserless（自定义许可、更老牌）。见 `../comparison.md`。

## 风险与注意

- **许可证 NOASSERTION**：自定义许可，商用前必须读条款——gh license 字段 2026-08-27 观测。
- 反检测不是主打能力，强对抗场景看 Patchright/Camoufox/云 Stealth。

## 来源

1. browserless — https://github.com/browserless/browserless（gh 一手数据 2026-08-27）
2. Vercel Agent Browser + Cloud Browser Integration — scrapfly.io（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录 |
