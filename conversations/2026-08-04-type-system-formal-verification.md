---
date: 2026-08-04
topic: 类型系统与形式化验证
related:
  - ../asked/items/type-system-and-formal-verification/
原始会话: ~/.claude/projects/-Users-taevas/19315383-3746-4a78-aff7-24be31a8d660.jsonl
---

# 2026-08-04 · 类型系统与形式化验证

用户问「类型系统、形式化验证 是什么」,AI 给出成体系的长答:类型系统(贴标签 + 静态约束、静态/动态 × 强/弱、类型推断、soundness 健全性、依赖类型)与形式化验证(建模/规约/证明三要素、safety 与 liveness、模型检测 vs 定理证明及工具对照)分讲,再合流到两者的关系——类型系统本质是轻量级自动化的形式化验证,底层是 Curry–Howard 同构(命题即类型、证明即程序),并给出「动态语言 → 静态强类型 → 高级类型 → 依赖类型 → 完整形式化验证」的保证强度谱系,收在「成本 vs 保证强度」的选型权衡。

用户随后要求「写进 outline,你可以丰富一下。并且格式写的易读」。AI 因缺实例凭据(本地未探到 Outline 实例)转而请用户提供 URL/API token/collection 名,并给出丰富版文档结构大纲;会话止于待提供凭据,当日未完成写入。讲义恢复为 asked/items/type-system-and-formal-verification(内容以原答案为骨架,为自洽补足谱系图说明,标「AI 重构」)。
