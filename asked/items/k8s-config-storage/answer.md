# k8s 里配置到底存在哪:deploy→cm/secret 反查

> **TL;DR**:Deployment **只引用不存储**配置——配置实体在 ConfigMap(明文)和 Secret(base64)里,deploy 通过两条通道接上:`envFrom` 注入环境变量、`volumes/volumeMounts` 挂载成文件。所以「这个服务在用哪份配置」的查法是固定三步:**看 deploy 的容器启动命令和 envFrom/volumes → 拿到引用的 cm/secret 名字 → 再查对应的 cm/secret 内容**。当日在一套生产部署上实走通。

*(恢复自 2026-08-17 生产排查问答,原答骨架忠实;集群代号/命名空间/服务名/IP 已脱敏泛化,方法与命令保留。)*

## 一、为什么会有这个问题

排查的起点是一次容器内报错:`kubectl exec` 进 `deploy/<svc>` 想跑 `node` 做 DNS 查询,报 `exec: "node": executable file not found in $PATH`——这个镜像不是 node 基础镜像,是编译型二进制直接打进去的,容器里可用的工具是 `nslookup` / `getent` / `nc` / `wget`。

顺带发现第二个问题:查询用的域名后缀是把**内部集群代号误当 DNS 域**(形如把集群编号拼进 `svc.cluster.<代号>`)。集群真实 DNS 域是不是 `cluster.local` 看 Pod 的 resolv.conf 就知道:

```
search <ns>.svc.cluster.local svc.cluster.local cluster.local
```

修正为 `<svc>.<ns>.svc.cluster.local`(或短名走 search 补全)后,解析正常到 Service 的 ClusterIP——「不存在的那条」整个集群都不会解析,`fudN` 之类的后缀只是被误当成域名用的代号。

## 二、核心知识点:deploy 只引用不存储

一个典型服务的配置全景(当日实测的一套):

- **容器启动命令**:`/app/<svc> -c /app/<config>.yaml`——主配置文件是挂载进去的。
- **主配置来自 ConfigMap**:该 cm 只有一个 key(如 `config.yaml`),挂载到容器的 `/app/<config>.yaml`。
- **账密不在配置文件里**:配置块里写了数据库地址/库名但**没有 username/password**——它们走 `envFrom` 的 **Secret** 注入成环境变量,进程启动时自己读。
- **证书/杂项文件**:若干 cm(证书.crt、seller.json 之类)以 volume 挂到指定路径。

## 三、反查命令集(从 deploy 到配置内容)

**第 1 步:看 deploy 引用了什么**

```bash
# 看环境变量来自哪个 cm/secret、挂载了哪些卷
kubectl get deploy -n <ns> <svc> -o yaml | less
# 或用 jq 提取关键部分
kubectl get -n <ns> deploy/<svc> -o json | \
  jq '.spec.template.spec.containers[0].envFrom, .spec.template.spec.volumes'
```

**第 2 步:查 ConfigMap(明文,不需要解码)**

```bash
kubectl get cm -n <ns>                        # 列出(DATA 列 = key 个数)
kubectl describe cm <name> -n <ns>            # Data 段直接显示每个 key 的值
kubectl get cm <name> -n <ns> -o yaml         # 完整定义 + data 明细
kubectl get cm <name> -n <ns> -o jsonpath='{.data.<key>}'   # 提取某个 key
```

**第 3 步:查 Secret(base64,要解码)**

```bash
kubectl get secrets -n <ns>
kubectl get secret <name> -n <ns> -o yaml     # 值是 base64
kubectl get secret <name> -n <ns> -o jsonpath='{.data.<KEY>}' | base64 -d
```

**只看有哪些 key 不看值(脱敏视角)**:

```bash
kubectl get cm <name> -o go-template='{{range $k,$v := .data}}{{$k}}{{"\n"}}{{end}}'
kubectl get secret <name> -o go-template='{{range $k,$v := .data}}{{$k}}{{"\n"}}{{end}}'
```

## 四、两条配套知识

- **声明侧 vs 实际生效侧**:查 cm/secret 看到的是声明的期望值;要看 Pod 里**实际生效**的值,`kubectl exec` 进去 `cat` 挂载文件 / `env` 看注入的环境变量。排障「为什么实际值不对」走后者,改配置/对比版本走前者。
- **改了 cm 之后谁会自动更新**:**只有以 volume 方式挂载的**才会自动更新(TTL 约 1 分钟);**以 envFrom 注入环境变量的不会变**,要重启 Pod 才生效。
- **Secret 的 base64 不是加密**:谁能 `kubectl get secret` 谁就能解码——RBAC 控制比编码重要。

## 出处

- 源对话归档:../../../conversations/2026-08-17-k8s-config-storage.md(2026-08-17)
- 原始会话:~/.claude/projects/-Users-taevas/94e8bf7d-1f7d-432d-8d29-d6e109c5c984.jsonl
- 关联条目:[k8s-kubectl-cheatsheet](../k8s-kubectl-cheatsheet/)(命令全景)、[tencent-tke-access](../tencent-tke-access/)
