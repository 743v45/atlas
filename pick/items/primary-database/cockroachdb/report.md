# CockroachDB

> **TL;DR**：强一致分布式与运维自动化最好的 NewSQL 之一，但 BUSL 源可用许可（2024-08 起对年收入 ≥$5M 企业收费）与云优先导向，让开源自托管的新采用需要掂量；跨区域强一致刚需时值得试。

- **结论**：trial（试用——跨区域强一致/超单机规模场景）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v26.2（2026-04-27 发布，当前最新大版线）；v25.4 等旧线维护中 | [1] |
| 许可证 | BUSL-1.1（源可用）：2019 年弃 Apache-2.0 转 BSL/BUSL；2024-08-15 起收费门槛从年收入 $10M 降至 $5M | [2] |
| 仓库 | https://github.com/cockroachdb/cockroach（⭐32,415，push 2026-08-07，gh 2026-08-27——注意推送间隔约 3 周，开发主干可能部分内移，待验证） | [6] |
| 维护活跃度 | Cockroach Labs 主导，历法版本号持续发版（26.1→26.2） | [1] |
| 流行度 | DB-Engines ≈第 65（2026-08 快照，呈下滑趋势） | [3] |
| 托管 | CockroachCloud（Serverless/Standard/Dedicated 档） | [4] |

## 为什么选（在其领域）

- **强一致 + 弹性伸缩**：Raft 复制 + range 自动再平衡，节点/区域级容灾，水平扩容对应用透明（taevasidian 底稿 2026-08）[5]。
- **跨区域部署简单**：多区域/存活区配置（survival goals）是同类中最省心的全球部署故事 [5]。
- **PG 线协议兼容**：驱动生态可直接复用 PostgreSQL 客户端（语法有差异，非 100% 兼容）[5]。
- **运维自动化好**：自动再平衡/自动修复，DBA 投入低于「PG + Patroni + Citus」自组装方案 [5]。
- **事务正确性有硬基础**：HLC 混合逻辑时钟支撑跨地域 Serializable 隔离；Geo-partitioning 可指定数据落点降延迟（taevasidian 底稿 2026-08）[5]。

## 为什么谨慎（trial 而非 adopt）

- **BUSL 许可闸门**：非 OSI 开源；年营收 ≥$5M 的企业自托管商用需付费（TechCrunch 2024-08 报道许可调整）[2]。这是三剑客中许可最不干净的一家——同场景下 YugabyteDB 已 100% Apache-2.0。
- **云优先的商业重心**：功能节奏向 CockroachCloud 倾斜（如 v25.4.x 部分版本仅限云集群，官方文档 2026-03 访问）[4]。
- **PG 兼容是协议级**：扩展（PostGIS/pgvector 等）不可用，语法差异带来迁移摩擦——「深兼容」的是 YugabyteDB（见 `../yugabytedb/report.md`）[5]。
- **热度下行**：DB-Engines 2026-08 排 ≈65 且趋势下滑；GitHub push 间隔变长（观测 2026-08-27，待验证）[3][6]。

## 对比

- vs **YugabyteDB**：同为 PG 兼容分布式；Yugabyte 深兼容（fork PG 查询层）+ Apache-2.0，Cockroach 强在托管成熟度与多区域故事。逐维度见 `../comparison.md`。
- vs **TiDB**：TiDB 走 MySQL 协议 + HTAP；Cockroach/Yugabyte 走 PG 兼容路线——先看团队协议栈再选（taevasidian 底稿 2026-08）[5]。
- vs **PostgreSQL**：单区域内 + 依赖扩展生态 → PG；跨区域强一致/超单机规模 → NewSQL [5]。

## 风险与注意

- BUSL 合规：营收接近 $5M 或有上市/并购预期的公司，自托管商用前需法务确认 [2]。
- 扩展生态不可用（PostGIS/pgvector 等），重度依赖 PG 扩展的团队迁移会痛 [5]。
- 单区域内性能不如原生 PG/MySQL（分布式共识开销），写延迟受多数派复制制约——「为了分布式而分布式」会得不偿失（taevasidian 底稿 2026-08）[5]。
- 开源社区活跃度依赖单一商业公司；GitHub 主仓 push 间隔 2026-08 观测约 3 周，持续观察（待验证）[6]。

## 来源

1. CockroachDB EOL/EOS 汇总（endoflife.date，访问 2026-08-27）— https://endoflife.date/cockroachdb
2. Cockroach Labs shakes up its licensing to force bigger companies to pay（TechCrunch，2024-08-15）— https://techcrunch.com/2024/08/15/cockroach-labs-shakes-up-its-licensing-to-force-bigger-companies-to-pay
3. DB-Engines Ranking（2026-08 快照，采集 2026-08-27）— https://db-engines.com/en/ranking
4. CockroachDB v25.4 Release Notes（官方文档，访问 2026-08-27）— https://www.cockroachlabs.com/docs/releases/v25.4
5. taevasidian《CockroachDB · 分布式 NewSQL 数据库选型报告》（2026-08 导出；2026-08-06 会话调研底稿）
6. gh repos/cockroachdb/cockroach（star/push 采集 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial（初始） | 首次记录：v26.2（2026-04）；BUSL ≥$5M 收费门槛是主要顾虑 |
