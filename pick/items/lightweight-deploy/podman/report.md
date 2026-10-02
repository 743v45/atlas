# Podman

> **TL;DR**：daemonless 无守护进程容器引擎、Docker 的直接替代：空闲零内存（对比 dockerd 常驻 140–180 MB），quadlet 把容器/卷/网络声明为 systemd unit、自启/重启/日志全交 systemd 原生管理，CLI/Dockerfile/Docker 兼容 API 让存量技能近乎无损迁移——适用域：Linux VPS 小规模自托管服务；rootless 边界坑与文档生态弱于 Docker 使整体定 trial，新装 Linux 机且无存量 Docker 生态的场景可按 adopt 用。

- **结论**：trial（试用；轻量轴——资源占用+运维心智——上赢 Docker，但 rootless 边界与 Compose 边缘差距要求使用者有 Linux 底子）
- **核实日期**：2026-10-02（gh 一手数据 + 官网/官方文档/LWN 当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 当前版本 | v6.1.3（2026-09-29 发布）；5.x 线并行维护（v5.8.8 同日发布，近三个月 5.8.6→5.8.8 三连发） | [2] |
| 上个大版本 | v6.0.0（2026-06-24 发布，断裂式变更见风险节） | [2][3] |
| 许可证 | Apache-2.0 | [1] |
| 治理 | Red Hat 主导研发多年 → 2024-11 宣布捐入 CNCF → 2025-01-21 接纳为 Sandbox | [5][6] |
| 维护活跃度 | ⭐32,985、push 2026-10-02（与采集同日）、open issues 1,014（gh 2026-10-02） | [1] |
| 平台 | Linux 原生；macOS/Windows 走 podman machine（VM 内跑）；FreeBSD 实验支持（14.3+） | [2][9] |
| 发行版地位 | RHEL 8 起替代 Docker 成默认容器引擎；Fedora/CentOS/Ubuntu/Debian 官方仓库直装 | [11] |

## 为什么选

1. **daemonless = 空闲零基线成本**。无常驻守护进程：没有容器在跑时 Podman 占 0 MB；对照 dockerd 空闲常驻 140–180 MB [8]。这是架构性差异——CNCF 官方描述即「without requiring a daemon or root privileges」[6]——不是调优得来的。对「一台 VPS 跑几个到十几个小服务」的场景，省掉的是常驻的百 MB 级基线。
2. **quadlet：容器声明即 systemd unit**。`.container`/`.volume` 等声明文件放进 `~/.config/containers/systemd/`（rootful 为 `/etc/containers/systemd/`），由 systemd generator 翻译成原生 unit [4]——开机自启（源文件内 `[Install] WantedBy=multi-user.target`）、重启策略、依赖编排（卷/网络按名引用即隐式接线）、`journalctl` 日志全部是 systemd 本身的能力，无额外组件常驻 [4]。rootless 实践要点：`loginctl enable-linger` 登出续命 + `systemctl --user daemon-reload` [10]。这是「容器引擎」与「systemd」两条部署路线之间的桥：日常运维心智收敛到 systemctl 一套命令。
3. **Docker 兼容是迁移成本的答案**。CLI 命令与 Dockerfile 直接用（drop-in replacement 口径 [11]）；`systemctl --user start podman.socket` 起兼容 API socket（systemd socket activation）后，官方 Docker Compose v2 经 `DOCKER_HOST=unix:///run/user/$UID/podman/podman.sock` 直连使用，是 2026 年的共识路线 [7]。存量技能与 compose 文件基本无损迁移。
4. **治理与成熟度双保险**。Red Hat 工程投入多年、RHEL 默认引擎的生产规模背书 [11]；2024-11 KubeCon NA 宣布连同 Buildah/Skopeo/Composefs/bootc/Podman Desktop 整体捐入 CNCF，2025-01-21 接纳为 Sandbox（LFX Health Score "Excellent (86)"）[5][6]——单一厂商绑定风险解除。v6.0.0 起 import 路径改 `go.podman.io/podman/v6`，GitHub 组织迁至 `podman-container-tools`（旧址自动重定向）[2]。
5. **rootless 安全边界**。容器由非 root 用户经 user namespace 运行，公网服务被攻破不直接等于主机失守 [6][10]——对自托管公网服务，这是 Docker rootful 默认之外的真实加分。

## 对比

| 维度 | Podman | Docker |
|---|---|---|
| 守护进程 | 无（daemonless）[6] | dockerd 常驻，空闲 140–180 MB [8] |
| 空闲内存 | 0 MB [8] | 见上 |
| 服务管理 | quadlet → systemd 原生（systemctl/journalctl）[4] | restart policy + compose，或 systemd 再包一层 |
| 权限模型 | rootless 一等公民 [6][10] | rootful 默认，rootless 非主路径 |
| Compose | 官方 Compose v2 经兼容 socket 可用；自带 podman-compose 但功能完整度更低（init containers 等缺失）[7] | 原生 |
| 文档/GUI 生态 | 较弱；Podman Desktop（v1.29，2026-10-02 快照）缓解 [9] | 最强 |
| systemd 集成 | quadlet 官方正路 [4] | 无对等物 |

多机编排非其射程（无原生多主机能力，该需求应看 Kubernetes/微型 PaaS，见类别横评）。逐维度横评见 `../comparison.md`（如存在）。

## 风险与注意

- **v6.0.0 是断裂式升级（2026-06-24）**：移除 BoltDB（启动时自动迁 SQLite）、cgroups v1（须 v2）、iptables（须 nftables）、CNI（须 Netavark）、slirp4netns（须 Pasta）、**Intel Mac 支持**、Windows 10 支持；须配套 Buildah v1.44/Skopeo v1.23/Netavark v2.0；社区口径「当迁移对待，而非原地版本升级」[2][3]。老机器（cgroups v1）直接不可用。
- **rootless 边界坑**：rootless Quadlet 必须用 systemd **user units**——系统级 unit 里用 `User=` 跑 rootless Podman **不受支持** [10]；登出后服务续命须 `enable-linger` [10]；容器内绑低端口（<1024）需调 sysctl `net.ipv4.ip_unprivileged_port_start`（待验证）；卷的 UID 映射（subuid/subgid）与镜像内用户对不齐是社区高频踩坑点（待验证，未单独取证）。
- **Compose 边缘差距**：官方 Compose 经兼容 socket 存在边缘 case；`podman-compose` 缺 init containers 等特性，远端场景差距更明显 [7]。
- **性能数据口径警示**：空闲内存优势无争议（架构性）；**负载下**各基准互相矛盾——有反例显示特定负载 Docker overhead 反而更低，精确数字只作量级参考 [8]。rootless 模式对双方都加约 25–30% 冷启动开销 [8]。
- **macOS/Windows 非一等公民**：走 podman machine VM，多一层 VM 心智；且 6.0 起 Intel Mac 不再支持，只剩 Apple Silicon [2][9]。

## 来源

1. containers/podman — https://github.com/containers/podman（gh 2026-10-02 采集：⭐32,985、push 2026-10-02、Apache-2.0、open issues 1,014；原始响应留档 raw/2026-10-02/gh/containers_podman.json）
2. Podman releases（gh api 2026-10-02 采集）：v6.1.3 发布 2026-09-29、v5.8.8 同日、v6.0.0 发布 2026-06-24T17:38Z；v6.0.0 release notes 摘录留档 raw/2026-10-02/gh/containers_podman_v6.0.0_release.json
3. LWN: Podman 6.0 released — https://lwn.net/Articles/1079600（访问 2026-10-02；留档 raw/2026-10-02/web/podman-lwn.net.md）
4. Podman 官方文档 quadlet-basic-usage(7) — https://docs.podman.io/en/latest/markdown/podman-quadlet-basic-usage.7.html（访问 2026-10-02；留档 raw/2026-10-02/web/podman-docs.podman.io.md）
5. Red Hat 公告：向 CNCF 捐赠容器工具集（2024-11 KubeCon NA）— https://www.redhat.com/en/blog/red-hat-contribute-comprehensive-container-tools-collection-cloud-native-computing-foundation（访问 2026-10-02；留档 raw/2026-10-02/web/podman-websearch-cncf.md）
6. CNCF 项目页 Podman Container Tools — https://www.cncf.io/projects/podman-container-tools（访问 2026-10-02；2025-01-21 Sandbox 接纳；留档 raw/2026-10-02/web/podman-cncf.io.md）
7. Compose 兼容聚合（WebSearch 2026-10-02）：OneUptime https://oneuptime.com/blog/post/2026-03-17-use-docker-compose-podman-socket/view 、GitHub discussion https://github.com/podman-container-tools/podman/discussions/29355 、Red Hat https://www.redhat.com/en/blog/podman-compose-docker-compose（留档 raw/2026-10-02/web/podman-websearch-compose.md）
8. 资源占用聚合（WebSearch 2026-10-02，口径警示见风险节）：Medium @jamilxt https://medium.com/@jamilxt/docker-vs-podman-in-2026-the-benchmarks-contradict-each-other-here-is-how-to-decide-6eda538f8190 、uptrace.dev https://uptrace.dev/comparisons/podman-vs-docker 、shattered.io https://shattered.io/docker-vs-podman-overhead-comparison-2026 等（留档 raw/2026-10-02/web/podman-websearch-memory.md）
9. podman.io 官网 — https://podman.io（访问 2026-10-02；安装文档 https://podman.io/docs/installation；留档 raw/2026-10-02/web/podman-podman.io.md）
10. Quadlet rootless 实践聚合（WebSearch 2026-10-02）：ubitools https://www.ubitools.com/podman-quadlet-guide 、unix.SE https://unix.stackexchange.com/questions/714167 、GitHub discussion https://github.com/podman-container-tools/podman/discussions/20573（留档 raw/2026-10-02/web/podman-websearch-quadlet.md）
11. RHEL/发行版打包聚合（WebSearch 2026-10-02）：Fedora Docs https://docs.fedoraproject.org/en-US/neurofedora/containers 、Podman 安装文档 https://podman.io/docs/installation 、Red Hat Developer 迁移指南 https://developers.redhat.com/blog/2020/11/19/transitioning-from-docker-to-podman（留档 raw/2026-10-02/web/podman-websearch-rhel.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（lightweight-deploy 类别新建；gh+官方文档+LWN+CNCF 当日核实） |
