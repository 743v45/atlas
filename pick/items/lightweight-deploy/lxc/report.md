# LXC / Incus（系统容器）

> **TL;DR**：系统容器路线的社区主线（Incus，Apache-2.0，LXD 社区分叉后由原班人马领导，LTS 7.0 支持至 2031-06），但对本类别根问题——部署几个 app 到一台 VPS——判 hold：应用部署退化为「容器内手动装环境 + 手写 init」，资源与运维开销都高于 Docker 系；其真正的适用域在本类别轴外——整机环境隔离、多发行版、快照回滚时才轮到它。

- **结论**：hold（对本类别根问题「部署几个到十几个 app」不推荐；若根问题换成「一台机器跑多个完整隔离环境」则立即翻正为 trial~adopt，见下文适用域反转）
- **核实日期**：2026-10-02（gh 一手数据 + 官网/公告当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 主对象 | Incus（社区主线，LinuxContainers 项目旗下） | [1][5] |
| 版本线 | 7.x：LTS 7.0（2026-05-05 发布，支持至 2031-06，前 2 年全修 + 后 3 年仅安全）；最新 feature 版 7.5.1（2026-09-25 发布） | [2][3] |
| 许可证 | Apache-2.0 | [2] |
| 维护活跃度 | ⭐6,310、push 2026-10-02（采集当日仍在推）、open issues 36；feature 版约月度节奏（gh 2026-10-02 采集） | [2] |
| 底座 | liblxc（lxc/lxc，上游已到 v7.0.0，2026-04-30 发布；⭐5,266）；Incus 7.0 硬依赖 LXC ≥6.0.0 | [3][4] |
| 定位 | 「现代系统容器、应用容器与虚拟机管理器」——三种实例类型并存（系统容器/应用容器/QEMU 虚拟机），类云体验 | [1][3] |

## 为什么不选（针对类别根问题：部署几个 app 到一台 VPS）

1. **应用部署心智错位**：系统容器的部署单元是「一台虚拟小机器」（完整 OS 环境），不是「应用」[1]。部署一个 web 服务 = 进容器装运行时 + 手写 systemd 单元（或 rc 脚本），没有镜像/Compose 式的「应用即产物」声明层 [1][3]。本类别其他候选（容器引擎、进程管理器、微型 PaaS）都以应用为一等公民，Incus 以环境为一等公民——拿它部署 app 是用 VM 的心智干轻活。
2. **轻量化轴上不占优**：同为共享宿主内核，系统容器空闲内存量级居中——Debian 13 base 空闲约 16 MB（Docker 容器几 MB～几十 MB、裸进程≈0；KVM VM 约 85 MB 起）[6]。比 VM 省的部分（独立内核）是真的，但对「就跑一个 app」而言，完整用户态（init + 系统服务）是纯 overhead。
3. **运维面按容器数放大**：N 个 app = N 套各自要升级/维护/备份的完整用户态（每个系统容器都是一个「迷你整机」，含 init 与全套系统服务 [1]）；进程管理器/Docker 路线在宿主侧维护一次即可。对「几个到十几个 app」的个人场景，这恰恰把类别轴上的「运维心智」做重了（由机制推导）。

### 适用域反转（何时解除 hold）

以下需求出现时，系统容器是同类最优解，本条目应升 trial~adopt：

- **整机环境隔离**：不同发行版并存（官方每日构建多发行版镜像 [1]）、整套技术栈独立、快照/整机回滚、跨主机迁移 [1]。
- **「轻 VM」场景**：Incus 同时管 QEMU 虚拟机，一套 CLI/REST API 覆盖容器与 VM 两种形态 [1][3]——要跑需要独立内核的东西（自建 DNS/邮件全套栈、内核模块实验）时不用再引入第二套管理面。
- **OCI 兼容桥梁**（6.3+）：可直接从 Docker Hub 等 OCI registry 拉应用镜像建应用容器（`incus remote add docker https://docker.io --protocol=oci`）[3]——但这恰恰说明：纯应用部署它只是「Docker 的一个次级入口」。

## 形态差异：LXD（亚种，不独立立目）

LXD 与 Incus 是同型工具的两个分叉形态（fork 未分家式的选型差异，按 RULES §1 以正文小节说明，不立条目）：

- **分叉史**：LXD 原属 LinuxContainers 社区 8 年余；2023-07 Canonical 将其收归内部治理，社区随即拉出 Incus，由 LXD 原负责人 Stéphane Graber 领导 [1][5]；linuxcontainers.org 的 LXD 页现已挂声明「LXD 项目不再是 Linux Containers 项目的一部分」——分叉永久且已定局 [5]。
- **Canonical LXD 现状**（gh 2026-10-02 实测 [4]）：未死——canonical/lxd 仍在 push（2026-10-02）、未 archived、⭐4,833；但许可证 AGPL-3.0（对比 Incus Apache-2.0），且 GitHub latest release 停在 lxd-6.9（2026-06-23，距采集日 3 个多月），同期 Incus 已发 7.5.1——社区动能与版本节奏都在 Incus 侧。
- **选择口径**：个人/小团队自托管场景选 Incus 不选 LXD——许可更宽（Apache-2.0 vs AGPL-3.0）、社区治理、发行版官方文档（Rocky Linux 等）与 2026 年安装指南已转向 Incus [5]。有个反向趣味事实：LXD 的 UI（lxd-ui）反被 Incus 生态吸收为 `incus-ui-canonical` 可选包 [7]。
- 教程检索注意：LXD/LXC/Incus 三名在网上长期混用，2023 年前的教程讲的都是 LXD，认准 linuxcontainers.org/incus 文档域 [5]。

## 对比

| 维度 | Incus 系统容器 | Docker/Compose | systemd 裸进程 | KVM VM | 微型 PaaS |
|---|---|---|---|---|---|
| 单实例空闲内存 | ~16 MB（Debian 13 base，第三方实测）[6] | 几 MB～几十 MB [6] | ≈0 | ~85 MB 起 [6] | 依底座 |
| 部署单元 | 完整环境 | 应用镜像 | 手写单元 | 完整机器 | 应用 |
| 应用声明层 | 无（OCI 入口为次级 [3]） | 有（镜像+Compose） | 无 | 无 | 有 |
| 隔离强度 | 中（共享内核 + 完整用户态边界）[1] | 中（共享内核） | 无 | 强（独立内核）[6] | 依底座 |
| 本类别贴合度 | 低（轴外强项） | 高 | 高（极简场景） | 低（更重） | 高 |

逐维度横评见类别 comparison（如存在）。

## 风险与注意

- **内核版本硬门槛**：Incus 7.0 要求宿主 Linux ≥6.12、QEMU ≥8.2 等 [3]——不少廉价/老式 VPS 内核旧且不可换，采买前先核对 `uname -r`；同时 7.0 弃用 CGroupV1 与 xtables [3]。
- **Web UI 非默认**：主发行渠道中 UI 是可选包（Zabbly `incus-ui-canonical` / Arch `incus-ui`），需 Incus 监听网络 + 客户端证书导入后才可用；2026-04 公告披露过一处 UI web server 漏洞（6.23.0 修复）——UI 面暴露到公网需谨慎 [7]。IncusOS（项目专属 OS）出厂带 UI，但那是整机方案不是包方案 [7]。
- **内存数据口径**：本报告内存数字均为 Proxmox/LXC 语境的第三方社区实测（访问 2026-10-02），非 Incus 官方基准；Incus 系统容器同以 liblxc 为底座、机制相同，量级可参考但非精确断言 [6]。
- **官网页面滞后**：访问 2026-10-02 时 Incus 主页仍写「当前 LTS 为 6.0，支持至 2029-06」，而 news 页 2026-05-05 已宣布 7.0 LTS——官方页面间更新不同步，时效判断以 news 页与 gh release 为准 [1][3]（待验证：主页是否随后续版本刷新）。
- **每 2 年一个 LTS 的跟进节奏**：feature 版月度发布、LTS 窗口错开（6.0 至 2029-06、7.0 至 2031-06）[3]，升级路径需要读 release notes，但窗口内可长期不动，个人场景跟 LTS 即可。

## 来源

1. Incus 官网主页（定位、三实例类型、镜像/profile/迁移/设备直通、Zabbly 商业支持） — https://linuxcontainers.org/incus/（访问 2026-10-02；原始摘录留档 raw/2026-10-02/web/lxc-linuxcontainers.org.md）
2. lxc/incus — https://github.com/lxc/incus（gh 2026-10-02 采集：⭐6,310、push 2026-10-02、Apache-2.0、latest v7.5.1 发布 2026-09-25、open issues 36；原始响应留档 raw/2026-10-02/web/lxc-github.com.md）
3. Incus 7.0 LTS 发布公告（2026-05-05，支持至 2031-06；OCI 镜像支持、依赖最低版本 Linux 6.12/LXC 6.0.0、弃用 CGroupV1/xtables） — https://linuxcontainers.org/incus/news/2026_05_05_16_29.html（访问 2026-10-02；留档 raw/2026-10-02/web/lxc-linuxcontainers.org-news.md）
4. lxc/lxc 与 canonical/lxd（gh 2026-10-02 采集：lxc ⭐5,266 / v7.0.0 发布 2026-04-30；lxd ⭐4,833 / AGPL-3.0 / latest lxd-6.9 发布 2026-06-23 / 未 archived） — https://github.com/lxc/lxc 、https://github.com/canonical/lxd（留档 raw/2026-10-02/web/lxc-github.com.md）
5. Incus/LXD 分叉现状（WebSearch，访问 2026-10-02；含 linuxcontainers.org LXD 迁移声明、stgraber.org、Rocky Linux 文档转向、Ubuntu 26.04 收录） — 留档 raw/2026-10-02/web/lxc-websearch-fork-status.md
6. 系统容器内存开销第三方实测（WebSearch，访问 2026-10-02：Alpine <4 MB vs VM ~60 MB [Reddit r/Proxmox]；Debian 13 ~16 MB vs ~85 MB [proxmoxmigracje.pl]；Nextcloud ~145 MB vs ~520 MB [proxmoxpulse.com]；Docker 几 MB～几十 MB [datazone.de]） — 留档 raw/2026-10-02/web/lxc-websearch-memory-overhead.md
7. Incus Web UI 与 Zabbly 打包渠道（WebSearch，访问 2026-10-02：UI 为可选包 incus-ui-canonical、`incus webui`、客户端证书；IncusOS 出厂带 UI；6.23.0 修复 UI 漏洞；Zabbly 构建目标 Ubuntu 22.04/24.04/26.04 + Debian 12/13，stable 与 lts-7.0 双通道） — 留档 raw/2026-10-02/web/lxc-zabbly-webui.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | hold | 首次记录（对类别根问题「部署几个 app 到一台 VPS」判 hold；适用域反转条件已写明） |
