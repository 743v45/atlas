# RAG 框架与平台 · 横评

> 主题：检索增强生成（RAG）怎么落地——代码框架、低代码平台、托管 API 三条路线十一个候选。
> 用户画像：agent 工程师求职 + 个人开发；学习原理与生产可用并重，开源优先，闭源托管作对照。
> 数据核查日：2026-09-17（gh API 直查 stars/pushed_at/license，NOASSERTION 均解码 LICENSE 原文；口碑来自 tavily 检索 + AIMultiple 2026-08 基准，原始留档 `raw/2026-09-17/web/`）。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| 求职/学习主线（默认答案） | **LangChain + LangGraph** | 生态与 JD 双料事实标准，agentic RAG 主路径 [1] |
| 文档密集 RAG 管线 | **LlamaIndex** | 数据连接器/索引/检索抽象最深，与 LangGraph 可同栈 [2] |
| 快速搭内部知识库应用 | **Dify** | 可视化编排+知识库+发布一站式，⭐156k 平台头部 [5] |
| 复杂文档问答生产 | **RAGFlow** | DeepDoc 版式感知切块 + 引用溯源，文档理解最深 [6] |
| 管线搭好后的质量调优 | **DSPy** | 签名+指标驱动优化器，评估闭环内置 [4] |
| 工程纪律优先的团队 | **Haystack** | 类型安全、组件可测试、企业审计口碑 [3] |
| 五分钟验证「要不要 RAG」 | OpenAI File Search | 一行调用，检索黑盒不可调 [8] |
| 已在 Azure/GCP 栈 | Azure AI Search / Vertex AI Search | 云栈内正解，栈外不引入 [9][10] |
| 拖拽教学/演示 | Flowise | 直观但生产路径弱，定位夹缝 [7] |

## 属性对比矩阵

| 维度 | LangChain | LlamaIndex | Haystack | DSPy | Dify | RAGFlow | Flowise | OpenAI FS | Azure AI Search | Vertex AI Search |
|---|---|---|---|---|---|---|---|---|---|---|
| 形态 | 代码框架 | 代码框架 | 代码框架 | 声明式优化 | 低代码平台 | RAG 引擎 | 可视化编排 | 托管 API | 托管 API | 托管 API |
| 许可 | **MIT** [1] | **MIT** [2] | **Apache-2.0** [3] | **MIT** [4] | 修改版 Apache-2.0 [5] | **Apache-2.0** [6] | Apache-2.0+商业 [7] | 闭源 [8] | 闭源 [9] | 闭源 [10] |
| 成本 | 免费·开源 | 免费·开源 | 免费·开源 | 免费·开源 | 免费+云 | 免费·自托管 | 免费+云 | 按量付费 | Search Unit 计费 | 按查询计费 |
| RAG 能力 | 组件全 | **最深** | pipeline 完整 | 优化层 | 内置偏默认 | **解析最深** | 依赖外接 | 黑盒 | hybrid+ranker | recall 导向 |
| agentic 支持 | **LangGraph 一梯队** | 有，较弱 | 有，生态小 | 非主打 | 可视化 Agent | 内置工作流 | 拖拽 Agent | 工具链内 | Azure Agent 集成 | Agent Builder |
| 上手路径 | 教程最多 | RAG 最快 | 组件化心智 | 需评测集 | Web UI | Web UI+Docker | 拖拽 | 一行调用 | Portal/SDK | Console/SDK |
| 维护活跃(pushed) | 2026-09-17 | 2026-09-15 | 2026-09-17 | 2026-09-17 | 2026-09-17 | 2026-09-17 | **2026-08-13** | 持续 | 持续 | 持续 |
| ⭐(2026-09-17) | 146,512 | 52,197 | 26,526 | 38,088 | 156,096 | 90,874 | 55,466 | — | — | — |
| verdict | **adopt** | **adopt** | trial | trial | trial | trial | hold | trial | assess | assess |

## 本类别三条结构性结论（2026-09-17 快照）

1. **框架与平台不是互斥选型**：生产形态常是「LlamaIndex/RAGFlow 管检索数据层 + LangGraph 管编排 + 专用向量库做底座」的组合；「选一个」的真正分叉在学习主线（写代码）与交付主线（用平台）之间 [1][2][5][6]。
2. **低代码的代价是定制天花板**：Dify/RAGFlow 把切块/检索策略收进平台抽象——「RAG 原理学习」价值低于手写；而托管 API（File Search 等）连管线都不可见，只适合需求验证 [5][6][8]。
3. **license 在平台层开始出现附加条款**：框架层四家全部干净（MIT×2/Apache×2）；平台层 Dify 修改版 Apache（多租户限制）、Flowise 企业目录双轨——自用无感，商用 SaaS 前必查 [5][7]。

## 决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖所列维度；维度外风险（抽象漂移、安全漏洞口碑、pushed 放缓、平台锁定）以各条目 verdict 为准——Dify 矩阵分低于 DSPy 与「Dify 是 trial」并存不是矛盾：矩阵度量「选型综合值」，verdict 度量「该场景该不该用」。

## 来源

1. https://github.com/langchain-ai/langchain + https://github.com/langchain-ai/langgraph（gh 2026-09-17）
2. https://github.com/run-llama/llama_index（gh 2026-09-17）
3. https://github.com/deepset-ai/haystack（gh 2026-09-17）
4. https://github.com/stanfordnlp/dspy（gh 2026-09-17）
5. https://github.com/langgenius/dify（gh 2026-09-17，license 经 LICENSE 解码）
6. https://github.com/infiniflow/ragflow（gh 2026-09-17）
7. https://github.com/FlowiseAI/Flowise（gh 2026-09-17，license 经 LICENSE.md 解码）
8. https://platform.openai.com/docs/assistants/tools-file-search（2026-09-17）
9. https://learn.microsoft.com/azure/search/（2026-09-17）
10. https://cloud.google.com/vertex-ai/search（2026-09-17）
11. 第三方基准 — AIMultiple 2026-08-04 五框架同 workload 横评；HN 2026-05-12 托管 RAG 评测（colon-md/retrievalci，小样本降权）；原始留档 `raw/2026-09-17/web/rag-frameworks-tavily-report.md`、`rag-platforms-tavily-report.md`、`rag-managed-api-tavily-report.md`
