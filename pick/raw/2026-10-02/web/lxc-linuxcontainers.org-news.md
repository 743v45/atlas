# Incus 7.0 LTS 发布公告 — linuxcontainers.org/incus/news

- 来源 URL：https://linuxcontainers.org/incus/news/2026_05_05_16_29.html
- 访问日期：2026-10-02（WebFetch 摘录）

## 发布日期与支持窗口

- 发布日期：2026-05-05
- EOL："Incus 7.0 LTS will be supported until June 2031"
- 支持划分：前 2 年 bug + 安全修复 + 少量可用性改进的点版本；之后转仅安全维护（"After that initial two years, Incus 7.0 LTS will move to security only maintenance"）——共 5 年。
- 背景：第二个 LTS；Incus 6.0 LTS（2024-05 发布）当时已进入仅安全阶段，支持至 June 2029。

## 关键特性

- **OCI 镜像支持**：6.3 引入，可从 OCI 镜像创建应用容器："incus remote add docker https://docker.io --protocol=oci"；容器配置（资源限制、syscall 拦截等）同样适用，运行在与系统容器相同的隔离环境。
- **内置 S3**：MinIO 后端被内置 S3 监听器取代（MinIO 上游停止维护），桶在首次访问时自动迁移。
- **低层备份 API**：NBD API + 脏位图（dirty bitmap），虚拟机增量备份与恢复。
- 其他：`core.shutdown_action` 关机疏散、`restricted.storage-pools.access`、集群再平衡 placement scriptlet、`incus image copy --reuse`、新增 Linstor 与 TrueNAS 存储驱动、网络地址集、依赖卷。

## 定位描述（原文）

- "Incus is a modern system container, application container and virtual machine manager."
- Apache 2.0 许可、社区主导、隶属 Linux Containers 组织；支持集群、本地/远程存储、传统或全分布式网络、完整 REST API。

## 依赖最低版本（软件要求）

Go 1.25、Linux 6.12、QEMU 8.2、LXC 6.0.0、nftables 1.0.0、dnsmasq 2.90、openvswitch 2.15.0（OVS/OVN 时）、ovn 23.03.0、ZFS 2.1.0、LVM 2.03.11。

- 注意：LXC 6.0.0 依赖印证 Incus 与 liblxc（lxc/lxc 仓库）的底层关系。

## 破坏性变更

弃用 CGroupV1 与 xtables（iptables/ip6tables/ebtables）支持。

## 页面缺失项

- 该公告页无 Web UI 相关特性；无内存/RAM 要求说明。
