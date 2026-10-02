# Quadlet（systemd 集成）— WebSearch 聚合

- 来源 URL: WebSearch 聚合页（查询词 "podman quadlet systemd unit generator rootless best practice 2025"，经 z.ai web_search_prime）
- 访问日期: 2026-10-02

## 关键事实（聚合摘要）

- **Quadlet 机制**：声明式 unit 文件（`.container` / `.volume` / `.network` / `.pod` / `.kube` / `.image` / `.build`），由 systemd generator 在启动时翻译成原生 systemd unit——容器的开机自启、重启策略、日志、依赖编排全部交给 systemd 本身管理，无需常驻守护进程。
- **Rootless 最佳实践**（多源收敛）：
  - `loginctl enable-linger <user>`：rootless 用户服务在登出后继续运行，服务器场景必开。
  - rootless Quadlet 必须用 systemd **user units**（文件放 `~/.config/containers/systemd/`）；在系统级 unit 里用 `User=` 跑 rootless Podman **不受支持**（unix.stackexchange #714167；GitHub discussion #20573 社区在讨论改进）。
  - 增改 Quadlet 文件后 `systemctl --user daemon-reload`。
  - 自动更新：`podman-auto-update`（`AutoUpdate=registry` 标签 + systemd timer）与 Quadlet 集成。
- **已知坑**：
  - Reddit r/podman 有 systemd 启动约 30 秒后停掉 Quadlet 容器的案例（依赖/健康检查配置问题类）。
  - 监控工具（如 uptime-kuma）需要挂 podman socket 的讨论。

## 引用来源

1. Podman 官方文档 quadlet-basic-usage(7) — https://docs.podman.io/en/latest/markdown/podman-quadlet-basic-usage.7.html
2. ubitools Quadlet 指南 — https://www.ubitools.com/podman-quadlet-guide
3. dev.to rootless Quadlet 步骤 — https://dev.to/lyraalishaikh/podman-quadlet-a-better-way-to-run-rootless-containers-with-systemd-3i3l
4. Twilio Blog Getting Started with Podman Quadlets — https://www.twilio.com/en-us/blog/developers/tutorials/building-blocks/getting-started-with-podman-quadlets
5. unix.stackexchange User= 不受支持 — https://unix.stackexchange.com/questions/714167/best-practices-for-running-a-rootless-container-as-a-systemd-service-with-user
6. GitHub discussion #20573 — https://github.com/podman-container-tools/podman/discussions/20573
7. Reddit r/podman 监控与坑讨论 — https://www.reddit.com/r/podman/comments/1qirijt/rootless_podman_quadlets_best_practices_to
