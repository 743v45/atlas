# pm2 内存占用（God daemon）WebSearch 检索留档

- 来源: WebSearch（检索词 `pm2 daemon memory usage overhead MB "pm2 God daemon" memory footprint`）
- 访问日期: 2026-10-02

## 各来源数据点

| 来源 | 数据点 | 语境 |
|---|---|---|
| Stack Overflow "Should PM2 God daemon always be running" (https://stackoverflow.com/questions/34520775/should-pm2-god-daemon-always-be-running) | **~27MB** 常驻 | 所有项目停掉后 daemon 仍常驻约 27MB RAM |
| Reddit r/node (https://www.reddit.com/r/node/comments/1ocoqxd/pm2_daemon_keeps_dying_on_hostinger_premium) | **~95MB** | Hostinger VPS 上 daemon 内存用量（该帖场景 daemon 频繁挂） |
| GitHub issue #5145 (https://github.com/Unitech/pm2/issues/5145) | **230MB**（512MB 机器的 ~50%） | v5.1.0，2021-08 创建，异常偏高 |
| GitHub issue #6113 (https://github.com/Unitech/pm2/issues/6113) | 22 天涨至 **~5.7GB** RSS | v6.0.14，websocket 高频 + 17 进程场景 |
| Superuser (https://superuser.com/questions/1465632/) | 高于预期 + heap limit 崩溃 | 旧版本案例 |

## 检索结果综合

「PM2 God Daemon 的基线 footprint 一般在 **27–100MB RSS**，但多个长期运行部署报告了显著内存泄漏（数百 MB 到数 GB），尤其 5.x 与 6.x 版本。」（WebSearch 结果原文转述）

## pm2 FAQ（检索结果引述）

「PM2 checks memory usage every 30 seconds and reloads processes exceeding a set threshold」——`max_memory_restart` 只管**应用进程**超限重启，不管 daemon 自身。
