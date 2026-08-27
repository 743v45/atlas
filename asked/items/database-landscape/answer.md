# 给你 10 种数据库,优先选哪些?——全景与决策漏斗

> **TL;DR**:没有绝对的「最好」,只有场景的「最对」。基本盘永远是 PostgreSQL(+Redis 做缓存),遇到具体瓶颈再引入场景专家;数据库选型的思考路径是一个决策漏斗,不是一次全景对比。

*(恢复自 2026-08-06 问答,原答骨架忠实;对比结论的落地版见 pick/items/primary-database。)*

## 三个梯队

**第一梯队·核心主力**(解决 80% 通用需求):

1. **PostgreSQL**——功能最强的开源关系库:完整 ACID、强一致性;扩展生态(TimescaleDB 时间序列、PostGIS 地理);JSON 支持好到能当半个文档库。核心业务、金融交易、严谨结构首选。
2. **Redis**——内存键值,微秒级读写;丰富数据结构(List/Hash/Set);原生分布式锁、发布订阅、延迟队列。缓存、Session、排行榜、秒杀的标配。

**第二梯队·场景专家**(规模或结构触发时引入):

3. **MongoDB**——Schema-less 文档存储,天然契合面向对象、开发快、自带分片。用户画像、CMS、需求频繁变动的初创。
4. **Elasticsearch**——倒排索引毫秒级全文检索+聚合分析。商品搜索、全局检索、日志分析(LIKE %x% 在海量下的替代品)。
5. **ClickHouse**——列式存储,压缩比高、向量化执行,亿级大宽表分析快到离谱。BI 报表、行为分析、流量统计。

**第三梯队·领域极客**(极端场景):

6. **TiDB / CockroachDB**——NewSQL:MySQL 协议+无限横向扩展+强一致分布式事务。主从遇存储瓶颈时的终极解。
7. **Neo4j**——图数据库:多对多深层关系(Join 雪崩处)。社交网络、反欺诈、知识图谱。
8. **InfluxDB**——时序数据库:高频带时间戳写入+时间窗口聚合。IoT 监控、Metrics。

## 四条新赛道(2020s 追加)

- **向量数据库**(Milvus/Pinecone/Qdrant)——AI 时代基石:高维向量相似检索(HNSW),RAG 外挂知识库、以图搜图、推荐。
- **宽表/键值巨兽**(Cassandra/HBase/DynamoDB/RocksDB)——PB 级、绝对不能宕机:去中心化无单点、LSM-Tree 顺序写。苹果/网飞核心数据。
- **云原生/Serverless**(Aurora/Neon/PlanetScale)——存算分离、按需计费缩到 0、全球只读节点秒级复制。SaaS、出海、流量波动。
- **嵌入式/边缘**(SQLite/DuckDB)——嵌进应用进程、零运维、单文件。手机本地缓存、桌面软件、本地分析(DuckDB 是「分析界的 SQLite」)。

## 选型决策漏斗

默认首选 **PostgreSQL** 支撑基本盘 → 遇并发瓶颈加 **Redis** → 遇搜索/日志引入 **Elasticsearch** → 非结构化频繁变动上 **MongoDB** → 海量报表同步到 **ClickHouse**。多模态组合拳是业界成熟解;大模型需求再加向量库。

## 出处

- 源对话归档:../../../conversations/2026-08-06-database-landscape.md(2026-08-06)
- 决策落地:pick/items/primary-database(PG adopt、SQLite adopt、其余 trial/assess)
