# 文档-代码关联横评（六级方案）

> 调研时间 2026-08-27（高强度调研版；框架源自 2026-08-25 会话），方法 tvly（Tavily）+ gh（GitHub CLI 一手数据）+ WebFetch（Docusaurus 文档页为 SPA，tvly 抓取失败后回退）。
> 核心命题：**个人/小团队，代码仓 + 知识库 + 博客三落点，文档与代码如何强关联**——不是「哪款文档工具最强」，而是「哪一层关联强度值得投入、靠什么机制保证不腐烂」。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 个人/小团队，叙述性文档+代码强关联，零外部依赖 | [嵌入级+CI 校验组合](ci-drift-combo/report.md) | 一天成本拿到 90% 的 Swimm 价值：CI exit 1 卡点保正确性 |
| TS 库要 API 参考文档 | [TypeDoc](typedoc/report.md) | 生成级：docstring 即文档，结构上无漂移 |
| 已决定用 React 系 SSG 建文档站 | [Docusaurus](docusaurus/report.md) | raw-loader 嵌入 + onBrokenLinks 默认 throw，机制开箱即用 |
| 企业团队、IDE 内协作、预算充足 | [Swimm](swimm/report.md)（仅团队场景） | 锚点级唯一实现：重构自动跟随 + verify 卡点 |
| 只要「AI 能读懂仓库」 | 组合方案的 AI 层（AGENTS.md + 每目录 index.md + llms.txt） | 60k+ 项目的厂商中立标准，半天落地 |

## 一、六级分级框架（关联强度递进）

同一问题的六级解法，每一级回答「文档拿什么钉在代码上」：

| 级 | 名称 | 钉子是什么 | 代表 | 一句话 | 致命局限 |
|---|---|---|---|---|---|
| 1 | 引用级 | 文件路径/行号/permalink | GitHub 默认链接 | 零成本，人人已在用 | 行号一次重构即失效；permalink 冻结历史、不随现状演进 |
| 2 | 嵌入级 | 构建时拉取代码片段 | Docusaurus raw-loader / Mintlify / Fern | 片段随源码自动更新，**结构上不可能漂移** | 只保护嵌入的片段；叙述性引用（"见 X 模块"）不在射程内 |
| 3 | 生成级 | docstring → 文档 | rustdoc / godoc / TypeDoc / OpenAPI | 单一事实源最彻底——文档就是代码的投影 | 只覆盖 API 面；「为什么这么设计」一概不承载 |
| 4 | 锚点级 | token/AST 锚点 | Swimm（唯一成熟实现） | 重构自动跟随 + CI verify 卡点，机制最强 | 商业闭源 SaaS + IDE 重流程；2026 转向企业现代化服务 |
| 5 | 决策级 | ADR 互引 | Backstage 约定 | 「为什么」有留痕、可追溯 | 不校验代码现状，纯纪律约束 |
| 6 | AI 时代 | agent 入口文件 | AGENTS.md + 每目录 index.md + llms.txt | 给 agent 的活地图，2026 事实标准 | 是「入口」不是「关联」；文件自身会腐烂，须纳入 CI |

**被 pick 的不是某一级，而是组合**：嵌入级（第 2 级）做主力 + CI 强制校验兜底 + ADR（第 5 级）留痕 + AI 层（第 6 级）入口——即 [ci-drift-combo](ci-drift-combo/report.md)。锚点级（第 4 级）机制最强但只有闭源商业实现，个人场景性价比不成立。

## 二、跨方案属性对比矩阵

| 维度 | ci-drift-combo | Swimm | Docusaurus | TypeDoc |
| ----- | -------------- | ----- | ---------- | ------- |
| 关联强度 | 嵌入级(+ADR/AI) | 锚点级(最强) | 嵌入级 | 生成级 |
| 标识 | symbol 引用 | AST/token 锚点 | 文件路径(构建时) | 符号级(API 面) |
| 单一事实源 | 代码仓 | 仓库 .swm(绑平台) | 代码仓(构建拉取) | 源码 docstring |
| CI 强制 | ✅ exit 1 卡点 | ✅ swimm-verify | ✅ 死链 throw | ⚠️ 无内建卡点 |
| 形态 | 同仓 docs/+脚本 | SaaS+IDE 插件 | SSG 框架 | CLI 生成器 |
| 许可 | 组合全开源可选 | 核心闭源 | MIT | Apache-2.0 |
| 成本 | 一天人力 | 按代码行数计价(查询 2026-08-27) | 免费开源 | 免费开源 |
| 重构跟随 | ❌ 靠 CI 拦截 | ✅ 锚点自动跟随 | ❌(路径变了 build 报错) | ✅(重新生成即同步) |
| 叙述性文档 | ✅ 主战场 | ✅ 主战场 | ✅ 主战场 | ❌ 仅 API 面 |
| IDE 内提醒 | ❌ | ✅ | ❌ | n/a |
| star（gh 2026-08-27） | —（自建，无单一 repo） | —（闭源；verify-action ⭐3） | ⭐66,092 | ⭐8,447 |
| 最后 push（同上） | — | —（action 2024-07-30） | 2026-08-26 | 2026-07-13 |
| verdict | **adopt** | hold | assess | trial |

## 二·五、决策矩阵（加权）

<!--gen:decision-matrix-->

> 注记（必读）：决策矩阵只覆盖上表所列维度。**Swimm 的总分被「锚点级最强」拉高，但其 hold 来自维度外因素**——商业闭源、按代码行数计价、2026 主业转向企业现代化服务（详见 [swimm/report.md](swimm/report.md)）。矩阵高分与谨慎 verdict 并存不是矛盾，是两层的分工。

## 三、GitHub 活跃度速查

<!--gen:activity-table-->

（Swimm 与组合方案无 stats：前者核心闭源（swimmio org 仅辅助仓库），后者为自建实践。组合方案的组件活跃度：lychee ⭐3,858 / Apache-2.0 / push 2026-08-25、AGENTS.md（openai/agents.md）⭐23,917 / MIT / push 2026-08-25、Backstage ⭐34,261 / Apache-2.0 / push 2026-08-26，均 gh 2026-08-27 快照。）

## 四、四支柱：强关联的操作性定义

六级方案的差异可压缩为四道题，**分水岭在第三道——没有强制校验，前两道答得再好也会随时间腐烂**（2026-08-25 会话结论）：

| 支柱 | 问题 | 谁答得最好 | 谁答不了 |
|---|---|---|---|
| 稳定标识 | 代码变了，文档引用还找得到吗？ | Swimm（AST 锚点）；生成级（符号即文档） | 引用级（行号必死） |
| 单一事实源 | 代码在哪，真相就在哪？ | 生成级（投影关系）；嵌入级（构建时拉取） | 双头维护的任何方案 |
| 强制校验 | 腐烂发生时，有什么会**失败**？ | 组合方案（exit 1 卡合并）；Swimm（verify 卡 PR）；Docusaurus（死链 throw） | 纯引用、纯 ADR、纯 AI 层 |
| 变更触发 | 改代码的人会被提醒改文档吗？ | Swimm（IDE 内实时）；组合方案（CI 拦截，慢一拍） | 生成级之外的静态方案 |

组合方案的取舍：第三、四支柱用 CI 兜底（牺牲 IDE 内即时性换零依赖），第一、二支柱用「symbol 引用 + 同仓 + 构建时嵌入」逼近（牺牲重构自动跟随换一天成本）。

## 五、选型决策树

```
文档要和代码强关联（个人/小团队）
│
├── 文档是 API 参考吗？
│   └── 是 → TypeDoc（TS）/ rustdoc / godoc（语言内建）——生成级，无漂移
│
├── 文档是叙述性内容（教程/设计/决策）？
│   ├── 要零外部依赖、一天落地 → 嵌入级+CI 校验组合（adopt）
│   │       docs/ 同仓 → 引用指 symbol → CI exit 1 卡合并 → ADR 留痕 → AGENTS.md/index.md/llms.txt
│   ├── 要 IDE 内实时提醒、是企业团队、有预算 → Swimm（唯一锚点级）
│   └── 站点还没建？→ SSG 选型（Docusaurus/MkDocs/Astro）另行决策，机制上都能载组合
│
└── 只是想让 AI 读懂仓库？
    └── AGENTS.md + 每目录 index.md + llms.txt（组合的 AI 层，可单独先用）
```

## 六、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| Fern | ⭐3,764 / Apache-2.0 / push 2026-08-26 / latest 5.23.3（2026-05-12），gh 快照 | 开源核（OpenAPI→SDK+文档生成），托管平台商业——API-first 公司向，嵌入级机制同 Docusaurus，个人无增量 |
| Mintlify | 闭源 SaaS | AI 时代 API 文档站流行选择；机制同嵌入级+生成级，纯托管形态，与「同仓单一事实源」冲突 |
| Backstage | ⭐34,261 / Apache-2.0 / push 2026-08-26，gh 快照 | 决策级平台化实现（ADR 一等公民+插件生态）；开发者门户对个人过重——其 ADR 文件约定已被组合方案直接吸收 |
| Doc Detective | ⭐129 / AGPL-3.0 / push 2026-08-25，gh 快照 | 开源「文档可执行化」框架：把文档步骤当测试跑——互补思路，规模尚小 |
| godoc / rustdoc | Go/Rust 语言内建 | 各语言生成级零配置默认；TS 对应物即 TypeDoc |
| 开源锚点级工具 | 2026-08-27 检索未见成熟实现 | 若出现「AST 锚点+CI verify」的开源 CLI，Swimm 的 hold 应立即重评 |

## 数据时间说明

本页所有 star / push / license 为 gh 2026-08-27 采集快照；Swimm 定价查询于 2026-08-27（第三方报价冲突已注明评测方与年份）；llms.txt v2 提案日期 2026-08-10；AGENTS.md 治理变更（LF AAIF）为 2025-12-09 官方新闻稿。**过期数据比没有数据更危险**——复用本页前先核对时效（RULES.md 第 3 节）。

## 来源（本页新增引用）

1. Linux Foundation 宣布成立 Agentic AI Foundation（2025-12-09）— https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation（访问 2026-08-27）
2. llms.txt v2 提案（Modified 2026-08-10）— https://llmstxt.org（访问 2026-08-27）
3. AGENTS.md 官网（60k+ 开源项目在用）— https://agents.md（访问 2026-08-27）
4. Swimm Pricing — https://swimm.io/pricing（访问 2026-08-27）
5. Swimm's sw.md format — https://swimm.io/blog/docs-as-code-understanding-swimm-sw-md-markdown-format（访问 2026-08-27）
6. Claude 历史会话（2026-08-25）——六级框架、四支柱与选型结论提取源

（各条目级论断的引用见其 report.md 文末来源列表。）
