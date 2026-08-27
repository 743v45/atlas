---
date: 2026-08-03
topic: 腾讯云 TKE 访问与 kubectl 上手
related:
  - ../asked/items/tencent-tke-access/
原始会话: ~/.claude/projects/-Users-taevas/bcbd5d97-4d63-4446-9e7b-c5883a11d7e1.jsonl
---

# 2026-08-03 · 腾讯云 TKE 访问与 kubectl 上手

用户从零问起:「怎么访问腾讯云容器服务」「怎么安装 kubectl」「tccli tke DescribeClusterKubeconfig --ClusterId 在哪个页面」「我想查看服务的日志怎么搞」「查看里面有多少个命名空间」「怎么查看 pod 的配置情况」「挂载的配置怎么查(我自己来)」。

AI 按四场景作答:控制台 Web UI(需 CAM 权限如 QcloudTKEFullAccess)/ 本地 kubectl 连集群(拿 kubeconfig → 配网络接入 → 验证)/ 访问集群内应用(LoadBalancer/Ingress、port-forward、ClusterIP)/ TCR 镜像服务登录。kubectl 安装实测本机已有(且指出 /usr/local/bin 非 brew 装的)。卡点实录:用户 tccli configure 配好后 DescribeClusterKubeconfig 仍不行,AI 指出 ClusterId 在控制台集群列表页「集群 ID」列可复制,且只要 kubeconfig 的话控制台「查看集群凭证」一键复制更省事;用 tccli 则区域必须与集群地域一致。鉴权链路:TKE 是 CAM 用户 → K8s RBAC 映射,子账号须在集群「访问管理」绑定 RBAC 角色否则 forbidden。当日实走通:连上集群、get nodes/pods 验证、namespace 列表、看服务日志(Service 本身无日志,要落到背后 Pod)、pod 配置反查(cm/secret 命名清单 + 资源侧声明 vs 进 Pod 看实际生效两路线对照)。(会话中出现的真实集群 ID、命名空间与服务名已脱敏,方法保留。)

讲义恢复为 asked/items/tencent-tke-access。
