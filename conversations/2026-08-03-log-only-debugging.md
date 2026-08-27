---
date: 2026-08-03
topic: 零指令纯日志投喂排障(holdon 支付回调 500)
related:
  - ../apprentice/items/express/log-only-debugging/
原始会话: ~/.claude/projects/-Users-taevas-code-holdcloud-holdon/fbcada82-29f1-4d1a-afa8-08e1b233036d.jsonl
---

# 2026-08-03 · 零指令纯日志投喂排障(holdon 支付回调 500)

会话 5 分钟(11:49~11:54 北京时间,GLM-5.2),用户**一个字的指令都没有**——首条消息就是一段生产日志,AI 自行完成排障。

## 需求的原始表述

没有表述。消息全文就是日志本身(脱敏节选,结构保真):

```
time="2026-08-03 11:41:06" level=info msg="POST /api/v1/callback/recharge/alipay 500 128.995848ms"
internal: ReasonInternalError POST /api/v1/callback/recharge/alipay HTTP/1.1
Host: <内部控制台域名>
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Error: alipay.TradeQuery <订单号>: recharge failed
holdon/backend/pkg/errors.NewInternalError
    /builds/platform/holdon/backend/pkg/errors/errors.go:135
holdon/backend/internal/api/utils.ResponseAPIError
    /builds/platform/holdon/backend/internal/api/utils/io.go:66
holdon/backend/internal/api/controllers/account.(*AccountAPIController).HandleAlipayRechargeCallback
    /builds/platform/holdon/backend/internal/api/controllers/account/recharge.go:170
…
(另含数条 /RPC/GetUserMoney 等正常请求日志)
```

## 关键转折

- 无转折——全程用户未介入。AI 走 systematic-debugging 证据收集:先从错误栈定位到支付宝充值回调 500,再对照上下文里的正常请求日志排除「整体服务故障」,收窄到单接口。
- 三层根因:① 诊断字段被丢弃(`TradeQuery` 的错误细节没有落日志);② `IsSuccess` 语义误用(把「查询成功」当「支付成功」);③ 回调 500 后支付平台重试,但重试请求不入账——钱付了、账没记。
- 根因落 `recharge.go:171-173`。

## 最终结论

- 收尾 AI 主动停手:「生产资金代码需你拍板」——定位到根因但不擅自动生产资金链路,把修复决策交还给人。
- 沉淀为 apprentice 课「零指令纯日志投喂排障」:信息完备时,日志比人转述更保真,直接投喂优于描述。
- 该问题次日在另一会话(22c19544 支付链会战)发展为完整的对账补偿方案,见 [2026-08-03-holdon-recharge-reconciler.md](2026-08-03-holdon-recharge-reconciler.md)。
