# 腾讯云 TKE 访问四场景 + kubectl 上手实录

> **TL;DR**:「访问腾讯云容器服务」按四场景对号入座:控制台 Web UI(CAM 权限)/ 本地 kubectl 连集群(拿 kubeconfig → 配网络接入 → 验证)/ 访问集群内应用(LoadBalancer、port-forward)/ TCR 镜像服务。最容易卡住的两步:① 网络接入——kubeconfig 里的 server 是 VPC 私网地址还是公网地址,决定要不要 VPN/云联网;② 鉴权——TKE 是 CAM 用户映射到 K8s RBAC,子账号没绑角色就是 forbidden。当日从零到连上集群、查 ns/日志/配置,全程走通。

*(恢复自 2026-08-03 问答,原答骨架忠实;真实集群 ID/命名空间/服务名已脱敏,方法保留。)*

## 一、四场景总览

**场景 1 · 控制台管理(Web UI)**:登录腾讯云控制台 →「容器服务 TKE」。需要账号具备对应 **CAM 权限**(如 `QcloudTKEFullAccess`)。

**场景 2 · 本地 kubectl 连集群 ⭐ 最常见**——见下节展开。

**场景 3 · 访问集群内部署的应用**:

- 对外暴露:`Service` 类型 `LoadBalancer`(腾讯云 CLB)或 `Ingress`。
- 本地调试:`kubectl port-forward svc/<name> 8080:80`。
- VPC 内访问:Service 的 ClusterIP / 内网域名。

**场景 4 · 容器镜像服务 TCR**:

```bash
docker login ccr.ccs.tencentyun.com -u <腾讯云账号ID> -p <密码>   # 个人版
# 企业版用各自实例域名,建议临时密钥
```

## 二、场景 2 展开:五步连上集群

1. **安装 kubectl**(版本与集群 K8s 版本差一个小版本以内)。macOS 推荐 `brew install kubectl`;无 brew 手动 curl `dl.k8s.io` 的 darwin/arm64 包;Linux/Windows 同理(curl / winget)。
2. **获取集群凭证(kubeconfig)**,两选一:
   - 控制台一键复制:集群详情 →「基本信息」→「集群APIServer信息」→「查看集群凭证」→ 复制 YAML。**只要连集群,这条最省事。**
   - 腾讯云 CLI:`tccli tke DescribeClusterKubeconfig --ClusterId cls-xxxx`——**ClusterId 在控制台「集群」列表页的「集群 ID」列**(有复制按钮),集群详情「基本信息」页顶部也有。
3. **配置**:`~/.kube/config`,或 `export KUBECONFIG=/path/to/kubeconfig`。
4. **网络接入(卡人最多的一步)**:
   - **公网访问**:集群「基本信息」→ 开启 **APIServer 外网访问**,会分配公网域名/IP,kubeconfig 里 `server` 指向它。
   - **内网访问**:`server` 是 VPC 私网地址,本地需通过 **VPN / 云联网 CCN / 专线**接入该 VPC。
5. **验证**:`kubectl get nodes`。

**tccli 的坑**:configure 配好后 `DescribeClusterKubeconfig` 仍不行,通常是**区域(Region)与集群地域不一致**——找不到集群。configure 里填的或 `--Region` 传的都要对上。

**鉴权链路**:TKE 的集群鉴权是 **CAM 用户 → K8s RBAC** 的映射。子账号需在「集群 → 访问管理」里绑定 RBAC 角色,否则 kubectl 报 `forbidden`。

## 三、连上之后的三个高频动作(当日实走)

- **看命名空间**:`kubectl get ns`(或 `get namespaces`)。
- **看服务日志**:**Service 本身没有日志**,日志在它背后的 Pod/容器里——先 `kubectl get pods -n <ns>`(或 `get svc` 找到后端),再 `kubectl logs <pod> -n <ns>`。
- **看 Pod 配置**:资源侧(`get pod -o yaml`、describe)看声明;实际生效侧 `exec` 进去看挂载文件和 `env`。配置实体在 cm/secret、deploy 只引用——详见 [k8s-config-storage](../k8s-config-storage/)。
- 顺手的:`kubectl get pods -A` 看全局健康度,`kubectl config current-context` 确认连的是哪个集群。

## 出处

- 源对话归档:../../../conversations/2026-08-03-tencent-tke-access.md(2026-08-03)
- 原始会话:~/.claude/projects/-Users-taevas/bcbd5d97-4d63-4446-9e7b-c5883a11d7e1.jsonl
- 关联条目:[k8s-kubectl-cheatsheet](../k8s-kubectl-cheatsheet/)(kubectl 全景)、[k8s-config-storage](../k8s-config-storage/)
