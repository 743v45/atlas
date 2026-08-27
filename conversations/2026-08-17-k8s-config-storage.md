---
date: 2026-08-17
topic: k8s 里配置到底存在哪
related:
  - ../asked/items/k8s-config-storage/
原始会话: ~/.claude/projects/-Users-taevas/94e8bf7d-1f7d-432d-8d29-d6e109c5c984.jsonl
---

# 2026-08-17 · k8s 里配置到底存在哪

起于一次容器内报错的排查(以下集群代号/命名空间/服务名/IP 均已脱敏泛化,方法保留):用户 kubectl exec 进 deploy 想跑 node 做 DNS 查询,报 executable file not found——镜像非 node 基础镜像;AI 改用镜像里有的 nslookup/getent,顺带发现查询用的域名后缀是把内部集群代号误当 DNS 域(该集群真实 DNS 域是 cluster.local,resolv.conf 的 search 列表可证),修正后短名/FQDN 均正常解析到 Service ClusterIP。

用户追问「看下 deploy 在用哪份配置」「配置怎么查询。cm 么」。AI 给出本条的核心知识点:**deploy 只引用不存储配置**——容器启动命令 /app/<svc> -c /app/<config>.yaml 的主配置来自 ConfigMap 挂载,数据库账密不在配置文件里、走 envFrom 的 Secret 注入;反查路径是 deploy → 找到引用的 cm/secret 名(envFrom + volumes.volumeMounts)→ 再查对应的 cm/secret。命令集:cm 用 -o yaml / -o jsonpath='{.data.<key>}'(明文),secret 的值是 base64 要解码;jsonpath 提 envFrom 和 volumes 一行拿到引用清单。当日实走通,配置来源全部定位(主 cm + 证书/JSON 若干挂载 + envFrom secret)。

讲义恢复为 asked/items/k8s-config-storage。
