# 向量数据库 · 横评

> 主题：RAG 检索底座选型——嵌入向量存哪、怎么查。
> 用户画像：个人/学习起步优先低运维；规模动机优先检索能力。开源优先，闭源托管作对照。
> 数据核查日：2026-09-17（gh API 直查 stars/pushed_at/license；口碑来自 tavily 检索综合，关键论断已与官方文档/一手 license 文件交叉核对，原始留档 `raw/2026-09-17/web/vector-databases-tavily-report.md`）。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| 已有 Postgres（默认答案） | **pgvector** | `CREATE EXTENSION` 即得，ACID/备份白拿，千万级向量内不用换 [1] |
| PG 不够用，亿级以内升级 | **Qdrant** | Rust 内核 + 过滤/量化强项 + Apache-2.0，云/自托管同核 [2] |
| 十亿级、吞吐极限 | **Milvus** | 分布式设计目标就是超大吞吐，代价是全家桶运维 [3] |
| 混合检索/库内模块优先 | **Weaviate** | BM25+向量原生融合，嵌入/重排模块在库内执行 [4] |
| 本地原型、notebook | **Chroma** | pip 即用零配置，生产再迁 [5] |
| 已有 ES 栈 | **Elasticsearch** | BM25+向量最成熟，顺手用；绿地不引入 [6] |
| 完全免运维且不差钱 | Pinecone | serverless 代名词，闭源+锁定+成本黑箱 [7] |

## 属性对比矩阵

| 维度 | pgvector | Qdrant | Milvus | Weaviate | Chroma | Elasticsearch | Pinecone |
|---|---|---|---|---|---|---|---|
| 形态 | Postgres 插件 | 专用向量库 | 专用库（分布式） | 专用向量库 | 嵌入式/单机 | 搜索引擎 | 全托管 SaaS |
| 许可 | **PostgreSQL** [1] | **Apache-2.0** [2] | **Apache-2.0** [3] | **BSD-3-Clause** [4] | **Apache-2.0** [5] | AGPL/SSPL/ELv2 三轨 [6] | 闭源 [7] |
| 成本 | 免费·自托管 | 免费+云 | 免费+云(Zilliz) | 免费+云 | 免费+云 | 免费+云 | 按量付费 |
| 混合检索 | SQL 全文+向量 | dense+sparse | dense+sparse | **内置 BM25+向量** | 有限 | **BM25+向量原生** | sparse+dense |
| 部署 | 随 PG 走 | 单机/集群/云 | 集群优先 | 单机/集群/云 | 进程内/单机 | 集群 | 仅云 |
| 规模定位 | 千万级内 | 亿级 | 十亿级 | 亿级 | 原型·百万级 | 亿级+ | 亿级 |
| 维护活跃(pushed) | 2026-09-10 | 2026-09-17 | 2026-09-17 | 2026-09-17 | 2026-09-17 | 2026-09-17 | 持续（托管） |
| ⭐(2026-09-17) | 23,040 | 34,628 | 46,138 | 16,815 | 29,315 | 77,923 | — |
| 运维面 | **零新增** | 低-中 | 高 | 中 | **零** | 高 | **零（托管）** |
| verdict | **adopt** | trial | trial | trial | trial | assess | assess |

## 本类别三条结构性结论（2026-09-17 快照）

1. **规模决定形态，不是品牌**：千万级内插件/嵌入式（pgvector/Chroma）够用且运维最轻；亿级内专用单机→集群（Qdrant/Weaviate）；十亿级才是 Milvus 的战场——先量规模再挑库 [1][2][3]。
2. **license 分化是隐性成本**：Apache-2.0/BSD/PostgreSQL 三家干净；ES 三轨（AGPL 默认）有合规心智负担；Dify 式附加条款在向量库阵营不存在但 ES 的历史分叉提醒「开源」不等于「无条款」[4][6]。
3. **全部候选 2026-09 仍活跃**：7 条中 5 个仓库当日有 push（gh 2026-09-17），本类别无停更陷阱；真正的坑在「为规模买单早了」而不是「选了死项目」。

## 决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖所列维度；维度外风险（单一公司主导、商业化转型、license 三轨）以各条目 verdict 为准——Qdrant 矩阵分高于 pgvector 与「pgvector 是 adopt」并存不是矛盾：矩阵权重对齐「检索能力优先」画像，adopt 结论对齐「已有 Postgres 时运维优先」的起步路径。

## 来源

1. https://github.com/pgvector/pgvector（gh 2026-09-17）
2. https://github.com/qdrant/qdrant（gh 2026-09-17）
3. https://github.com/milvus-io/milvus（gh 2026-09-17）
4. https://github.com/weaviate/weaviate（gh 2026-09-17，license 经 README/LICENSE 解码）
5. https://github.com/chroma-core/chroma（gh 2026-09-17）
6. https://github.com/elastic/elasticsearch（gh 2026-09-17，license 经 LICENSE.txt 解码：默认 AGPL/SSPL/ELv2 三轨）
7. https://www.pinecone.io/docs/ 、https://www.pinecone.io/pricing/（2026-09-17）
8. 口碑原始留档 — `raw/2026-09-17/web/vector-databases-tavily-report.md`（精确 QPS 数字无出处，全部不采用，仅采定性结论）
