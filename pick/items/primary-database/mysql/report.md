# MySQL

> **TL;DR**：可靠的老将，但新项目默认选择已让位 PostgreSQL：复杂查询、JSONB、扩展生态全面落后；已有 MySQL 栈、读多写少的简单 Web 场景仍值得继续用。

- **结论**：trial（试用——已有栈延续使用；新项目默认选 PostgreSQL）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 8.4 LTS 与 9.x Innovation 并行；2026-01 发布 9.6（Innovation），9.7 为旧序号模型最后一条线；此后转历法版本号（26.7 Innovation，2026-07-20） | [1] |
| 许可证 | GPL-2.0（Oracle 双轨：开源 GPL + 商业许可） | [5] |
| 仓库 | https://github.com/mysql/mysql-server（⭐12,407，push 2026-08-25，gh 2026-08-27） | [6] |
| 维护活跃度 | Oracle 主导，LTS + Innovation 双轨持续发布（9.7.2 tag 已出现，gh 2026-08-27） | [1][6] |
| 流行度 | DB-Engines 第 2（842.32 分，2026-08 快照），存量装机仍是互联网最大基本盘之一 | [3] |

## 为什么（还能）选

- **简单读多写少仍然快**：2026 年基准综述口径——简单 SELECT 比 PG 快 20–30%，单机写密集基准亦有约 30% 优势（评测：tech-insider 2026）[2]。架构上 InnoDB 聚簇索引（主键索引即数据），主键点查极快；二级索引存主键值需回表，与 PG 堆表+CTID 是两条路线（taevasidian 底稿）[5]。
- **复制与高可用链路全**：异步主从 → 半同步 → 组复制 MGR（Paxos 变种）按需升级；OCI/AWS 上的 HeatWave 内置内存列存可补 HTAP 短板（taevasidian 底稿）[5]。
- **运维与上手门槛低**：主从复制开箱即用、调参面窄，「Web 场景默认」三十年惯性，招人容易（评测：Bytebase 2025；taevasidian 底稿 2026-08）[4][5]。
- **生态位依旧庞大**：DB-Engines 第 2（2026-08）[3]；LAMP/WordPress/大量存量系统的事实标准，迁移成本即护城河 [5]。
- **托管选择成熟**：RDS/Aurora（MySQL 兼容）/PlanetScale（Vitess 分片托管）全云覆盖 [5]。

## 为什么不选（新项目）

- **复杂查询落后**：多表 JOIN、子查询、CTE、窗口函数场景优化弱于 PG，2026 年基准与社区综述均指向差距在扩大而非收窄（评测：tech-insider 2026；Bytebase 2025）[2][4]。
- **JSON 与类型系统弱一档**：JSON 列可索引性与 JSONB+GIN 有差距；无数组/范围类型；extension 生态远不及 PG [5]。
- **GPL 双轨的商务摩擦**：闭源产品嵌入分发需评估 GPL 传染或购买 Oracle 商业许可；PG 的 BSD 类许可无此顾虑 [5]。
- **版本模型噪音**：8.4 LTS / 9.x Innovation / 历法版本号（26.x）三轨并行，选型与升级路径需要额外甄别（官方文档，访问 2026-08-27）[1]。

## 对比

- vs **PostgreSQL**：见 `../comparison.md` 属性矩阵。一句话：新项目无历史包袱 → PG；已有 MySQL 栈、团队熟悉、需求简单 → 继续用不亏 [5]。
- vs **TiDB**：要分布式扩展时，TiDB 兼容 MySQL 协议，是 MySQL 栈的平滑升级路径（见 `../tidb/report.md`）[5]。

## 风险与注意

- Oracle 单一控制方的开源治理风险（历史分叉出 MariaDB 的原因），长期路线依赖需评估 [5]。
- 复杂分析/HTAP 需求继续增长时，PG 或外挂 OLAP 的架构组合更从容 [2][5]。
- 「MySQL 比 PG 快」在 2026 年仅对简单读成立，别拿旧结论做新决策（评测：tech-insider 2026）[2]。

## 来源

1. MySQL Reference Manual · 1.3 MySQL Releases: Innovation and LTS（含 9.7 为旧版本模型最后一条线、转 YY.M 历法版本号）— https://dev.mysql.com/doc/refman/9.3/en/mysql-releases.html （访问 2026-08-27）
2. PostgreSQL vs MySQL: 5 Benchmarks Reveal the Winner（tech-insider，2026）— https://tech-insider.org/postgresql-vs-mysql-2026
3. DB-Engines Ranking（2026-08 快照，采集 2026-08-27）— https://db-engines.com/en/ranking
4. PostgreSQL vs MySQL（Bytebase，2025）— https://www.bytebase.com/blog/postgres-vs-mysql/
5. taevasidian《MySQL · 关系型数据库选型报告》与《PostgreSQL 数据库横评》（2026-08 导出；2026-08-06 会话调研底稿）
6. gh repos/mysql/mysql-server（star/push/tags 采集 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial（初始） | 首次记录：DB-Engines 2026-08 第 2；版本模型转历法版本号（26.7） |
