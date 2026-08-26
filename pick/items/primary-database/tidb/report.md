# TiDB

> **TL;DR**：MySQL 协议栈的分布式/HTAP 升级路径：TiFlash 列存副本一库同时跑交易与分析，数百 TB 级有大型互联网实战；PG 生态项目优先看 YugabyteDB，自托管全家桶组件多运维不轻。

- **结论**：trial（试用——MySQL 栈的分布式/HTAP 升级、数百 TB 规模）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 8.5 LTS 线持续维护（8.5.7，2026-07-09）；2026-05 起转历法版本号，当前系列 v26.3（v26.3.10，2026-08-05） | [1][6] |
| 许可证 | Apache-2.0 | [6] |
| 仓库 | https://github.com/pingcap/tidb（⭐40,473，push 2026-08-26，gh 2026-08-27）——NewSQL 三剑客 star 最高 | [6] |
| 维护活跃度 | PingCAP 主导，LTS + 月度 DMR 双轨；2026-05 起历法版本号（v26.3.x） | [1][6] |
| 流行度 | DB-Engines ≈第 79（2026-08 快照，排名上行） | [4] |
| 托管 | TiDB Cloud：Starter（2025-08 由 Serverless 更名，含免费月额度，按 RU 计费）/ Essential / Dedicated / Premium（2026-08 public preview）（查询 2026-08-27） | [2][3] |

## 为什么选（在其领域）

- **MySQL 协议平滑升级**：兼容 MySQL 协议与大部分语法，MySQL 栈团队迁移心智成本最低（taevasidian 底稿 2026-08）[5]。
- **HTAP 一体**：TiKV（行存交易）+ TiFlash（列存副本，Raft learner 实时同步），一库同时服务 OLTP 与实时分析，免掉「PG + ClickHouse 双写」的外挂架构；分布式事务走 TSO 时间戳 + 两阶段提交 [5]。
- **海量规模实战**：数百 TB～PB 级在大型互联网公司（支付/订单/风控）有生产实证（taevasidian 底稿 2026-08）[5]。
- **云节奏快**：TiDB Cloud 2026-08 仍在加 Premium 档（Custom Retention 等），产品线活跃 [2]。

## 为什么谨慎（trial 而非 adopt）

- **全家桶组件多**：自托管 = TiDB + TiKV + PD（+ TiFlash + TiCDC），运维复杂度高于单机 PG，小团队慎入 [5]。
- **PG 支持仍次要**：主线 MySQL 协议，PG 兼容在增强但非第一公民——PG 生态项目直接看 YugabyteDB [5]。
- **兼容非 100%**：MySQL 高级特性（部分锁行为/系统函数）有差异，迁移需回归测试（待验证）[5]。
- **热度中等**：DB-Engines ≈79（2026-08），远低于传统四强——生态广度换深度，选它本质是选 PingCAP 栈 [4]。

## 对比

- vs **CockroachDB / YugabyteDB**：三足鼎立看协议栈——MySQL 系选 TiDB，PG 系选 Yugabyte（深兼容）或 Cockroach（托管成熟）；见 `../comparison.md` 属性矩阵。
- vs **ClickHouse**：要纯极致 OLAP 选 ClickHouse；要一库 HTAP 省掉双写架构选 TiDB [5]。
- vs **MySQL**：MySQL 是单机/主从；数据量与写入超限后的分布式续命就是 TiDB（见 `../mysql/report.md`）[5]。

## 风险与注意

- 绑定 PingCAP 商业栈的开源策略：核心 Apache-2.0，但运维面（TiDB Operator/Cloud）向自家收敛，大规模自托管评估时算清总成本 [2][5]。
- Starter 档按 RU 计费，突发流量成本模型要预先压测（查询 2026-08-27）[3]。
- 8.5 LTS 与 v26.x 双轨并行，新采用建议直接对齐 v26.x 历法线（2026-05 起）[1][6]。
- **杀鸡用牛刀反噬**：小数据量/低并发上 TiDB 比单机 MySQL 更慢更贵——分布式税真实存在，数据量没到单机瓶颈别上（taevasidian 底稿 2026-08）[5]。

## 来源

1. TiDB Release Timeline（8.5.7 · 2026-07-09）— https://docs.pingcap.com/tidb/stable/release-timeline （访问 2026-08-27）
2. TiDB Cloud Release Notes 2026（2026-08-05 更新，Premium 档 public preview）— https://docs.pingcap.com/tidbcloud/tidb-cloud-release-notes （访问 2026-08-27）
3. TiDB Cloud Review 2026（srvrlss；Starter 更名与 RU 计费）— https://www.srvrlss.io/provider/tidb （查询 2026-08-27）
4. DB-Engines Ranking（2026-08 快照，采集 2026-08-27）— https://db-engines.com/en/ranking
5. taevasidian《TiDB · 分布式 NewSQL 数据库选型报告》（2026-08 导出；2026-08-06 会话调研底稿）
6. gh repos/pingcap/tidb（star/push；tags v26.3.0→v26.3.10 提交日 2026-05-25→2026-08-05，采集 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial（初始） | 首次记录：8.5 LTS（8.5.7）+ 历法版本号 v26.3 双轨 |
