---
date: 2026-08-03
topic: holdon 支付链会战:主动对账补偿机制
related:
  - ../apprentice/items/express/audit-first-workflow/
  - ../apprentice/items/express/agent-fleet-parallelism/
原始会话: ~/.claude/projects/-Users-taevas-code-holdcloud-holdon/22c19544-6f8c-4fb1-b5d2-bec1ad6cc753.jsonl
---

# 2026-08-03 · holdon 支付链会战:主动对账补偿机制

4 小时会话(15:08~19:08 北京时间,GLM-5.2,194 轮),从一句问句走到 13 subagent 编队落地,是「调查先行 + 编队作战」两条方法线的完整现场。

## 需求的原始表述

用户在 IDE 里选中 `recharge.go` 微信回调段(320-357 行),问:

> 有没有主动处理支付完成的方式

## 关键转折(用户原话按序)

1. **问句起步,不带方案**——先让 AI 摸底,而不是直接下需求。
2. Explore 只读摸底结论:`QueryOrderByOutTradeNo` 等查询接口**存在但从未被调用**;系统 100% 依赖支付平台 webhook 回调;回调丢失则订单永远停在 Init;无任何定时对账。brainstorm 出 A/B/C 三案后用户拍板:
   > A,B,C 都做。
3. 定时策略口述(把领域约束带进设计):
   > B 10 分钟触发一次,查一下半小时到 1 小时内的未支付的账单。还支持手动触发单一查账。半小时/1小时是根据 超时时间来的。现在设定的 15 分钟。变量固定下来,具有相关性
4. **架构拍板(反接口倾向)**:
   > 不要 POST /callback/recharge/wechat/reconcile 接口。用脚本。单笔手动的用 http
5. > 微信和支付宝都要做的
6. > 并发实现 —— 触发 13 个 subagent 按 G1-G4 分组编队实现。
7. **幂等追问**(编队交付后的人肉验收):
   > 会不会重复充值
8. 上线收尾:
   > 我需要就加哪些配置,设置 —— AI 回以三步上线清单;末尾 `make tools` 本地构建报错(依赖链接问题),用户中断会话收场。

## 最终结论

- 交付:`cmd/recharge-reconciler` 定时对账脚本(复用既有幂等保护 `HandleRechargeRecord`)+ 手动单笔查账 http 路径;微信/支付宝双通道。
- 编队集成缝隙(Makefile 漏项等)由主线会话兜底修复——「编队不是撒手」的实证。
- 会战方法链沉淀为 apprentice 两课:「调查先行:审计驱动的开发工作流」(问句→摸底→拍板→验收)与「并行 agent 编队作战」(并发实现→幂等追问)。
