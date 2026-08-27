# 百 KB 即 IncompleteRead:自签 HTTPS 上 urllib 长响应截断

> **TL;DR**:错在「stdlib 能用 = 传输层稳」——urllib 在自签 HTTPS 长响应上断流,该换通道而不是继续修补。

- **状态**:fixed(已修正)
- **日期**:2026-08-05
- **出处**:Outline 发布 skill(urllib stdlib + 自签 https),search 大响应

## 经过

skill 自包含仅用 stdlib(`urllib.request` + `ssl._create_unverified_context()` 禁证书校验),对自托管 Caddy 自签 https 服务调 search 接口,返回大响应时 `resp.read()` 中途断流:`http.client.IncompleteRead: IncompleteRead(101623 bytes read, 15759 more expected)`。小响应(create-document 等)全部正常,同端点 curl 正常——问题只钉在 urllib + 自签 HTTPS + 长响应这个组合上。

## 根因

我以为是接口或网络偶发,其实是传输层选型假设没验证:「不依赖第三方库」这个洁癖被当成了传输可靠性的证据。stdlib 能发请求 ≠ 在所有 TLS/响应形态下读得全;而发现翻车后没有当场最小复现 + 复验,判断悬在印象上。

## 修正

skill 的 `_request` 底层换成 curl 子进程(`-sk` 跳过证书校验 + 双重重试)。三段链闭环:08-05 翻车定位 → 当天改 skill → 08-07 新会话对真实实例复验,704ms 成功。可复用判据:传输层问题先做「同端点换客户端」对照(curl 正常 = 库的问题);修完必须新起会话走真实链路复验,不复验不算修完。
