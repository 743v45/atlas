# LlamaIndex

> **TL;DR**：为 RAG 而生的数据框架——连接器、索引、检索抽象全场最深，文档密集场景管线首选；现已扩展为「文档处理平台」（LlamaParse/LlamaCloud 商业件并行）。

- **结论**：adopt 推荐
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/run-llama/llama_index | — |
| 维护活跃度 | pushed 2026-09-15，⭐52,197（gh 2026-09-17） | [1] |
| 定位 | 仓库描述「the document processing platform for AI」（2026-09-17 快照） | [1] |

## 为什么选（作为 adopt）

- **RAG 纯度最高**：40+ 数据连接器、树/关键词/知识图谱等多索引结构、切块/检索后处理原语是各家框架中最细的，「怎么把数据变成可检索上下文」这一个问题它回答得最完整 [2]。
- **文档密集场景的默认管线**：第三方横评将其定位为「数据密集、文档中心场景首选， messy corpus 下检索优势明显」[3]。
- **十行代码出管线**：`VectorStoreIndex.from_documents` + query engine 的最小路径是各家最短，学习曲线友好 [2]。

## 对比

- vs LangChain：检索/索引深度 LlamaIndex 胜，agent 编排广度 LangGraph 胜；同栈组合（LlamaIndex 管检索、LangGraph 管编排）是常见生产形态 [3]。
- 商业化件 LlamaParse（文档解析）/LlamaCloud 与开源核同品牌，注意边界，开源用不吃亏 [2]。

## 风险与注意

- API 面大且迭代快，教程版本漂移是社区常见抱怨；跟官方文档版本走 [2]。
- agent 能力有（AgentWorkflow 等）但生态声量明显小于 LangGraph，agentic 重场景别指望它当编排层 [3]。

## 来源

1. GitHub 仓库 — https://github.com/run-llama/llama_index（gh 2026-09-17：MIT、⭐52,197、pushed 2026-09-15）
2. 官方文档 — https://docs.llamaindex.ai/（2026-09-17）
3. 第三方基准与口碑 — AIMultiple 2026-08-04 横评 + tavily 综合结论，原始输出留档 raw/2026-09-17/web/rag-frameworks-tavily-report.md（关键论断经 gh 仓库描述交叉核对）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | adopt | 首次记录：RAG 数据侧默认答案 |
