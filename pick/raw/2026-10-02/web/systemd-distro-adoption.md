# WebSearch 留档：发行版默认采用 systemd 时间线

- 来源：WebSearch（查询 `Ubuntu Debian RHEL default init system systemd since which version adoption`）
- 访问日期：2026-10-02
- 主来源：[Systemd - Wikipedia](https://en.wikipedia.org/wiki/Systemd)、[Init - Debian Wiki](https://wiki.debian.org/Init)、[The history of systemd, and why it won - SSD Nodes](https://www.ssdnodes.com/learn/history-of-systemd)

## 采用时间线

| 发行版 | 版本 | 时间 | 之前的 init |
|---|---|---|---|
| Fedora | 15 | 2011-05 | Upstart（首个主要采用者） |
| Arch Linux | — | 2012-10 | SysVinit |
| RHEL | 7 | 2014-06 | Upstart（RHEL 6） |
| SLES | 12 | 2014-10 | SysVinit |
| Debian | 8 "Jessie" | 2015-04 | SysVinit |
| Ubuntu | 15.04 "Vivid Vervet" | 2015-04 | Upstart |

- Debian wiki：默认 init 自 Debian 8 起为 systemd（升级路径不强制迁移，新装默认）
- RHEL 7 的切换连带下游 CentOS/Rocky/AlmaLinux
- Wikipedia 总括：**「Since 2015, nearly all Linux distributions have adopted systemd」**
- systemd 由 Lennart Poettering（Red Hat）2010 年发起
