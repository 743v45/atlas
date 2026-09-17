# pgvector

> **TL;DR**：已有 Postgres 就从这里起步——一条 `CREATE EXTENSION vector` 获得向量检索，ACID、权限、备份、JOIN 全部白拿；千万级向量内不用考虑换库。

- **结论**：adopt 推荐
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | PostgreSQL（类 MIT/BSD 宽松，LICENSE 文件 GitHub 识别 NOASSERTION） | [1] |
| 仓库 | https://github.com/pgvector/pgvector | — |
| 维护活跃度 | pushed 2026-09-10，⭐23,040（gh 2026-09-17） | [1] |
| 形态 | Postgres 扩展，HNSW + IVFFlat 索引 | [2] |

## 为什么选（作为 adopt）

- **零新增组件**：向量作为表里的一列与业务数据同库同事务——过滤、JOIN、权限、备份恢复全是现成 PG 能力，不引入第二套运维面 [2]。
- **生态默认答案**：LlamaIndex / LangChain 均有官方 PostgresStore；Dify / RAGFlow 平台也内置 PG+pgvector 部署档 [3]。
- **持续迭代**：0.5x 起 HNSW、半精度向量、迭代扫描（0.8.x）逐步落地，放松了早年的规模天花板 [2]。
- 与本仓 data-storage 域「以 PostgreSQL 为锚——用到不够用为止」的哲学一致。

## 对比

- vs Qdrant/Milvus 等专用库：专用库在亿级向量、高 QPS、复杂 payload 过滤上更强，但要多养一套集群与数据同步；千万级内 pgvector 性能足够 [3]。
- vs Elasticsearch：ES 的 BM25+向量混合检索更成熟，但为了给 LLM 加检索引入整个 ES 集群不划算；PG 自带全文检索可做轻量混合 [2]。

## 风险与注意

- 亿级向量、极致 QPS 场景不是它的战场，此规模直接看专用库（见 comparison 矩阵）[3]。
- 索引构建慢于专用库；HNSW 参数（`ef_search` 等）需要按召回率自调 [2]。
- 超高维（>2000 维）索引支持有历史限制，半精度/位量化可绕 [2]。

## 来源

1. GitHub 仓库 — https://github.com/pgvector/pgvector（gh 2026-09-17：PostgreSQL License、⭐23,040、pushed 2026-09-10；LICENSE 文件解码确认）
2. 官方 README — https://github.com/pgvector/pgvector#readme（2026-09-17）
3. 口碑调研 — raw/2026-09-17/web/vector-databases-tavily-report.md（2026-09-17，AI 综合结论：pgvector 定位「与 SQL 生态紧耦合优先于裸性能」，已与一手数据交叉核对）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | adopt | 首次记录：起步默认答案，规模到墙再升级 |
