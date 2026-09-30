# 微信小程序原生开发

> **TL;DR**：微信官方原生开发是微信单端与性能敏感场景的默认答案——Skyline 渲染引擎 + glass-easel 组件框架把性能天花板拉到最高、新特性首发先到原生，代价是私有语法与零多端能力。

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 微信官方小程序框架（WXML/WXSS/JS·TS + 微信开发者工具），非开源项目、无仓库与 star 概念 | — |
| 版本 | 基础库 3.x 线；Skyline 正式版随基础库 3.0.0 发布（2023-07 官方公告） | [2] |
| Skyline 端支持 | Android 8.0.33+ / iOS 8.0.34+ / 开发者工具 Stable 1.06.2307260+；Windows、Mac 未支持（规划中）、企业微信未支持（开发中）（2026-09-30 查官方兼容表） | [1] |
| 维护活跃 | 微信官方持续迭代（基础库/开发者工具滚动发版），新能力（Skyline、glass-easel、worklet）全部首发于原生 | [1][3] |

## 为什么选（作为 adopt）

- **性能天花板**：官方口径 Skyline 应用后加载速度可提升 50%+，渲染管线精简、样式局部更新、rpx 原生计算（2023-07 官方发布，2026-09-30 复核文档仍在）[2][4]。第三方 2025 年横评结论一致：「Skyline 渲染引擎已经正式稳定，配合 Worklet 动画机制，原生小程序的性能天花板又被拉高了一截」「只跑微信、对性能有要求——原生就是最优解」[5]。
- **架构换代红利**：Skyline 创建独立渲染线程并把 JS 逻辑移入 AppService 独立上下文，减少 WebView 实例开销与 JSBridge 通信；glass-easel 新组件框架（Skyline 只支持 glass-easel）替代 exparser，启动与 setData 延迟更低 [3][4]。
- **渐进迁移无门槛**：Skyline 支持按页面粒度或分包粒度开启、与 WebView 页面混跳，不支持的环境自动回退 WebView，存量项目可逐页适配 [1][4]。
- **特性首发权**：worklet 动画、手势体系、scroll-view 列表反转、WXML 子树截图等 Skyline 增强能力均先在原生 DSL 上提供；跨端框架的对应支持全部是追赶者（Taro worklet 自 4.0.8 才支持且需半编译）[4][见 taro 报告]。

## 对比

- vs Taro / uni-app：跨端框架带运行时或编译抽象层，微信单端视角下性能上限低于原生；其价值在多端复用与语法栈迁移，不在微信端性能（见 `../comparison.md` 运行时体积行）[5]。
- vs Mpx：Mpx 编译输出原生 DSL、不动运行时，性能最接近原生；但增强语法仍是二次抽象，性能敏感页面的最终答案仍是原生 [见 mpx 报告]。

## 风险与注意

- **私有语法栈**：WXML/WXSS 非 Web 标准，技能与代码资产不可迁移到 Web/App；团队若有多端预期，原生不是起点 [5]。
- **Skyline 是 CSS 子集 + 默认值差异**：默认 flex 布局与 border-box 盒模型（与 Web 默认不同）、不支持 inline 布局、不支持原生导航栏（需 `navigationStyle: custom` 自绘）、SVG 渲染与组件 animate 接口不支持；官方推荐开启「默认 Block 布局 + 默认 ContentBox」贴近 Web 习惯 [1][4]。
- **平台覆盖不全**：Skyline 在 Windows/Mac/企业微信端未支持（官方规划中/开发中，2026-09-30 查），跑多端微信矩阵的项目必须保留 WebView 兼容轨 [1]。
- **组件库生态位**：官方 weui + 云开发是第一方配套，但第三方组件库丰富度低于 Vue/React 通用生态，复杂中后台式页面开发效率低于框架方案 [5]。

## 来源

1. 微信开放文档 — Skyline 常见兼容问题（各端支持矩阵、样式兼容策略）— https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/migration/compatibility.html（访问 2026-09-30，留档 `raw/2026-09-30/web/native-skyline-docs-weixin.md`）
2. 微信开放社区公告（转载）— 「小程序新渲染引擎 Skyline 发布正式版」，随基础库 3.0.0，加载速度提升 50%+（2023-07 官方口径）— 留档 `raw/2026-09-30/web/native-skyline-tavily.md`、`raw/2026-09-30/web/native-skyline-status-tavily.md`
3. 微信开放文档 — glass-easel 适配指引（Skyline 只支持 glass-easel；WebView 端基础库 3.8.12 起支持）— https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration.html（访问 2026-09-30）
4. 微信开放文档 — Skyline 特性（渲染线程架构、CSS 精简与局部更新、页面/分包粒度混用、scroll-view reverse 等）— https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/features.html（访问 2026-09-30）
5. 掘金 — 「还在纠结小程序用原生还是框架？5 种方案全拆解」（2025，五方案横评与决策树）— https://juejin.cn/post/7647438301876191258（留档 `raw/2026-09-30/web/uniapp-skyline-support-tavily.md`）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：微信单端+性能敏感默认答案，Skyline/glass-easel 新架构性能天花板 |
