# 主数据库选型 · 选型设计树

> 根问题的决策路径。叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 8 节）。

## 根问题

应用的第一个数据库选什么——以 PostgreSQL 为锚，横跨通用 OLTP、文档 NoSQL、列式 OLAP、嵌入式与分布式 NewSQL 的主数据库选型？（源自 2026-08-06 会话「Postgres 数据库横评」，复核 2026-08-27）

## 分叉与决策

### D1 跑在设备里还是服务器上？（形态分叉）

- 嵌入式/单文件/零运维（移动端、桌面、边缘、单机工具）→ SQLite 是唯一默认答案，与 PG 互补而非竞争。
- 叶：[SQLite](sqlite/) adopt
- 落选节点：DuckDB（「分析界 SQLite」，嵌入式 OLAP——若分析场景成立它才出场，观察名单）；Realm（已并入 Atlas Device SDK 转维护态，taevasidian 2026-08 底稿）。

### D2 核心负载是交易（OLTP）还是分析（OLAP）？

- 亿级大宽表聚合/日志/实时大盘 → 列式专库 ClickHouse；HTAP 一库（交易+分析）→ TiDB。
- OLTP 交易与点查仍是绝大多数应用的主体 → 转 D3。
- 叶：[ClickHouse](clickhouse/) trial（分析王者但非 OLTP 主库）
- 叶：[TiDB](tidb/) trial（HTAP 分叉见 D4）

### D3 关系还是文档？

- schema 剧变、原生分片刚需 → MongoDB；**其余大多数「想用 MongoDB」的需求，PG 的 JSONB+GIN 已覆盖且保留关系建模与 ACID**（taevasidian 底稿 2026-08 + tech-insider 2026）。
- 叶：[MongoDB](mongodb/) trial
- 落选节点：Couchbase（DB-Engines 2026-08 第 44，生态弱于 Mongo，无独立必要）。

### D4 数据量/写入超单机上限，或要跨区域强一致？

- 是 → NewSQL 三剑客，按协议栈与部署取向分叉：
  - MySQL 栈 → TiDB（协议平滑 + TiFlash HTAP + 海量实战）。
  - PG 栈 + 开源自托管优先 → YugabyteDB（100% Apache-2.0 + fork PG 查询层深兼容）。
  - 全托管优先、接受 BUSL → CockroachDB（托管成熟度最高；BUSL ≥$5M 收费门槛是闸门）。
- 否（单区域内 + 依赖扩展生态 + 追求成熟）→ 留在 PostgreSQL，用 Citus/托管云续命。
- 叶：[TiDB](tidb/) trial（MySQL 栈分布式升级）
- 叶：[YugabyteDB](yugabytedb/) trial（PG 栈 + 开源自托管）
- 叶：[CockroachDB](cockroachdb/) trial（全托管优先、接受 BUSL）
- 落选节点：Cassandra/HBase/DynamoDB（宽列 KV 是另一赛道的「巨兽」，主数据库语义下不竞争，taevasidian 有独立报告）。

### D5 剩下的一切（通用 Web/SaaS/复杂业务/AI 向量/GIS/时序）

- 2026 年共识默认答案：PostgreSQL——功能/正确性/扩展生态/许可四项全优（SO 2025 最常用；DB-Engines 2026-08 第 4 与 SQL Server 差 ~10 分）。
- 短板都有成熟补法：连接池（PgBouncer）、向量（pgvector）、地理（PostGIS）、时序（TimescaleDB）、分布式（见 D4）、OLAP（见 D2）。
- 叶：[PostgreSQL](postgresql/) adopt
- 落选节点：Oracle/SQL Server（预算充足+特定行业合规才考虑，「去 O」的替代答案正是 PG）；MariaDB（MySQL 的 GPL 分叉，治理独立性换生态割裂）；MySQL（简单读仍快 20–30% 且已有栈惯性大 → 转 D5' 存量延续）。

### D5' 已有 MySQL 栈怎么办？

- 读多写少、团队熟悉、需求简单 → 继续用不亏（trial）；新项目与复杂查询增长 → 转 D5（PG）或 D4（TiDB 分布式续命）。
- 叶：[MySQL](mysql/) trial

### D6 组合件（不参与「二选一」）

- Redis/Valkey（缓存/排行榜/限流）：与主库组合使用；Redis 8.0（2025-05）起 AGPLv3 三重许可，Valkey 为基金会分叉备选——观察名单，taevasidian 有独立报告。

## 决策矩阵一致性

加权排序（comparison.md）：PostgreSQL 84 > ClickHouse 80 > TiDB 78 > YugabyteDB 77——PG 独占 adopt 与矩阵第一一致；专家库（ClickHouse/TiDB/Yugabyte）矩阵高分但 verdict 停在 trial，是「维度外风险（OLTP 事务/生态规模/许可）由 verdict 把关」的两层分工（decision.json note）。
