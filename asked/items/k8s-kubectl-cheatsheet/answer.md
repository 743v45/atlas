# k8s 入门速查:kubectl 命令、资源缩写与层级结构

> **TL;DR**:kubectl 按「查看 / 增删改 / 调试日志 / 发布滚动 / 标签 / 集群节点 / 配置上下文」七组场景记,覆盖 90% 日常;14 个资源缩写(po/svc/deploy/rs/sts/ds/ns/cm…)是读输出的钥匙;层级结构记住「Node → Pod →(ReplicaSet 管副本)→ Deployment 管发布、Service 管访问」两棵半树;服务和脚本的区别就看 `restartPolicy: Always` 还是 `Never/OnFailure`。

*(恢复自 2026-08-07 连环问答,原答骨架忠实;按自洽重组章节。)*

## 一、kubectl 核心语法与三场景命令组

```bash
kubectl [命令] [资源类型] [资源名] [参数]
# 例: kubectl get pod nginx -n default
```

**1. 查看(Get / Describe)**——最常用,只读不改动:

| 命令 | 作用 |
|------|------|
| `kubectl get pods/svc/deploy/node -A` | 列出资源(`-A` 全部命名空间) |
| `kubectl describe pod <name>` | 看某资源的详细事件、调度、错误 |
| `kubectl get all` | 当前命名空间下所有常用资源 |
| `kubectl api-resources` | 列出集群支持哪些资源类型 |
| `kubectl explain pod.spec.containers` | 查资源字段定义(自带文档) |

**2. 增删改(Apply / Delete / Create)**——声明式优先:

```bash
kubectl apply -f deploy.yaml       # 创建或更新(幂等,最常用)
kubectl delete pod <name>          # 删除单个资源
kubectl create deployment nginx --image=nginx   # 命令式快速创建
kubectl edit svc <name>            # 直接打开编辑器改线上配置
kubectl scale deploy nginx --replicas=5         # 扩缩容
kubectl autoscale deploy nginx --min=2 --max=10 --cpu-percent=80  # HPA
```

**3. 调试与日志(Logs / Exec / Port-Forward)**——排障核心:

```bash
kubectl logs <pod>                 # 看容器日志
kubectl logs -f <pod> -c <容器>    # 跟踪日志 + 指定容器
kubectl logs <pod> --previous      # 看上次崩溃前的日志(很关键)
kubectl exec -it <pod> -- sh       # 进入容器终端
kubectl port-forward svc/mysql 3306:3306   # 本地转发,直连服务调试
kubectl cp <pod>:/etc/config ./config      # 拷贝文件
kubectl top pod / node             # CPU/内存实时占用(需 metrics-server)
```

另有发布滚动(`rollout status/history/undo`、`rollout restart`)、标签选择器(`label`、`-l app=nginx`、`--show-labels`)、集群节点(`cordon/drain/uncordon` 维护三连)、配置上下文(`config get-contexts/use-context`,多集群配 `kubectx`/`kubens` 极省事)、输出格式(`-o wide/yaml/json/jsonpath`、`-w` 监听)。

## 二、14 个资源缩写

```
po=Pod   svc=Service   deploy=Deployment   rs=ReplicaSet
sts=StatefulSet   ds=DaemonSet   ns=Namespace   cm=ConfigMap
```

(配套的还有 `secret`、`ing`(Ingress)、`job`/`cj`(CronJob)、`no`(Node)、`pv`/`pvc` 存储卷等。)`kubectl get svc` 与 `kubectl get services` 完全等价,输出列里的缩写同理。

## 三、资源层级:谁管谁

- **Node** 是物理/虚拟机,承载一切。
- **Pod** 是最小可调度单元(1 个或多个共享网络/存储的容器)。
- **ReplicaSet** 管「副本数恒定」;**Deployment** 管 ReplicaSet、负责滚动发布与回滚——你日常只跟 Deployment 打交道,ReplicaSet 是它内部机制。
- **StatefulSet**(有状态:稳定网络标识+存储)、**DaemonSet**(每节点跑一个,日志/监控 agent)是另两种工作负载。
- **Service** 是稳定的访问入口(ClusterIP 集群内 / NodePort / LoadBalancer),后面靠 label selector 选中一组 Pod;**Ingress** 在 Service 之上做七层路由。
- 配置面:**ConfigMap**(明文配置)/ **Secret**(base64 编码的敏感配置)被 Deployment 引用(envFrom 注入环境变量或 volume 挂载成文件)。

## 四、「服务和脚本怎么区分」

k8s 里没有「服务 vs 脚本」两种资源,区别落在**同一 Pod 模板的 `restartPolicy`** 上:

- `Always`(Deployment 的默认)→ 容器退出就重启 = **常驻服务**。
- `Never` / `OnFailure`(Job/CronJob 用)→ 跑完即退 = **一次性脚本**;CronJob 再套一层 schedule 管定时。

## 五、定时脚本(CronJob)排查链

```bash
kubectl get cj                     # 看 SCHEDULE / ACTIVE / LAST SCHEDULE
kubectl get jobs                   # CronJob 每次触发产生一个 Job,COMPLETIONS 1/1 成功
kubectl get pods | grep <job名>    # Job 创建的 Pod
kubectl logs <pod> --previous      # 挂掉那次的上次日志
# 手动触发一次(不等时间到):
kubectl create job --from=cronjob/<名> <手动job名>
# 暂停/恢复:
kubectl patch cronjob <名> -p '{"spec":{"suspend":true}}'
```

排查思路:没按时跑/跑挂 → `get cj` 看 schedule 和 ACTIVE → `get jobs` 看执行历史 → `logs` 看 Pod 日志。最常见原因:镜像拉不下来、cron 表达式写错、并发策略导致任务被跳过。

## 六、两个高频坑

- **看镜像来源**:`kubectl get pod <name> -o jsonpath='{.spec.containers[0].image}'`(或 `-o wide` 的 IMAGE 列)——「从哪拉的镜像」写在 Pod spec 里,镜像仓库凭证是同 ns 的 Secret(imagePullSecrets)。
- **Service 本身没有日志**:日志在它背后的 Pod 里。「看服务日志」= 找到服务选中的 Pod,看 Pod 日志。

## 出处

- 源对话归档:../../../conversations/2026-08-07-k8s-kubectl-basics.md(2026-08-07)
- 原始会话:~/.claude/projects/-Users-taevas/86bf1d57-f3a8-43d7-b18c-6e111d5ceaf3.jsonl(主体;另两场卫星会话见归档)
- 关联 artifact:~/docs/k8s-resource-hierarchy.html(资源层级 mermaid 关系图);当日同步发布至自托管 Outline(后弃用)
- 关联条目:[k8s-config-storage](../k8s-config-storage/)(配置存哪)、[tencent-tke-access](../tencent-tke-access/)(云上集群接入)
