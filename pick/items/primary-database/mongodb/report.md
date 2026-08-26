# MongoDB

> **TL;DR**：文档灵活与原生分片仍是刚需场景的好选择，但多数「想用 MongoDB」的需求 PostgreSQL JSONB 已能覆盖且更稳；SSPL 非 OSI 许可是商业采用的心理闸门。

- **结论**：trial（试用——schema 剧变/超大规模分片刚需时引入）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 最新大版 8.3（2026-05-07）；8.0 线维护至 8.0.29（2026-08-11） | [1][2] |
| 许可证 | SSPL-1.0（源可用，非 OSI 认证开源；2018 年起替代 AGPL） | [5] |
| 仓库 | https://github.com/mongodb/mongo（⭐28,507，push 2026-08-26，gh 2026-08-27） | [6] |
| 维护活跃度 | 季度级小版本稳定输出；8.0 线 2026-08-11 仍在发安全更新 | [2] |
| 流行度 | DB-Engines 第 5（384.88 分，2026-08 快照），NoSQL 第一 | [3] |
| 托管 | Atlas：免费 M0 层（512MB）+ Flex 弹性档 + 专用集群按小时计费；Serverless 实例已于 2026-01-22 退役并迁移至 Flex（查询 2026-08-27） | [4] |

## 为什么选（在其领域）

- **schema 灵活是真优势**：结构频繁变化的初创迭代、内容/CMS、用户画像等场景，改字段不动表结构，开发速度极快 [5]。
- **原生分片成熟**：内置 sharding，海量文档的水平扩展比「PG + Citus」更省心 [5]。
- **聚合管道与文档模型**：嵌套文档即对象，面向对象映射自然；聚合管道做流水线式数据加工直观 [5]。
- **托管体验好**：Atlas 覆盖多云 + 专有云，搜索（Atlas Search）、向量（Atlas Vector Search）一体化（查询 2026-08-27）[4]。

## 为什么不选（新项目默认）

- **先问 JSONB 够不够**：PG 的 JSONB + GIN 索引已覆盖大多数文档型需求，且同时保留关系建模、严格 ACID 与 SQL 生态——「半个 MongoDB」+ 全部 PostgreSQL（taevasidian 底稿 2026-08）[5]。
- **SSPL 许可闸门**：非 OSI 开源，云厂商不可自由托管（AWS 因此自研 DocumentDB）；自托管商用虽通常无碍，但法务评估是现实摩擦 [5]。
- **事务与一致性后天补齐**：多文档事务 4.0 才有（4.2 支持分布式事务），复杂关联查询（JOIN 式 `$lookup` 性能差）仍弱于关系库——关联密集型业务不适合（taevasidian 底稿 2026-08）[5]。

## 对比

- vs **PostgreSQL**：逐维度见 `../comparison.md`。判断口径：读多写多、schema 多变、要原生分片 → MongoDB；关系+文档混合、要 SQL 与强一致 → PG [5]。
- vs **MySQL**：两者都被 PG 挤压，但挤压的方向不同——MySQL 丢的是功能上限，MongoDB 丢的是「文档需求可被 JSONB 替代」的部分 [5]。

## 风险与注意

- SSPL 下游分发/嵌入产品的合规评估（法务介入成本）[5]。
- Atlas Serverless 已退役迁移 Flex（2026-01-22），若有旧架构文档需更新口径（查询 2026-08-27）[4]。
- 分片键选错的重构成本极高——引入前先做容量与访问模式规划 [5]。
- Schema-less 是双刃剑：字段规范与数据治理要靠应用层自我约束（taevasidian 底稿 2026-08）[5]。

## 来源

1. New in MongoDB · 8.3（2026-05-07）— https://www.mongodb.com/products/updates/mongodb-8-3 （访问 2026-08-27）
2. MongoDB 8.0 Release Notes（8.0.29 · 2026-08-11）— https://www.mongodb.com/docs/manual/release-notes/8.0 （访问 2026-08-27）
3. DB-Engines Ranking（2026-08 快照，采集 2026-08-27）— https://db-engines.com/en/ranking
4. MongoDB Pricing 2026（checkthat.ai，含 Serverless 退役与 Atlas 档位；查询 2026-08-27）— https://checkthat.ai/brands/mongodb/pricing
5. taevasidian《MongoDB · 文档型 NoSQL 数据库选型报告》（2026-08 导出；2026-08-06 会话调研底稿）
6. gh repos/mongodb/mongo（star/push 采集 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial（初始） | 首次记录：8.3（2026-05）；DB-Engines 2026-08 第 5 |
