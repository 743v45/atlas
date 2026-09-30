# 小程序开发框架 · 横评

> 主题：微信小程序的应用逻辑用什么写——原生、React 系、Vue 系、增强型还是 DSL 转换型，六条路线。
> 用户画像：通用视角按场景分流——个人快速开发 / 团队长期维护 / 多端复用三场景；**主评微信端表现**，「多端能力」为独立参考列、不计入决策矩阵权重（口径见 decision.json note）。
> 数据核查日：2026-09-30（gh API star/pushed/license）与 2026-10-01（release/npm/下载量/LICENSE 解码/口碑补查）；原始留档 `raw/2026-09-30/gh/`、`raw/2026-09-30/web/`、`raw/2026-10-01/gh/`、`raw/2026-10-01/web/`。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| 个人快速开发·微信单端 | **原生开发** | 官方工具直出、Skyline 渐进开启，无抽象层调试成本 [1][5] |
| 个人快速开发·有 Web/App 预期 | **uni-app**（Vue 栈）或 **Taro**（React 栈） | 语法迁移成本最低，多端出口现成 [5] |
| 团队长期维护·微信为主+可能多端 | **Taro**（React 团队）/ **uni-app**（Vue 团队） | 双寡头：活跃维护+生态最厚，v4.3.0 / 周下载 3.2 万、3.6 万 [2][3] |
| 团队长期维护·纯微信性能敏感大业务 | **原生**（或 **Mpx** 换工程化） | Skyline 性能天花板只有原生够得着；要响应式/状态管理再上 Mpx [1][4] |
| 多端复用·含 App/鸿蒙 | **uni-app** | 10+ 端覆盖最广，uni-app x 走 UTS 编译 Kotlin/Swift/ArkTS [3] |
| 多端复用·小程序矩阵为主 | **Taro** / **Mpx** | Taro 生态最厚；滴滴级复杂业务、性能敏感选 Mpx [2][4] |
| 存量微信/支付宝 DSL 互转 | ~~mor~~ 谨慎 | 能力对口但公开维护近乎停摆（稳定版 2024-05、npm 周下载 13），先评估自维护 [6] |
| 存量 Web 项目搬小程序（过渡） | ~~kbone~~ 不建议新项目 | 社区共识「别拿它做新项目」[5][7] |

## 属性对比矩阵

| 维度 | 原生开发 | Taro | uni-app | Mpx | morjs | kbone |
|---|---|---|---|---|---|---|
| 形态 | 官方原生框架 | 编译型跨端框架 | 编译型跨端框架 | 增强型编译框架 | DSL 转换框架 | Web 同构适配层 |
| 语法 | WXML/WXSS/JS·TS | React/Vue | Vue2/Vue3 | 类 Vue 增强 DSL | 微信/支付宝 DSL | Web 框架(Vue/React) |
| 多端能力（参考列） | 仅微信端 | 小程序×10+·H5·RN [2] | 10+端·含App/鸿蒙 [3] | 小程序多端+Web·RN [4] | 小程序×8+·Web [6] | 微信+Web 双端 [7] |
| Skyline 适配 | 原生·性能天花板 [1] | 官方支持·worklet 需半编译·长尾 bug 未清 [2] | 支持·配置透传·组件库适配参差 [3] | 选项式 API 可用·组合式 worklet 受限 [4] | 待验证·无公开文档 [6] | 不支持·WebView 同构与 glass-easel 体系不兼容 [7] |
| 运行时/包体积 | 0（基线） [5] | 带运行时（Taro3 口径 Hello World 280KB；4.x 有优化待实测）[2][8] | 带编译产物开销（官方自测口径 87KB）[9] | 最轻一档（官方自测口径 51KB）[9] | ≈0（转换即原生 DSL）[6] | 最重（官方自测口径 368KB）[9] |
| 维护活跃（pushed / release） | 官方滚动发版 | pushed 2026-09-30 / v4.3.0（2026-09-29）[2] | pushed 2026-09-30 / npm 2026-09-18 [3] | pushed 2026-09-29 / v2.11.1（2026-07-22）[4] | pushed 2025-11-06 / v1.0.113（2024-05-21）[6] | pushed 2025-10-20 / 无 release [7] |
| ⭐（gh 2026-09-30） | —（非开源） | 37,704 | 41,614 | 3,940 | 2,113 | 4,919 |
| npm 周下载（2026-09-22~28） | — | 32,352 [10] | 35,887 [10] | 2,114 [10] | 13 [10] | —（主包无独立下载量口径） |
| 归属背书 | 微信官方 | 京东凹凸实验室 | DCloud | 滴滴 | 饿了么（阿里系） | 腾讯 |
| 许可 | 平台绑定·闭源 | MIT（NOASSERTION 已解码）[2] | Apache-2.0 [3] | Apache-2.0 [4] | MIT [6] | BSD-3-Clause（NOASSERTION 已解码）[7] |
| verdict | **adopt** | **adopt** | **adopt** | trial | assess | hold |

## 本类别四条结构性结论（2026-09-30/10-01 快照）

1. **Skyline 把性能差距重新变回原生的护城河**：Skyline 随基础库 3.0.0 转正（2023-07 官方口径加载提升 50%+），2025 年第三方横评结论「Skyline 正式稳定后原生性能天花板最高」；跨端框架跟进全都打了折扣——Taro worklet 要半编译且手势 API 有「目前不可用」的开放 bug（gh 2026-09-30），uni-app 无等效 worklet 承诺，kbone 架构性无缘 [1][2][3]。
2. **跨端框架收敛为双寡头，第一代方案全是死分支**：WePY（2026-03 归档）、mpvue（2022-03 停更）、Remax（2024-03 归档）、Chameleon（2023-01 归档）全部出局，活下来的 taro/uni-app 各自绑定 React/Vue 语法栈——选框架先选语法栈，再在双寡头里二选一 [5]。
3. **运行时架构决定包体积与性能上限的序列**：编译输出原生 DSL（mor/mpx，≈0~51KB）优于带运行时的抽象层（uni-app 87KB / Taro 156KB 口径 / kbone 368KB，均为约 2020 官方自测、方向性参考）；Taro 的半编译、uni-app 的编译模式都是往「编译型」靠拢的自我修正 [9]。
4. **license 坑在腾讯系自定义 LICENSE**：taro/kbone 的 gh license API 都报 NOASSERTION，解码后实为 MIT / BSD-3-Clause；WePY 同为腾讯自定义 MIT 类文本（仓库**有** LICENSE 文件）——NOASSERTION ≠ 无许可，必须读原文（`raw/2026-10-01/gh/*-LICENSE-decoded.txt`）[2][7]。

## 决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖所列维度（微信端性能表现/维护活跃/生态社区/微信端开发效率/许可）；「多端能力」按用户口径作为独立参考列不参与加权，维度外风险（Skyline 长尾 bug、mor 停摆、kbone 无 release、运行时数据老化）以各条目 verdict 为准——矩阵总分 Taro/uni-app 微高于原生而三者同为 adopt 并存不是矛盾：矩阵度量「通用三场景的综合值」（跨端框架赢在效率与生态），verdict 度量「该场景该不该用」（纯微信性能敏感场景原生仍是第一答案）。

## 来源

1. 微信开放文档 — Skyline 兼容/特性/glass-easel 适配（访问 2026-09-30，留档 `raw/2026-09-30/web/native-skyline-docs-weixin.md`、`native-skyline-tavily.md`）
2. GitHub — NervJS/taro（gh 2026-09-30；LICENSE 解码与 v4.3.0 release 2026-10-01，留档 `raw/2026-10-01/gh/`）+ Taro Skyline 文档（docs.taro.zone/docs/skyline）+ Skyline 开放 issue（`raw/2026-09-30/gh/taro-skyline-issues.json`）
3. GitHub — dcloudio/uni-app（gh 2026-09-30）+ DCloud 问答 #151186（Skyline 配置，2023-03）+ Skyline issue（`raw/2026-09-30/gh/uniapp-skyline-issues.json`）+ uni-app x 定位（doc.dcloud.net.cn/uni-app-x，留档 `raw/2026-10-01/web/uniappx-vs-uniapp-tavily-2026-10-01.json`）
4. GitHub — didi/mpx（gh 2026-09-30）+ issue #1454 维护者回复（2024-04-25，`raw/2026-10-01/gh/mpx-issue-1454-comments.json`）+ PR #2540（2026-07 open）
5. 掘金 — 「还在纠结小程序用原生还是框架？5 种方案全拆解」（2025）— https://juejin.cn/post/7647438301876191258（留档 `raw/2026-09-30/web/uniapp-skyline-support-tavily.md`）
6. GitHub — eleme/morjs（gh 2026-09-30）+ Releases（2024-05-21）+ npm 周下载 13（2026-10-01 查）
7. GitHub — Tencent/kbone（gh 2026-09-30；LICENSE 解码 BSD-3-Clause 与无 release 确认 2026-10-01）+ glass-easel 适配指引
8. Vue Mini — 比较页（Taro3/kbone 重运行时口径，访问 2026-10-01）
9. Mpx 官方 — 框架运行时性能测评（mpx 51KB/uniapp 87KB/taro next 156KB/kbone 368KB，约 2020，评测方利益相关降权采信）— https://mpxjs.cn/articles/performance.html（留档 `raw/2026-10-01/web/package-size-tavily-2026-10-01.json`）
10. npm downloads API — 周下载窗口 2026-09-22~09-28（2026-10-01 查，留档 `raw/2026-10-01/gh/releases-npm-license-snapshot-2026-10-01.md`）
