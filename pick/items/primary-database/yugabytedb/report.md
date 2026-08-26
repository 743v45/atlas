# YugabyteDB

> **TL;DR**：2024 年起 100% Apache-2.0、深度 fork PG 查询层，是「要分布式又不想离开 PG 生态」时许可最干净、兼容最深的选择；生态规模与托管成熟度仍小于 CockroachDB。

- **结论**：trial（试用——PG 生态项目的分布式刚需首选候选）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v2026.1 STS（2026-06-29 发布，历法版本号）；最新 v2026.1.1.1（2026-08-18） | [2][6] |
| 许可证 | Apache-2.0（2024-06 起核心库 100% 开源，含原企业功能；自管平台 YugabyteDB Anywhere 为 Polyform 商业许可） | [1][5] |
| 仓库 | https://github.com/yugabyte/yugabyte-db（⭐10,500，push 2026-08-26，gh 2026-08-27） | [6] |
| 维护活跃度 | 历法版本号持续发版；2026-06 发布 2026.1 并推出 AMP（Agentic Multitenant PostgreSQL）新叙事 | [2][3] |
| 流行度 | DB-Engines 第 118（2.09 分，2026-08 快照）——三剑客中最低 | [4] |

## 为什么选（在其领域）

- **PG 深兼容是真的深**：直接 fork PostgreSQL 查询层（YSQL，复用 PG 的解析/优化/扩展机制），SQL 语法/行为最接近原生 PG——三剑客（vs CockroachDB 协议级兼容、TiDB MySQL 系）里对 PG 团队最友好；另有 Cassandra 风格 YCQL 双 API（taevasidian 底稿 2026-08）[5]。
- **许可最干净**：核心库 Apache-2.0 且企业功能也开源（2024-06 起），自托管商用零许可顾虑——对比 CockroachDB 的 BUSL ≥$5M 收费 [1]。
- **分布式能力完整**：Raft 复制、自动分片再平衡、跨区域部署（xCluster/geo-partition）[5]。
- **跟进 PG 新版本节奏**：官方持续声明与 PG 上游保持同步（Yugabyte 官方博客 2025–2026）[3]。
- **2026 新动向**：AMP（Agentic Multitenant PostgreSQL）瞄准 AI Agent 多租户场景（官方博客 2026-06-18）[3]。

## 为什么谨慎（trial 而非 adopt）

- **生态规模最小**：DB-Engines 第 118（2026-08）[4]；star 10,500 对比 CockroachDB 32,415、TiDB 40,473（gh 2026-08-27）[6]——社区内容、招聘池、第三方工具支持都更薄。
- **托管成熟度**：YugabyteDB Managed 体量小于 CockroachCloud/TiDB Cloud [5]。
- **部分 PG 扩展仍不可用/受限**：深兼容不等于全兼容，PostGIS 等重型扩展的支持矩阵需逐项核对（待验证）[5]。

## 对比

- vs **CockroachDB**：同赛道直接对位——Cockroach 强在托管与多区域故事，Yugabyte 强在 PG 兼容深度与 Apache-2.0 许可；开源自托管优先选 Yugabyte，全托管优先看 CockroachCloud。见 `../comparison.md`。
- vs **TiDB**：协议栈分野——PG 生态选 Yugabyte，MySQL 生态选 TiDB [5]。
- vs **PostgreSQL**：单机够用就别上分布式；Yugabyte 的定位是「PG 的水平扩展续命方案」[5]。

## 风险与注意

- 三剑客中热度最低，长期社区活力需观察（DB-Engines 2026-08）[4]。
- 商业模式把自管平台（Anywhere）留在商业许可，大规模自托管运维的平台能力要付费 [1][5]。
- PG 小版本同步存在滞后窗口，安全补丁跟进节奏需验证（待验证）。
- HTAP 分析能力弱（无原生列存副本）——既要分布式又要一库分析时 TiDB 更合适（taevasidian 底稿 2026-08）[5]。

## 来源

1. Why We Changed YugabyteDB Licensing to 100% Open Source（Yugabyte 官方博客，2024-06）— https://www.yugabyte.com/blog/why-we-changed-yugabyte-db-licensing-to-100-open-source
2. YugabyteDB Releases（官方文档，v2026.1 STS 2026-06-29）— https://docs.yugabyte.com/stable/releases/ybdb-releases （访问 2026-08-27）
3. A PostgreSQL Database for Every Agent（官方博客，2026-06-18，含 2026.1 与 AMP）— https://www.yugabyte.com/blog/a-postgresql-database-for-every-agent
4. DB-Engines Ranking（2026-08 快照，采集 2026-08-27）— https://db-engines.com/en/ranking
5. taevasidian《YugabyteDB · 分布式 NewSQL 数据库选型报告》（2026-08 导出；2026-08-06 会话调研底稿）
6. gh repos/yugabyte/yugabyte-db（star/push/release v2026.1.1.1 采集 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial（初始） | 首次记录：v2026.1（2026-06）；AMP 新叙事；DB-Engines 第 118 为主要顾虑 |
