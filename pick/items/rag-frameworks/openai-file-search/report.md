# OpenAI File Search

> **TL;DR**：Assistants 内置的一行调用 RAG——上传文件即得检索增强回答，原型验证最快；但锁 OpenAI 栈、检索黑盒不可调，控制力全场最低。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 闭源托管服务 | [1] |
| 入口 | https://platform.openai.com/docs/assistants/tools-file-search | — |
| 定位 | Assistants API 内置工具：文件上传 → 自动切块/嵌入 → 检索增强回答；vector store API 可独立挂接 | [1] |
| stats | 无 GitHub 主体仓库，不适用 refresh-stats | — |

## 为什么选（作为 trial）

- **摩擦最低**：无切块决策、无向量库部署、无嵌入管线——官方口径「上传文件、开启工具、查询」，适合需求验证与个人小工具 [1]。
- **与 Responses/Assistants 工具链原生协同**：code interpreter、function calling 同栈组合 [1]。

## 对比

- vs Azure AI Search / Vertex AI Search：托管三家中的极简档——检索策略（切块、排名）不可换，混合检索/rerank 自定义无门；第三方评测在 recall/precision 三项中均垫底（retrievalci 评测 2026-05，小样本降权参考）[2]。
- 数据必须进 OpenAI 云；BYO 模型不可能——学 RAG 原理价值低，用它的意义是「验证需求是否需要 RAG」[1][2]。

## 风险与注意

- 计费按存储（$/GB/天）+查询，规模化后成本不可自控（计价查询日 2026-09-17，采用前按官网当日价核算）[1]。
- 平台锁定：检索资产（切块/嵌入）不可导出到自建管线 [1]。

## 来源

1. 官方文档 — https://platform.openai.com/docs/assistants/tools-file-search（2026-09-17）
2. 第三方评测 — HN「RAG Eval Comparing Vertex/Bedrock/Azure/OpenAI」2026-05-12（github.com/colon-md/retrievalci，个人项目小样本，原始输出留档 raw/2026-09-17/web/rag-managed-api-tavily-report.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：需求验证器，不是学习工具 |
