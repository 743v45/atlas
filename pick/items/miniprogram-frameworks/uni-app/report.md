# uni-app

> **TL;DR**：Vue 系全端事实标准——一套代码 10+ 端、DCloud 插件市场生态最厚，框架开源（Apache-2.0）与 HBuilderX 闭源 IDE 双轨并存；微信端 Skyline 靠编译层配置透传，组件库适配参差。

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | npm latest 2.0.2-5020620260917001（2026-09-18 发布）——版本号内嵌 HBuilderX 版本段，与 HBuilderX 发布节奏绑定 | [2] |
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/dcloudio/uni-app（⭐41,614、pushed 2026-09-30，gh 2026-09-30；无 GitHub release，经 npm/HBuilderX 分发） | [1] |
| 维护活跃 | npm @dcloudio/uni-app 周下载 35,887（2026-09-22~09-28）；repo pushed 2026-09-30 | [1][2] |
| 归属 | DCloud（数字天堂），Vue 语系全端框架 | [1][6] |

## 为什么选（作为 adopt）

- **Vue 团队的全端默认答案**：一套 Vue2/Vue3 代码编译到微信/支付宝/百度/字节/QQ/快手/鸿蒙/H5/App 等 10+ 端；第三方 2025 年横评把 uni-app 列为「Vue 团队、快速交付+多端」的选择 [5]。中文教程密度与组件生态（uni-ui、uView、wot-design-uni 等）在 Vue 系里最厚。
- **插件市场是差异化生态**：DCloud 插件市场（模板/组件/uts 插件）体量远超同类框架的分发渠道，常见需求「先搜再写」的命中率是其工程效率优势（官方生态页，2026-09-30 访问）[5]。
- **Skyline 可用，走编译层透传**：uni-app 编译输出微信原生 DSL，pages.json 配 `"renderer": "skyline"` + manifest 配 `"lazyCodeLoading": "requiredComponents"` 即可在微信端开启 Skyline（DCloud 官方问答确认，2023-03 回复）[3]。
- **CLI 工程不绑 IDE**：Vue 主线支持 CLI 独立工程——编译器安装在项目下、不随 HBuilderX 升级，可在 vscode/webstorm 正常开发（官方 CLI 文档，2026-10-01 访问）[7]。

## 对比

- vs 原生：编译抽象层使微信端性能上限低于原生；Vue 语法与插件市场换来的是交付速度而非微信端极致性能 [5]。
- vs Taro：双寡头分野在语法栈（Vue vs React）与端侧重——uni-app 的 App 端有 weex/nvue 原生渲染传统，uni-app x 进一步走 uts 编译原生（见下节）；Taro 的 RN 端更成熟 [5][6]。
- vs Mpx：同出编译输出原生 DSL 的轻运行时思路，但 Mpx 的增强 DSL 面向小程序深度优化、生态小；uni-app 以 Vue 生态与插件市场取胜 [见 mpx 报告]。

## uni-app x 与主线的关系（正文辨析）

- **定位差异**：uni-app x 是新一代产品线——主语言为 UTS（TypeScript 语法超集），应用逻辑与插件均用 UTS 编写，App/Android 编译为 Kotlin、iOS 编译为 Swift、鸿蒙编译为 ArkTS，App 端原生渲染、无 js 引擎与 WebView；**而 Web/小程序端仍编译为 JavaScript**——uni-app x 的原生化红利不惠及微信端（官方文档 + 第三方解读，2025-05）[6]。
- **发布载体**：uni-app x 的版本演进与 HBuilderX（闭源免费 IDE）深度绑定（ask.dcloud 官方公告以「5.26 版本」叙述 uni-app x 更新）[3]；主线 uni-app 则框架开源（Apache-2.0）+ CLI 独立工程双轨 [1][7]。
- **选型含义**：本条目 verdict 针对主线 uni-app（微信小程序场景）；uni-app x 是「App/鸿蒙原生化」赛道的产品，微信端差异有限，按「独立 meta 才立条目」原则暂作本条正文小节，不独立立目。

## 风险与注意

- **开源框架 vs 闭源工具链的双轨心智**：框架代码 Apache-2.0 开源，但编译器主发布渠道在 HBuilderX（闭源免费、部分功能付费）；选择 uni-app = 部分接受 DCloud 工具链锁定，团队工程化（CI/自定义编译链）应优先走 CLI 路径 [1][7]。
- **Skyline 组件库适配参差**：框架层透传 Skyline 配置，但组件库各自跟进——sard-uniapp 自述「不支持 app-nvue、uni-app-x、Skyline」（2025-08，掘金 datePublished 核验 2026-10-01），TDesign uniapp 为 Skyline 单独加了 scroll-view type=list 适配；选组件库时 Skyline 兼容要逐个确认 [4]。
- **Skyline 深度适配薄**：gh 采集的 uni-app Skyline issue 数量少但扎根深（Map 组件问题 open 2026-01、Cli 项目早期不支持已关）；相比 Taro 的公开 worklet 支持，uni-app 没有等效的 worklet 编译承诺，复杂手势动画场景能力待验证（gh 2026-09-30）[4]。
- **uni-app x 的 CLI 支持程度待验证**：主线 CLI 文档成熟，uni-app x 是否/何时提供对等的 CLI 独立工程路径，官方文档未见明确承诺（查 2026-10-01）。

## 来源

1. GitHub — dcloudio/uni-app（gh 2026-09-30：⭐41,614、pushed 2026-09-30、Apache-2.0，留档 `raw/2026-09-30/gh/dcloudio-uni-app.json`）
2. npm — @dcloudio/uni-app latest 2.0.2-5020620260917001（2026-09-18）、周下载 35,887（窗口 2026-09-22~09-28，2026-10-01 查，留档 `raw/2026-10-01/gh/releases-npm-license-snapshot-2026-10-01.md`）
3. DCloud 问答 #151186 — 微信小程序 Skyline 配置方法（pages.json renderer + manifest lazyCodeLoading，2023-03 回复）+ uni-app x 版本公告 — https://ask.dcloud.net.cn/question/151186（留档 `raw/2026-09-30/web/uniapp-skyline-askdcloud.md`）
4. GitHub Issues — uni-app Skyline 相关 issue（Map 组件 open 2026-01 等，gh 2026-09-30，留档 `raw/2026-09-30/gh/uniapp-skyline-issues.json`）；组件库适配证据留档 `raw/2026-09-30/web/uniapp-skyline-tavily.md`（sard-uniapp 掘金 2025-08 自述、TDesign uniapp 适配说明；发布日期核验留档 `raw/2026-10-01/web/sard-uniapp-juejin-date-2026-10-01.md`）
5. uni-app 官网 — 生态页（插件市场/HBuilderX/uni-app x 产品矩阵，访问 2026-09-30）；掘金五方案横评（2025）
6. uni-app x 官方文档 — https://doc.dcloud.net.cn/uni-app-x/ （UTS 唯一语言、编译 Kotlin/Swift/ArkTS、小程序端编译 JS）；掘金解读（2025-05-14，留档 `raw/2026-10-01/web/uniappx-vs-uniapp-tavily-2026-10-01.json`、`raw/2026-10-01/web/uniappx-juejin-date-2026-10-01.md`）
7. uni-app 官方文档 — CLI 快速上手（编译器装项目下、不随 HBuilderX 升级）— https://uniapp.dcloud.net.cn/quickstart-cli.html（访问 2026-10-01，留档 `raw/2026-10-01/web/uniappx-cli-search2-2026-10-01.json`）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：Vue 系全端事实标准，Skyline 配置透传可用、组件库适配参差 |
