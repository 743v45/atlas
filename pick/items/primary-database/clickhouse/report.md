# ClickHouse

> **TL;DR**：列式 OLAP 王者：亿级大宽表聚合碾压行式数据库，2026 年按月历法版本滚动发布；但它不是 OLTP 主库——海量分析场景引入它，事务点查仍归 PostgreSQL。

- **结论**：trial（试用——海量日志/数仓/实时大盘场景引入）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 历法版本号按月滚动：26.3 LTS（2026-03-26）、26.6（2026-06）、26.7（2026-07-22）；LTS 线最新 v26.3.23.7-lts（2026-08-26） | [1][6] |
| 许可证 | Apache-2.0 | [6] |
| 仓库 | https://github.com/ClickHouse/ClickHouse（⭐49,464，push 2026-08-26，gh 2026-08-27）——本横评 star 最高的条目 | [6] |
| 维护活跃度 | 月度大版本 + 每周小版本，4 条支持线并行（26.7/26.6/26.3 LTS 等） | [1][7] |
| 流行度 | DB-Engines 第 26（24.95 分，2026-08 快照），OLAP 专库中排名最高之一 | [3] |
| 托管 | ClickHouse Cloud：Development 档 ≈$67/月起（计算 $0.22–0.75/CU 时 + 存储 $25.30–50/TB 月；查询 2026-08-27） | [2][4] |

## 为什么选（在其领域）

- **大宽表聚合无可匹敌**：列式存储 + 向量化执行 + 多核并行，亿级行聚合/日志分析/实时大盘显著快于行式数据库（taevasidian 底稿 2026-08）[5]。
- **压缩比高**：列式编码 + 专用编解码（Delta/ZSTD 等），日志类数据存储成本远低于行库 [5]。
- **真开源 + 迭代凶猛**：Apache-2.0；月度版本节奏，2026 年内已发 26.3→26.7 五个大版（官方 changelog，访问 2026-08-27）[1]。
- **生态渗透广**：可观测性（日志/指标/trace）、BI、特征平台大量采用；DB-Engines 第 26 且为 OLAP 专库头部（2026-08）[3]。

## 为什么不选（做主库）

- **不是 OLTP**：点查/事务/高频单行更新非其设计目标——它是分析引擎，不是交易引擎（taevasidian 底稿 2026-08）[5]。
- **自托管运维重**：分布式部署、资源配额、合并调度调优门槛高；多数团队走 ClickHouse Cloud（查询 2026-08-27）[2][4]。
- **SQL 方言自成一体**：与 PG/MySQL 语法有差异，JOIN 语义与物化视图模型需要学习成本 [5]。

## 对比

- vs **PostgreSQL**：PG 是行式 OLTP，ClickHouse 是列式 OLAP——HTAP 不要指望单机 PG，也不要指望 ClickHouse 做交易库；常见组合是 PG（交易）+ ClickHouse（分析）双写或 CDC 同步（taevasidian 底稿 2026-08）[5]。逐维度见 `../comparison.md`。
- vs **TiDB**：TiDB 走 HTAP 路线（TiFlash 列存副本），一体但要 NewSQL 全家桶；ClickHouse 纯分析但更极致（见 `../tidb/report.md`）[5]。

## 风险与注意

- 版本滚动极快（月度大版），跟随升级策略要预先定好（LTS 线 vs 最新线）[1]。
- 云成本模型按 CU 时计费，闲置计算也计费，长期跑批任务需估准（查询 2026-08-27）[2][4]。
- 「最终一致」的复制模型（ReplicatedMergeTree 异步复制），强一致读需求要显式处理 [5]。
- JOIN 是弱项：星型/雪花尚可，复杂多表 JOIN 需宽表化或物化视图预聚合；UPDATE/DELETE 走异步 mutation、代价高（taevasidian 底稿 2026-08）[5]。

## 来源

1. ClickHouse Changelog 2026（26.3 LTS 2026-03-26、26.6、26.7）— https://clickhouse.com/docs/resources/changelogs/oss/2026 （访问 2026-08-27）
2. ClickHouse Cloud · Billing Overview — https://clickhouse.com/docs/products/cloud/reference/billing/billing-overview （查询 2026-08-27）
3. DB-Engines Ranking（2026-08 快照，采集 2026-08-27）— https://db-engines.com/en/ranking
4. ClickHouse Pricing Models and Cost Analysis for 2026（improvado，2026）— https://improvado.io/blog/clickhouse-warehousing-pricing
5. taevasidian《ClickHouse · 列式 OLAP 数据库选型报告》（2026-08 导出；2026-08-06 会话调研底稿）
6. gh repos/ClickHouse/ClickHouse（star/push/license/release v26.3.23.7-lts 采集 2026-08-27）
7. ClickHouse EOL/EOS 汇总（endoflife.date，访问 2026-08-27）— https://endoflife.date/clickhouse

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial（初始） | 首次记录：26.3 LTS 线 + 月度滚动；⭐49,464 为本横评最高 |
