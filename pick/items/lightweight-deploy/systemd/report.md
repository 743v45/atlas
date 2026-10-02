# systemd（裸进程 + unit 托管）

> **TL;DR**：一台 Linux VPS 上跑几个到十几个小服务的轻量默认解：发行版自带零安装、无 daemon 中间层（应用总内存≈应用自身，对照组 PM2 daemon 约 83MB）、Restart=always 自愈与 journalctl 日志开箱即得；代价是仅 Linux、无隔离无镜像、部署无声明式回滚——适用域为进程级部署够用的个人/小团队自有 VPS。

- **结论**：adopt（适用域：自有/单台 Linux VPS、几个到十几个小服务、进程级部署够用、不要求不可变环境的个人/小团队）
- **核实日期**：2026-10-02（gh 一手数据 + 官网/多来源当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 定位 | Linux 系统与服务管理器（init system），以 PID 1 运行并拉起系统其余部分；组件含 journald 日志、resolved/networkd、cgroup 进程追踪、事务性依赖服务控制 | [1] |
| 版本线 | 最新稳定 v262（2026-09-22 发布）；v258（2025-09-17）起主版本节奏约 3 个月一版（此前约半年） | [2] |
| 许可证 | 仓库根 LICENSE.LGPL2.1（主体 LGPL-2.1）+ LICENSE.GPL2（部分组件 GPL-2.0）；GitHub API 检测值 GPL-2.0 为混合所致 | [2] |
| 维护活跃度 | ⭐16,768、push 2026-10-02、open issues 3,528（gh 2026-10-02）；v258/v259/v260/v261 四条 stable 线于 2026-09-10/11 同窗发补丁——多版本并行维护 | [2] |
| 发行版自带 | Fedora 15（2011-05）首采、RHEL 7（2014-06）、Debian 8（2015-04）、Ubuntu 15.04（2015-04）起默认；「自 2015 年起几乎所有主流发行版采用」 | [8] |

## 为什么选（轻量化轴上的论断）

1. **零安装、零部署栈资源**：systemd 是发行版底座本身（init system 自带），用它做部署不新增任何安装包、不引入常驻 daemon [8][1]。跑 Node 服务时总内存 ≈ 应用自身——Empellio 横评（2026-03）记 systemd「daemon RSS 0 MB（无独立 daemon，就是 PID 1 的一部分）、每进程额外开销 ~0 MB」；对照组 PM2 daemon ~83 MB、Supervisor ~31 MB Python 开销 [3]（该横评为 Oxmgr 厂商所写，非中立，但其 systemd 基础事实与 benchmark 口径完整，引用时保留利益声明）。systemd PID1 自身常驻内存属系统底座开销（与部署选型无关的必装项），公开数据仅轶事级「几十 MB 量级」，无权威基准（待验证）。
2. **进程管理能力开箱即得**：一个约 10 行的 unit 文件声明 `ExecStart`/`WorkingDirectory`/`User`/`Restart=always`/`Environment=NODE_ENV=production`，`[Install] WantedBy=multi-user.target` 实现开机自启，随后 `systemctl daemon-reload`/`start`/`enable` 即完成接管；崩溃自动拉起（`Restart=always` + `RestartSec=5`）[5][3]。另有 cgroup 资源记账、watchdog、socket activation、依赖排序等系统能力 [3][1]。
3. **日志内建**：journald 收集 + `journalctl -u <app> -f` 查询，日志轮转由 journald 自带，无需另装日志栈 [3]。注意持久化默认依赖发行版（见风险节）[9]。
4. **小机上比容器栈更省**：Deploysmith（2026-09-26；质性结论，作者明确声明无实测数字）：1 GB 内存小机上裸 VPS + systemd 每进程 RAM 更低、调试更简单、活动部件更少；完整 `node:24` 镜像在应用代码之前就「数百 MB」，1–2 GB 小机上 app + Postgres + Nginx 三容器「可能悄悄把你推进 swap」[4]。Docker 何时划算的对照：多服务独立版本、要整栈回滚、要交接给别人 [4]。
5. **标准组合 Caddy 反代**：Caddy 默认自动获取并续期全部站点的 TLS 证书（ACME），宣称「Every site on HTTPS」；当前 v2.11.6（2026-10-01 发布）、⭐76,231、Apache-2.0（gh 2026-10-02）[6][7]。systemd 管应用进程 + Caddy 占 80/443 反代自动 HTTPS，是该路线的标配拓扑——证书运维为零。

**benchmark 一组**（Empellio 2026-03；AWS EC2 t3.small 2vCPU/2GB、Ubuntu 22.04、管理 10 个 Node HTTP server、每组 20 次取中位数）[3]：

| 方案 | daemon 内存 | 冷启动（中位） | 崩溃恢复（中位） |
|---|---|---|---|
| **systemd** | 0 MB（无独立 daemon） | 78 ms | 182 ms |
| PM2 | ~83 MB | 1,247 ms | 412 ms |
| Supervisor | ~31 MB（Python） | — | 530 ms |

## 对比

| 维度 | systemd 裸进程 | PM2 | Docker/Compose |
|---|---|---|---|
| daemon 中间层内存 | 无（PID 1 一部分）[3] | ~83 MB [3] | dockerd 空闲 ~50–200 MB（轶事引述，无权威基准）|
| 隔离 | 无，宿主机直跑（依赖冲突风险）[5] | 无 | 容器隔离 + 镜像不可变 [5] |
| 部署/回滚 | 同步文件 + `systemctl restart`，无声明式回滚 | 类似 | 镜像版本化，可回滚 [4] |
| 多机/编排 | 无概念——单机多 unit，依赖排序靠 `After=`/`Wants=` [1][5] | 单机 | Compose 及编排生态 |
| 跨平台 | 仅 Linux [3][5] | 跨平台 | 跨平台 |
| 零停机/cluster | 无（需应用层自实现）[3] | cluster mode 内建 | 视编排方案 |
| 安装依赖 | 发行版自带，零安装 [8] | 需 Node | 需装 Docker 引擎 |

systemd vs Docker 的定性分工（_russell，2024-12/2025-07）：Docker 适合可移植、隔离部署；systemd 适合需要直接 OS 集成与更细服务控制的场景；Docker「因容器化有小额开销（通常可忽略）」，systemd 长驻进程「无容器开销」[5]。逐维度横向对比见类别 `../comparison.md`（如存在）。

## 风险与注意

- **仅 Linux**：无跨平台可能 [3][5]。
- **无隔离**：应用直跑宿主机，依赖/端口/文件系统与其他服务共享，冲突需自行约束；专用 `User=`、`PrivateTmp`、`NoNewPrivileges` 等沙箱指令可部分缓解，但不是容器级隔离 [5][3]。
- **无镜像/不可变环境**：部署 = 手动同步文件 + 重启，构建产物无版本化、无一键回滚；服务数量与交接需求上升后，这是该路线最大的心智负担（Deploysmith 归类：多服务/要交接是 Docker 的场景）[4]。
- **多应用 = 多 unit**：没有「编排」概念；服务间拓扑靠人维护，超出一台机器要换方案 [1][5]。
- **journald 持久化默认依赖发行版**：上游默认 `Storage=auto`——`/var/log/journal` 存在则持久、不存在则重启即失；`auto` 不自建目录，且发行版可覆盖（Raspberry Pi OS 2025-05-13 镜像起改默认 `volatile`）——上机第一件事确认 `ls /var/log/journal` [9]。
- **内存口径差异**：`systemctl status` 显示 cgroup 总内存而非单进程 RSS，与 `top`/`htop` 比对时数值不同（检索 2026-10-02，留档 raw/2026-10-02/web/systemd-websearch-benchmarks.md）。
- **PID1 自身内存无权威基准**：轶事级「几十 MB 量级」（待验证，下次更新 `verified` 时补齐或删除）。

## 来源

1. systemd 官网 — https://systemd.io/（访问 2026-10-02；官方定义/PID1/组件清单；留档 raw/2026-10-02/gh/systemd-versions-notes.md）
2. systemd/systemd — https://github.com/systemd/systemd（gh 2026-10-02 采集：⭐16,768、push 2026-10-02、检测许可 GPL-2.0（仓库实况 LGPL-2.1+GPL-2.0 混合）、v262 2026-09-22、v256–v262 主版本日期序列；原始响应留档 raw/2026-10-02/gh/systemd_systemd.json、raw/2026-10-02/gh/systemd_releases.json、raw/2026-10-02/gh/systemd-versions-notes.md）
3. Process Manager Comparison 2026（Empellio，2026-03；Oxmgr 厂商非中立）— https://dev.to/empellio/process-manager-comparison-2026-pm2-systemd-supervisor-oxmgr-and-more-4e0p（访问 2026-10-02；benchmark 与内存开销数据；留档 raw/2026-10-02/web/systemd-dev.to.md）
4. Docker vs a Raw VPS: When Containers Actually Pay Off（Deploysmith，2026-09-26；质性、作者声明无实测数字）— https://deploysmith.dev/hosting/docker-vs-vps（访问 2026-10-02；留档 raw/2026-10-02/web/systemd-dev.to.md）
5. Systemd vs. Docker: Exploring a Surprising Alternative（_russell，2024-12-09 发/2025-07-27 改；质性）— https://dev.to/_russell/systemd-vs-docker-exploring-a-surprising-alternative-4pmm（访问 2026-10-02；unit 文件范例与局限清单；留档 raw/2026-10-02/web/systemd-dev.to.md）
6. Caddy 官网 — https://caddyserver.com/（访问 2026-10-02；自动 HTTPS 宣称原文；留档 raw/2026-10-02/web/systemd-dev.to.md）
7. caddyserver/caddy — https://github.com/caddyserver/caddy（gh 2026-10-02 采集：⭐76,231、Apache-2.0、v2.11.6 2026-10-01；留档 raw/2026-10-02/gh/systemd-versions-notes.md）
8. Systemd - Wikipedia（发行版采用时间线）— https://en.wikipedia.org/wiki/Systemd（WebSearch 检索 2026-10-02；留档 raw/2026-10-02/web/systemd-distro-adoption.md）
9. journald 持久化机制（journald.conf(5) freedesktop / systemd-journald(8) Arch man / Red Hat sol. 696893 / raspberrypi bookworm-feedback#415）— WebSearch 检索 2026-10-02；留档 raw/2026-10-02/web/systemd-journald-persistence.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | adopt | 首次记录（lightweight-deploy 类别调研；gh 一手 + 6 组网络来源当日核实） |
