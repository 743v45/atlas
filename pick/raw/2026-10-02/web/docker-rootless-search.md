# Docker rootless mode 现状（2025）

- 来源：WebSearch（Z.ai web_search_prime 聚合），查询词「Docker rootless mode 2025 production readiness limitations ecosystem support cgroup」
- 访问日期：2026-10-02

## 关键事实

1. **生产可用性**：2025 年共识是 rootless 已「production-viable」，Docker 27（2024）以来大幅降低 daemon 风险；有文章称其成为「许多发行版的默认」（Medium @nexusphere——此说法存疑，主流安装路径仍默认 rootful，报告中按「成熟但不默认」处理）
2. **性能代价**：sanj.dev《Container Runtime Showdown 2025》——rootless 模式 2024 年显著成熟，但 **P99 延迟开销 20-40%**，容器密度低于 rootful
3. **内核/系统要求**（kenmuse.com）：
   - 宿主内核必须允许**非特权 user namespace 创建**（`kernel.unprivileged_userns_clone` 等设置）
   - BuildKit rootless 有额外注意项
   - 资源限制依赖 **cgroup 委派**，通常需 systemd 配置（thenewstack.io）
4. **网络限制**：slirp4netns / pasta 用户态网络栈（性能与端口能力受限）
5. **生态**：OpenShift 等已广泛采用非特权容器；与 Kubernetes/OCI 标准兼容

## 来源链接

- https://dowithsudo.com/blog/docker-rootless-mode-hardening
- https://sanj.dev/post/container-runtime-showdown-2025
- https://www.kenmuse.com/blog/rootless-docker-and-its-hidden-security-trade-offs
- https://thenewstack.io/how-to-run-docker-in-rootless-mode
- https://www.reddit.com/r/docker/comments/1n7bmfa/docker_rootless

## 解读

- rootless 生态支持度：可用但非默认、有性能税——「daemon 需 root」这一轻量化轴上的风险点，缓解方案存在但有代价
