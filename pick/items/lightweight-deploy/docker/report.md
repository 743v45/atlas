# Docker

> **TL;DR**：Linux 单机部署的行业默认与基线：daemon 常驻开销约 100 MB 级、compose 生态与可复现性使其仍是多应用单机的安全选择；轻量轴的真实痛点在桌面端 VM（常驻 2 GB+）与 daemon 单点/需 root——该问的不是「要不要 Docker」而是「是否只在服务器上用 Docker」。

- **结论**：adopt（适用域：**Linux 服务器上的单机多应用部署**；桌面端 macOS/Windows 开发环境不在此裁决内——那里 VM 常驻 2 GB+ 是真实痛点，见「轻量轴上的扣分」）
- **核实日期**：2026-10-02（gh 一手数据 + 官方文档当日核实；社区开销数据经检索聚合并注明性质）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | Engine v29.8.2（2026-09-30 发布；v29 版本线自 2025-11 起） | [2][9] |
| 许可证 | Apache-2.0（Engine 上游 Moby） | [1] |
| 仓库 | github.com/moby/moby：⭐72,144、push 2026-10-01（gh 2026-10-02 采集） | [1] |
| compose | docker/compose ⭐38,278、v5.5.1（2026-09-03）（gh 2026-10-02 采集） | [3] |
| 维护活跃度 | 功能版约月度（v29.7.0 7/30 → v29.8.0 9/3 → v29.9.0-rc 10/1），v25 旧分支 2026-09-30 仍在出补丁 v25.0.18 | [2] |
| Desktop 许可 | 个人/教育免费；企业 **<250 员工且 <$10M 年营收** 免费，超过需付费订阅（2021 年规则，2026-10 仍有效） | [5] |

## 为什么选（行业默认视角的四条论断）

1. **Linux 侧开销是「低」不是「高」**：想避开 Docker 的主要动机常来自桌面端体验，但部署目标 Linux VPS 上 daemon 空闲开销约 60-100 MB、带基础容器的全套约 100-500 MB（社区共识，非官方 benchmark，2026-10 检索聚合）[6]；容器本体开销近零（Torizon 基准：部署栈内存开销约 23 MB）[6]。对比桌面端 VM 的 2 GB+ [4]，**Docker 的「重」几乎全部在桌面端 VM 层，不在 Linux daemon**。
2. **compose 生态无可替代**：声明式单机编排事实标准——docker/compose ⭐38,278、v5.5.1（2026-09-03）、当日仍在推送（gh 2026-10-02）[3]；几乎每个开源自托管项目都以 `docker compose up` 为第一交付形态，第三方镜像仓库生态（Docker Hub 等）是其护城河。
3. **可复现性与回滚**：镜像=不可变交付物，「构建一次、随处运行」；应用崩溃回滚=切回上一镜像 tag，不需要在宿主机上排查「环境漂移」。对 3-15 个应用的单机场景，这是裸进程 + 进程管理器最难自费提供的性质（要自己造打包/回滚机制）。
4. **维护活跃与文档密度顶级**：Moby 月度功能版 + 旧版本线维护（v25.0.18，2026-09-30）[2]；Engine v29（2025-11）把 containerd image store 设为新装默认、镜像拉取据报快约 37%（二手转述，非官方实测）[9]——架构方向是向 OCI/containerd 标准收敛，不是加重。任何问题都能搜到答案，这是 AI 时代之外的另一种「文档冗余保险」。

### 轻量轴上的扣分（作为轻量化选择的视角）

同一事实从「轻量化」轴看有另一面，这是本类别横评真正要问的：

1. **桌面端 VM 是重量级**：macOS/Windows 上 Docker Desktop 跑 Linux VM，官方 Resource Saver 页面反向证实空闲常驻 **2 GB+**（「省 2 GB+」的前提是先占着 2 GB+）[4]；社区常见 2-8 GB 区间报告（Reddit「8 GB RAM」帖等，经验值）[6]。官方缓解：默认开启、空闲 5 分钟自动停 VM[4]——但唤醒要 3-10 秒，且 Windows/WSL 下只暂停引擎不停 VM，内存照占 [4]。
2. **daemon 单点 + 默认需 root**：所有容器经 dockerd，daemon 崩则全部容器停；默认安装 rootful，攻击面与误操作半径大。rootless 模式已生产可用（2025 共识），但有代价：P99 延迟开销 20-40%、容器密度下降（sanj.dev 2025）[8]，且依赖内核放行非特权 userns、资源限制需 systemd cgroup 委派、网络走 slirp4netns/pasta 用户态栈 [8]。
3. **概念与运维心智高于裸进程**：镜像分层、网络模式、卷、daemon 日志体系——「跑起来」容易，「精通」门槛真实存在；VPS 场景还有 UFW 被绕过（Docker 直写 iptables）、磁盘被镜像层吃满等经典坑（SSD Nodes VPS 指南，2026-10 检索聚合）[6]。
4. **政策与许可噪音**：Docker Hub 匿名拉取 10 次/小时（CI 场景痛点）、认证免费 100 次/小时、付费无限（2025-04-01 生效）[7]；Desktop 对超限企业收费（250 员工/$10M）[5]。对个人小服务影响很小，但政策曾反复变动（2025 年先紧缩后回调），说明**免费假设需要周期性复核**。

## 对比（同类形态，逐维度横评见 `../comparison.md`）

| 维度 | Docker + compose | systemd 裸跑 | Podman（rootless 优先） |
|---|---|---|---|
| 常驻开销 | daemon 约 60-100 MB + 容器近零（~23 MB/栈）[6] | 无 daemon，近零 | 无 daemon |
| 可复现/回滚 | 镜像级，最强 | 需自建（打包脚本/软链切换） | 镜像级（OCI 同源） |
| 生态/文档 | 最大（compose + Hub）[3] | 每应用自定义 unit | 兼容 OCI，compose 支持为外围 |
| 单点/权限 | daemon 单点、默认 root [8] | 无单点、按服务授权 | 无 daemon、rootless-first [8] |
| rootless 代价 | P99 +20-40%（可选启用）[8] | 不适用 | 默认即 rootless（同一量级代价）[8] |

微型 PaaS / 托管平台类条目多数以容器运行时为底座或以订阅费换运维——具体形态待该条目报告核实（待验证），此处不替它们下结论。

## 风险与注意

- **「轻」与「重」取决于宿主**：Linux 服务器低开销 [6] vs 桌面端 2 GB+ VM [4]——本报告 verdict 只覆盖前者；在 mac/Win 开发机上追求轻量应看桌面端替代（本类别或相邻类别条目）。
- **daemon 单点与 root 默认**：可用 rootless 缓解，接受 P99 +20-40% 与 userns/cgroup 前提 [8]；个人 VPS 上更常见的做法是接受 rootful + 管好暴露面（UFW 绕过坑 [6]）。
- **磁盘增长**：镜像层与构建缓存随时间累积，v29 切 containerd store 时有迁移期重复层报告（社区，2026-10 检索）[9]；VPS 小盘需定期 `prune`。
- **Hub 拉取限额**：匿名 10/h、认证免费 100/h（2025-04-01 起）[7]——部署脚本务必登录认证；CI 无认证拉取是主要受灾区。
- **许可边界记两条**：Engine/Moby Apache-2.0 永远免费 [1]；Desktop 250 员工/$10M 门槛只影响企业桌面端 [5]，个人与小团队不受影响。
- 待验证：微型 PaaS 条目对 Docker 的依赖关系；桌面端 VM「常见 2-8 GB」区间的更严谨出处（现为论坛经验值 [6]）。

## 来源

1. moby/moby — https://github.com/moby/moby（gh 2026-10-02 采集：⭐72,144、push 2026-10-01、Apache-2.0、open_issues 3,913；原始响应留档 raw/2026-10-02/web/docker-api.github.com.md）
2. moby/moby releases — `gh api repos/moby/moby/releases`（2026-10-02：v29.8.2 2026-09-30、v29.9.0-rc.1 2026-10-01、v25.0.18 2026-09-30；节奏留档 raw/2026-10-02/web/docker-releases-cadence.md）
3. docker/compose — https://github.com/docker/compose（gh 2026-10-02 采集：⭐38,278、v5.5.1 2026-09-03；留档同 [1] 文件）
4. Docker Docs · Resource Saver — https://docs.docker.com/desktop/use-desktop/resource-saver/（访问 2026-10-02：默认开启、空闲 5 分钟停 VM 省 2 GB+、唤醒 3-10 s、WSL 只暂停引擎；留档 raw/2026-10-02/web/docker-docs-resource-saver.md）
5. Docker Docs · Desktop 订阅许可 — https://docs.docker.com/subscription-billing/desktop-license（经 WebSearch 聚合 2026-10-02：<250 员工且 <$10M 免费、超限需 Pro/Team/Business；留档 raw/2026-10-02/web/docker-desktop-license-search.md）
6. dockerd Linux 开销与 VPS 坑 — WebSearch 聚合 2026-10-02：Docker Forums（daemon 300-400 MB 报告）、Taubyte（基础套件 100-200 MB）、Torizon（容器开销 ~23 MB）、Stackademic（自托管空闲 300-500 MB）、SSD Nodes（UFW/磁盘坑）；聚合共识空闲 daemon 约 60-100 MB；留档 raw/2026-10-02/web/dockerd-linux-overhead-search.md
7. Docker Hub 政策 — 官方公告 https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience（经 WebSearch 聚合 2026-10-02：2025-04-01 起付费无限/免费认证 100/h/匿名 10/h；留档 raw/2026-10-02/web/docker-hub-policy-search.md）
8. rootless 模式现状 — WebSearch 聚合 2026-10-02：sanj.dev《Container Runtime Showdown 2025》（P99 +20-40%）、kenmuse.com（userns 前提）、The New Stack（cgroup 委派）；留档 raw/2026-10-02/web/docker-rootless-search.md
9. Engine v29 — release notes https://docs.docker.com/engine/release-notes/29（经 WebSearch 聚合 2026-10-02：2025-11 发布、containerd image store 新装默认、API ≥1.44、拉取快约 37% 为二手转述；留档 raw/2026-10-02/web/docker-engine-v29-search.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | adopt | 首次记录（作为 lightweight-deploy 类别的基线参照立项：Linux 服务器域 adopt，桌面端痛点如实记录） |
