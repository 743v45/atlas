# ChatPRD

> **TL;DR**：最成熟的专用 AI PRD 平台：起草+CPO 视角评审+Linear/Notion/Confluence/MCP 流转一体（免费档 / Pro $15/月 / Teams $29/席/月，2026-08-27 查询）；生成质量已被通用 Claude 追平甚至反超，付费理由收窄为 PM 团队标准化与流转集成。

- **结论**：trial（试用——PM 团队标准化场景值得付费，独立开发者无需）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | SaaS（app.chatprd.ai），面向产品经理的 AI 平台 | [2] |
| 价格 | Free $0（3 chats）；Pro $15/月（年付 $179）；Teams $29/席/月（年付 $349/席）（官网 pricing，2026-08-27 查询） | [1] |
| 用户规模 | 官网宣称 100,000+ PM、Fortune 500 到 seed 团队（2026-08-26 会话读官网） | [2][5] |
| 合规 | SOC 2 Type II、SSO、BYO LLM（官网宣称，2026-08-26） | [5] |

## 为什么试用

- **专用工具里最成熟**：四大功能块——AI Documentation（粗想法/会议记录→PRD、one-pager、user stories、技术 spec、GTM brief，自动 gap 分析）、AI Coaching（CPO 视角评审+打分）、Integrations（Linear/Notion/Confluence/Google Docs 导出、PRD→Linear ticket、Slack、MCP、v0/Lovable 生成原型）、Team（共享项目空间、自定义 persona）（2026-08-26 会话读官网）[2][5]。
- **结构化输出是强项**：Fireside PM 横评第 2 名，「结构最规范、最像人写的」（2025-12-08）[3]；Aakash Gupta 对撞测试与 Claude 打平（均 B+）（IdeaPlan 2026 引述）[6]。
- **生成器同质化是行业共识**：各家生成器用同样的底层模型，输出质量在收敛，差异在进上下文的东西与流转集成（Enterpret 2026-07-29）[4]——ChatPRD 的护城河正是 PM 工作流集成那一侧。

## 为什么不是 adopt

- **生成质量不占优**：同题实测输给通用 Claude（Fireside PM 2025-12：Claude 第 1、ChatPRD 第 2）[3]；Storyflow 2026 也将 Claude 评为 specs 阶段最强 [7]。已有 Claude 订阅者，为「生成」付费的理由消失。
- **独立开发者场景结论**：核心付费理由是团队场景——给没有 PM 的团队配「AI PM」、统一文档标准、PRD→Linear 流转；独立开发者 + 已有 Claude Code 基本没有付费必要（2026-08-26 会话结论）[5]。CPO 评审可用 Hustle Badger 的 Claude Code PRD Reviewer 方案本地复刻 [8]。

## 对比

- 与 Claude 直写：见 [claude](../claude/report.md)——质量 Claude ≥ ChatPRD，ChatPRD 赢模板库与流转。
- 与 Notion AI：ChatPRD 是「文档生成器」，Notion AI 是「文档平台的内联 AI」——前者重 PM 深度，后者重协作承载（Enterpret 2026 [4]、BuildBetter 2026 [9]）。

## 风险与注意

- **英文产品**：界面、模板、AI 输出以英文为主，中文 PRD 场景体验待验证。
- **底层模型依赖**：BYO LLM 是 Teams/企业能力，Pro 档模型选择受平台控制 [5]。
- **Lenny 订阅者福利**：Lenny's Newsletter 年度订阅者可领一年 Pro（到期按 $180/年续）——符合条件者可零成本试用（官网 /lenny 页，2026-08-27 查询）[10]。

## 来源

1. ChatPRD Pricing — https://www.chatprd.ai/pricing（查询 2026-08-27）
2. ChatPRD 官网 — https://www.chatprd.ai/（访问 2026-08-26 会话 / 2026-08-27）
3. I Tested 5 AI Tools to Write a PRD — Fireside PM 2025-12-08，https://firesidepm.substack.com/p/i-tested-5-ai-tools-to-write-a-prdheres
4. The 6 Best AI Tools for Writing a PRD Grounded in Customer Evidence — Enterpret 2026-07-29，https://www.enterpret.com/guides/the-6-best-ai-tools-for-writing-a-prd-grounded-in-customer-evidence-in-2026-fgpsr
5. Claude 会话 d77eeed3（2026-08-26）——官网功能块画像与适配判断
6. AI PRD Generator: 6 Free Tools Tested vs ChatPRD 2026 — IdeaPlan 2026，https://www.ideaplan.io/blog/best-free-ai-prd-generators-2026
7. The 12 Best AI Tools for Product Managers in 2026 (Tested) — Storyflow 2026，https://storyflow.so/blog/best-ai-tools-for-product-managers-2026
8. 13x PRD Examples（Claude Code PRD Reviewer）— Hustle Badger，https://www.hustlebadger.com/what-do-product-teams-do/prd-template-examples/
9. Best ChatPRD Alternatives in 2026 — BuildBetter 2026，https://blog.buildbetter.ai/best-chatprd-alternatives-in-2026-ai-prd-generators-for-product-teams
10. ChatPRD × Lenny's Newsletter 优惠页 — https://www.chatprd.ai/lenny（查询 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录（历史会话结论 + 价格核实） |
