# RAG 框架与平台 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

RAG 管线怎么落地——写代码、用平台、还是调托管？（2026-09-17 会话；用户画像：agent 工程师求职 + 个人开发，学习原理与生产可用并重）

## 分叉与决策

### D1 写代码还是不写代码？

- 求职/学习动机下「一行调用」是反教育——托管 API 检索黑盒，学不到切块/检索/重排原理；但它是需求验证器。
- 叶：[LangChain / LangGraph](langchain/) adopt（写代码路线的生态与 JD 双料事实标准；LangGraph 承担 agentic 编排后主业转向 agent 工程）
- 叶：[OpenAI File Search](openai-file-search/) trial（需求验证器定位：五分钟验证「要不要 RAG」，不是学习工具）

### D2 写代码：主线框架选谁？

- 通用编排（LangChain）与数据专精（LlamaIndex）回答的是两个问题——管线怎么搭 vs 数据怎么变成可检索上下文；生产常同栈。
- 叶：[LlamaIndex](llamaindex/) adopt（数据连接器/索引/检索抽象最深，文档密集场景默认管线）
- 叶：[Haystack](haystack/) trial（工程纪律优先的团队备选主线：类型安全+组件可测试；社区声量小一档）
- 叶：[DSPy](dspy/) trial（不是编排对手而是优化层：管线搭好后用指标自动调 prompt，前置成本是评测集）

### D3 不写代码：平台选谁？

- 平台化一站式 vs 文档理解深度是两种交付动机；可视化纯原型是教学场景。
- 叶：[Dify](dify/) trial（内部应用快跑平台头部：可视化编排+知识库+发布一站式；多租户商用看修改版 Apache 条款）
- 叶：[RAGFlow](ragflow/) trial（文档问答生产力首选：DeepDoc 版式感知切块 + 引用溯源；部署面较重）
- 叶：[Flowise](flowise/) hold（拖拽教学直观，但无内置模型/知识库管理，被 Dify 与手写两头挤压；pushed 放缓待观察）

### D4 云栈内要不要用托管搜索？

- 已在 Azure/GCP 栈的企业用户，托管搜索的权限/合规/连接器是白拿；栈外引入无理由。
- 叶：[Azure AI Search](azure-ai-search/) assess（托管三家能力天花板：hybrid+语义 ranker+字段级权限+合规最全）
- 叶：[Vertex AI Search](vertex-ai-search/) assess（recall 导向 + BigQuery/Workspace grounding 一体，GCP 栈内正解）

## 落选节点（不立条目的死分支）

- **裸 API 手写（OpenAI/Anthropic SDK 直接拼）**：学原理的最佳练习、面试的加分答案——但它是练习不是选型，不立目；框架的存在意义正是省掉这部分脚手架。学习路径上「裸写一版对照框架」写进了 LangChain 条目的风险节。
- **Pathway**：实时/流式知识库取向，被「LlamaIndex Alternatives」类对比文提名；社区体量与 RAG 主流生态位小，不占大牌坑位，观察名单。
- **Vectara**：闭源 RAG-as-a-service（检索+生成全托管），与托管 API 路线重叠且声量弱于云厂商三件套；闭源+锁定代价同 Pinecone 逻辑，不重复立目。
- **CrewAI / AutoGen 等 multi-agent 框架**：它们回答「多 agent 怎么协作」，RAG 只是可选配件——域外（归 dev-automation 域的问题），本类别不收。
- **LangChain 0.x 时代教程生态**：不是条目而是时代切片——1.0 前「链式抽象过重」的社区争议是 LangChain 早年主要差评源，1.0 + LangGraph 收敛后回稳，本树记录此背景避免误用旧口碑。

## 观察名单（下次复核触发器）

- Flowise：pushed 持续停滞（2026-12 复核）→ hold 维持或升级为停更警示
- Dify：2026-06 安全漏洞口碑（tavily AI 综合，待验证）→ 查实后写入风险节并复核 verdict
- DSPy：评测集建起来后实跑一轮 → trial 升级评估
- Azure/Vertex：若出现跨云抽象层（如 LangChain retriever 全兼容）→ 重估锁定代价权重
