# TDesign 小程序

> **TL;DR**：腾讯官方设计系统的小程序实现——2026-09 仍月度发版、57 组件中 61% 已官方适配 Skyline，一套设计语言同时覆盖微信原生与 uni-app

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/Tencent/tdesign-miniprogram（⭐1,771、pushed 2026-09-30，gh 2026-10-01） | [1] |
| 最新版本 | 1.17.0（2026-09-23；npm 同版本，2026-10-01 查询） | [2][3] |
| 组件规模 | 57 组件（官方 Skyline 适配 issue 自述「全体组件 35/57」，2026-08 更新） | [4] |
| 维护活跃度 | 月度级发版（1.16.0 2026-08-06 → 1.16.1 2026-09-09 → 1.17.0 2026-09-23）；npm 月下载 38,099（2026-08-30→09-28），本类别最高 | [2][3] |

## 为什么选（作为 adopt）

- **腾讯官方背景 + 持续演进**：Tencent 官方出品，2026 年保持月度级发版节奏（gh 2026-10-01）；同为 MIT 许可。在 vant-weapp 进入慢修后，它是原生赛道「还有人维护」的主要选项 [1][2]。
- **Skyline 是本类别唯一的官方适配线**：官方维护「🚀 Skyline：组件适配进度」跟踪 issue——35/57 组件（61%）已适配，建议 Android + 微信 8.0.49 体验完整功能（issue 更新至 2026-08-25）[4]。微信新渲染引擎迁移趋势下，这是其他候选都没有的投入 [7]。
- **双栈覆盖**：仓库自述「Wechat MiniProgram and Uniapp UI components lib」——微信原生与 uni-app 共用一套 TDesign 设计语言，多端复用场景下视觉与组件 API 一致 [1]。
- **实际使用量第一**：npm 月下载 38,099（2026-08-30→09-28），高于 @vant/weapp 的 18,870——star 落后（1,771 vs 18,457）但用量领先，属于「新一代默认项」的典型形态 [3][5]。

## 对比

- vs vant-weapp：tdesign 组件数少一档（57 vs 约 68）但全部在维护，Skyline 官方适配；vant-weapp 存量生态与语料仍最厚。新项目（尤其团队长期维护）tdesign 更稳，快速出活 vant-weapp 更顺 [2][4][5]。
- vs weui：同为腾讯出品，tdesign 是完整设计系统（含主题定制），weui 是微信原生视觉的小集合（22 组件）[4][8]。
- vs wot-design-uni / uview-plus：后两者是 uni-app 编译路线（webview 渲染），tdesign 原生实现可跟进 Skyline；代价是组件生态与社区声量小于 uni-app 侧热门库 [4][7]。

## 风险与注意

- **Skyline 适配未完成**：22/57 组件（39%）尚未适配（含 Calendar、Picker、Dialog、Swiper 等常用件，2026-08 清单）——迁移项目需对照官方进度表逐个确认 [4]。
- **star 与教程存量小**：⭐1,771（gh 2026-10-01），社区教程与 AI 语料厚度不如 vant-weapp，个人快速开发时遇到问题可参考的中文问答较少 [1][5]。
- 暗黑模式官方文档未见明确声明——「待验证」：选型前用官方主题定制文档实测（tdesign.tencent.com/miniprogram）。

## 来源

1. GitHub 仓库 — https://github.com/Tencent/tdesign-miniprogram（gh 2026-10-01：MIT、⭐1,771、pushed 2026-09-30，描述「Wechat MiniProgram and Uniapp UI components lib」）
2. Releases — https://github.com/Tencent/tdesign-miniprogram/releases（gh 2026-10-01：1.17.0 2026-09-23 / 1.16.1 2026-09-09 / 1.16.0 2026-08-06）
3. npm — https://www.npmjs.com/package/tdesign-miniprogram（2026-10-01 查询：1.17.0 / 2026-09-23，近月下载 38,099）
4. Skyline 适配进度 issue #3149 — https://github.com/Tencent/tdesign-miniprogram/issues/3149（gh 2026-10-01 抓取：35/57 已适配，更新至 2026-08-25）
5. GitHub 仓库 — https://github.com/youzan/vant-weapp（gh 2026-10-01：⭐18,457，对照数据）
6. 原始快照 — raw/2026-09-30/gh/tdesign-miniprogram.json（gh 2026-09-30）
7. WeUI/Skyline 语境 — 微信官方 Skyline 文档（留档 raw/2026-09-30/web/native-skyline-docs-weixin.md）
8. WeUI 组件库官方文档 — https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/extended/weui（访问 2026-09-30）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：官方背景 + 月度发版 + Skyline 官方适配唯一选项 |
