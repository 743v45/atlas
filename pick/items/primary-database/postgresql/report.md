# PostgreSQL

> **TL;DR**：2026 年通用数据库的默认答案：功能最全、扩展生态最强、许可最友好；短板（连接模型重、VACUUM、原生分布式弱、OLAP 非主场）都有成熟周边补法——用 Postgres，直到它真的不够用为止。

- **结论**：adopt（推荐——新项目默认选择）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 稳定版 18.x（18.0 于 2025-09-25 发布，小版本持续更新）；PG 19 Beta 2 已于 2026-07-16 发布 | [2][3] |
| 许可证 | PostgreSQL License（类 BSD，可闭源二次分发） | [2] |
| 仓库 | https://github.com/postgres/postgres（⭐21,899，push 2026-08-26，gh 2026-08-27） | [9] |
| 维护活跃度 | 30 年历史，大版本年发；2026-06/07 连发 19 Beta 1/2，GA 预计 2026-09 | [3][8] |
| 流行度 | DB-Engines 第 4（684.58 分，2026-08 快照），与第 3 名 SQL Server（694.56）差距缩至 ~10 分 | [4] |
| 开发者口碑 | Stack Overflow 2025 调查：全量受访者最常用且最被向往（most desired/admired）的数据库 | [5] |

## 为什么选

- **SQL 标准兼容性最高**：窗口函数、递归 CTE、`LATERAL`、物化视图、`RETURNING`、`MERGE`、虚拟生成列（PG 18）几乎应有尽有；复杂查询（多表 JOIN/子查询/CTE）优化普遍优于 MySQL [6][10]。
- **扩展机制是护城河**：extension 一等公民——PostGIS（地理）、pgvector（向量/RAG）、TimescaleDB（时序）、Citus（分布式）、pg_partman（分区）可在不 fork 源码的前提下加载新类型/函数/索引；FDW 还能跨数据源联邦查询 [10]。2026 年 AI 场景下「PG + pgvector」已是 RAG 事实标准之一 [10]。
- **事务与类型系统严谨**：严格 ACID，DDL 可事务化回滚；JSONB（GIN 可索引）、数组、范围类型、自定义复合类型齐全 [10]。
- **性能面足够宽**：2026 年基准综述口径——简单 SELECT MySQL 快 20–30%，但复杂 JOIN/分析查询 PG 明显占优（评测：tech-insider 2026）[6]；PG 18 引入异步 I/O（AIO），顺序扫描提速 2–3 倍 [10]。
- **许可与生态位**：BSD 类许可无商业限制；所有主流云均有托管（RDS/Aurora/Neon/Supabase/阿里云 RDS 等），Serverless PG 已成独立赛道 [10][7]。
- **2026 动能**：DB-Engines 分数与 SQL Server 差距仅 ~10 分（2026-08 快照）[4]；SO 2025 开发者调查最常用 [5]；PG 19 Beta 已预告 parallel autovacuum、heap REPACK 等直击 VACUUM 痛点的特性（评测：JusDB 2026）[8]。

## 对比

- vs **MySQL**：复杂查询/JSON/扩展/正确性全面领先，社区共识是差距持续扩大；MySQL 仅在简单读多写少、已有 LAMP 栈时占优 [6][10]。逐维度对比见 `../comparison.md`。
- vs **MongoDB**：JSONB + GIN 覆盖大多数文档型需求，且保留关系建模与 ACID；「想用 MongoDB 时先问 JSONB 够不够」[10]。
- vs **NewSQL 三家**（CockroachDB/YugabyteDB/TiDB）：超单机规模、跨区域多活强一致时让位；单区域内 + 依赖 PostGIS/pgvector 生态时仍选 PG [10]。
- vs **ClickHouse**：亿级大宽表聚合不是 PG 主场，OLAP 外挂 ClickHouse 或走 HTAP [10]。

## 风险与注意

- **连接模型重**：每连接一进程，数千连接后内存/上下文切换开销大，强依赖 PgBouncer 类连接池 [10]。
- **MVCC bloat**：更新产生 dead tuples，大表 VACUUM 是运维负担，autovacuum 调优复杂；PG 19 的 parallel autovacuum/REPACK 正在缓解（Beta，JusDB 2026）[8]。
- **原生分布式弱**：水平分片靠 Citus 或云方案，高可用需 Patroni 等外部工具，非开箱即用 [10]。
- **调参复杂**：默认配置保守，生产需大量调参（shared_buffers/work_mem/wal/autovacuum）[10]。

## 来源

1. PostgreSQL 19 Beta 2 Released — https://www.postgresql.org/about/news/postgresql-19-beta-2-released-3350 （访问 2026-08-27；Beta 1 为 2026-06，Beta 2 为 2026-07-16）
2. PostgreSQL 18.0 Release Notes — https://www.postgresql.org/docs/release/18.0/ （访问 2026-08-27；发布日 2025-09-25）
3. 同 [1]，Beta 节奏与 GA 预告
4. DB-Engines Ranking（2026-08 月度快照，采集 2026-08-27）— https://db-engines.com/en/ranking
5. Stack Overflow Developer Survey 2025 · Technology — https://survey.stackoverflow.co/2025/technology （2025-07 发布；截至 2026-08-27 为最近一期）
6. PostgreSQL vs MySQL: 5 Benchmarks Reveal the Winner（tech-insider，2026）— https://tech-insider.org/postgresql-vs-mysql-2026
7. Neon vs Supabase（closefuture，2026；含 Databricks 2025-05 收购 Neon 与调价）— https://www.closefuture.io/blogs/neon-vs-supabase
8. PostgreSQL 19 Beta New Features: Parallel Autovacuum, REPACK & More（JusDB，2026-06）— https://www.jusdb.com/blog/postgresql-19-beta-new-features-dba-guide
9. gh repos/postgres/postgres（star/push/license 采集 2026-08-27）
10. taevasidian《PostgreSQL 数据库横评：技术架构、优缺点与选型》（2026-08-25 导出，源自 2026-08-06 会话深度调研）——本报告架构论断底稿

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt（初始） | 首次记录：DB-Engines 2026-08 第 4、SO 2025 最常用、PG 19 Beta 2 在途 |
