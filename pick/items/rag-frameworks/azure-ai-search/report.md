# Azure AI Search

> **TL;DR**：托管三家能力天花板——hybrid + 语义 ranker、字段级权限过滤、企业合规认证最全；只在 Azure 栈内才是正解，栈外没有引入理由。

- **结论**：assess 评估
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 闭源托管服务（Microsoft） | [1] |
| 入口 | https://learn.microsoft.com/azure/search/ | — |
| 定位 | 搜索即服务：向量+BM25 混合、semantic ranker、字段/文档级权限、SharePoint/Blob/Purview 连接器 | [1] |
| stats | 无 GitHub 主体仓库，不适用 refresh-stats | — |

## 为什么 assess（而非推荐）

- **能力是托管三家最强**：2026-05 第三方评测中总分第一（84.0，recall 90.9%/precision 67.8%，hybrid+semantic ranker 组合）；合规认证（FedRAMP High、DoD IL5）企业市场独档 [2]。
- **但价值严格绑定 Azure 栈**：已有 Entra ID/SharePoint/Purview 的企业用户是天然用户；个人项目或非 Azure 团队，「为 RAG 进 Azure」成本结构不成立（Search Unit 月费起步）[1][2]。

## 对比

- vs Vertex AI Search：Google 栈对应物，recall 更高但自定义面窄；两家按云栈二选一 [2]。
- vs 自建（pgvector+rerank）：托管换来权限/合规/免运维，失去控制力与可迁移性 [2]。

## 风险与注意

- 计价按 Search Unit + 查询量，起步价高于 OpenAI File Search 的轻量档（计价查询日 2026-09-17）[1]。
- 评测出处为个人项目（3 分 HN 帖），数字降权参考，结论（三家相对位次）与官方能力面对照一致 [2]。

## 来源

1. 官方文档 — https://learn.microsoft.com/azure/search/（2026-09-17）
2. 第三方评测 — HN「RAG Eval Comparing Vertex/Bedrock/Azure/OpenAI」2026-05-12（github.com/colon-md/retrievalci），原始输出留档 raw/2026-09-17/web/rag-managed-api-tavily-report.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | assess | 首次记录：Azure 栈内正解，栈外不引入 |
