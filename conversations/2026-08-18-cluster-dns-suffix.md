---
date: 2026-08-18
topic: 集群编号误当 k8s DNS 域后缀
related:
  - ../mistakes/items/cluster-suffix-dns/
原始会话: ~/.claude/projects/-Users-taevas/94e8bf7d-1f7d-432d-8d29-d6e109c5c984.jsonl（08-17）+ ef20cf99-55a4-4926-bb29-7b804189affe.jsonl（08-18）
---

# 2026-08-17~18 · 集群编号误当 k8s DNS 域后缀

集群内 gRPC 调用持续报错：

```
Error: 14 UNAVAILABLE: Name resolution failed for target
       dns:<order>.<ns>.svc.cluster.fudN:8443
```

（ns 为内部命名空间名，此处脱敏；`fudN` 为内部集群编号。）

**原始表述（翻车证据）**：多份 ConfigMap 配置里都是 `<svc>.<ns>.svc.cluster.fudN:8443` 形式的地址——「所有配置都是……都是 fudN 呀」。据此坚信错误结论：「为什么要改成 cluster.local。明明应该是 fudN」。

**关键转折**：双变体对照实验打破僵局——Pod 内 `require('dns').lookup()` 分别解析 `...svc.cluster.fudN`（失败）与短形式 `<svc>.<ns>`（成功）；再看容器 `/etc/resolv.conf` 的 search 列表，真实的集群 DNS 域是 `cluster.local`。`fudN` 是内部集群编号，不是 DNS 域——所有配置都写它，只说明所有配置同源同错，不是它正确的证据。

**最终结论（沉淀）**：统一改用短形式 svc 名（`dns:<svc>.<ns>:8443`），同 ns 内更短。判据沉淀：DNS 域的事实来源是 resolv.conf search 列表与解析实验，不是配置文件里的多数。沉淀为本馆错题 [cluster-suffix-dns](../mistakes/items/cluster-suffix-dns/)。
