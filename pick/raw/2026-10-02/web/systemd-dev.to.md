# 留档：Process Manager Comparison 2026（dev.to/empellio）

- 来源：https://dev.to/empellio/process-manager-comparison-2026-pm2-systemd-supervisor-oxmgr-and-more-4e0p
- 访问日期：2026-10-02（WebFetch）
- 发表：2026-03-10，2026-03 更新；原作者 oxmgr.empellio.com（Empellio）
- **利益声明：作者为 Oxmgr 厂商，非中立评测；但 systemd 基础事实与 benchmark 口径完整，可引用（注明评测方与利益关系）**

## systemd 关键数据

- 语言 C，许可 LGPL-2.1，首发 2010，状态 active，几乎所有现代 Linux 发行版的 init system
- 定位「OS-native approach」；评语：unit 文件上手前提下，Linux 生产稳定性「unbeatable」
- **内存开销：daemon RSS 0 MB（无独立 daemon——就是 PID 1 的一部分，常驻）；每进程额外开销 ~0 MB；10 进程总计 ~0 MB**
- **Benchmark 环境：AWS EC2 t3.small（2 vCPU / 2 GB RAM）、Ubuntu 22.04、管理 10 个 Node.js HTTP server；每组 20 次取中位数**
  - 冷启动：中位 78 ms，P95 121 ms
  - 崩溃恢复：中位 182 ms，P95 234 ms
- 对比组（同环境）：
  - PM2：daemon ~83 MB RAM；冷启动 ~1,247 ms；崩溃恢复 ~412 ms
  - Supervisor：~31 MB Python 开销；恢复 ~530 ms；维护模式（maintenance mode）
- 功能：Restart=always / RestartSec=5、journald（journalctl -u myapp -f，自带轮转）、Environment=NODE_ENV=production、cgroups、namespaces、watchdog、socket activation、依赖排序、安全沙箱（PrivateTmp、NoNewPrivileges）、开机自启（原生）
- 缺失：cluster mode、零停机 reload、跨平台（**仅 Linux**）、config-as-code「Partial」、无 web dashboard
- 决策指引：Linux 上 OS 级服务集成选 systemd；512 MB VPS 场景（与 Oxmgr 配合）；或作为 Oxmgr 的启动器

# 留档：Docker vs a Raw VPS: When Containers Actually Pay Off（deploysmith.dev）

- 来源：https://deploysmith.dev/hosting/docker-vs-vps
- 访问日期：2026-10-02（WebFetch）
- 发表：2026-09-26（sources checked 2026-09-27）
- **诚实声明：文中无实测数字**——作者原话「We publish idle/reload and memory numbers for these two setups only once we've measured them on a clean, paid VPS」「treat any figures above as structure, not results」→ 只可引用其**质性结论**，不可引数字

## 质性结论

- Docker 内存限制算的是整个容器（base image + runtime + container layer），不是 app 进程本身
- 1–2 GB 小机上 app + Postgres + Nginx 三容器「可能悄悄把你推进 swap」
- 完整 `node:24` 镜像在应用代码之前就「数百 MB」；multi-stage + node:24-slim 可削减
- 示例 compose 限额：app 384 MB / 0.50 CPU，Postgres 18 256 MB
- **何时用裸 VPS + systemd/PM2**：一台服务器一个 app、无团队、轻数据库或文件存储、内存受限（1 GB 小机、磁盘受限硬件）→ 每进程 RAM 更低、调试更简单、活动部件更少
- **何时用 Docker**：多个独立版本的服务、需要整栈可回滚部署、要把环境交给别人
- 总立场：「Docker isn't a default, it's a tool for a specific job.」

# 留档：Systemd vs. Docker: Exploring a Surprising Alternative（dev.to/_russell）

- 来源：https://dev.to/_russell/systemd-vs-docker-exploring-a-surprising-alternative-4pmm
- 访问日期：2026-10-02（WebFetch）
- 发表：2024-12-09，2025-07-27 编辑

## 要点

- **纯质性对比，无 benchmark/内存数字**；Docker「因容器化有小额开销（通常可忽略）」，systemd「长驻进程性能通常更好，因为没有容器开销」
- systemd 优势：长驻进程性能、更深宿主 OS 集成、日志/资源分配/服务依赖的细粒度控制
- unit 文件范例（pocketbase.service）：`[Unit]` After=network.target；`[Service]` ExecStart=/usr/local/bin/pocketbase serve --http=0.0.0.0:8090、WorkingDirectory、Restart=always、User、Group；`[Install]` WantedBy=multi-user.target；随后 systemctl daemon-reload / start / enable
- 局限：systemd 仅 Linux；app 直跑宿主机 → 可能与其他系统服务有依赖冲突；**systemd 缺 Docker 的隔离**——控制力的代价是 Docker 提供「完整隔离的自包含环境」
- 结论：Docker 适合可移植、隔离部署；systemd 适合需要直接 OS 集成与更细服务控制的场景

# 留档：Caddy 官网首页

- 来源：https://caddyserver.com/
- 访问日期：2026-10-02（WebFetch）

## 要点

- 定位：「The Ultimate Server」「The most advanced HTTPS server in the world」；web server / reverse proxy（HTTP、HTTPS、WebSockets、gRPC、FastCGI、负载均衡、健康检查、动态上游）/ PHP 应用服务器（FrankenPHP）/ 内部 CA（Smallstep 库驱动的 PKI 套件）
- **自动 HTTPS 原话**：「By default, Caddy automatically obtains and renews TLS certificates for all your sites.」「Every site on HTTPS」——含 localhost 与内网 IP；「Watch in real-time as Caddy serves HTTPS in < 1 minute」
- 证书机制：默认 ACME 自动获取+续期；On-Demand TLS（TLS 握手时签发，SaaS 客户域名场景）；集群协调（共享存储的实例以 fleet 方式共享密钥与 OCSP staple）；自动续期被吊销的证书（引 2020 大规模吊销事件）；默认 staple/缓存 OCSP
- 规模宣称：管理超 5000 万张证书；首个全自动化公共证书管理的 server
- 合规宣称：PCI、HIPAA、NIST 默认合规
- 许可：页面只说「free open source project」未写具体许可证名；© 2026 ZeroSSL
