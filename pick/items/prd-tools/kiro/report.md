# Kiro（AWS）

> **TL;DR**：AWS 的 spec-driven IDE：EARS 句式需求→设计→任务→实现流水线，FastCheck 从需求生成性质测试，spec 审批门可做治理；与 spec-kit 同流派但绑定自家 IDE 与 credits（Free 50 credits / Pro $20/月，2026-07 观测）——适合 AWS 重度团队，已有 Claude Code 者换不动。

- **结论**：assess（评估——范式正确，但为它换 IDE 的理由不足）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | spec-driven IDE：Web / CLI / 桌面客户端 | [1][2] |
| 价格 | Free $0（50 credits/月，含开放权重模型与 Claude Sonnet 4.5）；Pro $20/月（1,000 credits）；Pro+ $40/月（2,000 credits）；超额 $0.04/credit（kiro.dev/pricing，2026-07 观测口径） | [3][4] |
| 底座 | Amazon Bedrock，深度集成 AWS 服务 | [5] |
| spec 能力 | Feature Spec / Quick Spec（免审批门直出三件套）/ Analyze Requirements（查歧义与缺口） | [2] |

## 为什么评估

- **把「先需求后代码」做成了硬流程**：同一句 prompt，在 Cursor/Bolt 直接产代码，Kiro 先产出 requirements 文档——拆成离散 user stories、每条带验收标准，再走 design 与 tasks（Vibe Coder 2026 实测）[5]。这正是 spec-driven 范式的卖点。
- **EARS 句式 + 可测试性**：需求强制写成 EARS 风格（When…, If…, Then…），自动提取 property-based 可测属性，交给内置 FastCheck 生成 fuzzed 正确性测试（2026 年评测口径）[5]——「PRD 条目可执行化」在 IDE 层做得最深。
- **治理能力独有**：spec 审批门（approve 才能进实现）、GovCloud 部署、分层定价控额度——受监管团队的差异化点 [5]。

## 为什么不是 trial/adopt

- **范式可用开源平替**：同流派的开源 spec-kit（⭐131k、MIT、30+ agent 通用）装进现有 Claude Code 即可获得 specify→plan→tasks 主流程，不换 IDE、不买 credits——见 [spec-kit](../spec-kit/report.md)。
- **credits 经济学**：spec 生成也计入 credits（50/月起），流程越纪律越烧额度（2026-07 定价口径）[3][4]。
- **AWS 向绑定**：Bedrock 底座与 AWS 集成是双刃剑——非 AWS 栈团队受益有限 [5]。

## 对比

- 与 spec-kit：Kiro = 闭源 IDE + EARS 硬约束 + 测试生成；spec-kit = 开源流程框架 + agent 中立。选 Kiro 本质是选「整套 IDE」，选 spec-kit 是选「流程纪律」（见 `../comparison.md` 决策树）。

## 风险与注意

- **闭源快速迭代**：功能与定价 2026 年内多次调整（新 pricing 公告可证），采购前以 kiro.dev/pricing 当日为准 [3][4]。
- **评测多为 2026 上半年口径**（vibecoder 2026、re:Invent DEV314），迭代快，半年后需复核 [5]。

## 来源

1. Kiro 官网 — https://kiro.dev（访问 2026-08-27）
2. Specs - Features - Docs — https://kiro.dev/docs/specs（访问 2026-08-27）
3. Kiro Pricing — https://kiro.dev/pricing（访问 2026-08-27）
4. Kiro Pricing (2026): Plans, Credits, Overage — MorphLLM 2026-07，https://www.morphllm.com/kiro-pricing
5. Amazon Kiro Reviewed for Spec-Driven AI Development in 2026 — Vibe Coder Blog 2026，https://blog.vibecoder.me/amazon-kiro-spec-driven-development-reviewed

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | assess | 首次记录（2026 新增条目：spec-driven IDE 流派） |
