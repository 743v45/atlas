---
date: 2026-08-18
topic: deepseek-harness 自治理审查(门的门)
related:
  - ../asked/items/gate-of-gates-green-not-sound/
原始会话: ~/.claude/projects/-Users-taevas-code-openresources-deepseek-harness/163afc75-d939-4984-ae98-aa89375ad52d.jsonl
---

# 2026-08-18 · deepseek-harness 自治理审查(门的门)

全量审查的收尾维度,任务书:「审查治理体系自身的治理(self-governance)与已知漏洞——防漂移工具自己会不会漂移?」,覆盖治理脚本测试覆盖、manifest 自治理、仓库自认漏洞、实际漂移实例、scripts/AGENTS.md、防漂移的漂移(gate 清单结构)六个面,要求产出抽查发现的漂移实例作为核心价值,证据带 file:line。

核心结论:治理的「机制层」有效(调度器有 spec、CI 结构被钉住、type-equiv manifest 双向自校验),但漂移发生在无人守望的层间缝隙。实证发现:28 个 verify-* 入口中 15 个零测试,覆盖率门作用域只覆盖 packages/*/*/src、scripts/ 治理代码完全豁免;doc-budgets 注释宣称的 5% headroom ratchet 未被脚本强制;AGENTS.md:100 / vendor/README.md:34 的 private:true 漂移(commit 97eb14a007 已删);vendor/README.md manifest 表 9 行版本全部过期(根因:check-vendor-manifest.sh 只盯 vendor/*/src/**,版本号 release 逃过守卫且该守卫仅本地 hook 不进 CI);供应链 gate verify-vendored-links 只被本地 hygiene 聚合调用、CI 全部 15 个 workflow 零引用,verify-cordis-api 是完全孤儿(无任何引用方);doc-budgets 软目标全线失守且 4 个文件 headroom 为 0-1.1%;AGENTS.md:73 称 hygiene 为 4 项检查实际跑 12 项。

方法论沉淀:「green gate means consistent, not sound」(i18n/README.md:40)——CI 绿只证明「接受当前仓库」,不证明「拒绝坏仓库」;knip 把 package.json scripts 当 entry 抓不到孤儿 gate。讲义恢复为 asked/items/gate-of-gates-green-not-sound。
