# WeUI

> **TL;DR**：微信官方视觉组件库——扩展库引入不占包体积是独门优势，但仅 22 组件、更新缓慢，只适合轻量场景或对官方视觉有硬要求的界面

- **结论**：trial 试用
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | weui-miniprogram：MIT；weui-wxss：腾讯格式 LICENSE 文件注明「源码以 MIT 许可发布」（gh 识别为 NOASSERTION，2026-10-01 解码原文确认） | [1][2][9] |
| 仓库 | https://github.com/wechat-miniprogram/weui-miniprogram（⭐2,429、pushed 2026-04-28，gh 2026-10-01）；样式库 https://github.com/Tencent/weui-wxss（⭐15,278、pushed 2026-03-12） | [1][2] |
| 最新版本 | npm weui-miniprogram 1.5.6（2024-11-15；2026-10-01 查询）；GitHub releases 止于 v1.0.8（2021-04-14） | [3] |
| 维护活跃度 | 仓库仍有 push（2026-04-28）但发版缓慢：npm 末版 1.5.6（2024-11-15）后近两年无发版；月下载 2,341（2026-08-30→09-28）——数值偏低主因是扩展库方式不经过 npm | [1][3] |

## 为什么选（作为 trial）

- **微信官方设计与小程序团队出品**：官方文档自述「由微信官方设计团队和小程序团队为微信小程序量身设计」，「微信内部多个小程序项目已经使用」——与微信原生控件的视觉/交互一致性没有替代品 [4]。
- **扩展库引入不占包体积（独门优势）**：官方文档明确「支持扩展库引入，不占用小程序包体积」——对 2MB 主包红线敏感的小程序，这是其他任何组件库都给不了的 [4]。
- **组件少且更新慢，只够轻量场景**：src/components 实测 22 个组件目录（gh 2026-10-01），远少于其余候选（57–142）；npm 发版以年计——完整App级界面应选其他库，weui 适合工具类轻界面、表单页、或只用其个别控件（msg、dialog、uploader 等）[3][5]。

## 对比

- vs vant-weapp / tdesign：weui 组件少一个量级（22 vs 57–68）但视觉是「微信亲儿子」；后两者适合整体 UI 框架，weui 更像「官方控件补丁包」[4][5]。
- vs firstui：firstui 主打颜值与模板且商业收费，weui 官方免费——两者不在同一价值轴上 [6]。

## 风险与注意

- **Skyline 兼容无官方声明**——「待验证」：官方文档与 issue 区均未检索到 weui 组件的 Skyline 适配结论（gh/官网检索 2026-09-30～10-01），押 Skyline 前先实测。
- **演进停滞风险**：weui-wxss 样式库 pushed 2026-03-12、组件库发版以年计（2026-10-01 核实）——不建议围绕它做深度定制架构 [1][2][3]。
- 许可证注意：gh API 将 weui-wxss 标为 NOASSERTION，解码后为「腾讯开源惯例文件，源码 MIT」——合规可商用，但引用时注明自定义 LICENSE 文件 [9]。

## 来源

1. GitHub 仓库 — https://github.com/wechat-miniprogram/weui-miniprogram（gh 2026-10-01：MIT、⭐2,429、pushed 2026-04-28；src/components 实测 22 组件目录；releases 止于 v1.0.8 2021-04-14）
2. GitHub 仓库 — https://github.com/Tencent/weui-wxss（gh 2026-10-01：⭐15,278、pushed 2026-03-12）
3. npm — https://www.npmjs.com/package/weui-miniprogram（2026-10-01 查询：1.5.6 / 2024-11-15，近月下载 2,341）
4. 微信官方文档 WeUI 组件库 — https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/extended/weui（访问 2026-09-30：「支持扩展库引入，不占用小程序包体积」，留档 raw/2026-09-30/web/sard-ui-search.md）
5. 组件实测 — raw/2026-10-01/gh/ui-libs-component-counts2.md（gh 2026-10-01）
6. FirstUI 对照 — raw/2026-09-30/web/firstui-price.md（查询 2026-09-30）
7. 原始快照 — raw/2026-09-30/gh/weui-miniprogram.json、weui-wxss.json（gh 2026-09-30）
8. TDesign 对照 — https://github.com/Tencent/tdesign-miniprogram/issues/3149（gh 2026-10-01）
9. weui-wxss LICENSE 解码 — raw/2026-10-01/gh/weui-wxss-license-decode.md（gh 2026-10-01：「source code is licensed under the MIT License」）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：官方视觉 + 零包体积独门，组件少更新慢只做轻量场景 |
