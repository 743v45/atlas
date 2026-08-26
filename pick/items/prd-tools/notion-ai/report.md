# Notion + Notion AI

> **TL;DR**：英文协作团队的默认 PRD 落点：Notion AI 内联起草+数据库跟踪，协作最强一档；但 AI 需 Business 档（$20/席/月，2026）且 agent 批量读写慢、数据不在本地——协作优先选它，AI 共建优先选别的。

- **结论**：assess（评估——团队已在 Notion 上则顺势用，否则不为此迁移）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | SaaS 协作知识库（文档 + 数据库 + 模板） | [1] |
| 价格 | 2026 四档：Free $0 / Plus $10/席/月（年付）/ Business $20/席/月（年付，含 Notion AI 全量功能）/ Enterprise（FelloAI 2026 汇总口径） | [2] |
| AI 能力 | Notion AI 内联起草、Agent、AI Meeting Notes（Business 档） | [2] |

## 为什么评估（而非 adopt）

- **协作侧确实强**：数据库视图做需求跟踪、权限管理、模板市场（含 Lenny 1-pager 等官方 PRD 模板）——英文团队「文档+跟踪」一站式，2026 年横评常列为 Notion-native 团队默认项（TicNote 2026 [4]、BuildBetter 2026 [3]）。
- **AI 定价门槛**：完整 Notion AI（含 Notion Agent）要 Business 档 $20/席/月（2026 年价格，FelloAI 与多家确认）[2]；纯 AI 起草质量又不如直接用 Claude（Fireside PM 2025-12 横评）[5]。
- **agent 批量读写慢**：AI 共建场景下批量读写走 API 很慢、共建体验差、数据不在本地——知识库选型时的实测排除理由（2026-08-20 会话），同样适用于「开发时 AI 消费 PRD」[6]。
- **中文协作非其主场**：中文团队的等价物是飞书（文档+多维表格+审批一体），见 [feishu-docs-base](../feishu-docs-base/report.md)。

## 对比

- 与飞书：同档协作能力，选型基本等价于「团队语言/生态在英文 Notion 还是中文飞书」。
- 与 ChatPRD：ChatPRD 可导出 Notion——生成器与承载平台可组合而非二选一（ChatPRD 官网集成列表，2026-08-26 会话）[7]。

## 风险与注意

- **AI 能力与席位绑定**：成员一多 AI 成本线性上涨；Free/Plus 档 AI 受限（2026 价格口径）[2]。
- **数据导出摩擦**：离开 Notion 的迁移成本真实存在（历史共识，推导自 SaaS 形态 [1]）。

## 来源

1. Notion 官网 — https://www.notion.com（访问 2026-08-27）
2. Notion AI Pricing 2026: Plans, Cost & Add-On Status — FelloAI 2026，https://felloai.com/notion-ai-pricing
3. Best ChatPRD Alternatives in 2026 — BuildBetter 2026，https://blog.buildbetter.ai/best-chatprd-alternatives-in-2026-ai-prd-generators-for-product-teams
4. Best AI PRD Generators for Startups (2026) — TicNote 2026，https://ticnote.com/en/blog/ai-prd-generator
5. I Tested 5 AI Tools to Write a PRD — Fireside PM 2025-12-08，https://firesidepm.substack.com/p/i-tested-5-ai-tools-to-write-a-prdheres
6. Claude 会话 99faa8a0（2026-08-20）「个人知识库，和 ai 共建，用什么工具管理」——API 慢的排除理由
7. Claude 会话 d77eeed3（2026-08-26）「prd 最佳工具」——集成口径

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | assess | 首次记录 |
