# Chroma

> **TL;DR**：原型最快路径——`pip install chromadb` 即用的嵌入式向量库，零配置起步；分布式与生产能力是短板，定位正转向「Search infrastructure for AI」。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/chroma-core/chroma | — |
| 维护活跃度 | pushed 2026-09-17，⭐29,315（gh 2026-09-17） | [1] |
| 定位 | 仓库描述「Search infrastructure for AI」（2026-09-17 快照）；Chroma Cloud 商业化并行 | [1][2] |

## 为什么选（作为 trial）

- **上手摩擦全场最低**：Python 进程内跑、默认本地持久化，几行代码出第一个 RAG 原型；教学与 notebook 场景事实标准 [2]。
- **默认嵌入打包**：内置默认嵌入函数，BYO 模型也可换；LangChain/LlamaIndex 教程普遍拿它当示例库 [2]。
- **社区体量大**：⭐29.3k，超过 Qdrant 与 pgvector 之外的大多数对手 [1]。

## 对比

- vs pgvector：同为「轻起步」答案——pgvector 换来的是与业务库同事务+生产即视感；Chroma 换来的是零 PG 依赖的纯本地开发体验 [2][3]。
- 生产化路径：单机/客户端-服务器模式可用但分布式能力弱于 Qdrant/Milvus，规模上去要迁移——迁移本身不难（数据导出），但索引参数体系要重建 [2][3]。

## 风险与注意

- **商业化转型期**：重心向 Chroma Cloud 移动（新定位描述可见），开源单机版的演进节奏需持续观察 [1][2]。
- 混合检索（关键词+dense）能力有限，做 hybrid RAG 不是它的强项 [3]。

## 来源

1. GitHub 仓库 — https://github.com/chroma-core/chroma（gh 2026-09-17：Apache-2.0、⭐29,315、pushed 2026-09-17）
2. 官方文档 — https://docs.trychroma.com/（2026-09-17）
3. 口碑调研 — raw/2026-09-17/web/vector-databases-tavily-report.md（2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：本地原型默认，生产换库 |
