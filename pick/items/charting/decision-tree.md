# 图表可视化 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

「让 AI 写」的前提下，图表（触发场景：桑基图）用什么库？（2026-08-18 会话首问；2026-08-27 入库）

## 分叉与决策

### D1 前提先立：图给人看还是给 AI 写？

- 会话定调：「最佳用什么。让 ai 写」——裁决维度是 **AI 代写友好度**，不是人工表达力。
- 决策：声明式配置 > 命令式代码；自包含交付物 > 工程构建；可闭环验证（写→看→改）优先。

### D2 AI 代写友好度裁决

- ECharts：一个 `option` 对象 + CDN 两行 → 单文件 HTML，浏览器即开即验，布局数学全由引擎算——四项全优。
- 落选节点：d3-sankey（命令式 + 手动布局，AI 写错率高，仅极致定制回头再看）；mermaid `sankey-beta`（三列 CSV 声明式可，但定制太弱、>~15 节点不可用）；Plotly（Python 工作流内次选，HTML 略重、交互样式弱一档）；RAWGraphs / Flourish（无代码人拖数据，非 AI 代写通道）；Tableau / Power BI（BI 环境自带桑基但别扭）。
- 叶：[Apache ECharts](echarts/) adopt

## 叶子

- 叶：[Apache ECharts](echarts/) adopt
