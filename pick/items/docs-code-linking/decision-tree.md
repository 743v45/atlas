# 文档-代码关联 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

文档与代码如何做到强关联（个人/小团队：代码仓 + 知识库 + 博客三落点）？（调研 2026-08-25）

## 分叉与决策

### D1 关联强度分级：六级光谱

- 引用级（md 链接/permalink）→ 嵌入级（Docusaurus/Fern 构建时拉代码）→ 生成级（TypeDoc/godoc 从 docstring）→ 锚点级（Swimm token/AST）→ 决策级（ADR 互引）→ AI 时代（AGENTS.md/index.md/llms.txt）。
- 决策框架：**四支柱**——稳定标识 / 单一事实源 / 强制校验 / 变更触发；**分水岭在第三条**：「检测可漂移」≠「强关联」。

### D2 标识用什么：行号还是 symbol？

- 行号在重构后静默失效——引用一律指 symbol/文件路径，永不指行号。这条纪律拿到锚点级 80% 的能力。

### D3 强制力从哪来：工具还是 CI？

- Swimm 值钱的是 `swimm-verify` GitHub Action 而非锚点算法——但商用 SaaS + IDE 插件 + 团队流程对个人/小团队过重（2026 还战略转向企业现代化服务、定价改按代码行数）。
- 决策：**自建「嵌入级 + CI 强制校验」**（同仓 docs/ + 引用指 symbol + CI 死链检查 exit 1 卡合并 + ADR 留痕），成本一天，强制力来自 CI 而非工具。
- 叶：[CI 校验组合](ci-drift-combo/) adopt · 落选节点：[Swimm](swimm/) hold（团队场景可复评）

### D4 生成级要不要？

- API 参考由 docstring 生成（单一事实源），作为组合的补充组件——TypeDoc 周下载 490 万是生态位证明。
- 叶：[TypeDoc](typedoc/) trial

### D5 载体选什么 SSG？

- 嵌入级载体按知识库/博客形态另行决策（Hugo 通道已存在），Docusaurus 是候选非必选。
- 叶：[Docusaurus](docusaurus/) assess

### D6 2026 新变量：AI 层标准落定

- AGENTS.md 入 Linux Foundation AAIF（2025-12）、llms.txt v2 提案（2026-08）——AI 层并入组合作为组件；若出现「AST 锚点 + CI verify」的开源 CLI，Swimm 的 hold 应立即重评（观察名单注记）。

## 决策矩阵一致性

加权排序：ci-drift-combo 97 > swimm 86 > typedoc 82 > docusaurus 75——swimm 高分与 hold 并存即「机制强但 SaaS 重流程」，注记分工。
