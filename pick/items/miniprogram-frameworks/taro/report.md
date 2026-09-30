# Taro

> **TL;DR**：React 系多端小程序事实标准——京东系活跃维护（v4.3.0，2026-09-29 发布），官方支持 Skyline 但 worklet 需半编译且长尾 bug 未清，React 团队多端场景默认答案，微信单端极致性能让位原生。

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v4.3.0（2026-09-29 发布；4.x 主线） | [2] |
| 许可证 | MIT（gh license API 报 NOASSERTION，LICENSE 原文为标准 MIT 文本，Copyright 2018 O2Team，2026-10-01 解码） | [1] |
| 仓库 | https://github.com/NervJS/taro（⭐37,704、pushed 2026-09-30，gh 2026-09-30） | [1] |
| 维护活跃 | 最新 release 2026-09-29、repo pushed 2026-09-30；npm @tarojs/taro 周下载 32,352（2026-09-22~09-28） | [2][3] |
| 归属 | 京东凹凸实验室（NervJS）维护，React 语系起家、4.x 同时支持 Vue | [1][4] |

## 为什么选（作为 adopt）

- **React 系多端的事实标准**：一套 React 代码编译到微信/支付宝/百度/字节/QQ/京东/H5/RN 等 10+ 端；第三方 2025 年横评将 Taro 列为「React 团队、多端需求」的默认答案 [4][5]。社区配套（taro-ui、京东系组件库）与国内教程密度在 React 系小程序框架里无对手。
- **工具链持续跟进**：已支持 Vite 8 + React 19 与微信小程序开发热更新，并提供全自动分包方案缓解主包 2MB 限制（官方 discussion，2025）[6]；v4.3.0 继续增强 List/WaterFlow（Skyline 时代组件）与独立分包编译 [2]。
- **Skyline 官方支持**：官方文档明确支持在微信小程序开启 Skyline（renderer/componentFramework 配置与原生一致），worklet 动画自 4.0.8 起支持——在跨端框架里对 Skyline 的跟进速度第一梯队 [4]。

## 对比

- vs 原生：Taro 的编译抽象层使微信端性能上限低于原生；追求 Skyline 极致性能（手势/worklet/长列表）时，Taro 需半编译模式且有长尾 bug（见风险），微信单端性能敏感项目应直接用原生 [4][5]。
- vs uni-app：同为双寡头，分野在语法栈——React 团队选 Taro、Vue 团队选 uni-app；uni-app 生态多 App/鸿蒙原生化路线（uni-app x），Taro 的多端广度胜在 RN 端 [5][见 uni-app 报告]。
- vs Mpx：Mpx 编译输出原生 DSL、运行时更轻，性能上限高于 Taro 的运行时方案；但 React 语法、社区体量、京东系组件生态都是 Taro 更厚 [见 mpx 报告]。

## 风险与注意

- **Skyline 长尾 bug 未清**：gh 采集的开放 issue 包括「Skyline 手势相关 API 均有 bug，目前不可用」（2026-03 更新）、自定义 tabbar 渲染不出（2026-06 更新）、Span 组件渲染成 View、navigateTo+routeType 黑屏、compileMode 打包白页等（gh 2026-09-30）[7]。微信端重度使用 Skyline 手势/tabbar 的项目，对应页面建议原生或降级 WebView。
- **worklet 需半编译模式**：使用 worklet 必须开启 experimental.compileMode 半编译并勾选「JS 编译成 ES5」，代码包体积少量增加——配置成本与包体积代价要在立项时计入 [4]。
- **运行时体积历史包袱**：Taro 3 时代「Hello World 280KB」是社区公认的运行时开销口径（Vue Mini 比较页，采集 2026-10-01）；4.x 有 tree-shaking 与半编译改进，但跨端框架的运行时不会归零，包体积敏感场景需实测（待验证：4.3.0 实际基座体积）[8]。
- **抽象层滞后窗口**：微信新特性（新组件/新 API/Skyline 增强）到 Taro 可用存在窗口期，追新需求时要评估等待或逃生舱（原生组件直接写）成本 [4][7]。

## 来源

1. GitHub — NervJS/taro（gh 2026-09-30：⭐37,704、pushed 2026-09-30；LICENSE 解码 2026-10-01，留档 `raw/2026-09-30/gh/NervJS-taro.json`、`raw/2026-10-01/gh/taro-LICENSE-decoded.txt`）
2. GitHub Releases — v4.3.0（2026-09-29，gh 2026-10-01，留档 `raw/2026-10-01/gh/taro-v4.3.0-release.md`）
3. npm — @tarojs/taro 周下载 32,352（窗口 2026-09-22~09-28，2026-10-01 查，留档 `raw/2026-10-01/gh/releases-npm-license-snapshot-2026-10-01.md`）
4. Taro 官方文档 — Skyline（仅微信端、worklet 自 4.0.8、需半编译 compileMode）— https://docs.taro.zone/docs/skyline（访问 2026-09-30，留档 `raw/2026-09-30/web/taro-skyline-docs.md`）
5. 掘金 — 「还在纠结小程序用原生还是框架？5 种方案全拆解」（2025）— https://juejin.cn/post/7647438301876191258（留档 `raw/2026-09-30/web/uniapp-skyline-support-tavily.md`）
6. GitHub Discussions #19379 — Taro 支持 Vite 8 + React 19 + 热更新 + 全自动分包（2025，留档 `raw/2026-09-30/web/taro-skyline-support-tavily.md`）
7. GitHub Issues — taro Skyline 开放 bug 集合（gh 2026-09-30 采集，留档 `raw/2026-09-30/gh/taro-skyline-issues.json`）
8. Vue Mini — 比较页（Taro 3/Remax/kbone 归类重运行时方案、Hello World 280KB 口径）— https://vuemini.org/guide/comparisons（访问 2026-10-01，留档 `raw/2026-10-01/web/package-size-tavily-2026-10-01.json`）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：React 系多端事实标准，Skyline 支持第一梯队但长尾 bug 未清 |
