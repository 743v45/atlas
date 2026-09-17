# LangChain / LangGraph

> **TL;DR**：生态最大的 LLM 编排框架——LangGraph 承担 agentic 编排后主业已转向 agent 工程（仓库自述「The agent engineering platform」），RAG 教程、集成与招聘 JD 三料事实标准。

- **结论**：adopt 推荐
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/langchain-ai/langchain（⭐146,512、pushed 2026-09-17，gh 2026-09-17） | [1] |
| LangGraph | https://github.com/langchain-ai/langgraph（⭐41,810、MIT、pushed 2026-09-17，gh 2026-09-17） | [2] |
| 配套 | LangSmith（观测/评估，商业）、LangGraph Platform（部署） | [3] |

## 为什么选（作为 adopt）

- **生态与人才市场双第一**：⭐146.5k 全场最高；模型/向量库/加载器集成覆盖最广；agent 工程师 JD 的事实关键词（本次选型动机）[1][3]。
- **agentic RAG 路径完整**：LangGraph 以状态图/检查点编排多步 agent 流程，「检索作为 tool」的 agentic RAG 主流实现路径，2026 年第三方基准将 LangChain+LangGraph 列为同 workload 对比组 [4]。
- **1.0 后口碑回稳**：早期抽象过重争议后，核心 API 收敛、LangGraph 成独立稳定项 [3]。

## 对比

- vs LlamaIndex：RAG 纯度与数据抽象 LlamaIndex 更深；编排广度、agent 生态、就业市场 LangChain 胜——两者常同栈使用（LlamaIndex 管检索、LangGraph 管编排）[4]。
- vs DSPy：DSPy 管优化不管编排，可在 LangChain 管线之上叠加做 prompt 调优 [4]。

## 风险与注意

- 抽象层数多，链路调试比裸写难；不熟悉时容易「会用不知道为什么」——学习期建议同时裸写一版对照。
- 商业件（LangSmith/Platform）与开源件边界要分清，避免默认依赖托管服务 [3]。

## 来源

1. GitHub 仓库 — https://github.com/langchain-ai/langchain（gh 2026-09-17：MIT、⭐146,512、pushed 2026-09-17，描述「The agent engineering platform」）
2. GitHub 仓库 — https://github.com/langchain-ai/langgraph（gh 2026-09-17）
3. 官方文档 — https://python.langchain.com/ 、https://langchain.com（2026-09-17）
4. 第三方基准 — AIMultiple 2026-08-04 五框架同 workload 横评（GPT-4.1-mini + BGE-small），原始输出留档 raw/2026-09-17/web/rag-frameworks-tavily-report.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | adopt | 首次记录：生态/JD 事实标准，agentic RAG 主路径 |
