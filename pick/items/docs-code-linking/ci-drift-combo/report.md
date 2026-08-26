# 嵌入级+CI 校验组合

> **TL;DR**：自建「嵌入级+CI 强制校验」：同仓 docs/ + 引用只指 symbol 不指行号 + CI 死链检查 exit 1 卡合并 + ADR 留痕 + AGENTS.md/llms.txt——一天成本的简化版 Swimm，个人/小团队最优解。

- **结论**：adopt（推荐——本类别被 pick 的方案）
- **核实日期**：2026-08-27（框架源自 2026-08-25 会话调研）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 自建实践组合（非单一工具）：同仓 docs/ + SSG 嵌入 + CI 校验脚本 + ADR 目录 + AI 入口文件 | [1][9] |
| 组成件许可 | 全链路可纯开源（SSG/链检工具 MIT·Apache-2.0 等） | [3][4] |
| 部署成本 | 一天（组合内每个组件均 ≤ 半天） | [9] |
| 仓库 | 无（自建方案，无单一 repo） | — |

## 为什么选

### 四支柱逐条兑现

问题的本质是「文档与代码如何强关联」。六级方案（引用级→嵌入级→生成级→锚点级→决策级→AI 时代）的差异可压缩为四支柱：**稳定标识 / 单一事实源 / 强制校验 / 变更触发**，分水岭在第三条——没有强制校验，前两条都会随时间腐烂 [9]。本组合逐条兑现：

1. **单一事实源 = 代码仓**：docs-as-code——文档与代码同仓、同版本、同 review 流程，这是 Write the Docs 官方指南的定义性实践 [1]。知识库（条目式）与博客（叙述式）另落他处时，凡涉及代码的内容一律以「嵌入/引用代码仓」为源，不在第二处复制代码。
2. **稳定标识 = 只指 symbol，永不指行号**：文档里引用代码用文件路径 + 函数/类型/常量名，不用 `src/foo.ts#L42` 行号锚——行号在任何一次重构后即失效，是引用级的致命伤 [9]。GitHub permalink（commit 哈希锚定）可精确但不随代码演进，只适合「历史快照」注脚，不适合「现状」引用。
3. **强制校验 = CI exit 1 卡合并**（分水岭支柱）：
   - 死链：SSG 构建即查——Docusaurus `onBrokenLinks` 默认 `throw`，生产构建发现死链直接失败，"确保永不带死链上线"[2]；纯 Markdown 仓用 lychee（Rust 链检器，⭐3,858 / Apache-2.0 / push 2026-08-25，gh 2026-08-27）扫内外链 [4]。
   - 漂移：嵌入片段用构建时拉取（见下）天然无漂移；叙述性引用做自建校验——CI 里 `grep` 文档中的 symbol 名是否仍存在于代码，失配即 exit 1。误报用白名单文件豁免（写明「该引用已移除」的日期与原因）。
   - 卡点位置：GitHub Actions required check——校验不过 PR 不能合并，等价于 Swimm `swimm-verify` 的机制，但零外部依赖。
4. **变更触发 = 双向钩子**：改代码的人被 CI 挡下（改了 symbol 没改文档→fail）；改文档的人被死链检查挡下（引用了不存在的路径→fail）。两条边都有反馈回路，这是「活文档」与「死文档」的操作性区别 [1][9]。

### 嵌入级是性价比甜点

- 构建时拉取片段：Docusaurus 官方文档示例 `import MyComponentSource from '!!raw-loader!./myComponent'` + `<CodeBlock>`——源文件一改，下次构建文档自动更新，**结构上不可能漂移** [3]。Mintlify/Fern 同机制（SaaS 化版本）。
- 与锚点级（Swimm）相比：少了 IDE 内漂移提醒与 token/AST 锚点的「重构自动跟随」，但这两者是流程增益而非正确性必需——CI 卡点才是正确性保障，而它已具备 [9]。

### 决策级 + AI 层是加法不是替代

- **ADR 留痕**：`docs/adr/NNNN-标题.md` 记录「为什么这么做」，与代码互链。Backstage 把 ADR 作为其开发者门户的一等公民并在官方文档确立约定（⭐34,261 / Apache-2.0，gh 2026-08-27）——个人场景取其约定（文件命名+状态头+互链），不取其平台 [5]。
- **AI 入口**：AGENTS.md 已是事实标准——OpenAI 2025-08 发布，2025-12-09 随 Linux Foundation 成立 Agentic AI Foundation（与 MCP、goose 同为创始贡献）成为厂商中立规范，60k+ 开源项目与 Amp/Codex/Cursor/Devin/Gemini CLI 等代理采用 [6][8]。每目录 `index.md`（该目录是什么、入口在哪）+ 仓库根 AGENTS.md（构建/测试命令、约定）即「给 agent 的活地图」。对外站点补 `/llms.txt`：v2 提案 2026-08-10 更新，加入 `rel="alternate" type="text/markdown"` 与 `rel="describedby"` 链接关系，OpenAI/Anthropic/Gemini 的开发文档均已发布该文件 [7]。

## 实施清单（一天）

| 时段 | 动作 | 工具 |
|---|---|---|
| 上午 | 代码仓建 `docs/`（与 `src/` 同级）；文档引用规范：路径+symbol，禁行号 | — |
| 上午 | 关键片段改构建时嵌入 | Docusaurus raw-loader [3] 或等效 |
| 下午 | CI 加两道检查并设 required：死链（SSG build / lychee）+ symbol 存在性（grep 脚本） | [2][4] |
| 下午 | `docs/adr/0001-文档规范.md` 落第一条 ADR：本规范本身 | [5] |
| 收尾 | 根目录 AGENTS.md + 各目录 index.md；对外站挂 llms.txt | [6][7][8] |

## 对比

与 Swimm（锚点级）、Docusaurus（嵌入级工具载体）、TypeDoc（生成级）的逐维对比见 `../comparison.md`。

## 风险与注意

- **无 IDE 内提醒**：漂移只在 CI 暴露，写代码时无即时反馈——比 Swimm 体验差一档，个人节奏下可接受（提交前本地跑同一脚本可补）[9]。
- **grep 式 symbol 校验是近似的**：重名 symbol 会假阳性（白名单兜底）、注释里的引用查不到（假阴性）。覆盖率约 90%+ 的工程足够，追求精确需 AST 级——那就是 Swimm 的领地 [9]。
- **AI 层文件自身会腐烂**：AGENTS.md/index.md 写了不维护比没有更糟（agent 会信任过期指令）——必须纳入同一 CI 检查（文档中提到的路径存在性）。
- 组合无单一供应商，SSG 选型（Docusaurus vs MkDocs vs Astro）是独立决策，本条目不锁定——见 [docusaurus](../docusaurus/report.md)。

## 来源

1. Docs as Code — Write the Docs 官方指南 — https://www.writethedocs.org/guide/docs-as-code/（访问 2026-08-27）
2. docusaurus.config.js | onBrokenLinks 默认 throw — https://docusaurus.io/docs/api/docusaurus-config（访问 2026-08-27）
3. Importing code snippets（raw-loader 示例）— https://docusaurus.io/docs/markdown-features/react（访问 2026-08-27）
4. lychee — https://github.com/lycheeverse/lychee（gh 2026-08-27：⭐3,858 / Apache-2.0 / push 2026-08-25）
5. Backstage Architecture Decisions（ADR 约定）— https://backstage.io/docs/architecture-decisions（访问 2026-08-27；star/push 为 gh 2026-08-27 快照）
6. Linux Foundation 宣布成立 Agentic AI Foundation（2025-12-09，AGENTS.md 为创始贡献）— https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation（访问 2026-08-27）
7. llms.txt v2 提案（Modified 2026-08-10）— https://llmstxt.org（访问 2026-08-27）
8. AGENTS.md 官网（60k+ 开源项目在用）— https://agents.md（访问 2026-08-27）
9. Claude 历史会话（2026-08-25）——六级分级框架、四支柱与选型结论提取源

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（历史会话结论 + 2026-08-27 高强度复核：LF AAIF 治理、llms.txt v2、工具活跃度） |
