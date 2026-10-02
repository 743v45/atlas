# Coolify

> **TL;DR**：微 PaaS/Web UI 派代表：面板托管一切（Git 推送部署、300+ 一键服务、多机编排），自托管免费无功能墙、停用后应用照跑——代价是 2GB 级资源底线与面板 root 级攻击面（52,890 暴露实例教训），适合要 PaaS 体验且能守暴露面纪律的个人/小团队。

- **结论**：trial（适用域：想要 Web UI 微 PaaS 体验（一键服务市场 / Git push 自动部署 / 多机面板）、接受 2GB 级资源底线与面板暴露面纪律（PrivateIP/VPN 访问）；单机资源极简派与纯声明式信仰者不适用）
- **核实日期**：2026-10-02（gh 一手数据 + 官方文档 + Wayback 历史快照当日采集）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v4.3.23（2026-09-18 发布；2026-10-02 快照） | [2] |
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/coollabsio/coolify（2021-01-25 创建） | [1] |
| 维护活跃度 | ⭐62,500、push 2026-10-02（当日实测）、forks 5,580、open issues 737（gh 2026-10-02 采集） | [1] |
| release 节奏 | 2025-04→2026-09 共 100 个 release（月均 ~5.6；2026-08 单月 16 个；2026-06/07 各仅 1 个，节奏不均但无断档） | [2] |
| 维护模式 | 自托管 Free Forever + Coolify Cloud 托管面板双轨（Cloud $5/月含 2 台服务器，+$3/月/台，年付 -20%；2026-09-20 定价页快照） | [8] |

## 为什么选（该形态内）

1. **微 PaaS 体验的天花板级开源实现**：Web UI 全托管——Git 推送自动部署、PR preview 环境、部署 webhook、镜像回滚；构建源覆盖 GitHub/GitLab/Bitbucket/Gitea，构建方式覆盖 Nixpacks/Railpack/Dockerfile/Docker Compose/预构建镜像；300+ one-click 服务带持久化存储与自动生成凭据 [4]。全类目 star 增速最快：36,408（2025-01）→ 49,193（2026-01）→ 62,500（2026-10-02），2026 年月均增速较 2025 年提速约 39%，仍在加速 [1][5]。
2. **Apache-2.0 + 无功能墙 + 退出无害**：开源版「no feature behind the paywall」（官方哲学声明），全部功能免费；配置留在用户服务器上，停用 Coolify 后正在运行的应用不受影响、仍可管理——PaaS 类产品里少见的低锁定声明 [4]。商业模式靠 Cloud 托管面板（$5/月起）+ 赞助商，不靠开源版设卡 [8]。
3. **多机编排开箱即用**：面板可添加任意 SSH 可达的远程 VPS（官方推荐架构 = 1 台面板机 + N 台应用机），API/CLI/MCP/团队 RBAC 齐全；Cloud 版连接服务器台数不限 [4][8]。
4. **微型 PaaS = 藏 Docker 而非绕开**：一键安装脚本装的就是 Docker Engine 26+，Coolify 自身也是一组 docker compose 容器（含 PostgreSQL/Redis/SOKATE 等依赖）跑在宿主机上 [3]。对用户而言 Docker 被面板抽象掉了（点按钮即得容器），但故障排查时仍需 Docker 知识兜底——这是该形态的本质属性，横评时与其他路线的根本差异所在 [3]。

## 对比（同类目其他路线）

- 与 **裸 Docker/docker compose**（基线）：coolify 把 compose 手写、镜像构建、HTTPS 证书、域名反代、备份全部 GUI 化，代价是面板本体 + 官方最低 2 Core/2GB RAM/30+ GB 存储的资源底线与一个 root 级常驻攻击面 [3][7]；裸 compose 反过来，零面板开销但一切手写。
- 与 **Kamal**（声明式/CLI 派）：Kamal 无 Web UI、以 YAML + CLI 提交部署心智，资源占用远低于 coolify（无常驻面板服务）；coolify 换来一键服务市场与 PR preview 等 PaaS 便利。两者是「面板省心」与「声明式可控」的路线之争，不是优劣关系。
- 与 **systemd 裸进程 / pm2**：后两者资源占用极低、无容器化隔离；coolify 提供容器隔离与完整应用生命周期，但 2GB 底线在小 VPS 上是硬门槛（官方还提示构建期内存挤占可能拖垮同机面板，建议加 swap）[3]。
- 逐维度对比见 `../comparison.md`（如存在）。

## 风险与注意

- **面板 = root 级攻击面（最大风险，有实测教训）**：Coolify 面板持有全部被管服务器的 SSH root 凭据。2026-01 官方一次披露 11 个 critical 漏洞（CVE-2025-66209~66213 多数 CVSS 10.0、CVE-2025-64419/64420/64424、CVE-2025-59156~59158），含 root 命令执行与 root SSH 私钥泄露；Censys 同期实测 **52,890 个实例直接暴露公网**（德国 ~15,000、美国 ~9,800、法国 ~8,000）[6][7]。官方安装文档自己建议用 PrivateIP/VPN 访问面板 [3]——采用本方案等于接受「面板绝不裸奔公网」的运维纪律。2025-01 还有 CVE-2025-22605/22606（认证命令注入 RCE，beta.253 修复）；阿联酋网络安全委员会 2025-01-29 发 Alert 88 警告勒索软件风险，比利时 CCB 2026-01 同类警告 [7]。
- **「批量删除+勒索」传闻未证实**：调研未找到「攻击者批量删除 Coolify 实例并勒索」实际事件的任何可信报道——相关表述均为漏洞披露时的风险警告；用户侧零星被黑个案（挖矿）与升级自伤（连点更新按钮致 env 丢失，discussion #3687）存在 [7]。引用时勿夸大为既成事故。
- **两年两波 critical 批量披露 → 升级纪律必须严格**：2025-01 与 2026-01 两次批量披露说明面板代码的安全更新节奏快于一般基础设施软件；官方有自动更新通道（2025 年初曾对暴露实例强制推送），自托管应开启自动更新或至少每周跟进 [7]。
- **单维护者依赖**：前 100 名贡献者中创始人 andrasbacsai 一人 12,909 次提交，是第二名（peaklabs-dev，1,853）的约 7 倍——核心代码高度集中一人，bus factor 低是结构性风险 [9]。
- **release 节奏快且不均**：月均 5.6 个 release、2026-08 单月 16 个 vs 2026-06/07 各 1 个——追新有稳定性风险，滞后有安全风险，生产实例建议跟版本但不追当日最新 [2]。
- **资源口径**：官方最低 2 Core/2GB RAM/30+ GB 存储为面板+同机部署的底线；数据库类一键服务（Supabase/Appwrite 等）官方明示需要远超此线 [3]。「资源占用：高」的矩阵评级即据此（类目内相对 systemd/pm2 而言）。

## 来源

1. coollabsio/coolify — https://github.com/coollabsio/coolify（gh 2026-10-02 采集：⭐62,500、push 2026-10-02T15:21:45Z、Apache-2.0、forks 5,580、open issues 737、created 2021-01-25；原始响应留档 raw/2026-10-02/gh/coollabsio_coolify.json）
2. coollabsio/coolify releases — https://github.com/coollabsio/coolify/releases（gh 2026-10-02 采集：最新 v4.3.23 2026-09-18；2025-04-28→2026-09-18 共 100 个 release 的月度分布留档 raw/2026-10-02/gh/coollabsio_coolify_releases.json）
3. Coolify 官方安装文档 — https://coolify.io/docs/installation（访问 2026-10-02：最低 2 Core/2GB RAM/30+ GB、安装脚本装 Docker Engine 26+、手动安装即 docker compose up、PrivateIP 建议、构建期内存提示；留档 raw/2026-10-02/web/coolify-coolify.io-installation.md）
4. Coolify README — https://github.com/coollabsio/coolify（gh api 2026-10-02：功能清单、300+ one-click services、Git 推送部署/PR preview/回滚、多服务器管理、API/CLI/MCP/RBAC、双轨模式、退出无害与 no-paywall 声明；留档 raw/2026-10-02/gh/coollabsio_coolify_readme.md）
5. Wayback Machine star 序列 — web.archive.org 对 repo 页的 8 个快照（2025-01-18→2026-09-04：36,408→61,371）+ 当日 gh 62,500（访问 2026-10-02；留档 raw/2026-10-02/web/coolify-web.archive.org-star-history.md）
6. The Hacker News — https://thehackernews.com/2026/01/coolify-discloses-11-critical-flaws.html（2026-01-08 报道：11 个 critical 漏洞、多数 CVSS 10.0、Censys 52,890 暴露主机及分国别分布、beta.445/451/420.7 修复映射；访问 2026-10-02）
7. 安全事件调研汇总 — NVD CVE-2025-22605（https://nvd.nist.gov/vuln/detail/CVE-2025-22605 ）、UAE Cyber Security Council Alert 88（2025-01-29 PDF）、比利时 CCB 警告页（2026-01-07 更新）、Censys advisory（https://censys.com/advisory/cve-2025-64424-cve-2025-64420-cve-2025-64419 ）、Reddit r/selfhosted 被黑个案、GitHub discussion #3687（访问 2026-10-02；多轮检索汇总留档 raw/2026-10-02/web/coolify-websearch-security-incidents.md）
8. Coolify Cloud 定价页 — https://coolify.io/pricing（Wayback 2026-09-20 快照，访问 2026-10-02：自托管 Free Forever 无功能限制、Cloud $5/月含 2 台服务器 +$3/月/台年付 -20%、社区 20k+；留档 raw/2026-10-02/web/coolify-pricing-team.md）
9. 维护集中度 — gh api contributors（2026-10-02：andrasbacsai 12,909 次提交 vs 第二名 peaklabs-dev 1,853；留档 raw/2026-10-02/web/coolify-pricing-team.md §二）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（gh + 官方文档 + Wayback 历史快照当日采集；安全事件史经多源交叉核实，「批量删除勒索」传闻未证实故未采信为既成事故） |
