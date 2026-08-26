# 主数据库横评（以 PostgreSQL 为锚）

> 调研时间 2026-08-27，方法 tvly（Tavily）+ gh（GitHub 一手数据）+ DB-Engines 2026-08 快照 + 官方文档/发布说明。
> 核心命题：**应用的第一个数据库选什么**——源自 2026-08-06 会话「Postgres 数据库横评，对比其他数据库，优缺点，技术架构」的高强度复核版：结论方向不变（PG 是 2026 年通用默认答案），数据全部刷新到 2026-08-27，并新增 DB-Engines 排名胶着、三家转历法版本号、Redis 8 AGPL 化等新事实。
> 同主题深度底稿：taevasidian `tech/数据库选型/`（27 份单库报告，2026-08 导出）。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 通用 Web/SaaS 后端、复杂业务、关系+JSON 混合 | [PostgreSQL](postgresql/report.md) | 功能/正确性/扩展生态/许可四项全优，2026 共识默认 |
| 简单 CRUD、读多写少、已有 MySQL 栈 | [MySQL](mysql/report.md) | 简单读仍快 20–30%，运维惯性是资产 |
| 边缘/嵌入式/移动端/单机工具 | [SQLite](sqlite/report.md) | 单文件零运维，公共领域许可 |
| schema 剧变、内容平台、原生分片刚需 | [MongoDB](mongodb/report.md) | 先问 PG JSONB 够不够——多半够 |
| 海量日志/数仓/实时大盘（OLAP） | [ClickHouse](clickhouse/report.md) | 列式向量化，大宽表聚合碾压行库 |
| 跨区域强一致、超单机规模（MySQL 栈） | [TiDB](tidb/report.md) | MySQL 协议平滑升级 + HTAP 一体 |
| 跨区域强一致（PG 栈、开源自托管） | [YugabyteDB](yugabytedb/report.md) | Apache-2.0 + fork PG 查询层深兼容 |
| 跨区域强一致（全托管优先） | [CockroachDB](cockroachdb/report.md) | 托管成熟度最高；BUSL 许可要过法务 |
| AI/RAG 向量、GIS、时序 | **PostgreSQL** + pgvector/PostGIS/TimescaleDB | 扩展即插件，生态护城河 |
| 缓存/排行榜/限流 | Redis/Valkey（观察名单） | 与主库组合使用，非二选一 |

## 一、先想清楚要哪类数据库

| 层 | 回答的问题 | 代表 |
|---|---|---|
| OLTP 主库 | 交易与点查、强一致 | [PostgreSQL](postgresql/report.md)、[MySQL](mysql/report.md) |
| 文档 NoSQL | schema 多变、原生分片 | [MongoDB](mongodb/report.md) |
| OLAP 专库 | 亿级聚合分析 | [ClickHouse](clickhouse/report.md) |
| 嵌入式 | 设备内/单文件 | [SQLite](sqlite/report.md) |
| 分布式 NewSQL | 超单机规模、跨区域强一致 | [CockroachDB](cockroachdb/report.md)、[YugabyteDB](yugabytedb/report.md)、[TiDB](tidb/report.md) |

这五层是**分工而非全面竞争**：大型系统常「PG（交易）+ Redis（缓存）+ ClickHouse（分析）」叠用。选错层的代价远大于同层内选错产品。

## 二、2026 年关键事实（本次调研新发现）

- **排名胶着**：DB-Engines 2026-08——Oracle 1123.43 / MySQL 842.32 / SQL Server 694.56 / **PostgreSQL 684.58**（第 4 与第 3 仅差 ~10 分，历史最小差距区间）；MongoDB 第 5、Redis 第 8、SQLite 第 11、ClickHouse 第 26。
- **开发者口碑一边倒**：Stack Overflow 2025 调查（截至 2026-08-27 最近一期）PG 为最常用且最被向往的数据库。
- **三家转历法版本号**：MySQL（26.7，2026-07）、TiDB（v26.3，2026-05 起）、CockroachDB（v26.2，2026-04）、YugabyteDB（v2026.1，2026-06）——「年份.月份」成为数据库版本号新时尚，选型时别把 26.x 当成倒退。
- **许可时间线仍在发酵**：CockroachDB 2024-08 起 BUSL 收费门槛降至年收入 $5M；Redis 8.0（2025-05）新增 AGPLv3 三重许可；YugabyteDB 2024-06 起 100% Apache-2.0。
- **性能口径修正**：2026 基准综述——MySQL 简单 SELECT 快 20–30%、PG 复杂查询/JOIN 明显占优；旧结论「MySQL 全面更快」已过时（tech-insider 2026）。

## 三·五、属性对比矩阵

| 维度 | PostgreSQL | MySQL | SQLite | MongoDB | ClickHouse | CockroachDB | YugabyteDB | TiDB |
|---|---|---|---|---|---|---|---|---|
| 定位 | 通用 OLTP | 通用 OLTP | 嵌入式 | 文档 NoSQL | 列式 OLAP | 分布式 NewSQL | 分布式 NewSQL | 分布式 HTAP |
| 当前版本（2026-08-27） | 18.x 稳定 / 19 β2 | 8.4 LTS / 26.7 | 3.53.3 | 8.3 | 26.7（26.3 LTS） | v26.2 | v2026.1 | 8.5 LTS / v26.3 |
| 许可 | PostgreSQL（BSD 类） | GPL-2.0 | 公共领域 | SSPL-1.0 | Apache-2.0 | **BUSL-1.1（源可用）** | Apache-2.0 | Apache-2.0 |
| 水平扩展 | 弱（Citus/云） | 中（中间件） | 无 | 原生分片 | 原生分布式 | 原生分布式 | 原生分布式 | 原生分布式 |
| 协议/SQL 兼容 | 原生 | MySQL 方言 | SQL 大子集 | MQL（非 SQL） | SQL 自有方言 | PG 线协议 | **PG 深兼容** | MySQL 为主 |
| 扩展生态 | **最强**（PostGIS/pgvector/TimescaleDB…） | 插件有限 | FTS5/R-Tree | Atlas 全家桶 | 物化视图/字典 | PG 扩展大多不可用 | 部分 PG 扩展 | 自有生态（TiFlash/TiCDC） |
| star（gh 2026-08-27） | 21,899 | 12,407 | 10,346 | 28,507 | **49,464** | 32,415 | 10,500 | 40,473 |
| DB-Engines（2026-08） | 第 4（684.58） | 第 2（842.32） | 第 11 | 第 5 | 第 26 | ≈65 | 第 118 | ≈79 |
| 托管起步（查询 2026-08-27） | Neon 免费 / Aurora $0.12/ACU 时 | RDS/PlanetScale | 无需（Turso） | Atlas M0 免费 | CH Cloud ≈$67/月 | CockroachCloud | YB Managed | TiDB Cloud Starter 免费 |
| 一句话 | 通用默认答案 | 老将续命 | 边缘之王 | 先问 JSONB | OLAP 王者 | 托管最成熟 | 许可最干净 | MySQL 栈分布式 |

（版本/许可/排名/价格均为标注日期的快照；性能与口碑结论的评测方与年份见各条目报告来源列表。）

## 决策矩阵（加权）

<!--gen:decision-matrix-->

## 四、GitHub 活跃度速查

<!--gen:activity-table-->

（star/push 为 gh 2026-08-27 采集快照。注意 cockroachdb/cockroach push 2026-08-07、间隔约 3 周，开发重心或有内移，待验证；其余条目 push 均在 2026-08-25/26。）

## 五、选型决策树

```
应用的第一个数据库选什么？
│
├── 跑在设备/单文件里（移动端、桌面、边缘）?
│   └── SQLite（并发写多用户网络服务才升级 PG）
│
├── 核心是海量分析（日志/数仓/大盘）?
│   ├── 纯 OLAP、追求极致 → ClickHouse
│   └── 交易+分析一库 → TiDB（HTAP）
│
├── schema 剧变/超大文档分片?
│   ├── PG JSONB 够用（多数情况）→ PostgreSQL
│   └── 真需要原生分片 → MongoDB
│
├── 数据量/写入超单机上限，或跨区域多活强一致?
│   ├── 团队是 MySQL 栈 → TiDB
│   ├── 团队是 PG 栈
│   │   ├── 开源自托管优先、要深兼容 → YugabyteDB（Apache-2.0）
│   │   └── 全托管优先、接受 BUSL → CockroachDB
│
└── 其余一切（通用 Web/SaaS/复杂业务/AI 向量/GIS/时序）
    └── PostgreSQL（+ pgvector / PostGIS / TimescaleDB 按需插装）

组合拳常见形态：PG（主存）+ Redis/Valkey（缓存）+ ClickHouse（分析）。
```

**一句话总结**：2026 年的最稳妥决策仍是「用 Postgres，直到它真的不够用为止」；不够用的判据不是拍脑袋，而是上面的分叉——单机容量、跨区域强一致、亿级聚合、schema 剧变，各有一条明确的退出路径。

## 六、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| Redis | ⭐76,112（gh）；8.10.1（2026-08-17） | 缓存/组合件而非主库选项；8.0（2025-05）起 AGPLv3/SSPLv1/RSALv2 三重许可。taevasidian 有独立报告 |
| Oracle / SQL Server | DB-Engines 第 1/3（2026-08） | 预算充足+特定行业合规才考虑，去 O 的首选替代正是 PG |
| MariaDB | DB-Engines 第 13（2026-08） | MySQL 的 GPL 分叉，治理独立性换取生态割裂 |
| DuckDB | DB-Engines 第 42（2026-08），上升期 | 「分析界 SQLite」，本地单机分析场景与 SQLite 互补。taevasidian 有独立报告 |
| Valkey | DB-Engines 第 99（2026-08） | Redis 2024 改许可后的 Linux 基金会分叉，云厂商背书 |
| Neon / Supabase / Aurora | 均为 PG 托管形态 | 属「PG 发行版/云服务」子题，若需要可另立 postgres-variants 类别（Neon 已于 2025-05 被 Databricks 收购并调价） |
| Citus / TimescaleDB / pgvector | PG 扩展 | 不是独立数据库，是 PG verdict 的一部分（扩展生态护城河的具体构件） |

## 数据时间说明

本页所有 star / push / license 为 gh 2026-08-27 采集快照；DB-Engines 为 2026-08 月度快照（采集 2026-08-27）；版本为各官方发布说明核对值（访问 2026-08-27）；价格为厂商页/第三方评测查询 2026-08-27 口径；性能与口碑结论标注评测方与年份（tech-insider 2026、SO 2025、taevasidian 2026-08）。复用前先核对时效（RULES.md 第 3 节）。
