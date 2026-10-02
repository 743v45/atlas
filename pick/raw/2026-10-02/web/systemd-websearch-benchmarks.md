# WebSearch 留档：systemd PID1 内存开销 + systemd vs Docker 对比

- 来源：WebSearch（z.ai web_search_prime），查询 2 条
- 访问日期：2026-10-02
- 查询 1：`systemd PID1 memory usage overhead MB idle benchmark`
- 查询 2：`systemd vs docker memory usage comparison benchmark small VPS node.js`

## 查询 1 关键结果（PID1 内存）

1. **[systemd pid 1 memory leak when systemctl start many services](https://github.com/systemd/systemd/issues/15220)** — PID1 RSS 每个 service 增长约 150KB，unit 停止后不回落（历史泄漏 issue，已修复类）。
2. **[Is systemd-nspawn a better alternative to Docker?](https://botmonster.com/self-hosting/systemd-nspawn-lightweight-containers-without-docker)** — 引述 dockerd 空闲占 **50–200MB RAM**，对比 systemd PID1 开销更小。
3. **[Debian in 2026: Transitioning from systemd to OpenRC](https://sesamedisk.com/debian-openrc-migration-2026)** — 指出 init system 的独立可复现 benchmark **稀缺**，多数内存开销论断是轶事性的。
4. **[Why does systemctl show high memory usage when top/htop show less?](https://superuser.com/questions/1431117/why-does-systemctl-show-high-memory-usage-when-top-and-htop-show-much-less)** — `systemctl status` 报的是整个 cgroup 的内存，比单进程 RSS 高，口径差异。
5. **[Why is reported memory usage of a systemd service different](https://askubuntu.com/questions/1510119/)** — RSS vs cgroup 记账口径差异。
6. **[systemd Using 4GB RAM After 18 Days](https://serverfault.com/questions/755818/)** — 老版本泄漏报告（~200MB/天）。
7. **[Why is systemd-journal taking up 110 MB?](https://bbs.archlinux.org/viewtopic.php?id=190200)** — journald 内存占用与 maxsize 限制。

**小结**：没有权威的 PID1 空闲 RSS 基准；轶事数据在**几十 MB**量级，显著低于 dockerd 的 50–200MB。报告中写「系统开销 MB 级（数十 MB 量级）」需标注出处性质。

## 查询 2 关键结果（systemd vs Docker / Node 部署）

1. **[Process Manager Comparison 2026: PM2, Systemd, Supervisor, Oxmgr and More](https://dev.to/empellio/process-manager-comparison-2026-pm2-systemd-supervisor-oxmgr-and-more-4e0p)** — 2026 年的 Linux/Node 进程管理器横评，含 systemd。
2. **[Docker vs a Raw VPS: When Containers Actually Pay Off](https://deploysmith.dev/hosting/docker-vs-vps)** — 小 VPS 上容器额外吃内存，裸进程（systemd）每进程 RAM 更低；含 benchmark。
3. **[Systemd vs. Docker: Exploring a Surprising Alternative](https://dev.to/_russell/systemd-vs-docker-exploring-a-surprising-alternative-4pmm)** — 长驻进程无容器开销、原生跑在宿主机，性能更好。
4. **[Why I Stopped Using Docker Compose and Went Back to Systemd](https://blog.stackademic.com/why-i-stopped-using-docker-compose-and-went-back-to-systemd-yes-really-82381cbf5fb6)** — systemd 内置服务存活/内存/CPU/实时日志/重启计数，不需要额外工具。
5. **[How Efficient Are Containers vs Virtual Machines?](https://oneuptime.com/blog/post/2026-01-16-containers-vs-vms-density-efficiency-comparison/view)** — 容器 vs VM 密度对比（OneUptime 2026-01-16）。
6. **[HN: Is there any reason not to use Docker instead of systemd?](https://news.ycombinator.com/item?id=36747851)** — systemd 原生处理 crash-restart 与依赖排序。
7. **[Reddit r/node: Which one do you use to host nodejs?](https://www.reddit.com/r/node/comments/1u2xiln/)** — 共识：频繁部署/CI-CD 用 Docker；小规模 systemd 更简单。

**小结**：小 VPS 场景 systemd 内存开销低于容器运行时是多个来源的共同结论；需 WebFetch 原文拿具体数字。
