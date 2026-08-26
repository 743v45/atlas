# Donut Browser

> **TL;DR**：开源反检测浏览器中唯一自带本地 REST API + MCP server 的孤例——「反检测 × Agent 直连」一步到位；AGPL-3.0、日更活跃。

- **结论**：trial（试用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐3,718（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-26（日更） | [1] |
| 许可证 | AGPL-3.0（云端同步 Wayfern 部分闭源） | [1][2] |
| 形态 | Profile 管理 GUI + 本地 REST API + MCP server + 同步服务 | [2] |

## 为什么选

- **给 Agent 用的反检测浏览器**：Agent 可直接通过 MCP 创建/切换指纹 Profile 再驱动浏览器——反检测与 MCP 访问合二为一，目前开源界的孤例 [2]。
- **治理干净**：零遥测、无需账号、本地优先 [2]。
- **维护活跃**：2026 年开源反检测浏览器中被评为「最活跃维护」（Nextbrowser 2026 评测），gh 数据佐证（日更）[1]。

## 对比

同类诉求（反检测 + CDP + MCP）的 Clawbrowser 仅 ⭐3,718（见同目录报告，hold）；轻量替代 stealth-browser-mcp ⭐3,718（观察名单，见 `../comparison.md`）。

## 风险与注意

- **AGPL-3.0**：传染性许可，二次开发/网络服务注意合规。
- 云端同步组件（Wayfern）部分闭源——只用本地功能不受影响 [2]。
- 体量 3.7k star，商业支持与生态弱于商业指纹浏览器。

## 来源

1. donutbrowser — https://github.com/zhom/donutbrowser（gh 一手数据 2026-08-27）
2. Open Source Antidetect Browser — https://donutbrowser.com（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录；两份调研（反检测 + 访问层）的交集孤例 |
