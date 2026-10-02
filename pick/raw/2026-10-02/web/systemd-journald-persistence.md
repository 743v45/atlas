# WebSearch 留档：journald 持久化默认行为

- 来源：WebSearch（查询 `journald Storage=auto persistent /var/log/journal default volatile man page`）
- 访问日期：2026-10-02
- 关键来源：[journald.conf(5) freedesktop 官方 man](https://www.freedesktop.org/software/systemd/man/journald.conf.html)、[systemd-journald(8) Arch man](https://man.archlinux.org/man/systemd-journald.8)、[Unix & Linux SE: Storage=persistent](https://unix.stackexchange.com/questions/513212/)、[Red Hat: enable persistent logging](https://access.redhat.com/solutions/696893)

## 事实

- 上游默认 `Storage=auto`：**`/var/log/journal/` 在启动时存在 → 持久存储；不存在 → 易失（`/run/log/journal`，重启丢失）**。Arch man 原话：「By default, log data is stored persistently if /var/log/journal/ exists during boot, with an implicit fallback to volatile storage otherwise.」
- `auto` **不会自行创建** `/var/log/journal`——目录的存在即开关（手动 `mkdir -p /var/log/journal` 或由发行版 tmpfiles 规则创建）
- journald 启动时先写易失存储，`journalctl --flush`（或 SIGUSR1）后切换到持久存储
- Red Hat：默认 journal 只在 `/run/log/journal` 小环形缓冲（非持久），除非启用持久化
- **发行版可覆盖上游默认**：Raspberry Pi OS 2025-05-13 镜像把默认从 `Storage=auto` 改成 `Storage=volatile`（github.com/raspberrypi/bookworm-feedback/issues/415）→ 部署时应显式确认目标机的 journal 持久性
