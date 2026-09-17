# Pinecone

> **TL;DR**：全托管向量检索的代名词——serverless 免运维、规模弹性好；但闭源按量计费、数据出域、平台锁定，学习与个人场景性价比低。

- **结论**：assess 评估
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 闭源 SaaS（托管版不开源；官方客户端 SDK 各语言开源） | [1] |
| 主页 | https://www.pinecone.io/ | — |
| 定位 | serverless 向量数据库，sparse+dense 混合、rerank、托管嵌入一体 | [1] |
| stats | 无 GitHub 主体仓库，不适用 refresh-stats | — |

## 为什么 assess（而非推荐）

- **免运维是真价值**：索引伸缩、副本、多区域全托管，serverless 档按读写计费，没有集群可操心——早期它几乎定义了「向量数据库」品类 [1]。
- **代价三项**：闭源（无法自托管，数据必须出域）；成本随规模/QPS 增长且公式不透明（对比自托管固定成本）；API 锁定（换库要重写索引管理代码）[1][2]。
- **格局已变**：2026 年开源阵营（Qdrant/Weaviate/Milvus）+ 云厂商原生方案成熟，「只有 Pinecone 能扛规模」的窗口期已关闭 [2]。

## 对比

- vs Qdrant Cloud / Zilliz Cloud / Weaviate Cloud：开源核心+托管的双轨模式给了「随时可搬走」的退路，Pinecone 没有 [2]。
- vs pgvector：个人项目/学习场景 Pinecone 免费档可用但学到的是平台 API 不是检索原理 [2]。

## 风险与注意

- 数据出域敏感的场景（内网合规）直接排除。
- 免费档规格与计价随时间调整，采用前按官网当日价核算（查询日 2026-09-17）[1]。

## 来源

1. 官方文档与定价 — https://www.pinecone.io/docs/ 、https://www.pinecone.io/pricing/（2026-09-17）
2. 口碑调研 — raw/2026-09-17/web/vector-databases-tavily-report.md（2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | assess | 首次记录：免运维但闭源锁定，个人场景性价比低 |
