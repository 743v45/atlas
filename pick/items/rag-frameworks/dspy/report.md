# DSPy

> **TL;DR**：把 prompt 变成程序的声明式框架——用签名定义输入输出、用指标驱动的优化器自动调 prompt；定位是管线的「优化层」而非完整编排，可与 LangChain/LlamaIndex 叠加。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/stanfordnlp/dspy | — |
| 维护活跃度 | pushed 2026-09-17，⭐38,088（gh 2026-09-17） | [1] |
| 背景 | Stanford NLP 出品，仓库自述「programming—not prompting—language models」 | [1] |

## 为什么选（作为 trial）

- **方法论独一档**：把手写 prompt 换成「签名（Signature）→ 模块（Module）→ 优化器（Optimizer/MIPROv2 等）」三件套，用评测指标自动搜索 prompt/few-shot 组合——RAG 答案质量的「评估闭环」它内置了 [2]。
- **第三方基准中的差异点**：AIMultiple 2026-08 横评将 DSPy 列为五框架之一，标签是「程序化 prompt 优化 + 框架开销最小」，且可与 LangChain/LlamaIndex 组件兼容叠加 [3]。
- **学术血统 + 活跃维护**：Stanford 主导，38k star 持续 push [1]。

## 对比

- vs 三个编排框架：LangChain/LlamaIndex/Haystack 回答「管线怎么搭」，DSPy 回答「搭好后怎么变好」——组合使用而非互斥 [2][3]。
- 单独当 RAG 主框架可以但生态少；更常见是在已有管线上对检索-生成环节做指标化调优 [2]。

## 风险与注意

- **评估集是前置成本**：没有标注评测集就没有优化器可言——它惩罚「没有评估的 RAG 团队」，个人项目要先花力气建评测集。
- 概念抽象（teleprompter→optimizer 改名史等）文档演进快，跟官方 dspy.ai 学 [2]。

## 来源

1. GitHub 仓库 — https://github.com/stanfordnlp/dspy（gh 2026-09-17：MIT、⭐38,088、pushed 2026-09-17）
2. 官方文档 — https://dspy.ai/（2026-09-17）
3. 第三方基准 — AIMultiple 2026-08-04 横评（含框架开销对比），原始输出留档 raw/2026-09-17/web/rag-frameworks-tavily-report.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：优化层定位，评测集齐了再上 |
