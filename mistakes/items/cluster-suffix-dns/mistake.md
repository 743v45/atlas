# 「明明应该是 fudN」:集群编号误当 k8s DNS 域后缀

> **TL;DR**:错在把「所有配置都这么写」当成了「这么写是对的」——配置多数只能证明同源,不能证明正确;DNS 域的事实来源是 resolv.conf。

- **状态**:fixed(已修正)
- **日期**:2026-08-17
- **出处**:本机两场会话(08-17 报错排查 / 08-18 对峙定案),公司集群 gRPC 调用

## 经过

集群内 gRPC 持续报 `Error: 14 UNAVAILABLE: Name resolution failed for target dns:<svc>.<ns>.svc.cluster.fudN:8443`。多份 ConfigMap 里地址全是 `...svc.cluster.fudN` 形式——「所有配置都是……都是 fudN 呀」。面对「改成 cluster.local」的提议,当时坚持错误结论:「为什么要改成 cluster.local。明明应该是 fudN」。Pod 内 `dns.lookup` 双变体对照:带 `cluster.fudN` 后缀解析失败,短形式 `<svc>.<ns>` 成功;`/etc/resolv.conf` 的 search 列表里真实集群 DNS 域就是 `cluster.local`。

## 根因

我以为是 DNS 偶发故障,其实是证据层级错位:拿「配置文件里的多数」当事实来源,而配置是待验证的断言,不是证据——所有配置都写 `fudN` 只说明它们同源同错。`fudN` 是内部集群编号,被误当成 DNS 域后缀;坚信自己见过这个后缀,是在用印象对抗可实测的解析结果。

## 修正

统一改用短形式 svc 名(同 ns 内 `dns:<svc>:8443`,跨 ns `dns:<svc>.<ns>:8443`)。可复用判据:DNS 域的事实来源 = 容器 resolv.conf 的 search 列表 + 双变体解析对照实验;配置多数性永远不进证据链。
