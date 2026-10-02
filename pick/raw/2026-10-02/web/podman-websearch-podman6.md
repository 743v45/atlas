# Podman 6.0 发布信息 — WebSearch 聚合

- 来源 URL: WebSearch 聚合页（查询词 "Podman 6.0 release date new features 2025"，经 z.ai web_search_prime）
- 访问日期: 2026-10-02
- 原始命中: LWN.net https://lwn.net/Articles/1079600 、Fedora Wiki https://fedoraproject.org/wiki/Changes/Podman6 、heise online、Medium

## 关键事实（聚合摘要）

- **Podman 6.0.0 发布于 2026 年 6 月（约 6 月 24 日）**，不是 2025 年；GitHub 官方路线图原计划 Podman 6 于 Spring 2026 发布，如期兑现。2025 年的版本属 5.x 线（如 5.6）。
- 主要新特性（聚合多源）：
  1. **移除遗留组件**（本 release 最大变化）：移除 slirp4netns 支持、cgroups v1 支持、BoltDB 数据库后端
  2. 网络改进：容器多静态 IP、网络栈现代化、网络隔离改进
  3. Docker 兼容性扩展（Docker API 兼容面扩大）
  4. Podman Machine 与 Quadlet 有显著改进
  5. Podman Desktop 1.28/1.29 完整支持 Podman 6.0（含 VM 配置集成）
- 升级建议：因组件移除，社区建议把 6.0 升级当「迁移」对待，而非原地版本升级。

## 待复核

- 6.0.0 精确发布日期（约 2026-06-24）待 LWN 原文核实（另行 fetch 留档）。
