# 个人知识库横评（AI 共建视角）

> 调研时间 2026-08-27，方法 gh（GitHub CLI 一手数据）+ tvly（Tavily）。
> 核心命题：**AI 共建知识库的本质是「AI 对存储层的原生访问权」**——agent 能不能不经过 API / 中间商，直接读写你的知识资产？2026 年最大动态是全行业向这个方向收敛：Obsidian 官方发布 CLI 与 agent skills（⭐47k）、思源内置 MCP 与智能体、Bear 2.8 带 CLI+MCP——「notes as agent context」成了新轴线（Ry Walker Research 2026）。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| AI 共建个人知识库（生产落地） | [Markdown + Git 仓库工作流](markdown-git-vault/report.md) | 文件直写零中间商，Git 记录人机分工，INDEX 索引控 token |
| 上述方案的阅读器层 | [Obsidian](obsidian/report.md) | 纯 md 打开即读、[[双链]] 文件层机制、随时可换 |
| 在意开源协议的阅读器 | [Logseq](logseq/report.md) | AGPL 开源、OG 模式纯 md（注意 2.0 已转 SQLite beta） |
| 块级粒度 + 中文原生 + 官方 AI 集成 | [思源 SiYuan](siyuan/report.md) | 块级引用最细、v3.8.0 内置 MCP+Agent——但数据非纯 md |
| 自托管 Web 多端访问 | [Trilium / TriliumNext](trilium-next/report.md) | Docker 部署好、层级树知识库——但 AI 通道弱 |
| 团队 Wiki / 权限协作 | [Outline](outline/report.md) | 自托管免费、2026 仍活跃——个人双链场景已废弃迁出 |
| 团队协作 + 数据库视图 + 付费 AI | [Notion](notion/report.md) | 协作最强，但 API 慢 + 数据不本地，AI 共建被否 |

## 一、判断框架：三个问题定生死

1. **数据在哪**——纯 Markdown 文件（可 grep / diff / 直写）还是应用自管数据库（API 代理）？
2. **AI 怎么写**——文件系统原生访问，还是 API / MCP 通道（有速率、有 schema、有中间层）？
3. **换掉它多贵**——阅读器层可换（数据零迁移）还是存储层锁定（导出有损）？

本选型的答案：数据必须是纯 md（1），AI 必须文件直写（2），存储层永不锁定（3）——Obsidian 只承担阅读器角色（3 的保险）。

## 二、属性对比矩阵

| 维度 | Markdown+Git 工作流 | Obsidian | Logseq | 思源 SiYuan | Trilium/Next | Outline | Notion |
|---|---|---|---|---|---|---|---|
| 数据形态 | **纯 Markdown** | **纯 Markdown** | MD（OG）/ SQLite（2.0 beta） | 自管数据库（.sy+索引） | 自管数据库 | Postgres + 对象存储 | SaaS |
| 双链 | AI 织 [[网]] + 阅读器算反链 | **[[文件层]]，反链/图谱核心** | 有（大纲内） | **块级**（最细） | 有（克隆树） | ❌ 无 [[]] | 反链弱 |
| AI 写入 | **文件直写** | 官方 CLI + agent skills（1.12/2026-01 起） | 文件直写（OG 模式） | **内置 MCP+Agent**（v3.8.0，2026-08） | 社区 MCP（⭐64/67，非官方） | API（慢） | API（慢） |
| 自托管 | ✅ 完全（git 即同步） | ✅ 本地 | ✅ 本地 | ✅ Docker | ✅ Docker | ✅ Docker | ❌ |
| 成本 | 免费 | 免费（Sync $4/月可选） | 免费 | 免费（官方同步付费） | 免费 | 自托管免费 / 云 $10/月起 | 完整 AI $20/人/月 |
| 许可 | MIT（自有仓库） | 商业（个人免费） | AGPL-3.0 | AGPL-3.0 | AGPL-3.0 | BSL 1.1 | 商业 SaaS |
| 维护活跃度 | —（自有） | 闭源；1.13（2026-07） | 2.0.1（2026-07-13） | v3.8.2-alpha（2026-08-26） | v0.105.0（2026-08-19） | v1.9.2（2026-07-21） | —（SaaS） |
| star（gh 2026-08-27） | 0（私有落地库） | —（闭源；skills 库 ⭐47,329） | ⭐44,642 | ⭐45,994 | ⭐37,598 | ⭐40,339 | — |
| verdict | **adopt** | **adopt**（阅读器） | assess | assess | assess | hold | hold |

（star / push 为 gh 2026-08-27 采集快照；定价为官网 2026-08-27 查询；版本与功能出处见各条目报告来源列表。）

## 决策矩阵（加权）

<!--gen:decision-matrix-->

## 三、GitHub 活跃度速查

<!--gen:activity-table-->

（Obsidian 本体闭源无 repo stats——其 agent skills 仓库 kepano/obsidian-skills ⭐47,329 可作生态活跃度代理，gh 2026-08-27；markdown-git-vault 为私有方案仓库，star 无意义。）

## 四、选型决策树

```
个人知识库要和 AI 共建
│
├── 数据必须纯文件（grep/diff/直写）?
│   ├── 是 → Markdown + Git 仓库工作流（Claude Code 直写 + INDEX 索引）
│   │        └── 阅读器选谁?
│   │            ├── 生态最大、[[双链]]文件层 → Obsidian（官方 CLI/skills 已出）
│   │            └── 必须开源 → Logseq（锁 OG 文件模式，2.0 是 SQLite beta）
│   └── 否 → 接受 API/MCP 通道代理?
│        ├── 是，要块级粒度+中文+官方 AI → 思源 SiYuan（v3.8.0 内置 MCP+Agent）
│        ├── 是，要多端 Web 自托管 → Trilium（Docker，并回原名后仍活跃）
│        └── 否 → 团队协作场景 → Notion（API 慢+数据不本地，个人 AI 共建出局）
│
└── 团队 Wiki / 权限场景（非本选型）→ Outline（自托管免费、2026 活跃）
```

## 五、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| RAG 型 AI 知识库（Khoj 等） | khoj-ai/khoj ⭐36,728、push 2026-08-02（gh 2026-08-27） | 自托管 second brain；黑盒检索、token 低效——千条内 ripgrep 够用，本选型已否；库大后重评 |
| Reor | reorproject/reor ⭐8,568、**push 2025-05-13**（gh 2026-08-27） | 本地 AI 笔记（RAG+自动关联）；**停更一年余，勿选** |
| Memos | usememos/memos ⭐62,558、push 2026-08-26、MIT（gh 2026-08-27） | 快速捕获型，2026 已改口「Markdown-native」；无双链体系，与页面阅读型知识库场景错位 |
| AFFiNE | toeverything/AFFiNE ⭐71,912、push 2026-08-26（gh 2026-08-27） | Notion+Miro 形态、极活跃；数据库底层，AI 共建通道同 Notion 类问题 |
| Anytype | anyproto/anytype-ts ⭐8,705、push 2026-08-26（gh 2026-08-27） | 本地优先+加密同步；自有对象模型非纯 md，agent 通道弱 |
| Bear 2.8 / ZenNotes / Scratch | 2026 年带 CLI+MCP 或内置 Claude Code（Ry Walker Research 2026） | 「notes as agent context」新轴线佐证；Mac 极简向，非双链知识库 |
| OpenKnowledge | openknowledge.ai（宣称 AI-native md 编辑器、原生 MCP） | 2026 新品，规模与存续待验证 |
| NotebookLM / Mem / Tana / Reflect / Capacities | 已入 2026 agent-native 评测（Consilience 2026-07-16，四标准：数据访问/持久上下文/工具/可编辑产出） | SaaS 为主、上下文持久化各异；本选型的「存储层访问权」标准下均非候选 |

## 数据时间说明

本页所有 star / push / license 为 gh 2026-08-27 采集快照；定价为各官网 2026-08-27 查询；版本线与功能现状出处见各条目报告的来源列表（访问日期均为 2026-08-27）。复用前先核对时效（RULES.md 第 3 节）。
