# Milvus

> **TL;DR**：十亿级向量的重炮——LF AI & Data 毕业项目、Zilliz 商业背书，超大规模吞吐第一梯队；代价是 etcd/对象存储等分布式全家桶，个人项目过重。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/milvus-io/milvus | — |
| 维护活跃度 | pushed 2026-09-17，⭐46,138（gh 2026-09-17） | [1] |
| 血统 | LF AI & Data 毕业项目，Zilliz 主导并供 Milvus Cloud（Zilliz Cloud） | [2] |

## 为什么选（作为 trial）

- **规模天花板最高一档**：为十亿级向量设计，多索引类型（IVF/HNSW/DiskANN/GPU 索引），dense+sparse 混合检索已原生支持 [2]。
- **生态位置稳固**：Dify / RAGFlow 默认向量后端之一，K8s Operator、Backup 工具链齐 [2][3]。
- **治理与商业双背书**：基金会毕业项目治理 + Zilliz 商业公司持续投入，star 46k 全场第二 [1][2]。

## 对比

- vs Qdrant：超大规模吞吐更强、索引种类更多；但部署依赖 etcd/Pulsar(Kafka)/对象存储，亿级以内的项目 Qdrant/pgvector 更轻 [2][3]。
- 个人/学习场景不推荐——Milvus Lite（pip 内嵌模式）可本地跑，但那与「选 Milvus」的规模理由自相矛盾；Lite 适合开发调试 [2]。

## 风险与注意

- **运维重是本条目的核心代价**：分布式组件多，资源占用大；Docker Compose 单机档可用但偏离其设计目标 [2]。
- 版本升级与数据迁移成本高于单二进制对手 [2]。

## 来源

1. GitHub 仓库 — https://github.com/milvus-io/milvus（gh 2026-09-17：Apache-2.0、⭐46,138、pushed 2026-09-17）
2. 官方文档 — https://milvus.io/docs（2026-09-17：架构与部署形态、Milvus Lite）
3. 口碑调研 — raw/2026-09-17/web/vector-databases-tavily-report.md（2026-09-17，AI 综合结论「超大规模吞吐领先」采定性不采数字；含 milvus.io/zilliz.com 检索结果）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：规模到十亿级再考虑 |
