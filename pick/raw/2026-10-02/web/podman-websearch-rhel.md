# RHEL 默认引擎 / 发行版打包 — WebSearch 聚合

- 来源 URL: WebSearch 聚合页（查询词 "RHEL 10 podman default container engine replace docker fedora debian ubuntu package"，经 z.ai web_search_prime）
- 访问日期: 2026-10-02

## 关键事实（聚合摘要）

- **Red Hat 自 RHEL 8 起不再以 Docker 为默认容器工具，改用 Podman**（RHEL 10 延续）；Podman 自 RHEL 8 起即为系统组件。
- Fedora Docs 口径：Podman 是 Docker 的替代品，不需要管理员（root）权限，多数场景可 drop-in 替换。
- 官方安装文档（podman.io/docs/installation）覆盖：Fedora、CentOS、RHEL 系；**Ubuntu/Debian 官方仓库有包**；FreeBSD 实验支持（14.3+）。
- 迁移资料：Red Hat Developer 官方 Docker→Podman 迁移指南（developers.redhat.com，2020-11-19 起）。

## 引用来源

1. Fedora Docs — https://docs.fedoraproject.org/en-US/neurofedora/containers
2. Podman 官方安装文档 — https://podman.io/docs/installation
3. DeployHQ 博客（RHEL 8 起默认）— https://www.deployhq.com/blog/understanding-podman-docker-s-open-source-alternative
4. Red Hat Developer 迁移指南 — https://developers.redhat.com/blog/2020/11/19/transitioning-from-docker-to-podman
5. xtom 对比 — https://xtom.com/blog/docker-vs-podman-container-engine-comparison
