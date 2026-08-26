# TypeDoc

> **TL;DR**：生成级代表：从 TS docstring 生成 API 文档，周下载 490 万、维护十年；作为组合方案在「API 参考」环节的补充直接可用——但不解决知识库/博客的叙述性文档关联。

- **结论**：trial（试用——TS 库的 API 参考文档环节，非关键路径直接用）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v0.28.20（2026-07-05 发布） | [1][4]（gh 2026-08-27） |
| 许可证 | Apache-2.0 | [1][3]（gh 2026-08-27） |
| 仓库 | https://github.com/TypeStrong/TypeDoc | — |
| 维护活跃度 | ⭐8,447 / push 2026-07-13；npm 周下载 4,925,127（gh / npm 2026-08-27 快照） | [1][2] |
| TS 兼容 | 0.28 支持 TS 5.0–5.8；0.28.18（2026-03-23）起支持 TS 6.0 | [3][4] |

## 为什么（值得试用）

- **生成级的正确性模型最干净**：文档从源码 docstring **生成**而非「关联」——单一事实源就是源码本身，漂移在结构上不存在；标识天然是符号级（导出的函数/类型/接口）。这是六级方案中对「单一事实源」支柱兑现最彻底的层级（2026-08-25 会话结论）[6]。
- **生态事实标准**：TS 生态 API 文档默认选择——周下载 490 万、维护十年、v0.28.20（2026-07-05）仍在出功能版本（`@reexport` 标签、fragment 锚点等）[2][4]。1063 个依赖包、350 个版本（npm 2026-08-27）[2]。
- **与组合方案互补而非竞争**：[ci-drift-combo](../ci-drift-combo/report.md) 管叙述性文档（知识库/博客/ADR）；TypeDoc 管 API 参考面。typedoc-plugin-markdown 4.10.0（2026-02-06）可输出 Markdown 喂给 Docusaurus/MkDocs，融入同一站点与同一 CI [5]。
- **边界清晰所以只 trial**：只覆盖 TS、只覆盖 API 面——架构决策、教程、业务逻辑叙述一概不管；非 TS 项目对应物是各语言内建（godoc/rustdoc，见 `../comparison.md` 观察名单）。

## 对比

与 Swimm（锚点级）/Docusaurus（嵌入级）/组合方案的逐维对比见 `../comparison.md`。

## 风险与注意

- **十年仍是 0.x**：主版本从未到 1.0，minor 间有破坏性 API 变更史（0.26/0.27 已仅安全维护、更早版本 unmaintained [3]）——锁定版本、升级看 changelog。
- docstring 只有一层：写在代码里的注释天然偏「怎么用」，偏「为什么」的内容仍需 ADR/叙述文档承载（生成级与决策级是互补层）[6]。
- 输出体积随导出面线性增长，大库全量生成可考虑 `--entryPoints` 收敛。

## 来源

1. TypeStrong/TypeDoc — https://github.com/TypeStrong/TypeDoc（gh 2026-08-27：⭐8,447 / Apache-2.0 / push 2026-07-13 / latest v0.28.20 2026-07-05）
2. typedoc — npm — https://www.npmjs.com/package/typedoc（访问 2026-08-27：周下载 4,925,127 / v0.28.20）
3. TypeDoc Overview（版本-兼容矩阵）— https://typedoc.org/documents/Overview.html（访问 2026-08-27）
4. TypeDoc Changelog（v0.28.20 2026-07-05；v0.28.18 支持 TS 6.0）— https://typedoc.org/documents/Changelog.html（访问 2026-08-27）
5. typedoc-plugin-markdown Changelog（4.10.0，2026-02-06）— https://typedoc-plugin-markdown.org/docs/CHANGELOG（访问 2026-08-27）
6. Claude 历史会话（2026-08-25）——生成级定位与互补结论提取源

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录（2026-08-27 高强度调研新增：生成级代表、组合方案的 API 参考补充） |
