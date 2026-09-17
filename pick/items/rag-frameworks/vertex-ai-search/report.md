# Vertex AI Search

> **TL;DR**：GCP 栈的托管 RAG——第三方评测 recall 最高（94.5%），BigQuery/GCS/Workspace grounding 一体，按千次查询计价简单；同样只在 GCP 栈内成立。

- **结论**：assess 评估
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 闭源托管服务（Google） | [1] |
| 入口 | https://cloud.google.com/vertex-ai/search | — |
| 定位 | Vertex AI Agent Builder 下的搜索/grounding 服务：原生向量+混合检索、数据连接器（BigQuery/GCS/Workspace） | [1] |
| stats | 无 GitHub 主体仓库，不适用 refresh-stats | — |

## 为什么 assess（而非推荐）

- **recall 导向的检索质量**：2026-05 第三方评测 recall 94.5% 三家最高（precision 54.7% 偏低——「多召回待精排」取向），$4–6/千次查询的计价模型简单 [2]。
- **分析型 GCP 环境顺路**：数据已在 BigQuery/GCS 时 grounding 集成最省事；Assured Workloads 覆盖合规需求 [1][2]。

## 对比

- vs Azure AI Search：可调项与权限粒度 Azure 更深，recall 与计价简洁 Vertex 更好；云栈决定选择 [2]。
- vs OpenAI File Search：接入复杂度高一档，能力面也宽一档 [2]。

## 风险与注意

- 同 Azure：栈外不引入；评测出处小样本降权（结论与官方能力面对照一致）[2]。

## 来源

1. 官方文档 — https://cloud.google.com/vertex-ai/search（2026-09-17）
2. 第三方评测 — HN「RAG Eval Comparing Vertex/Bedrock/Azure/OpenAI」2026-05-12（github.com/colon-md/retrievalci），原始输出留档 raw/2026-09-17/web/rag-managed-api-tavily-report.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | assess | 首次记录：GCP 栈内正解，栈外不引入 |
