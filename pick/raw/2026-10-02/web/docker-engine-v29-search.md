# Docker Engine v29 发布要点（2025-11）

- 来源：WebSearch（Z.ai web_search_prime 聚合），查询词「Docker Engine 29 release highlights changes containerd image store 2026」
- 访问日期：2026-10-02

## 关键事实

1. **Docker Engine v29（2025-11 发布）把 containerd image store 设为新装实例的默认**镜像/内容存储（Docker Blog + docs.docker.com/engine/storage/containerd）；从旧版升级则保留 classic image store
2. 新 snapshotter 下镜像拉取据报 **快约 37%**（daily.dev 二手转述，标注为非官方实测）
3. 最低 Engine API 升到 **1.44**（progosling.com 转述）
4. `/var/lib/docker` 不再「hermetic」——镜像与 containerd 存储共享（Hacker News 讨论：https://news.ycombinator.com/item?id=47986331）
5. 社区报告：切换到 containerd store 时压缩基础镜像层出现**重复存储**（r/selfhosted）；29.6.0 的 `docker save` 压缩输出变大（Docker Forums）
6. 官方 release notes：https://docs.docker.com/engine/release-notes/29

## 解读

- v29 是「foundation release」：镜像存储层向 containerd 架构收敛（为与 k8s 生态对齐），方向是更标准化而非更重
- 对个人小服务影响：新装默认即 containerd store，磁盘占用偶有迁移期重复层问题（升级注意项）
