# Incus 官网主页 — linuxcontainers.org/incus/

- 来源 URL：https://linuxcontainers.org/incus/
- 访问日期：2026-10-02（WebFetch 摘录）

## 项目定位（原文关键句）

- "next-generation system container, application container, and virtual machine manager" —— 下一代系统容器、应用容器与虚拟机管理器，提供类似公有云的使用体验（"Incus provides a cloud-like environment"）。
- 起源："a community driven alternative to Canonical's LXD"，由 Aleksa Sarai 创建，由"LXD 的原班创建者中的许多人"领导维护。

## 三种实例类型（页面明确列出）

1. 系统容器（system container）："simulates a virtual version of a full operating system"
2. 应用容器（application container，类似 Docker）
3. 虚拟机（virtual machine，QEMU）

## 核心 API 与功能列表

- 安全设计（非特权容器 unprivileged、认证）、可扩展（"from a laptop to clusters of thousands of compute nodes"）、基于事件、远程使用、项目隔离（projects）
- 基于镜像：每日构建多种 Linux 发行版镜像；profiles 配置机制
- 备份与迁移：备份恢复、快照、跨主机镜像传输、实例迁移
- 可配置性：多存储后端（dir/btrfs/lvm/zfs/ceph…）、网络管理（桥接、跨主机隧道）、资源限制（CPU/内存/网络 I/O）、设备直通（USB、GPU、NIC）
- 集成：Ansible、Terraform/OpenTofu、Kubernetes Cluster API（出自 7.0 LTS 公告页）

## 版本线（页面当日口径）

- 页面原文："The current LTS release is Incus 6.0 and is supported until June 2029."
- 功能版约每月发布一次，页面未列具体版本号。
- ⚠️ 与 news 页（2026-05-05 发布 Incus 7.0 LTS）存在滞后——主页访问当日仍写 6.0 为当前 LTS，两处数据均按各自访问日记录。

## Web UI

- 主页面**未提及 Web UI**。

## 发行渠道

- "Incus works on any recent Linux distribution"，官方不直接打包，依赖各发行版仓库或第三方仓库。
- 客户端（CLI）支持 Windows 与 macOS，可远程连 Linux 上的 Incus 服务器。
- 商业支持来自 Zabbly（Zabbly 同时赞助项目基础设施）。
- 提供在线试用（try-it-online）。
