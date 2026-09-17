# Dify

> **TL;DR**：低代码 LLM 应用平台头部（⭐156k 全场最高）——可视化编排 + 知识库 + Agent 一站式，快速搭内部应用首选；深度定制与多租户商用是天花板。

- **结论**：trial 试用
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 修改版 Apache-2.0（附加条件：多租户环境商用需授权 + 前端 LOGO/版权不可移除；LICENSE 解码确认，GitHub 识别 NOASSERTION） | [1] |
| 仓库 | https://github.com/langgenius/dify | — |
| 维护活跃度 | pushed 2026-09-17，⭐156,096（gh 2026-09-17，全场候选最高） | [1] |
| 技术栈 | Python 后端 + TypeScript 前端，Docker Compose / Helm 自托管 | [1] |

## 为什么选（作为 trial）

- **从 0 到内部应用最快的一档**：Web UI 里完成 prompt 编排、知识库上传、模型接入、发布为 API/WebApp；向量库可插（pgvector/Qdrant/Milvus/Weaviate 等）[2]。
- **插件生态与社区体量第一**：156k star，模型/工具插件市场活跃，中文文档与社区是一线水平（LangGenius 中国团队）[1][3]。
- **企业功能分层清晰**：自托管 OSS 免费覆盖个人与单组织内部使用 [1]。

## 对比

- vs RAGFlow：Dify 赢在应用平台面（编排/发布/多模型）；RAGFlow 赢在文档理解深度（版式感知切块、引用溯源）——知识库问答重文档解析选 RAGFlow，重应用编排选 Dify [3]。
- vs 手写框架：平台限死了检索管线内部的定制空间；切块策略、混合检索调优深度到平台边界为止 [3]。

## 风险与注意

- **多租户商用限制**：用 OSS 源码对外运营多租户 SaaS 需商业授权——内部工具不受影响 [1]。
- 2026-06 有安全漏洞的社区口碑（tavily AI 综合提及，**待验证**）；自托管暴露公网时按安全清单配置 [3]。
- 检索质量调优受平台抽象约束，「RAG 原理学习」价值低于手写框架。

## 来源

1. GitHub 仓库 + LICENSE — https://github.com/langgenius/dify（gh 2026-09-17：⭐156,096、pushed 2026-09-17；license 2026-09-17 解码）
2. 官方文档 — https://docs.dify.ai/（2026-09-17）
3. 口碑调研 — raw/2026-09-17/web/rag-platforms-tavily-report.md（2026-09-17，AI 综合结论与一手数据冲突处已按 gh/LICENSE 修正）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | trial | 首次记录：内部应用快跑平台，多租户商用看 license |
