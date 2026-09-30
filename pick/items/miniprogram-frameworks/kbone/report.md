# kbone

> **TL;DR**：腾讯 Web 同构过渡方案——把存量 Web 项目搬进小程序的历史答案，重运行时（官方自测口径 368KB）叠加约一年无 push、无 release，社区共识是别拿它做新项目。

- **结论**：hold 观望
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 无 GitHub release（releases/latest 返回 404，gh 2026-10-01）；以 npm 子包（miniprogram-render 等）发布 | [2] |
| 许可证 | BSD-3-Clause（gh license API 报 NOASSERTION；LICENSE 为腾讯自定义文本「Kbone is licensed under the BSD 3-Clause License, except for the third-party components listed below」，2026-10-01 解码） | [1] |
| 仓库 | https://github.com/Tencent/kbone（⭐4,919、pushed 2025-10-20——截至 2026-10-01 约 11 个月无 push，gh 2026-09-30） | [1] |
| 归属 | 腾讯（wechat-miniprogram 组织生态） | [1] |

## 为什么不选（作为 hold）

- **定位已被时代消化**：kbone 的使命是「微信小程序和 Web 端同构」——用模拟 DOM/BOM 的适配层让 Vue/React Web 项目几乎零改造跑进小程序。这解决的是 2019-2021 年「存量 Web 迁小程序」的过渡问题；如今 Taro/uni-app 均已原生支持编译到 H5 与小程序双端，同构需求的正解变成了「跨端框架反向覆盖」，kbone 的生态位被两端挤压 [3][4]。
- **重运行时是硬伤**：Vue Mini 比较页把 kbone 与 Taro 3/Remax 归为同一类「模拟 DOM API + 运行时递归 VDOM 生成 UI 树」的重运行时方案 [4]；Mpx 官方自测运行时体积 368KB（同口径下 mpx 51KB、uni-app 87KB，约 2020 年数据、利益相关降权采信）——包体积敏感的小程序场景里这个基座开销最难接受 [5]。
- **维护停摆**：repo pushed 2025-10-20（约 11 个月无 push）、无 release 机制（gh 2026-09-30/2026-10-01）[1][2]。
- **社区共识明确**：2025 年第三方横评一句话收尾——「kbone 只适合迁移过渡，别拿它做新项目」，同文决策树将其标注为过渡方案 [3]。

## 对比

- vs Taro/uni-app：Web 端与小程序端双兼容的需求，Taro/uni-app 以「编译到两端」实现且各自生态活跃；kbone 以「运行时同构」实现但停更——同一需求两条路线，社区已用脚投票。
- vs 原生：kbone 项目在小程序端跑在 WebView 渲染 + 模拟 DOM 适配层上 [4]，而 Skyline 只支持 glass-easel 组件框架、绕开 WebView DOM 体系 [6]——kbone 的同构机制与 Skyline 架构不兼容（推断），性能敏感路径与微信新特性均不占优。

## 风险与注意

- **新项目采用 = 接手无主代码**：11 个月无 push、无 release 渠道，遇到基础库破坏性变更无人响应 [1][2]。
- **存量迁移项目的兜底认知**：若 2026 年仍要用 kbone，只应作为「存量 Web 代码暂时跑进小程序」的过渡态，并同步规划向 Taro/uni-app 或原生重写的退路 [3]。

## 来源

1. GitHub — Tencent/kbone（gh 2026-09-30：⭐4,919、pushed 2025-10-20；LICENSE 解码 BSD-3-Clause 2026-10-01，留档 `raw/2026-09-30/gh/Tencent-kbone.json`、`raw/2026-10-01/gh/kbone-LICENSE-decoded.txt`）
2. GitHub Releases API — releases/latest 返回 404（gh 2026-10-01，留档 `raw/2026-10-01/gh/releases-npm-license-snapshot-2026-10-01.md`）
3. 掘金 — 「还在纠结小程序用原生还是框架？5 种方案全拆解」（2025，「别拿它做新项目」原文）— https://juejin.cn/post/7647438301876191258（留档 `raw/2026-09-30/web/uniapp-skyline-support-tavily.md`）
4. Vue Mini — 比较页（kbone 归类模拟 DOM 重运行时方案）— https://vuemini.org/guide/comparisons（访问 2026-10-01，留档 `raw/2026-10-01/web/package-size-tavily-2026-10-01.json`）
5. Mpx 官方 — 框架运行时性能测评（kbone 368KB，约 2020，评测方利益相关降权采信）— https://mpxjs.cn/articles/performance.html（留档同上）
6. 微信开放文档 — glass-easel 适配指引（Skyline 只支持 glass-easel 组件框架）— https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration.html（访问 2026-09-30，留档 `raw/2026-09-30/web/native-skyline-tavily.md`）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | hold | 首次记录：Web 同构过渡方案，重运行时 + 停摆 + 社区共识「别做新项目」 |
