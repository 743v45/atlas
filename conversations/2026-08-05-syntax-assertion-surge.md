---
date: 2026-08-05
topic: AI 凭印象断言「语法对」被 Surge 报错打脸
related:
  - ../mistakes/items/syntax-assertion-surge/
原始会话: ~/.claude/projects/-Users-taevas/c03ea2ba-0390-4900-bc02-7698f0048c8b.jsonl
---

# 2026-08-05 · AI 凭印象断言「语法对」被 Surge 报错打脸

**原始表述（翻车证据）**：用户配置 Surge ssh 代理（内网 IP 已脱敏）：

```
我用的 surge，
[Proxy]
JumpServer = ssh, 10.x.x.x, 22, username=root, private-key-path=~/.ssh/id_rsa
但是说载入失败 Invalid line #20: JumpServer = ssh, 10.x.x.x, 22, …
```

AI 此前对这行配置断言「语法对」。

**关键转折**：用户贴出 Surge 的 `Invalid line #20` 报错，AI 认错原话：「报错说明 Surge 不认这行的语法——**我上一条说"语法对"是错的，这次我查官方文档确认准确写法，不猜了。**」此后搜索配额耗尽、文档站被网络策略挡住，仍换读取通道把官方文档读到了才给出写法。

**最终结论（沉淀）**：对「语法/接口签名/配置格式」类可查证事实，文档确认前不断言——验证先于信任；凭印象的「对」是负资产，错得越自信，用户排障越绕路。沉淀为本馆错题 [syntax-assertion-surge](../mistakes/items/syntax-assertion-surge/)。
