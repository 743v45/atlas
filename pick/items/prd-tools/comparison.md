# PRD 工具横评（协作文档 × AI 直写 × Spec-Driven）

> 调研时间 2026-08-27，方法：历史会话 d77eeed3（2026-08-26「prd 最佳工具」）结论提取 + tvly（Tavily）网络调研 + gh（GitHub CLI 一手数据）。
> 核心命题：**PRD 到底给谁读**——给人（协作评审平台）、给 AI（spec-driven 可执行流程），还是给自己+AI（独立开发者的思考锚）。2026 年这条赛道最大的动态是 **spec-driven 开发把 PRD 变成 agent 的直接输入**（GitHub Spec Kit ⭐131k 一年破十万星），以及**生成器同质化**（各家都用同样的底层模型，质量收敛，差异转移到上下文与流转）。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 中文团队协作写 PRD + 需求跟踪 | [飞书文档+多维表格](feishu-docs-base/report.md) | 评论/@/审批原生，智能伙伴生成 PRD，agent 经 lark-doc/base 直读直写 |
| PRD 起草与评审质量优先 | [Claude 直写](claude/report.md) | 五工具横评第一（Fireside PM 2025-12），零新增订阅 |
| PRD 是给 agent 的开发输入（repo 内） | [Spec Kit](spec-kit/report.md) | specify→plan→tasks→implement→converge，30+ agent 通用，MIT |
| PM 团队要文档标准 + Linear/Notion 流转 | [ChatPRD](chatprd/report.md) | 专用平台最成熟：模板库 + CPO 评审 + 流转集成 |
| 英文团队协作承载 | [Notion + Notion AI](notion-ai/report.md) | 协作最强档；AI 要 Business $20/席（2026） |
| AWS 栈团队要需求→测试硬流程 | [Kiro](kiro/report.md) | EARS 需求 + FastCheck 性质测试 + 审批门 |
| 反馈洪流聚类成 roadmap | Productboard（hold） | 那是「证据聚合」赛道，个人/小团队不值 |

## 一、三条路线的本质差异

| 维度 | 协作文档流（飞书 / Notion / ChatPRD） | AI 直写（Claude） | spec-as-code（spec-kit / Kiro） |
|---|---|---|---|
| PRD 的角色 | 团队评审的社交资产 | 思考的产物、可落任何载体 | agent 的可执行输入 |
| 生命周期 | 活文档，评论驱动迭代 | 会话产物，靠宿主持久化 | repo 资产，与代码同版本控制 |
| 2026 增量 | AI 内联化（智能伙伴 / Notion AI） | 质量横评第一但无协作层 | **新范式**：spec 可收敛校验（converge / FastCheck） |
| 短板 | agent 批量读写受限（API 慢 / 额度计费） | 无承载、上下文不持久 | 人类评审体验弱 |

关键行业判断：**生成器在收敛，差异在上下文**——「生成 PRD 的工具都用同样的模型，输出质量趋同；差异在生成前往上下文里装了什么、生成后能流转到哪里」（Enterpret 2026-07-29）。因此选型重心从「谁写得最好」转向「谁离你的工作流最近」。

## 二、属性对比矩阵

| 维度 | 飞书文档+多维表格 | Claude 直写 | Spec Kit | ChatPRD | Notion AI | Kiro | Productboard |
|---|---|---|---|---|---|---|---|
| 形态 | SaaS 文档+表格 | LLM 对话/CLI | CLI+slash 命令（开源） | SaaS AI PM 平台 | SaaS 知识库 | spec-driven IDE | SaaS 需求管理 |
| AI 能力 | 智能伙伴生成 PRD+搭表 | 横评第一的起草+评审 | 借宿主 agent | 起草+CPO 评审 | 内联起草 | EARS 生成+FastCheck | 反馈聚类（起草弱） |
| 协作 | 评论/@/审批原生 | ❌ 靠宿主 | git PR | Teams 共享空间 | 数据库视图/权限 | spec 审批门 | 门户+路线图 |
| Agent 读写 | ✅ API+CLI（实测） | ✅ 本身即 agent | ✅ Markdown 即上下文 | MCP（官网宣称） | API 慢 | IDE 内置自家 agent | ❌ |
| 价格（查询日） | 免费档+订阅，AI 按额度（2026-08-27） | Pro $20/月量级（2026） | 免费开源 | Free / $15 / $29（2026-08-27） | Business $20/席含 AI（2026） | Free 50cr / $20（2026-07） | $19 / $59 per maker（2026） |
| 中文 | ✅ 原生 | ✅ 中英皆可 | README 中文版 | ❌ 英文 | 界面支持中文 | ❌ 英文 | 界面多语言（待验证） |
| verdict | adopt | adopt | trial | trial | assess | assess | hold |

（各格数据来源见对应条目报告；star 级数据见下方活跃度表。）

## 决策矩阵（加权）

<!--gen:decision-matrix-->

注记：决策矩阵只覆盖所列维度；维度外风险（ChatPRD 英文产品、Kiro 需换 IDE、Productboard 赛道错位）以各条目 verdict 为准——矩阵高分与谨慎 verdict 并存是两层分工，不是矛盾。

## 三、GitHub 活跃度速查

<!--gen:activity-table-->

（本类开源项仅 spec-kit；OpenSpec 在观察名单。商业 SaaS（飞书/ChatPRD/Notion/Kiro/Productboard）无 stats，活跃度以官网迭代与评测时间衡量。spec-kit ⭐131,655、push 2026-08-26；OpenSpec ⭐66,338、push 2026-08-26——gh 2026-08-27 采集，待 refresh-stats 写入后由此表自动渲染。）

## 四、选型决策树

```
要写 PRD
│
├── PRD 主要给谁读？
│   ├── 给 AI（开发输入 spec）
│   │   ├── 要流程纪律 + 可收敛校验 → Spec Kit（开源，装进现有 agent）
│   │   ├── 愿换 IDE + AWS 栈 → Kiro（EARS + FastCheck + 审批门）
│   │   └── 要轻量 / brownfield → OpenSpec（观察名单）
│   ├── 给人（团队协作评审）
│   │   ├── 中文团队 → 飞书文档 + 多维表格
│   │   ├── 英文团队 → Notion + Notion AI（Business 档）
│   │   └── PM 团队要标准 + 流转 → ChatPRD（Linear/Notion/Confluence）
│   └── 给自己 + AI（独立开发者）
│       └── Claude 直写：餐巾纸粗纲 10-15 分钟 → AI 展开 → 逐段迭代
│           （承载按协作者生态选飞书或 repo；评审用多 persona 红队复刻）
│
└── 真正的痛点是「反馈太多理不出 roadmap」？
    └── 证据聚合赛道（Productboard / Enterpret / BuildBetter）——先确认规模再付钱
```

务实组合（本库采纳，2026-08-26 会话定调）：**Claude 生成 + 飞书承载（中文协作）+ repo 内 spec（agent 执行侧）**——「给人读的 PRD」与「给 AI 执行的 spec」分层并存，而非一门工具打天下。模板层结论：Lenny 1-Pager 骨架 + SeatGeek Decision Journal（决策理由段，治「想清楚的东西会忘」）+ Linear Milestones 语义（PRD 先变、代码后动）。

## 五、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| OpenSpec（Fission-AI） | ⭐66,338，MIT，push 2026-08-26（gh） | 轻量 spec-driven，brownfield 友好，`/opsx:propose` 工作流；spec-kit 的轻替代 |
| 墨刀 AI（万兴科技） | 中文教程 2026-07-14 更新 | 中文原型 + PRD 自动化一体；中文 PM 场景的候选，质量待实测 |
| Confluence + Rovo（Atlassian） | 2026 横评常客 | Jira PD + Rovo 组合面向 Atlassian 标准化团队（BuildBetter 2026） |
| Enterpret / BuildBetter / Dovetail | Enterpret 指南 2026-07-29 | 「证据聚合」赛道：反馈→PRD 的上下文供给侧 |
| PRDKit | Telos 对比 2026-02 收录 | 唯一主打文档+线框图/流程图并出的工具 |
| TicNote Cloud / Telos / Productly | 各自博客 2026 | 新一批「startup COO」型工具，自评口径为主，独立评测缺 |
| GitHub Copilot Workspace | $10/mo（TicNote 2026） | repo 感知的技术规格（API 契约/数据模型），业务上下文弱 |
| vibe-coding-prompt-template（KhazP） | ⭐2,872，push 2026-08-21（gh） | PRD/Tech Design/MVP 提示词模板集，模板层而非工具层 |
| Hustle Badger PRD Reviewer | 方案页（2026） | Claude Code 多 persona 红队评审，本地复刻 ChatPRD CPO Coaching |

## 六、模板层速览（会话沉淀，与工具正交）

2026 趋势是模板变薄：从 20 页 Word 转向 **1-pager + AI 起草 + 持续迭代**；核心分节收敛为「背景与问题 → 目标与度量 → 范围（做/不做什么）→ 方案概述 → 里程碑 → 开放问题」。代表模板按轻重光谱：Intercom Intermission（一页铁律）→ Linear 三段式 → Lenny 1-Pager → Kevin Yien 五阶段 → Shape Up（Appetite）→ ChatPRD 官方十段 → Amazon PR/FAQ（逆向工作法）→ SeatGeek Decision Journal（决策日志）。完整版存于飞书两篇（2026-08-26 会话由 agent 写入）：[PRD 工具与模板全景研究](https://icnk3gqknrte.feishu.cn/docx/M72Od0wGRo9kQyxkPtPcR977nye)、[PRD 模板库 · 十一套可复制模板](https://icnk3gqknrte.feishu.cn/docx/XWIPdnvcWotjr0xa7gNcZo6Qnme)。

## 数据时间说明

本页价格均注查询日期（ChatPRD/飞书 2026-08-27，Kiro 2026-07 口径，Notion/Productboard/Claude 为 2026 年评测方口径）；评测结论均注评测方与时间（Fireside PM 2025-12、Enterpret 2026-07、Storyflow/BuildBetter/IdeaPlan/TicNote 2026）；star/push 为 gh 2026-08-27 采集快照。复用前先核对时效（RULES.md 第 3 节）。
