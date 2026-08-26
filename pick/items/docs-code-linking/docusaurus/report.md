# Docusaurus

> **TL;DR**：嵌入级代表载体：raw-loader 构建时拉源码片段+onBrokenLinks 默认 throw 卡死链，Meta 出品、66k star 活跃；但选 SSG 是站点形态决策，须与知识库/博客落点合并另评——本类别只确认其嵌入机制可载组合方案。

- **结论**：assess（评估——机制已确认可用，站点选型待与知识库/博客落点合并决策）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v3.10.2（2026-07-10 发布） | [1]（gh 2026-08-27） |
| 许可证 | MIT | [1]（gh 2026-08-27） |
| 仓库 | https://github.com/facebook/docusaurus | — |
| 维护活跃度 | ⭐66,092 / push 2026-08-26（gh 2026-08-27）——Meta 背书 + 高频发布 | [1] |

## 为什么（评估中）

- **嵌入级机制官方内建**：文档页直接 `import MyComponentSource from '!!raw-loader!./myComponent'` + `<CodeBlock>` 把源文件按原文嵌入——构建时拉取，源码一改下次构建即更新，片段**结构上不可能漂移**（单一事实源天然成立）[2]。
- **死链卡点是默认行为**：`onBrokenLinks` 默认 `throw`——生产构建发现死链直接失败，官方定位就是「确保永不 ship 死链」；另有 `onBrokenAnchors`/`onBrokenMarkdownLinks` 可调（后者 v3.9 起移至 `markdown.hooks`，v4 将移除顶层配置）[3]。这使它成为 [ci-drift-combo](../ci-drift-combo/report.md) 第三支柱（CI 强制）开箱即用的载体。
- **为什么不是 adopt**：本类别解决「文档-代码如何关联」，Docusaurus 回答的是「站点怎么生成」——后者牵涉 React/Node 栈接受度、知识库与博客是否同站等形态问题，属另一维度决策（参见 `../knowledge-base/` 类别）。若已有纯 Markdown 仓，迁入 React 化 SSG 的成本需要单独权衡（2026-08-25 会话结论）[4]。
- 备选对照：MkDocs（纯 md、Python 系）、Astro（内容优先）同样可实现嵌入+链检组合；机制层面无排他性优势，选型让渡给站点形态决策 [4]。

## 对比

与 Swimm（锚点级）/TypeDoc（生成级）/组合方案（本类别被 pick 项）的逐维对比见 `../comparison.md`。

## 风险与注意

- React/MDX 栈对非前端背景者有学习税；纯 md 仓库迁移需重构 frontmatter 与链接结构。
- `onBrokenLinks` 只在生产构建（`docusaurus build`）生效——本地 dev 不报，CI 必须跑 build 才有卡点 [3]。
- raw-loader 嵌入按文件路径标识：文件改名/移动时构建报错（可捕获），但「symbol 改名而文件仍在」不在其检查范围——组合方案需补 symbol 级校验（见组合条目）。

## 来源

1. facebook/docusaurus — https://github.com/facebook/docusaurus（gh 2026-08-27：⭐66,092 / MIT / push 2026-08-26 / latest v3.10.2 2026-07-10）
2. Importing code snippets（raw-loader 示例）— https://docusaurus.io/docs/markdown-features/react（访问 2026-08-27）
3. docusaurus.config.js | onBrokenLinks/onBrokenAnchors/onBrokenMarkdownLinks — https://docusaurus.io/docs/api/docusaurus-config（访问 2026-08-27）
4. Claude 历史会话（2026-08-25）——本报告提取源

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | assess | 首次记录（历史会话结论 + 2026-08-27 复核版本/机制文档） |
