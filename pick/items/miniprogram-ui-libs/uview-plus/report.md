# uview-plus

> **TL;DR**：uView 官方双仓冻结（2025-01）后的社区接棒者——uView2 API 高兼容 + 3.7 万 npm 下载/月的高频更新；uView 谱系 fork 生态，长期维护看接棒者

- **结论**：trial 试用
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/ijry/uview-plus（⭐719、pushed 2026-09-28，gh 2026-10-01） | [1] |
| 最新版本 | npm uview-plus 3.8.126（2026-09-28；2026-10-01 查询） | [2] |
| 组件规模 | src/uni_modules/uview-plus/components 实测 142 个组件目录（含配对子组件） | [1] |
| 维护活跃度 | 高频小版本滚动（3.8.x 三位数版本号）；npm 月下载 36,753（2026-08-30→09-28），uni-app 侧最高 | [2] |

## uView 谱系（先读这个）

uView 是 uni-app 生态曾经最流行的 UI 框架，官方两仓已冻结：uView 1.x（umicro/uView，⭐4,220，pushed 2025-01-02）与 uView 2.0（umicro/uView2.0，⭐1,789，pushed 2025-01-02）[3]。官方停更后社区出现两条接棒 fork：

- **uview-plus**（ijry/uview-plus，本条目）：「基于 uView2.0 初步修改」，保持选项式 API 与 mixins 兼容，未用 TS 重写但带独立类型声明包；另规划 uview-ultra（uni-app x 版，uts + 组合式 API 重构）[4]。
- **uview-pro**（anyup/uView-Pro，未立条目）：与 plus 不同源——「基于 uView 1.8.8 用 TypeScript 重构」，Vue3+TS、80+ 组件（目录实测 99 项）、暗黑模式、多语言，已上架华为鸿蒙商店；v0.6.19（2026-09-07）活跃但版本号未到 1.0 [5]。
- 另有 @climblee/uv-ui（uView2 另一 fork，npm 月下载 1,719，2026-10-01 查询）声量更小，不单独立目 [6]。

## 为什么选（作为 trial）

- **接棒者更新频率实打实**：npm uview-plus 3.8.126（2026-09-28）——三位数小版本号意味着持续滚动修复；月下载 36,753（2026-08-30→09-28）为 uni-app 侧组件库最高，冻结前 uView 存量用户的迁移主通道 [1][2]。
- **迁移成本最低的 uView2 延续**：官方文档自述「尽可能兼容原有 uview2 各种 API（如 mixins），方便升级」——存量 uView2 项目续命首选 [4]。
- **兼容面最宽**：uni-app 全端 + nvue 兼容 + 鸿蒙方向（官网自述「全面兼容 nvue/鸿蒙/uni-app-x」）[4]。

## 对比

- vs wot-design-uni：uview-plus 胜在 uView2 生态兼容与用量（36.8k vs 17.5k/月）；wot 胜在 Vue3+TS 原生架构、暗黑、AI 工具链。存量 uView 项目选 plus，新 Vue3 项目 wot 起点更干净 [2][7]。
- vs uni-ui：uni-ui 有 DCloud 官方兜底；uview-plus 社区接棒——「官方 vs 高频社区」的取舍 [8]。
- vs uview-pro：plus 是 uView2 血统（JS、选项式），pro 是 uView1 血统 TS 重写（Vue3+TS、暗黑）；两者 API 不完全互通，选错血统迁移成本高 [4][5]。

## 风险与注意

- **fork 生态的结构性风险**：上游官方仓冻结（2025-01-02）后由个人接棒——再断更的可能性永远存在；升级到 uview-ultra（uni-app x）或切换 wot/uni-ui 是预案 [3][4]。
- **高频小版本 = 稳定性噪音**：3.8.x 滚动快，升级需盯 changelog；锁版本上线是基本纪律（npm 2026-10-01 观测）[2]。
- **Skyline 无适配证据**——「待验证」：未检索到 skyline 适配声明或进度表（gh 检索 2026-10-01）；web 技术路线（同 wot/sard）大概率不支持微信 Skyline [9]。

## 来源

1. GitHub 仓库 — https://github.com/ijry/uview-plus（gh 2026-10-01：MIT、⭐719、pushed 2026-09-28；src/uni_modules/uview-plus/components 实测 142 项）
2. npm — https://www.npmjs.com/package/uview-plus（2026-10-01 查询：3.8.126 / 2026-09-28，近月下载 36,753）
3. 官方冻结证据 — raw/2026-09-30/gh/uview1.json、uview2.json（gh 2026-09-30：umicro/uView ⭐4,220 与 umicro/uView2.0 ⭐1,789，均 pushed 2025-01-02）
4. uview-plus 官方文档/插件市场 — https://uview-plus.jiangruyi.com 与 https://ext.dcloud.net.cn/plugin?name=uview-plus（访问 2026-10-01：「基于uView2.0初步修改」「未使用typescript重写，但带有独立的类型申明包」「uview-ultra v4 (uni-app-x版本)」，留档 raw/2026-10-01/web/uview-lineage-tavily.json）
5. uview-pro 仓库 — https://github.com/anyup/uView-Pro（gh 2026-10-01：MIT、⭐555、pushed 2026-09-20、v0.6.19 2026-09-07、自述「基于 uView 1.8.8 用 TypeScript 重构…80+ 组件…鸿蒙」；components 目录实测 99 项）
6. npm — https://www.npmjs.com/package/@climblee/uv-ui（2026-10-01 查询：近月下载 1,719）
7. wot-design-uni 对照 — https://github.com/Moonofweisheng/wot-design-uni（gh 2026-10-01）
8. uni-ui 对照 — https://github.com/dcloudio/uni-ui（gh 2026-10-01）
9. Skyline 语境 — https://github.com/Moonofweisheng/wot-design-uni/issues/317（gh 2026-10-01：web 路线适配 Skyline 工作量大）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：uView 谱系社区接棒，高频更新 + 兼容迁移双价值 |
