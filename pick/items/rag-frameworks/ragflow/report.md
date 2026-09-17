# RAGFlow

> **TL;DR**：文档理解最深的开源 RAG 引擎——版式感知切块（DeepDoc）、答案引用溯源、内置知识图谱，生产级文档问答利器；Apache-2.0 干净许可，中文社区一线。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/infiniflow/ragflow | — |
| 维护活跃度 | pushed 2026-09-17，⭐90,874（gh 2026-09-17） | [1] |
| 技术栈 | Python（DeepDoc 解析）+ Go/TS 组件，Docker Compose 部署 | [1] |

## 为什么选（作为 trial）

- **切块是它的护城河**：DeepDoc 做 PDF/扫描件的版式分析（表格、布局、阅读顺序），「按文档结构切」而不是「按 token 数硬切」——复杂文档场景检索质量差异的根源就在这一层 [2]。
- **引用溯源开箱即用**：答案逐句挂原文引用位置，企业场景「答案可核查」的硬需求直接满足 [2]。
- **规模与口碑**：⭐90.9k（仅次于 LangChain/Dify），InfiniFlow 中国团队主导，中文文档与社区一线；2026 年第三方对比将其列为「复杂 PDF、多文档推理」生产选项 [1][3]。

## 对比

- vs Dify：文档解析深度 RAGFlow 胜，应用编排/插件生态/发布面 Dify 胜；两者可组合（RAGFlow 做知识层、Dify 做应用层）[3]。
- vs 手写框架：想深学 RAG 原理手写，想快出文档问答系统 RAGFlow [3]。

## 风险与注意

- 部署面比 Dify 重（解析服务+ES/Infinity 存储+向量库多个组件），资源占用高 [2]。
- Agent 工作流能力有但编排生态小于 Dify/LangGraph，别当 agent 平台用 [2]。

## 来源

1. GitHub 仓库 — https://github.com/infiniflow/ragflow（gh 2026-09-17：Apache-2.0、⭐90,874、pushed 2026-09-17、语言构成直查）
2. 官方文档 — https://ragflow.io/docs（2026-09-17）
3. 口碑调研 — raw/2026-09-17/web/rag-platforms-tavily-report.md（2026-09-17，AI 综合结论中「Go 编写」「Apache-2.0 无附加」等与一手冲突处已按 gh/LICENSE 修正）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：文档问答生产力首选 |
