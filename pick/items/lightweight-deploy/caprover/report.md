# CapRover

> **TL;DR**：微型 PaaS 老牌（2017 起）：Web 面板 + 360 个一键应用 + 自动 HTTPS 把 Docker 藏在一键体验后面，空闲仅约 300-400MB RAM，2026 年维护明显回升（8 月连发 5 版、issue 当天关闭）——个人 VPS、简单单容器工作流值得用，但单维护者 bus factor=1，不设为无脑默认项。

- **结论**：trial（适用域：个人/小团队的单台 Linux VPS、以单容器部署为主、想要「面板 + 一键应用 + 自动 HTTPS」省心体验、不依赖 Docker Compose 编排的场景）
- **核实日期**：2026-10-02（gh 一手数据 + 官方文档 + 第三方对比文当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 当前版本 | v1.15.4（2026-08-30 发布） | [2] |
| 许可证 | Apache-2.0 + 附加条款 appendix（付费功能不可修改/不可再分发付费版；GitHub 识别为 NOASSERTION） | [1] |
| 定位 | "Scalable, Free and Self-hosted PaaS"（自动 Docker + Nginx） | [1][7] |
| 底层 | 必须有 Docker（≥25.x），自身以 `docker run caprover/caprover` 容器运行，反向代理 Nginx，编排 Docker Swarm | [4][6] |
| 维护活跃度 | ⭐15,177、push 2026-09-30、2026 年至 10 月初 237 commits（2025 全年仅 92）、open issues 178（gh 2026-10-02 采集） | [1][3] |

## 为什么值得用（trial 的四条论断）

1. **微型 PaaS = Docker 被藏起来，不是绕开**：安装即 `docker run -p 80:80 -p 443:443 -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock ... caprover/caprover` [4]，官方测试基线 Ubuntu 24.04 + Docker 25+ [4]；用户面对的是 Web 面板（端口/持久目录/环境变量/实例数）与 `caprover deploy` CLI，Let's Encrypt 自动签发续期 [7]。对「想省心但接受 Docker 存在」的人，心智负担远低于裸 Docker + 手配 Nginx。
2. **一键应用市场 360 个（2026-10-02 实测）**：WordPress、数据库、Nextcloud、n8n、Authentik 等 [8]；第三方评测称其「三者中最成熟，2017 年即发布，边缘情况被充分理解，社区已为常见问题记录解法」[6]。成熟度是老牌项目的真实壁垒。
3. **资源占用为同类最低档**：官方要求 1GB RAM 起步（512MB 警告构建期不够）[4]；2026-02 第三方实测空闲 RAM 约 300-400MB、空闲 CPU 1-2%、空闲容器 3-4 个——对照 Coolify 约 500-700MB、官方最低 2GB [6]。在 5 美元档 1GB VPS 上是现实可用的。
4. **2026 年维护回升，且应用可脱离 CapRover 存活**：2026 年 8 月单月连发 5 个 release（v1.15.0-1.15.4），全年 commits 237 已是 2025 年（92）的 2.5 倍 [2][3]；2026-09 的新 issue 多为当天～次日关闭（如 #2499 关闭耗时 2.5 小时）[9]。架构上应用本质是 Docker Swarm service，「可从 Swarm 安全移除而应用继续运行」[5]——工具停更的最坏情形下用户资产仍在，这是它区别于深度锁定型面板的降险性质。

## 为什么不设为默认 adopt（三条保留）

1. **bus factor = 1，结构性风险**：githubsaturn 一人 1,837 contributions，第二名 25（差 73 倍）；近期 30 个 commit 作者全部是他本人（gh 2026-10-02 统计）[3]。「开发放缓」的社区担忧自 2022 年就有（Discussion #1544），维护者立场一贯是「稳定优先、拒绝为 <5% 用户加功能」[5]——2026 年回升是单人节奏的回升，不是团队化。
2. **Docker Compose 支持有限**：2026-02 第三方评测称之为「2026 年该工具最显著的局限」[6]；底层押注 Docker Swarm 而非 Compose/K8s 主流生态，UI「功能可用但过时」[6]。Compose 文件写好的人迁入有摩擦。
3. **周边完整性一般**：数据库经一键模板部署被当作普通应用，备份需自行配 cron/脚本；API 有但文档与通知集成弱于新竞品 [6]；内置 Netdata 监控过时，社区提议换 Beszel（#2410，2026-07，暂无人接）[9]。

## 对比（同类微型 PaaS / 部署工具，详见类别横评）

| 维度 | CapRover | Dokku | Coolify |
|---|---|---|---|
| 底层 | Docker Swarm + Nginx [6] | git push 极简主义 | Traefik，多服务器管理而非集群 [6] |
| 资源占用 | 空闲 ~300-400MB，最低 1GB [4][6] | 更轻（无面板） | 空闲 ~500-700MB，最低 2GB [6] |
| 一键应用 | 360 个 [8] | 少 | 插件市场式 |
| 成熟度 | 2017 年起，9 年 [1] | 2013 年起 | 2022 年起 [6] |
| 核心短板 | bus factor=1、Compose 有限 [3][6] | 无 Web 面板、插件碎片 | 年轻、资源重 |

选型直觉：要「面板 + 一键 + 集群可扩展」且资源紧张 → CapRover；要极简 git push 无面板 → Dokku；要新潮 UI + Compose 原生且资源宽裕 → Coolify。

## 风险与注意

- **单维护者风险是结构性的**：无法靠「等它恢复活跃」化解；上生产前评估逃生路径（应用是 Swarm service 可直接 `docker service` 接管，数据卷自备份）[3][5]。
- **面板安全暴露面**：安装需开放 80/443/3000 端口 [4]，且容器挂载 `/var/run/docker.sock` [4]——面板被攻破等同宿主机 root；务必强密码 + 防火墙限制 3000 端口来源，付费版 CapRover PRO 有 IP 白名单等企业功能（免费版无）[9]。
- **release tag 命名有笔误先例**（v1.14.1 的 tag 实为 `v.14.1`）[2]，脚本化升级时按 release 列表而非 tag 规律处理。
- **许可证不是纯 Apache-2.0**：LICENSE 附 appendix——付费功能不可修改/不可再分发、免费功能修改须开源分发，冲突时 appendix 优先 [1]。自用不受影响，二次分发改造版需注意。
- 待验证：2FA 在免费版的落地状态（2022-2023 维护者承诺「未来几个月」[5]，现状未核实）。

## 来源

1. caprover/caprover 仓库元数据与 LICENSE — https://github.com/caprover/caprover（gh 2026-10-02 采集：⭐15,177、push 2026-09-30、open issues 178；原始响应留档 raw/2026-10-02/gh/caprover_repo.json 与 caprover-gh-metrics.md）
2. caprover/caprover releases — https://github.com/caprover/caprover/releases（gh 2026-10-02 采集：v1.15.4 @ 2026-08-30 及近 10 版节奏；留档 raw/2026-10-02/gh/caprover_releases.json）
3. commits 年度分布与贡献者集中度 — https://github.com/caprover/caprover（gh 2026-10-02 采集：2025 年 92 / 2026 年 237 commits；githubsaturn 1,837 vs 第二名 25；留档 raw/2026-10-02/gh/caprover-gh-metrics.md）
4. CapRover 官方入门文档（服务器要求） — https://caprover.com/docs/get-started（访问 2026-10-02：1GB RAM 起步、Ubuntu 24.04 + Docker 25+、端口 80/443/3000、docker run 安装命令；留档 raw/2026-10-02/web/caprover-caprover.com.md）
5. Discussion #1544「Stale Development」 — https://github.com/CapRover/CapRover/discussions/1544（访问 2026-10-02：2022 年维护放缓讨论与维护者「稳定优先」立场、应用可脱离 Swarm 运行；留档 raw/2026-10-02/web/caprover-github-discussion-1544.md）
6. MassiveGRID「Dokploy vs Coolify vs CapRover」 — https://www.massivegrid.com/blog/dokploy-vs-coolify-vs-caprover/（2026-02-27 发布，访问 2026-10-02：空闲资源实测、Compose 支持短板、三者底层对比；留档 raw/2026-10-02/web/caprover-massivegrid.com.md）
7. CapRover 官网首页 — https://caprover.com/（访问 2026-10-02：定位口号、面板/CLI/集群功能、OpenCollective 捐赠；留档 raw/2026-10-02/web/caprover-home-caprover.com.md）
8. caprover/one-click-apps — https://github.com/caprover/one-click-apps（gh 2026-10-02 采集：public/v4/apps/ 下 360 个应用、push 2026-09-29；留档 raw/2026-10-02/gh/caprover-gh-metrics.md）
9. issue 抽样与 CapRover PRO 检索 — https://github.com/caprover/caprover/issues（gh 2026-10-02 采集：2026-09 issue 响应时长、#2410 Netdata→Beszel 提议、"CapRover PRO" 命中 9 个 issue；留档 raw/2026-10-02/gh/caprover-gh-metrics.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（gh 一手数据 + 官方文档 + MassiveGRID 2026-02 对比当日核实） |
