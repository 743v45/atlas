# 长报告回传只剩最后一句:final text 不是传输通道

> **TL;DR**:错在拿 subagent 的 final text 当可靠传输通道——它是摘要面,不是数据面;长产物该落盘走路径。

- **状态**:fixed(已修正)
- **日期**:2026-07-28
- **出处**:robin CLI 会话,final whole-branch review subagent(merge gate 审查)

## 经过

final whole-branch review subagent 完成了完整审查(按约定格式:原则覆盖/跨任务一致性/Critical/Important/Minor 裁决/Verdict 六段),coordinator 收到的却只剩最后一句(`--force` 无效)。coordinator 被迫要求整份重发:「你的审查完成了,但返回的内容只剩最后一句……我需要全部 findings 才能决定修复范围。」

## 根因

我以为是偶发丢消息,其实是通道选型错误:final text 是给「结论摘要」的,长度有限、越界静默截断——拿它传整份结构化长报告,等于用便签纸寄档案。审查工作本身没有白做,但交付链在最后一环断了,merge 决策拿不到输入。

## 修正

长报告落盘为文件、回传路径引用(报告本体走文件系统,final text 只回「结论 + 路径」),不全靠 final text。可复用判据:凡产物超过一段话,落盘是唯一可靠通道;回传的是指针,不是本体。
