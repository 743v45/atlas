---
date: 2026-08-23
topic: 并行 agent 编队作战:方法线汇总
related:
  - ../apprentice/items/express/agent-fleet-parallelism/
原始会话: |
  汇总归档(方法线跨多会话,非单一来源):
  - 小天机 08-23 两会话(ds-phoneness 会战、测试质量会战)——源对话在小天机,待同步补档
  - 本机 robin SDD 编队现场: ~/.claude/projects/-Users-taevas-code-upyun-robin/41f4fc3f-f48f-4bc9-862e-bb1530fe11e8.jsonl (07-28, GLM-5.2)
  - 本机 holdon 支付链编队: 22c19544 (08-03), 见 2026-08-03-holdon-recharge-reconciler.md
  - 其余本机例(robin 28-subagent、longxia、workbuddy、11-agents 写库、deepseek、bili)未逐一定位原始 jsonl,据 dig INBOX 摘要收录
---

# 2026-08-23 · 并行 agent 编队作战:方法线汇总

「调查先行」管单会话怎么走,「编队作战」管任务大到单会话装不下时怎么拆、怎么并发、怎么验收。本文汇总两机多会话里的编队实例与共同纪律。

## 需求的原始表述(代表句)

- robin 现场(07-28),AI 逐任务串行实现两轮后,用户一句触发编队:
  > 能并发实现不
- holdon 支付链(08-03):
  > 并发实现
- longxia(本机):2 句话需求即启动 19-agent 三层审计,交付 C1-C14 编号问题清单。

## 关键转折

- **robin SDD 编队现场**(最完整的本机档案):任务先拆成带完整代码块的 brief,每任务配 Implement + Review 成对 subagent;Implement 走 RED→GREEN(先复现 `Cannot find module` 再实现);Review 独立对照 brief 逐项核(Spec Compliance / Strengths / Issues 按 Critical-Important-Minor / Assessment 结论「Approved」)。中途有 subagent 被 kill,半成品由后续任务接力而非重跑全量——**接力是常态,不是事故**。
- **holdon G1-G4 编队**:13 subagent 分四组实现,集成缝隙(Makefile 漏项)暴露后由主线会话兜底——编队交付 ≠ 完成,集成面归主线。
- **11 agents 5m45s 并发写库零失败**:每个 agent 回传自己写入条目的真实 URL 作为自验证证据——把「报告完成」变成「可点开验证」,这是编队的验证闭环。
- **deepseek 维度切分法**:大任务按维度切片,每片附必读清单 + 穷举式指令,单会话 2-6 分钟收敛一片。
- **bili 9 路十分钟齐发**:齐发后用户中途手动砍掉部分——编队也允许人随时裁撤,不是发出去就等。
- 小天 08-23 两会战(ds-phoneness、测试质量)采用轮次制验收,第 5 轮验收词:「复核修复本身」——最后一轮不查新问题,专查修复有没有引入新伤。

## 最终结论

- 共同纪律:① 文件级隔离分工(各 agent 认领不相交文件集);② 每任务 review gate(subagent 当裁判);③ 集成缝隙与兜底归主线;④ 验收轮次制,末轮复核修复本身;⑤ 回传可验证证据(URL/命令输出),不收口头「完成」。
- 沉淀为 apprentice 课「并行 agent 编队作战」。
