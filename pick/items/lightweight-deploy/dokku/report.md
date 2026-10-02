# Dokku

> **TL;DR**：单机微型 PaaS 的事实标准：git push 即部署、buildpack 路线免写 Dockerfile、官方插件全家桶（Postgres/Redis/Let's Encrypt 等 28 个）加内置 nginx 路由与零停机发布——本质是把 Docker 藏起来而非绕开，官方 1GB 内存是硬门槛（不足时部署直接 remote rejected）；日常部署运维心智最低，但深度排障仍落到 Docker 层、单维护者依赖（9,759 vs 603 commits）是结构性风险——适用 Ubuntu/Debian VPS 上 CLI 优先的个人/小团队多应用托管。

- **结论**：trial（适用域：自有 Linux VPS、接受 CLI 工作流、几个到十几个应用的托管——试用顺利可直接当主力）
- **核实日期**：2026-10-02（gh 一手数据 + 官方文档当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v0.38.31（2026-09-27 发布）；v0.38 系列 2026-05 起已发 30+ 个 patch | [1] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/dokku/dokku（2013-06 创建，Go + Shell） | [1] |
| 维护活跃度 | ⭐32,157、push 2026-10-01（gh 2026-10-02 采集）；30 个 release / 4.5 个月（2026-05-10 → 2026-09-27） | [1] |
| 定位 | "The smallest PaaS implementation you've ever seen"——单机 Heroku，"Powered by Docker" | [2] |
| 支持系统 | Ubuntu 22.04/24.04/26.04 或 Debian 11+（AMD64/arm64）；安装约 5-10 分钟 | [3] |
| 最低内存 | Docker 调度器 1GB（K3s 调度器 2GB/节点）；<1GB 部署可能直接失败 | [3][4] |

## 为什么选（微型 PaaS 路线的核心论据）

1. **部署心智最低：git push 即部署**。每个应用一个 git remote，push 即构建即上线，官方定位即 "you can push Heroku-compatible applications to it via Git" [2]。这是八条部署路线里「上线一个新应用」步骤最少的。
2. **buildpack 路线免写 Dockerfile**：默认走 Herokuish（Heroku buildpacks），push 纯代码即可；builder 链可插拔七种（herokuish / Cloud Native Buildpacks / Dockerfile / Lambda / Nixpacks / Railpack / Null），Dockerfile 只在 herokuish 与 pack 都未命中时才被自动选中 [5]。不懂 Docker 概念也能完成日常部署。
3. **插件生态是数据服务全家桶**：官方插件 28 个——Postgres / MariaDB / MySQL / Redis / Mongo / Memcached / RabbitMQ / Elasticsearch / Let's Encrypt 等一条龙，另加活跃社区插件 53 个（合计约 155 个，其中 55 个已因并入核心而弃用）[6]；`dokku postgres:create` 级别的一条命令替代手写 compose + 网络对接。Let's Encrypt 插件独立活跃（⭐1,119、push 2026-09-28）[9]。
4. **域名路由与证书开箱即用**：默认 proxy 是内置 nginx（0.5.0 起解耦，`proxy:set` 可换 caddy/haproxy/traefik/openresty 共五种）[8]，配合 letsencrypt 插件自动签续证书 [6][9]；官方文档化零停机部署 [8]。
5. **升级纪律健全**：官方维护 0.5 → 0.38 共 **25 份迁移指南**（0.20 起每代都有），升级前有明确的 stop/rebuild 指引 [7]；发布节奏极密（30 release / 4.5 个月，gh 2026-10-02 采集）[1]，bug 修复以天计。
6. **控制面自身极轻**："As Dokku does not run any daemons, the security risk introduced by our software is minimal"——dokku 自身无常驻进程，VPS 上常驻的只有 dockerd + nginx + 各应用容器 [7]。第三方横评同样给出 "smallest resource footprint and the fewest moving parts"（2026-08 观测）[10]。

## 为什么不选（改用其他路线的信号）

1. **它不绕开 Docker，是把 Docker 藏起来**：dokku 官方自述 "Powered by Docker" [2]，每应用一个容器、构建用 herokuish 镜像。轻量化的下限被 Docker 底座钉死（见类别 docker 条目：daemon 常驻 + 需 root）。想去掉这层，看 podman/systemd 路线。
2. **1GB 内存是官方硬门槛且 1GB 档确实翻车**：官方明言 "Having less than 1 GB of system memory available for Dokku and its containers may result in unexpected errors"，典型症状是部署报 `! [remote rejected] master -> master (pre-receive hook declined)`，官方解法是 swap 扩到物理内存 2 倍 [4]；社区有真实 OOM 踩坑记录（构建期内存压力主要来自 buildpack 编译与应用容器）[11]。内存预算应按「1GB + swap」起跳。
3. **深度排障仍要懂 Docker**：buildpack 构建失败、网络不通、存储卷问题，最终都落到 `docker` 层排查；buildpack 屏蔽的是日常路径，不是故障路径 [5][11]。
4. **需要 Web UI 或集群就别选它**：无 dashboard 是设计选择而非缺陷 [10]；第三方共识定位 "Dokku is better for hardcore CLI teams with simple stacks"，要 Web UI 看 Coolify/Dokploy，要集群看 CapRover [12]。

## 对比

| 维度 | Dokku | 裸 Docker/compose（本类别基线） | Podman/quadlet | PM2 |
|---|---|---|---|---|
| 部署动作 | git push | docker compose up（手写 YAML） | quadlet unit + systemd | pm2 start |
| 证书/域名路由 | letsencrypt 插件 + 内置 nginx 自动配 [6][8] | 自配（caddy/traefik 或手写） | 自配 | 无（无 HTTP 层） |
| 免写 Dockerfile | ✅（默认 buildpack）[5] | ❌ | ❌ | ❌（裸进程） |
| 底座 | Docker（被藏起来）[2] | Docker 本尊 | 无 daemon | Node 常驻 God daemon |
| 数据服务 | 插件一条命令（官方 28 个）[6] | 手写 compose 服务段 | 手写 quadlet | 不适用 |

与同赛道微型 PaaS（横评，2026-10 检索 [10][12]）：**CapRover**（Web UI + 一键应用 + 内置集群）、**Coolify/Dokploy**（GUI 派新贵）、**Kamal**（无常驻控制面的部署工具，非完整 PaaS）。dokku 的差异化＝纯 CLI + 插件生态 + 单机最小 footprint。逐维度宽表见类别索引与 `_meta.json` columns。

## 风险与注意

- **单维护者依赖（最大结构性风险）**：josegonzalez 一人 9,759 commits，第二名 michaelshobbs 603（gh 2026-10-02 采集，35 倍差距）[1]——项目实质 Bus Factor ≈ 1。缓解因素：13 年历史、发布极密、MIT 许可（最坏情况可 fork）、有商业版 Dokku Pro 持续输血 [2][10]；但任何「关键插件长期靠一个人响应」的预期都要有心理准备。
- **升级须读迁移指南**：每代大版本（0.x 每 +1）都有 migration guide [7]；同时升级 docker/herokuish 时官方建议先 `dokku ps:stop --all` 再重建（有请求打到错误容器的已知风险）[7]。0.x 版本号 13 年未到 1.0， breaking change 的预期要保留。
- **支持系统面窄**：仅 Ubuntu 22.04/24.04/26.04 或 Debian 11+ [3]——Arch/RHEL 系没有官方安装路径。
- **构建在本机跑**：buildpack 编译消耗 VPS 自身内存/CPU，小内存机器需用官方 resource-management 对 build 过程限流，或外推到 CI [11]（待验证：CI 外推的具体插件方案未深入核实）。
- **社区插件衰减**：约 155 个插件中 19 个无人维护、55 个已弃用 [6]——选社区插件前先查维护状态。

## 来源

1. dokku/dokku — https://github.com/dokku/dokku（gh 2026-10-02 采集：⭐32,157、push 2026-10-01、MIT、open issues 30、v0.38.31 2026-09-27、30 release/4.5 个月、contributors josegonzalez 9,759 vs michaelshobbs 603；原始响应留档 raw/2026-10-02/gh/dokku_dokku.json、dokku-releases.json、dokku-contributors.json）
2. Dokku 官网首页 — https://dokku.com/（访问 2026-10-02；留档 raw/2026-10-02/web/dokku-dokku.com-home.md）
3. Installation 官方文档 — https://dokku.com/docs/getting-started/installation/（访问 2026-10-02；留档 raw/2026-10-02/web/dokku-dokku.com-installation.md）
4. Advanced Installation 官方文档 — https://dokku.com/docs/getting-started/advanced-installation/（访问 2026-10-02；留档 raw/2026-10-02/web/dokku-dokku.com-advanced-installation.md）
5. Herokuish Buildpacks 官方文档 — https://dokku.com/docs/deployment/builders/herokuish-buildpacks/（访问 2026-10-02；留档 raw/2026-10-02/web/dokku-dokku.com-herokuish-buildpacks.md）
6. 插件生态官方页 — https://dokku.com/docs/community/plugins/（访问 2026-10-02；留档 raw/2026-10-02/web/dokku-dokku.com-plugins.md）
7. Upgrading 官方文档 — https://dokku.com/docs/getting-started/upgrading/（经 gh api 读仓库 docs/getting-started/upgrading/index.md，访问 2026-10-02；留档 raw/2026-10-02/web/dokku-dokku.com-upgrading.md）
8. Proxy Management 官方文档 — https://dokku.com/docs/networking/proxy-management/（经 gh api 读仓库 docs/networking/proxy-management.md，访问 2026-10-02；留档 raw/2026-10-02/web/dokku-dokku.com-proxy-management.md）
9. dokku/dokku-letsencrypt — https://github.com/dokku/dokku-letsencrypt（gh 2026-10-02 采集：⭐1,119、push 2026-09-28）
10. WZ-IT: Self-hosted PaaS compared 2026 — https://wz-it.com/en/blog/self-hosted-paas-comparison-coolify-dokploy-caprover（访问 2026-10-02；2026-08-23 观测快照；注意：作者运营 Coolify 托管服务，利益相关声明见文内；留档见 raw/2026-10-02/web/dokku-websearch-paas-comparison.md 引文）
11. WebSearch: dokku 内存/低内存 VPS 实测与官方口径汇总 — https://dokku.com/docs/getting-started/advanced-installation、https://aaron.com.es/blog/dokku-performance-issues-vps（检索 2026-10-02；留档 raw/2026-10-02/web/dokku-websearch-memory.md）
12. WebSearch: dokku vs caprover vs coolify vs kamal 横评 — https://kanopylabs.com/blog/coolify-vs-dokku-vs-caprover 等（检索 2026-10-02；留档 raw/2026-10-02/web/dokku-websearch-paas-comparison.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（gh 一手数据 + 官方文档当日核实；类内 docker=adopt 为基线，dokku 作为其上的体验增强层定 trial——Bus Factor≈1 与 1GB 硬门槛两点未消化前不升 adopt） |
