# 留档：gh api systemd/systemd 主版本发布日期序列

- 来源：`gh api 'repos/systemd/systemd/releases?per_page=100'`（jq 过滤主版本 tag）
- 采集日期：2026-10-02
- 原始 releases 快照：`raw/2026-10-02/gh/systemd_releases.json`

## 主版本发布日期

| tag | published_at | 间隔 |
|---|---|---|
| v256 | 2024-06-11 | — |
| v257 | 2024-12-10 | ~6 个月 |
| v258 | 2025-09-17 | ~9 个月 |
| v259 | 2025-12-17 | ~3 个月 |
| v260 | 2026-03-17 | ~3 个月 |
| v261 | 2026-06-19 | ~3 个月 |
| v262 | 2026-09-22 | ~3 个月 |

## 补充观测（同日 releases 前 10 条）

- v262 稳定版 2026-09-22 发布（最新稳定线）
- v258.11 / v259.9 / v260.5 / v261.3 四条 stable 分支在 2026-09-10/11 同窗发补丁 → 多版本并行维护
- rc 节奏：v262-rc1 (2026-09-01) → rc2 (2026-09-08) → rc3 (2026-09-15) → v262 (2026-09-22)，约一周一个 rc

## 仓库 stats（gh 2026-10-02）

- systemd/systemd：⭐16,768、pushed_at 2026-10-02T15:14:15Z、license 检测 GPL-2.0、open_issues 3,528、archived=false
- 仓库根许可文件：LICENSE.LGPL2.1、LICENSE.GPL2、LICENSES/（主体 LGPL-2.1，部分 GPL-2.0；GitHub 检测值 GPL-2.0 是混合所致）

# 留档：gh api caddyserver/caddy

- 采集日期：2026-10-02（`gh repo view`）
- ⭐76,231、pushed_at 2026-10-02、Apache-2.0
- latest release：v2.11.6，published_at 2026-10-01

# 留档：systemd.io 官网首页

- 来源：https://systemd.io/（访问 2026-10-02，WebFetch）
- 官方定义：「a suite of basic building blocks for a Linux system」；系统与服务管理器**以 PID 1 运行并启动系统其余部分**
- 关键特性：激进并行化启动、socket 与 D-Bus activation、按需 daemon 启动、**基于 cgroup 的进程追踪**、事务性（transactional）依赖服务控制
- 组件：PID 1 管理器、日志 daemon（journald）、hostname/date/locale 等基础配置工具、登录用户/容器/VM 追踪、系统账户与 runtime 目录、网络配置/时间同步/日志转发/名字解析 daemon、mount/automount、systemd-boot UEFI 引导管理器、systemd-homed、systemd-resolved、systemd-coredump、tmpfiles
- 文档：systemd.io（Concepts/Booting/Interfaces）+ freedesktop.org man pages；另有发行版 wiki 与 RHEL/SUSE 厂商文档
- 页面无许可证与版本号（© systemd, 2026）
