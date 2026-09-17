# Elasticsearch

> **TL;DR**：BM25+向量混合检索最成熟的搜索引擎——kNN 能力经生产大规模验证；但三轨 license 与 JVM 集群运维使它只对存量 ES 用户「顺手」，为 RAG 新引入不值。

- **结论**：assess 评估
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 三轨：AGPL-3.0 / SSPL v1 / Elastic License 2.0（默认三轨授权，x-pack 目录仅 ELv2；LICENSE.txt 解码确认，GitHub 识别 NOASSERTION） | [1] |
| 仓库 | https://github.com/elastic/elasticsearch | — |
| 维护活跃度 | pushed 2026-09-17，⭐77,923（gh 2026-09-17） | [1] |
| 形态 | JVM 搜索引擎，dense_vector + kNN 搜索、BM25 原生、ESS/语义 reranker | [2] |

## 为什么 assess（而非推荐）

- **能力是第一梯队**：文本检索四十年积累 + 8.x/9.x 的 HNSW 向量检索，hybrid search（BM25+向量+rerank）开箱即用，RAG 场景的检索质量上限高 [2]。
- **但引入成本与 RAG 动机不匹配**：为给 LLM 加检索拉起一个 ES 集群，运维面（JVM 调优、分片、安全配置）远超需求；pgvector/Qdrant 在 RAG 常见规模内已够 [3]。
- **license 心智负担**：2021 起的 SSPL/ELv2 分叉风波、2024-08 加回 AGPL——三轨并存对商用自托管/再分发的合规判断有真实成本（自用免费不受影响）[1]。

## 对比

- vs OpenSearch（AWS 分叉）：同为 Lucene 系，OpenSearch Apache-2.0 更干净；本仓不单独立目，存量二选一时按 license 与云绑定关系定（落选节点见 decision-tree）。
- vs pgvector：混合检索成熟度 ES 胜；「已经有一个 Postgres」的场景 pgvector 完胜——这正是多数 RAG 项目的起点 [3]。

## 风险与注意

- 存量 ES 用户做 RAG 是顺路（索引/权限/监控全复用），此场景可升 trial；绿地项目不建议引入（维持 assess）。
- 三轨 license 下做托管服务转售需逐条对照 ELv2/AGPL 条款 [1]。

## 来源

1. GitHub 仓库 + LICENSE.txt — https://github.com/elastic/elasticsearch（gh 2026-09-17：⭐77,923、pushed 2026-09-17；license 三轨说明 2026-09-17 解码）
2. Elastic 官方 — https://www.elastic.co/search-labs（2026-09-17：向量/混合检索能力面）
3. 口碑调研 — raw/2026-09-17/web/vector-databases-tavily-report.md（2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | assess | 首次记录：存量 ES 栈顺手用，绿地项目不引入 |
