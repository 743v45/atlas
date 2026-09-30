# wot-design-uni

> **TL;DR**：uni-app 生态 Vue3+TS 组件库新星——80+ 组件、暗黑模式、AI 友好（LLMs.txt/MCP Server），维护活跃；webview 路线不支持微信 Skyline

- **结论**：trial 试用
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/Moonofweisheng/wot-design-uni（⭐2,300、pushed 2026-09-24，gh 2026-10-01） | [1] |
| 最新版本 | 1.14.0（2026-01-04 发版；npm 同版本，2026-10-01 查询；仓库 push 持续到 2026-09-24） | [2][3] |
| 组件规模 | 官网自述 80+ 高质量组件（components 目录实测 102 项，含配对子组件） | [4][5] |
| 维护活跃度 | npm 月下载 17,492（2026-08-30→09-28）；个人主导 + 赞助模式，issue 响应活跃（Skyline 诉求 issue 2024-05 开、2026-09 关闭回复） | [2][6] |

## 为什么选（作为 trial）

- **uni-app 侧技术栈最现代**：Vue3 + TypeScript 构建，遵循 wot design 设计规范；支持暗黑模式、国际化（内置 15 种语言包）与自定义主题——uni-app 生态里「原生 Vue3 体验」的代表 [4]。
- **AI 友好定位独一份**：官网提供 LLMs.txt、MCP Server、CLI 与 AI Skills，明确为 AI 编码场景优化（「Are you an LLM? View /llms.txt」）——AI 辅助开发工作流中组件用法幻觉率更低 [4]。
- **生态背书在积累**：unibest（活跃的 uni-app 快速开发模板，文档 2026-04-25 更新）默认集成 wot-ui——v1 即 wot-design-uni；该次更新脚手架新增 wot-ui-v2 选项（@wot-ui/ui）并在交互中前置显示，v1 定位转为兼容老项目 [7]。

## 对比

- vs uni-ui：wot 是社区新星（Vue3+TS+暗黑+AI 工具链），uni-ui 是 DCloud 官方标配（跟随 uni-app x 演进）；wot 体验新，uni-ui 兜底强 [8]。
- vs uview-plus：uview-plus 继承 uView2 API（选项式、JS 为主），老项目迁移顺；wot 是全新 Vue3+TS 架构，新项目更干净 [9]。
- vs tdesign（uni-app 版）：tdesign uni-app 版组件与微信原生版同设计语言且跟进 Skyline；wot 组件更多、定制更自由，但不支持 Skyline [6][10]。

## 风险与注意

- **不支持微信 Skyline**：适配请求 issue（#317，2024-05）由维护者回复「有计划支持……工作量有点大」后关闭（2026-09-16）——Skyline 要求 ::before 伪元素、不支持 gap 等差异需逐组件改造；押 Skyline 的微信项目不可选 [6]。
- **单点维护风险**：个人主导项目（Moonofweisheng），bus factor 低于腾讯/DCloud 官方出品；当前更新频率高（2026-09 仍有 push）但对「团队 5 年期维护」场景要留后手 [1]。
- GitHub releases 非高频通道（1.14.0，2026-01-04）——判活看 push 与 npm（2026-10-01 口径）[2][3]。

## 来源

1. GitHub 仓库 — https://github.com/Moonofweisheng/wot-design-uni（gh 2026-10-01：MIT、⭐2,300、pushed 2026-09-24；components 目录实测 102 项）
2. npm — https://www.npmjs.com/package/wot-design-uni（2026-10-01 查询：1.14.0 / 2026-01-04，近月下载 17,492）
3. Releases — https://github.com/Moonofweisheng/wot-design-uni/releases（gh 2026-10-01：v1.14.0 2026-01-04）
4. 官网 — https://wot-ui.cn（访问 2026-09-30：「80+ 高质量组件」「AI 友好：LLMs.txt、MCP Server、CLI 与 AI Skills」「15 种语言包」，留档 raw/2026-09-30/web/sard-ui-search.md）
5. Introduction 页 — https://wot-design-uni.pages.dev/guide/introduction（访问 2026-10-01，留档 raw/2026-10-01/web/skyline-wot-tavily.json）
6. Skyline issue #317 — https://github.com/Moonofweisheng/wot-design-uni/issues/317（gh 2026-10-01：2024-05 开，维护者「工作量有点大」，已关闭）
7. unibest 文档 — https://unibest.tech/base/7-ui（2026-04-25 更新，默认 UI 库 wot-ui；留档 raw/2026-10-01/web/skyline-wot-tavily.json）
8. uni-ui 对照 — https://github.com/dcloudio/uni-ui（gh 2026-10-01）
9. uview-plus 官方文档 — https://uview-plus.jiangruyi.com（访问 2026-10-01，留档 raw/2026-10-01/web/uview-lineage-tavily.json）
10. TDesign Skyline 进度 — https://github.com/Tencent/tdesign-miniprogram/issues/3149（gh 2026-10-01）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：uni-app 侧最现代选项，Skyline 不支持是硬边界 |
