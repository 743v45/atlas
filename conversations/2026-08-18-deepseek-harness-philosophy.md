---
date: 2026-08-18
topic: deepseek-harness 设计哲学分析
related:
  - ../asked/items/deepseek-harness-design-philosophy/
原始会话: ~/.claude/projects/-Users-taevas-code-openresources-deepseek-harness/78f956bc-bb7b-4aca-895a-671827784f26.jsonl
---

# 2026-08-18 · deepseek-harness 设计哲学分析

用户对只读仓库 /Users/taevas/code/openresources/deepseek-harness 下指令「分析其设计哲学。放 analyze/ 下」。AI 按强制并发规则先侦察仓库布局(50+ 包、双语文档体系、Agent Notes 治理体系),一次派发 10 个并行维度 agent(核心架构 / capability seam / 类型边界 / 会话可观测性 / 测试 / 治理 / 防御模式 / vendoring / loop 与工具 / 前端 SDK,deps 因 fork 失败重发一次),交叉综合而非简单拼接,落盘 analyze/DESIGN_PHILOSOPHY.md(完整版,全部论断带 file:line 证据)+ design-philosophy.html(5 张 mermaid 关系图,浏览器实测 5 SVG 全渲染零语法错误)。

核心结论:仓库围绕第一性假设「读者与贡献者是跨 session 无记忆的 AI agent」设计,推导出七根支柱——一切皆插件(连 agent-loop 都是)、单一事实源其余皆投影(Model-visible ⟺ logged 有 runtime 断言)、信任边界由序列化介质枚举、capability seam 按演化速率划界、响亮失败(过度拒绝优于静默残缺)、判断落成机器可校验工件(决策→Note、规则→27 门)、测试即证据(per-file 100% 是删代码机制)。附赠发现一处真实文档漂移:AGENTS.md:100 与 vendor/README.md:34 仍写 vendored 包 private:true,但 @deepseek-ai/cordis 4.0.1 已公开发布。

关键转折:用户随后追加「精简重点版 + 主索引 + 最终 HTML 单页报告」的需求,AI 补齐 analyze/KEY_POINTS.md(~90 行重点提炼)、INDEX.md(主索引)、index.html(单页报告,重点 + 内嵌 5 图,实测渲染通过),analyze/ 目录定型为 5 个文件;收尾清理全部 11 个 subagent,仓库本身零修改。

讲义为「指向条目」:asked/items/deepseek-harness-design-philosophy 存 TL;DR + 骨架,正文指向该仓库 analyze/ 落盘文件,不搬运正文。
