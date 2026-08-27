---
date: 2026-08-05
topic: urllib 在自签 HTTPS 长响应上 IncompleteRead
related:
  - ../mistakes/items/urllib-selfsigned-truncation/
原始会话: ~/.claude/projects/-Users-taevas/b0872007-d95e-468a-90d3-c91d2dcf6e05.jsonl（08-05 翻车）→ 666c3f48-2551-49df-ba92-d4e8faadc4ec.jsonl（08-05 修 skill）→ 9e00e9e0-f8eb-4d23-bc37-a33de6204012.jsonl（08-07 复验）
---

# 2026-08-05~07 · urllib 在自签 HTTPS 长响应上 IncompleteRead

Outline 发布 skill（自包含、仅 stdlib：`urllib.request` + `ssl._create_unverified_context()` 禁证书校验，对自托管 Caddy 自签 https 服务）在 search 接口返回大响应时读不全：

```
http.client.IncompleteRead: IncompleteRead(101623 bytes read, 15759 more expected)
```

**原始表述（翻车证据）**：`resp.read()` 在长响应（实测百 KB 级）中途断流，已读 101623 字节、还差 15759——不是接口报错，是传输层截断；create-document 等小响应全部正常，问题只出在大响应上，且同端点 curl 正常。

**关键转折**：判定为 urllib 在自签 HTTPS 长响应场景下的传输缺陷（不稳、难在 stdlib 内修），不再修补 urllib，改通道——skill 的 `_request` 底层换成 curl 子进程（`-sk` 跳过证书校验 + 双重重试）。

**最终结论（沉淀）**：三段链闭环：08-05 翻车会话定位 → 当天修 skill（curl 替换）→ 08-07 新会话对真实 Outline 实例复验，704ms 成功写入并返回文档 url。修正固化进 taevas-plugins 的 outline skill。沉淀为本馆错题 [urllib-selfsigned-truncation](../mistakes/items/urllib-selfsigned-truncation/)。
