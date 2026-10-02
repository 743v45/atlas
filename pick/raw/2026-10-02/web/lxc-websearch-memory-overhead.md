# WebSearch 汇总 — 系统容器内存开销（LXC vs VM vs Docker）

- 采集方式：WebSearch（查询 "LXC system container idle memory overhead MB compared virtual machine docker"）
- 访问日期：2026-10-02
- 性质：**第三方社区实测/博客数据**，非官方基准；引用时标注评测方与时间（均为访问 2026-10-02 时检索到的现存内容）

## 实测数据点

| 工作负载 | LXC 系统容器 | 完整 VM | 出处 |
|---|---|---|---|
| Alpine Linux（全新装） | 空闲 <4 MB | 空闲 ~60 MB | Reddit r/Proxmox（yy0kha） |
| Debian 13（base system） | 空闲 ~16 MB | 空闲 ~85 MB | proxmoxmigracje.pl |
| Nextcloud（同负载对比） | 空闲 ~145 MB | 空闲 ~520 MB（Ubuntu 24.04 KVM） | proxmoxpulse.com |

- Proxmox 社区口径：同等服务下 LXC 空闲内存约为 KVM VM 的 **1/3～1/4**（"LXC using roughly 3–4x less RAM at idle than an equivalent KVM VM"）。
- VM 空闲开销量级：完整 guest 内核 + init + 驱动，**50–500+ MB** 随发行版浮动。
- Docker 空闲容器：几 MB～几十 MB（同为共享内核，但面向单应用，无 init/完整用户态）。
- KVM CPU 开销：5–15%（Beawit Consulting 口径）。

## 原始链接

1. https://www.reddit.com/r/Proxmox/comments/yy0kha/confused_on_when_to_use_vm_vs_lxc — Alpine <4MB（LXC）vs ~60MB（VM）
2. https://proxmoxmigracje.pl/en/vm-vs-container-memory — Debian 13 16MB vs 85MB
3. https://proxmoxpulse.com/articles/lxc-vs-kvm-proxmox-resource-overhead — Nextcloud 145MB vs 520MB
4. https://datazone.de/en/aktuelles/docker-lxc-vm-comparison — Docker vs LXC vs VM 综合对比

## 使用注意

- 这些数字是 Proxmox 语境下的 LXC（liblxc）；Incus 系统容器同以 liblxc 为底座，机制相同（共享内核 + namespace/cgroup），数字量级可参考但非 Incus 实测。
- LXC 与 Docker 的空闲内存差距主要是「完整 init + 全套用户态服务」 vs 「单进程」；但两者都共享宿主内核，远低于 VM。
- 社区数据无标准化测试环境，报告中作为量级参考引用，不作精确断言。
