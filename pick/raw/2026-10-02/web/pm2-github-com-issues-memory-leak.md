# pm2 God daemon 内存泄漏 issue 摘要（原始 json 见 ../gh/pm2-issue-6113.json）

- 来源 URL: https://github.com/Unitech/pm2/issues/6113 与 https://github.com/Unitech/pm2/issues/5145（经 `gh api repos/Unitech/pm2/issues/<n>`）
- 访问日期: 2026-10-02

## issue #6113 — "PM2 God Daemon Memory Leak (6.0.14)"

- 状态（2026-10-02 查）：**open**，created 2026-05-16，closed_at null，仅 1 条评论
- 环境：pm2 6.0.14、Node 20.20.2、Debian 12、AMD EPYC 16 核、websocket 高频游戏服（17 个 cluster 进程）
- 症状：22 天 uptime 后 PM2 daemon RSS ~5.7GB；应用进程本身健康；`~/.pm2/logs` 仅 3.5MB；watch 关闭、无 restart storm
- 临时处置：`pm2 save && pm2 kill && pm2 resurrect` 后恢复正常
- 提交者猜测方向：内部 IPC/event bus、stdout/stderr 流处理、cluster worker 通信、daemon 侧缓冲

## issue #5145 — "PM2 v5.1.0: God Daemon taking up huge amounts of memory"

- 状态（2026-10-02 查）：**open**，created 2021-08-06（至访问日近 5 年未关闭）
- 症状：daemon 230MB，占 512MB 机器约 50% RAM
