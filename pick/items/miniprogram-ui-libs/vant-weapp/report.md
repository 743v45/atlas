# vant-weapp

> **TL;DR**：微信原生小程序组件库事实标准——⭐18.4k、教程与 AI 语料最厚、v1.11.7 稳定可用；代价是 2024-10 起进入慢修模式，新特性基本停摆

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/youzan/vant-weapp（⭐18,457、pushed 2026-05-09，gh 2026-10-01） | [1] |
| 最新版本 | v1.11.7（2024-10-14 发版；npm @vant/weapp 1.11.7，2026-10-01 查询） | [2][3] |
| 维护活跃度 | 近一年仅依赖升级类提交（最后一个功能修复 commit 2025-04-12）；月均 npm 下载 18,870（2026-08-30→09-28） | [3][4] |
| 姊妹产品 | youzan/vant（Vue 版，⭐24,385、pushed 2026-09-29，gh 2026-09-30）——注意两者是平行产品线，Vue 主仓的活跃不代表 weapp 库在演进 | [5] |

## 为什么选（作为 adopt）

- **原生小程序赛道的事实标准**：本类别最高 star（⭐18,457，gh 2026-10-01），2017 年开源至今教程、问答与 AI 训练语料最厚——个人快速开发场景出活最快，LLM 生成 vant-weapp 代码的命中率显著高于小众库 [1]。
- **组件广度与稳定性兼得**：dist 目录实测 68 个组件目录（含配对子组件，gh 2026-10-01），v1.11.7 经大量生产项目验证；MIT 许可，商用无忧 [1][3]。
- **慢修不等于不可用**：小程序 UI 组件库形态已高度成熟，2024-10 后无新特性发布（releases 止于 v1.11.7，2024-10-14）但 npm 下载仍保持 1.9 万/月（2026-08-30→09-28 数据）——存量生态仍在大量使用与验证 [2][4]。

## 对比

- vs tdesign：vant-weapp 赢在存量生态与语料（star 10 倍差）；tdesign 赢在维护活性（1.17.0，2026-09-23 发版 vs vant-weapp 2024-10）与 Skyline 官方适配（35/57 组件，61%）——团队长期维护且押 Skyline 的项目优先 tdesign，快速出活与求稳优先 vant-weapp [2][6][7]。
- vs weui：组件规模 68 vs 22；weui 有微信官方视觉与扩展库零包体积优势，vant-weapp 是自由定制路线 [8]。
- 注意：youzan/vant（Vue）与 youzan/vant-weapp 是两个仓库、两条产品线；「Vant 4 还在活跃更新」不能作为 weapp 库的判活依据 [5]。

## 风险与注意

- **发版停滞**：releases 止于 2024-10-14（v1.11.7），2025-04 后无功能类 commit（gh 2026-10-01）——新特性需求（如 Skyline 深度适配）大概率无人响应 [2][3]。
- **Skyline 兼容靠社区**：无官方 Skyline 适配声明，issue 区有 skyline 模式下的开放 bug（:host 伪类多出样式、NavBar 不适配、popup 被键盘遮挡，2024-10 至 2025-06 报告，gh 2026-10-01）——押 Skyline 渲染的项目需先验证目标组件 [7]。
- 需要持续演进 + 官方兜底的团队，把 tdesign 作为同赛道备选（见 ../tdesign/）。

## 来源

1. GitHub 仓库 — https://github.com/youzan/vant-weapp（gh 2026-10-01：MIT、⭐18,457、pushed 2026-05-09；dist 实测 68 个组件目录）
2. Releases — https://github.com/youzan/vant-weapp/releases（gh 2026-10-01：v1.11.7，2024-10-14）
3. Commits — https://github.com/youzan/vant-weapp/commits（gh 2026-10-01：最后一个功能修复 2025-04-12，其后为依赖升级）
4. npm — https://www.npmjs.com/package/@vant/weapp（2026-10-01 查询：1.11.7 / 2024-10-14，近月下载 18,870）
5. 姊妹仓库 — https://github.com/youzan/vant（gh 2026-09-30：⭐24,385、pushed 2026-09-29，Vue 产品线）
6. npm — https://www.npmjs.com/package/tdesign-miniprogram（2026-10-01 查询：1.17.0 / 2026-09-23，近月下载 38,099）
7. Skyline 相关 issues — https://github.com/youzan/vant-weapp/issues（gh 2026-10-01 检索 "skyline"：开放 bug 3 例，2024-10～2025-06）
8. WeUI 组件库官方文档 — https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/extended/weui（访问 2026-09-30，留档 raw/2026-09-30/web/sard-ui-search.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：原生赛道事实标准，慢修模式下仍是最稳默认项 |
