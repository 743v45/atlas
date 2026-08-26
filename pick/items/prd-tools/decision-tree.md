# PRD 工具 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 8 节）。

## 根问题

PRD 用什么工具写最好、用什么模板？（2026-08-26 会话；用户背景：飞书重度 + 自托管 Outline + Claude Code）

## 分叉与决策

### D1 承载层：生态内还是新工具？

- 用户生态内成本最低：飞书文档 + 多维表格（智能伙伴生成 PRD、lark-doc/base 实测 agent 读写）。
- 落选节点：[Notion AI](notion-ai/) assess（英文协作默认落点，但 AI 需 Business $20/席/月且 agent 批量 API 慢）。
- 叶：[飞书文档+多维表格](feishu-docs-base/) adopt

### D2 AI 生成质量：谁写得最好？

- **纠错**：Fireside PM 五工具横评真冠军是 Claude 不是 ChatPRD（原文核验「It was Claude :-)」，2025-12-08）。
- 元洞察：工具基线决定上限——**差 prompt + Claude > 好 prompt + 弱工具**；方法论用「餐巾纸粗纲 10-15 分钟再 AI 展开」。
- 叶：[Claude 工作流](claude/) adopt · [ChatPRD](chatprd/) trial（质量已被 Claude 追平，付费理由收窄为 PM 团队标准化+流转；价格 Free/$15/$29 已核实）

### D3 2026 新维度：spec-driven 开发（会话未覆盖、调研新增）

- PRD 给 AI 消费从观点变成制度化工具链：github/spec-kit 一年 ⭐131k（specify→plan→tasks→implement）、AWS Kiro 把 EARS 做成 IDE 硬流程。
- 叶：[spec-kit](spec-kit/) trial · [Kiro](kiro/) assess

### D4 证据聚合赛道要不要？

- Productboard 类面向产品发现/用户证据，个人/小团队不值（$19/$59 per maker）。
- 落选节点：[Productboard](productboard/) hold

### D5 模板选什么？（不立条目，进 comparison 模板谱系）

- 融合建议：Lenny 1-Pager 骨架 + SeatGeek Decision Journal（治「想清楚的会忘」）+ Linear Milestones 语义 + Intercom 约束（一页大白话）。
- 2026 趋势：模板变薄（20 页 Word → 1-pager + AI 起草）。
