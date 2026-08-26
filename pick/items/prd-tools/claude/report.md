# Claude（Agent 直写）

> **TL;DR**：PRD 写作质量横评第一（Fireside PM 2025-12 实测：Claude 胜 ChatPRD、Gemini、ChatGPT、Grok）：口述→起草→红队评审→按模板写入飞书或 repo，零新增订阅；它只管生成，协作与承载交给宿主工具。

- **结论**：adopt（推荐）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | LLM 对话（claude.com）/ 终端 agent（Claude Code）/ Projects 长上下文 | [1][2] |
| 价格 | Pro 档 $20/月量级（TicNote 与 BuildBetter 2026 口径，均指向 Claude Projects $20/mo）；有免费档 | [3][6] |
| 横评战绩 | 五工具 PRD 写作横评第 1（Fireside PM，2025-12-08 发布） | [1] |

## 为什么选

- **质量第一有实测背书**：Tom Leung（Fireside PM）对 ChatGPT / Claude / Gemini / Grok / ChatPRD 五工具同题实测，排名：①Claude（最佳整体质量、最有说服力的 mockup、战略思考最强）②ChatPRD（结构最规范、「最像人写的」）③Gemini ④ChatGPT（可靠但平庸）⑤Grok（落后 1-2 年）；TLDR 原文「It was Claude :-)」（2025-12-08）[1]。注意：搜索摘要常误传为 ChatPRD 胜出，读原文可纠正 [1][5]。
- **2026 年的独立评测延续同一结论**：Storyflow《12 Best AI Tools for PM 2026 (Tested)》：「Claude is strongest for PRDs and specs」——纯对话 AI 里 specs 阶段的最强选择 [2]。Aakash Gupta 的对撞测试中 Claude 与 ChatPRD 打平（均 B+），Claude 战略思考得分更高（IdeaPlan 2026 引述）[4]。
- **零新增订阅**：已在 Claude 订阅 / Claude Code 里，横评第一名就是日常工具——专用 PRD 工具（ChatPRD 等）对独立开发者的增量主要剩团队标准化与流转集成，不在生成质量（2026-08-26 会话结论）[5]。
- **工作流可闭环**：「餐巾纸背面」方法论——人先花 10-15 分钟写粗纲（Why / Target User / Problem / Key Elements / Success Metrics），交给 Claude 展开再逐段迭代；差的 prompt + Claude > 好的 prompt + 弱工具（Fireside PM 2025-12）[1]。多 persona 红队评审（工程 lead、CEO 视角打分）可用 Claude Code 本地复刻（Hustle Badger 方案）[7]。闭环实证：本工作流的两篇产出（全景研究 + 模板库）即由该会话的 agent 直接写入飞书（2026-08-26）[8]。

## 对比

- 与 ChatPRD：生成质量 Claude ≥ ChatPRD（两处独立评测）[1][4]；ChatPRD 赢在 PM 模板库、Linear/Notion/Confluence 流转与团队空间——PM 团队标准化场景才值得付费，见 [chatprd](../chatprd/report.md)。
- 与 spec-kit：Claude 产 PRD 文本，spec-kit 定义「spec→plan→tasks」的可执行流程并把任意 agent 装进去；spec-kit 的 constitution/任务分解可视为给 Claude 直写加纪律（见 `../comparison.md`）。

## 风险与注意

- **没有协作层**：评论、@人、审批、版本历史一概没有——PRD 的承载与评审必须交给飞书 / Notion / repo（本库方案：Claude 生成 + 飞书承载）[5]。
- **上下文不持久**：纯对话形态跨长周期会丢项目上下文（Storyflow 2026：「chat substrate still loses project context across long cycles」）[2]——用 Projects / CLAUDE.md / spec 文件兜底。
- **输入质量决定输出质量**：一句话生成的 PRD 是「任何产品都能用的平均值」，粗纲纪律不可省（Fireside PM 2025-12）[1]。

## 来源

1. I Tested 5 AI Tools to Write a PRD—Here's the Winner — Tom Leung / Fireside PM，2025-12-08，https://firesidepm.substack.com/p/i-tested-5-ai-tools-to-write-a-prdheres
2. The 12 Best AI Tools for Product Managers in 2026 (Tested) — Storyflow 2026，https://storyflow.so/blog/best-ai-tools-for-product-managers-2026
3. Best AI PRD Generators for Startups (2026) — TicNote 2026，https://ticnote.com/en/blog/ai-prd-generator
4. AI PRD Generator: 6 Free Tools Tested vs ChatPRD 2026 — IdeaPlan 2026（引 Aakash Gupta 实测），https://www.ideaplan.io/blog/best-free-ai-prd-generators-2026
5. Claude 会话 d77eeed3（2026-08-26）「prd 最佳工具」——横评修正与工作流结论
6. Best ChatPRD Alternatives in 2026: 8 AI PRD Tools Ranked — BuildBetter 2026，https://blog.buildbetter.ai/best-chatprd-alternatives-in-2026-ai-prd-generators-for-product-teams
7. 13x PRD Examples including Real PRD Templates（Claude Code PRD Reviewer）— Hustle Badger，https://www.hustlebadger.com/what-do-product-teams-do/prd-template-examples/
8. PRD 工具与模板全景研究 — 飞书文档（本工作流产物，agent 写入 2026-08-26），https://icnk3gqknrte.feishu.cn/docx/M72Od0wGRo9kQyxkPtPcR977nye

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（历史会话结论 + 双评测核实） |
