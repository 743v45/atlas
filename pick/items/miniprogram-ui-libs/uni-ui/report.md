# uni-ui

> **TL;DR**：DCloud 官方 uni-app 组件库——全端兼容（含 uni-app x 方向）、npm 2.3 万下载/月的生态标配；GitHub releases 通道失灵，判活要看 npm 与 push

- **结论**：trial 试用
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/dcloudio/uni-ui（⭐2,091、pushed 2026-09-30，gh 2026-10-01） | [1] |
| 最新版本 | npm @dcloudio/uni-ui 1.5.12（2026-03-26；2026-10-01 查询）；GitHub releases 止于 v1.3.6（2021-07-09），已失灵 | [2][3] |
| 组件规模 | npm 包 lib 目录实测 63 项（含配对子组件与样式，约 60 个用户组件） | [4] |
| 维护活跃度 | 仓库 push 至 2026-09-30；npm 月下载 22,778（2026-08-30→09-28） | [1][2] |

## 为什么选（作为 trial）

- **DCloud 官方出品 = uni-app 生态兜底**：与 uni-app/HBuilderX/uniCloud 同厂，仓库结构已含 uni-app x（uts/uvue）工程文件（main.uts、App.uvue，gh 2026-10-01）——押 uni-app x 方向时官方库跟进最稳 [1]。
- **用量扎实**：npm 月下载 22,778（2026-08-30→09-28），在 uni-app 侧组件库中仅次于 uview-plus [2]。
- **主题体系完整**：仓库含 theme.json 与平台配置（platformConfig.json），支持 uni 编译到十几个平台（描述自述「全端兼容」）[1]。

## 对比

- vs wot-design-uni：uni-ui 官方兜底、组件为 uni_modules 插件化按需引入；wot 技术栈更现代（Vue3+TS、暗黑、AI 工具链）且社区热度上升。官方优先选 uni-ui，开发体验优先 wot [5]。
- vs uview-plus：uview-plus 用量更大（36,753/月 vs 22,778/月）且 uView2 用户迁移顺；uni-ui 官方属性是差异化壁垒 [2][6]。
- 注意：GitHub releases 止于 2021 但产品未死（npm 2026-03 仍在发版）——该库的「判活仪表盘」必须用 npm 版本与 repo push，不能用 GitHub releases [2][3]。

## 风险与注意

- **发布通道混乱**：GitHub releases 4 年未更新（2021-07），组件以 uni_modules/HBuilderX 插件市场为主要分发——版本管理需自行以 npm/插件市场为准（2026-10-01 核实）[2][3]。
- **Skyline 无适配结论**：issue 区「最新版 uni-ui 适配 skyline 渲染了么」（2024-05）仍开放无官方答复（gh 2026-10-01）——「待验证」[7]。
- **暗黑模式未声明**——「待验证」：官方文档未见统一暗黑方案，选型前实测 [8]。

## 来源

1. GitHub 仓库 — https://github.com/dcloudio/uni-ui（gh 2026-10-01：MIT、⭐2,091、pushed 2026-09-30；根目录含 main.uts / App.uvue / theme.json）
2. npm — https://www.npmjs.com/package/@dcloudio/uni-ui（2026-10-01 查询：1.5.12 / 2026-03-26，近月下载 22,778）
3. Releases — https://github.com/dcloudio/uni-ui/releases（gh 2026-10-01：仅 v1.3.6，2021-07-09）
4. npm tarball 实测 — raw/2026-10-01/gh/ui-libs-uniui-firstui.md（2026-10-01：lib 目录 63 项）
5. wot-design-uni 对照 — https://github.com/Moonofweisheng/wot-design-uni（gh 2026-10-01）
6. uview-plus 对照 — https://www.npmjs.com/package/uview-plus（2026-10-01 查询：近月下载 36,753）
7. Skyline 问询 issue — https://github.com/dcloudio/uni-ui/issues（gh 2026-10-01 检索 "skyline"：2024-05 问询开放无答复）
8. uni-app 官网 uni-ui 页 — https://uniapp.dcloud.net.cn/component/ui.html（访问 2026-10-01，页面 JS 渲染仅框架文案，留档 raw/2026-10-01/web/uni-ui-docs.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：官方兜底与 uni-app x 方向是核心价值 |
