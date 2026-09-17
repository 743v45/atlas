# Weaviate

> **TL;DR**：内置混合检索 + 模块化推理的老牌向量库——BM25 与向量原生融合、嵌入/重排模块可在库内执行，BSD-3-Clause 许可全场最干净。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | BSD-3-Clause（README 声明 + LICENSE 文件；GitHub 识别 NOASSERTION） | [1] |
| 仓库 | https://github.com/weaviate/weaviate | — |
| 维护活跃度 | pushed 2026-09-17，⭐16,815（gh 2026-09-17） | [1] |
| 形态 | Go 实现的向量数据库，模块化架构 + GraphQL/REST/gRPC API | [2] |

## 为什么选（作为 trial）

- **混合检索是第一公民**：`hybrid` 查询原生融合 BM25 与向量分数（alpha 可调），RAG 场景最常用能力不用外挂 [2]。
- **模块在库内执行**：text2vec / reranker / qna-generator 等模块让嵌入与重排在数据库侧完成，省一层服务编排 [2]。
- **许可最干净**：BSD-3-Clause，无 Dify 式附加条款、无 ES 式三轨选择困难 [1]。

## 对比

- vs Qdrant：同档规模（亿级）与部署形态；Weaviate 混合检索/生成模块更全，Qdrant 过滤与量化粒度更细；两者是专用库里最直接的对位竞品 [2][3]。
- vs Milvus：纯 ANN 极限吞吐不如，胜在轻与功能整合 [3]。
- star 增速落后 Qdrant（16.8k vs 34.6k，gh 2026-09-17），社区声量是其现实短板 [1]。

## 风险与注意

- 1.x 时代 API 有过破坏性演进历史，升级需看 changelog（待验证：当前 2.x 稳定面的迁移成本）[2]。
- 生成式模块的模型托管配置较绕，通常实际项目仍把嵌入/生成放应用侧，只用其检索核 [2]。

## 来源

1. GitHub 仓库 — https://github.com/weaviate/weaviate（gh 2026-09-17：BSD-3-Clause 经 README/LICENSE 解码、⭐16,815、pushed 2026-09-17）
2. 官方文档 — https://weaviate.io/developers（2026-09-17）
3. 口碑调研 — raw/2026-09-17/web/vector-databases-tavily-report.md（2026-09-17，AI 综合结论「语义丰富查询见长、纯 ANN 速度落后 Milvus/Qdrant」）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：混合检索优先时与 Qdrant 对位比选 |
