# WebSearch 汇总 — Incus/LXD 分叉现状 与 Incus Web UI

- 采集方式：WebSearch 两次（"Incus LXD fork 2026 community LinuxContainers status Canonical" / "Incus web UI built-in browser interface version 6.0 included"）
- 访问日期：2026-10-02

## 一、分叉现状（搜索一）

- Incus 是 Canonical 2023 年把 LXD 收归内部治理后、LinuxContainers 社区拉出的 fork；命名取自砧状云（Cumulonimbus incus），由 LXD 原负责人 **Stéphane Graber** 领导。
- linuxcontainers.org 的 LXD 页现挂声明："The LXD project is no longer part of the Linux Containers project but can now be found directly on Canonical's websites" —— 分叉为永久且已定局。
- Rocky Linux 等发行版官方文档已采用 Incus；OneUptime 2026-03 的 Ubuntu 安装指南、Ubuntu 26.04 安装指南收录 Incus——2026 年社区已向 Incus 收拢。
- Canonical LXD 继续以自家治理并行维护（GitHub canonical/lxd 2026-10-02 实测未 archived、仍在 push）。
- 原始链接：
  - https://github.com/lxc/incus
  - https://www.canonical.com/lxd（Canonical LXD 官方页）
  - https://linuxcontainers.org/lxd/（迁移声明）

## 二、Web UI 现状（搜索二）

- 历史状态：Stéphane Graber 2023-11 博客——"Unlike LXD, Incus doesn't have an official web UI. Instead, it just serves whatever web UI you want."（Incus 守护进程可伺服任意 UI 静态文件）
- 2024 前后：社区方案是把 **incus-ui-canonical**（原 LXD UI 的开源延续）放到 /opt/incus/ui，由 Incus 在 8443 端口连同 API 一起伺服；需要创建客户端证书并装到浏览器（setup 指南：discuss.linuxcontainers.org/t/19522、blog.simos.info）。
- Stéphane Graber 有 "Let's package a web UI for Incus!" 视频——方向是打包成可选包（incus-ui-canonical）随 Zabbly 仓库分发。
- 6.0 发布时（2024-05）**未内置** UI；为可选安装。
- ⚠️ 2025-2026 是否已默认捆绑：本轮搜索未取到一手确认（待验证），后续以 Incus 文档 docs.incus 或 Zabbly 包列表复核。
- 原始链接：
  - https://discuss.linuxcontainers.org/t/how-to-install-and-setup-the-incus-web-ui/19522
  - https://blog.simos.info/how-to-install-and-setup-the-incus-web-ui
  - https://stgraber.org/2023/11/25/adding-a-web-ui-to-the-incus-demo-service
  - https://github.com/osamuaoki/incus-ui-canonical
  - https://linuxcontainers.org/incus/news/2024_12_19_22_12.html（6.0 LTS 发布期 news，支持至 2029-06）
