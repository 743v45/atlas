# 小程序开发框架 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

小程序应用逻辑用什么写——原生、React 系、Vue 系还是增强型？（2026-10-01 会话；用户画像：通用视角按场景分流——个人快速开发 / 团队长期维护 / 多端复用，**主评微信端表现**；「多端能力」为独立参考列、不计入决策矩阵权重）

## 分叉与决策

### D1 只做微信还是要多端？

- 多端预期决定框架是否入场：纯微信单端时框架只剩「工程化增强」价值，没有「跨端」价值；这是第一分叉（掘金 2025 横评同构：「选框架的核心逻辑就两条：你用什么语法，你要不要跨端」[5]）。
- **只做微信 → D1a**；**要多端 → D2**。

### D1a 纯微信：性能敏不敏感？

- Skyline 正式稳定后（基础库 3.0.0，2023-07 官方口径加载提升 50%+），性能敏感页面（长列表/手势/复杂动效）只有原生够得着天花板；跨端框架的 worklet/手势跟进全部滞后或有 bug（Taro 手势 API 开放 bug「目前不可用」gh 2026-09-30）[1][2]。
- 性能不敏感的普通页面（表单/展示/工具），「原生 vs 框架」退化为开发效率之争——团队 Vue/React 栈派框架、无栈个人开发者用原生官方工具最快 [5]。
- 叶：[微信小程序原生开发](native/) adopt（单端+性能敏感默认答案：Skyline/glass-easel 新架构性能天花板、新特性首发先到原生）
- 叶：[Taro](taro/) adopt（纯微信 React 栈团队的合理选择；Skyline 可用但重度手势页建议原生）
- 叶：[uni-app](uni-app/) adopt（纯微信 Vue 栈同理；插件市场让快速交付更快）

### D2 要多端：语法栈选谁？

- 双寡头分野就在语法栈：React 团队 Taro、Vue 团队 uni-app；含 App/鸿蒙原生化预期时 uni-app 系（uni-app x 编译 Kotlin/Swift/ArkTS）覆盖更广 [2][3][5]。
- 叶：[Taro](taro/) adopt（React 系多端事实标准：v4.3.0 活跃、Vite 8 + React 19 跟进、多端广度含 RN）
- 叶：[uni-app](uni-app/) adopt（Vue 系全端事实标准：10+ 端 + DCloud 插件市场生态最厚；框架开源与 HBuilderX 闭源双轨要在工程化时辨析）

### D2b 特例：存量 Web 项目要搬进小程序？

- 这个老问题已被跨端框架消化——Taro/uni-app 均可同时编译 H5 与小程序；kbone 的运行时同构是 2019-2021 年的过渡答案，重运行时（368KB 官方自测口径）叠加 11 个月无 push、无 release，社区共识「别拿它做新项目」[5][7]。
- 叶：[kbone](kbone/) hold

### D3 增强/转换型值不值？

- 双寡头之外只剩两条 niche 路线，入场的唯一理由是它们的独特点打中你的场景：复杂小程序业务的性能上限（Mpx 编译输出原生 DSL、运行时最轻一档），或存量微信/支付宝 DSL 双栈合并（mor 转换即原生代码）[4][6]。
- 代价都在生态：Mpx 社区小一档（⭐3.9k、npm 周下载 2.1k），组合式 API 下 Skyline worklet 受限；mor 公开维护近乎停摆（稳定版 2024-05、pushed 2025-11、周下载 13）——后者因此从 trial 下修 assess [4][6]。
- 叶：[Mpx](mpx/) trial（滴滴级复杂业务、性能敏感、接受增强 DSL 生态半径时的正确选择）
- 叶：[mor](morjs/) assess（能力对口但公开维护三重停摆证据，采用前先跑通转换评估自维护承诺）

## 落选节点（不立条目的死分支）

- **WePY**（Tencent/wepy，⭐22,538）：第一代 Vue 风格组件化框架，2026-03-18 仓库归档（gh 2026-09-30，archived:true）。判死证据=归档本身；生态位被 uni-app（标准 Vue）完全替代。勘误：任务预判「仓库无 LICENSE 文件」不成立——LICENSE 存在，为腾讯自定义 MIT 类文本（binary/source 均 MIT + 第三方组件列表，gh license API 因非标准文本报 NOASSERTION；解码留档 `raw/2026-10-01/gh/wepy-LICENSE-decoded.txt`）。
- **mpvue**（Meituan-Dianping/mpvue，⭐20,237）：美团出品、Vue1 时代的小程序框架，pushed 2022-03-02 停更四年半（gh 2026-09-30）；Vue 语法需求由 uni-app 承接，无复活迹象。
- **Remax**（remaxjs/remax，⭐4,552）：「用真正的 React 写小程序」的运行时方案，2024-03-07 归档（gh 2026-09-30）；React 需求由 Taro 承接，重运行时路线被半编译/编译型方案迭代。
- **Chameleon**（didi/chameleon，⭐8,944）：滴滴「一套代码多端」的早期尝试，2023-01-07 归档（gh 2026-09-30）；滴滴系的多端需求由同门 Mpx 承接，自家项目都不再用它。

## 观察名单（下次复核触发器）

- **Taro Skyline 长尾 bug**：手势 API「目前不可用」、自定义 tabbar 渲染不出等开放 issue 清零情况（gh 2026-09-30 基线）→ 清零后 Mpx 的微信端性能卖点被压缩，Taro 权重上调。
- **mor**：2027-01 前仍无 push/release → assess 降 hold。
- **Mpx**：PR #2540「mpx skyline skill」落地与组合式 API worklet 支持进展 → 落地则 trial 内升。
- **uni-app x**：CLI 独立工程能力（当前待验证）与微信端差异化能力若落地 → 考虑从 uni-app 正文小节独立立目。
- **native Skyline 平台覆盖**：Windows/Mac/企业微信端支持落地（官方「规划中/开发中」，2026-09-30 查）→ 落地后微信矩阵类应用的 WebView 兼容负担下降。
- **kbone**：无重启迹象，维持 hold；若 pushed 恢复月级活跃再重估（当前 11 个月无 push，gh 2026-09-30）。

## 来源引用

[1] native/report.md 引用的微信开放文档（Skyline 兼容表/特性/glass-easel）；[2] taro/report.md 引用的 Taro 文档与 gh issue/release；[3] uni-app/report.md 引用的 DCloud 问答/官方文档；[4] mpx/report.md 引用的 issue #1454/官方性能测评/npm；[5] 掘金五方案横评（2025，留档 `raw/2026-09-30/web/uniapp-skyline-support-tavily.md`）；[6] mor/report.md 引用的 gh/npm/release 数据（`raw/2026-10-01/gh/releases-npm-license-snapshot-2026-10-01.md`）；[7] kbone/report.md 引用的 gh 仓库/无 release/自测体积数据（同上快照留档 + `raw/2026-10-01/gh/kbone-LICENSE-decoded.txt`）。
