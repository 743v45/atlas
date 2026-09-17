# Qdrant

> **TL;DR**：PG 不够用后的第一升级——Rust 内核、payload 过滤与量化压缩是强项，Apache-2.0 且开源/云同核，亿级向量下性能与运维复杂度的均衡首选。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/qdrant/qdrant | — |
| 维护活跃度 | pushed 2026-09-17，⭐34,628（gh 2026-09-17） | [1] |
| 公司 | Qdrant GmbH，2026 年融资 $28M | [3] |

## 为什么选（作为 trial）

- **性能/功能的均衡位**：Rust 实现，HNSW 为主；payload 索引+过滤检索是招牌能力，量化（标量/二进制/product）显著降内存 [2]。
- **dense+sparse 原生混合**：内置 sparse 向量支持，BM25 风格稀疏检索可与稠密向量在同一查询融合，RAG 混合检索不必外挂 [2]。
- **部署形态全**：单机二进制 → 分布式集群 → Qdrant Cloud（混合/私有云），开源内核与云同核，迁移路径清晰 [2]。
- **口碑定位**：2026 年对比文普遍将其列为「速度、磁盘效率、实时更新的均衡权衡」选项 [3]。

## 对比

- vs pgvector：规模、QPS、过滤复杂度全面更强，代价是多养一套组件+数据同步；PG 够用时不必上 [3]。
- vs Milvus：Milvus 十亿级吞吐更高但运维重（依赖 etcd/对象存储等）；亿级以内 Qdrant 更轻 [3]。
- 是 Dify、RAGFlow、LlamaIndex 的默认集成项之一 [3]。

## 风险与注意

- 单一商业公司主导（Qdrant GmbH），公司风险与融资进度挂钩（$28M，2026）[3]。
- 分布式模式的分片/副本运维有学习成本，个人项目单机模式即可 [2]。

## 来源

1. GitHub 仓库 — https://github.com/qdrant/qdrant（gh 2026-09-17：Apache-2.0、⭐34,628、pushed 2026-09-17）
2. 官方文档 — https://qdrant.tech/documentation/（2026-09-17）
3. 口碑调研 — raw/2026-09-17/web/vector-databases-tavily-report.md（2026-09-17，含 Qdrant $28M 融资报道；精确 QPS 数字无出处不采用，仅采定性结论）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：PG 之后的专用库默认升级项 |
