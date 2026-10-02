# Kamal

> **TL;DR**：容器化小应用的声明式部署甜点：一条 `kamal deploy` 在任意 VPS 上实现零停机部署 + 单机多应用，控制面仅 kamal-proxy ~14MB 内存——但 Docker 是硬前提（不用管、没绕开），适用域是已容器化或愿容器化、要零停机与多应用复用一台 VPS 的个人/小团队。

- **结论**：trial（适用域：**有 Docker 心智、几台到十几台 VPS 上跑几个到十几个容器化应用**；无 Docker 意愿或想完全零心智 → 走托管平台，见对比）
- **核实日期**：2026-10-02（gh 一手数据 + 官网/37signals 官方博客/三方对比当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本线 | v1.0.0（2023-09-19）→ v2.0（2024-09-26 公告，Rails 8 起默认内置）→ 当前 **v2.12.0（2026-06-18）**；截至 2026-10-02 **无 Kamal 3**；2.x 约每季度一个 minor（2.7→2.12，2025-06 至 2026-06）；v1 线到 2025-06-25 还有补丁（v1.9.3） | [1][3] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/basecamp/kamal（homepage: https://kamal-deploy.org） | [1][2] |
| 维护活跃度 | ⭐14,625、push 2026-09-30、fork 754、open issues 153（gh 2026-10-02 采集）；生产背书：37signals 用它在自己硬件上跑 HEY，HEY 部署已在 Kamal 2 上 | [1][2][3] |
| 部署目标形态 | 任意可容器化 web app：官网原文 "Originally built for Rails apps, Kamal will work with any type of web app that can be containerized"；Kamal 2 公告原文 "web apps written in any language or framework" | [2][3] |

## 为什么选（轻量化轴上的四条论断）

1. **控制面极轻，资源占用有实测数**：Kamal 2 用自研 kamal-proxy（Go 单二进制，官方定位 "a tiny HTTP proxy"）替代 Traefik [3][8]。三方基准（Kamal v2.2.0，Ubuntu 24.04，2026）：kamal-proxy 空闲 **14.2MB 内存 / 0.1–0.3% CPU**；对照组 Coolify 空闲 885.6MB（7 容器）、1.8–4.2% CPU；1GB RAM 的 $4/mo VPS 即可跑 Kamal（剩 ~980MB 给应用）[5]。应用容器另算（小 Rails 应用 ~150–300MB/容器，kamal-proxy discussion #222，2026-10-02 检索）[9]。
2. **一条命令 + 声明式配置，零停机开箱即得**：`config/deploy.yml` 声明服务器列表、镜像、环境，之后 "a simple `kamal deploy` is all it takes"；vanilla Ubuntu + SSH key 即可，Docker 自动装（"auto-provisioned with Docker…just basic Docker commands being called"）；零停机（gapless）、回滚复用旧镜像、单机多应用按 hostname 路由、Let's Encrypt 自动 HTTPS、维护模式，全是 proxy 内建 [2][3][6]。
3. **规模弹性覆盖个人/小团队全谱**：Kamal 2 设计目标即 "50 servers or deploying 5 apps to a single server" 双向适用；accessories 机制把 Redis/DB/队列作为旁挂容器声明管理 [3][6]。37signals 的 ONCE（2026-04）直接复用 kamal-proxy 做单机多应用 console，侧面印证 proxy 组件的独立与轻量 [4]。
4. **37signals 全线生产使用 + 活跃维护**：HEY 跑在 Kamal 2 上 [3]，官网列 Basecamp/HEY/Fizzy/ONCE 均用其部署 [2]；仓库 2023-01 创建，2026-09-30 仍有 push，发行节奏稳定 [1]。

## 对比（轻量化横轴的关键差异；类别级并排见 `../comparison.md`）

| 对手 | 与 Kamal 的差异 |
|---|---|
| 裸进程 / systemd | 不需要 Docker、控制面为零；但零停机切换、回滚、多应用反向代理、HTTPS 全要手搓——Kamal 用「装个 Docker」换走这些 [3][6] |
| docker compose 手工 | 同为容器，但构建/传镜像/registry/零停机切换/多机全手工；Kamal 把这些收敛成声明式一条命令 [2][6] |
| Coolify 等微型 PaaS | Coolify 有 Web UI 与一键应用商店，但控制面空闲 885MB+ 且官方建议 8–16GB 机器；Kamal 无常驻 UI、控制面 14MB，1GB VPS 可用——代价是没有图形面板 [5] |
| 托管平台（Heroku/Render/Fly.io） | 零运维心智、免容器化、有 autoscaling [6]；月费高且数据在他家。Kamal 不支持 autoscaling、不 provision 服务器、本地构建 [6]。官方自己也警告：若 Linux/Docker 仍觉困难，"You're probably still better off with a fully managed service" [2] |
| ONCE（37signals 同门） | ONCE 是复用 kamal-proxy 的单机 console，面向非程序员装公开应用；Kamal 是给开发者部署自己私有应用的完整工具，两者定位官方原话即已二分 [4] |

## 风险与注意

- **Docker 硬依赖——「不用管 Docker 但没绕开」**：Kamal 的省心建立在容器之上：服务器自动装 Docker（curl 脚本进 root shell）、应用必须打成镜像、需要容器 registry（Docker Hub 免费层仅 1 个私有仓库）[2][6]。不支持 Podman 等替代引擎（issue #61，2026-04 讨论仍在）[7]。不想容器化 = 此路不通。
- **本地构建**：镜像默认在本地 Docker 构建（需本地 Docker 环境 + registry 往返）；无 CI 远程构建流水线时大镜像部署慢 [6]。remote builds 有开关，但构建链心智仍在。
- **无 autoscaling / 无监控内建**：不配负载均衡器、不自动扩缩；观察性靠接第三方（judoscale 等）[6]。
- **文档缺口与边角（2026-04 批评帖）**：缺完整 deploy.yml 示例、部署取 git HEAD 而非工作区文件、secrets 注入在子 shell 失败时可能静默为空、net-ssh 纯 Ruby 加密实现的安全质疑——该帖作者结论 "not ready for production use yet" 属一家之言（HEY 大规模生产在用），但可见线程内无维护者回应，边角问题真实存在 [7]。
- **社区重心在 Rails**：语言无关有三方实证（Python/Django 教程、Reddit 自托管群体、非 Rails 部署剧集）[9]，但主流文档、教程与生态心智仍是 Rails/Ruby 视角，非 Ruby 用户遇到问题时社区参照系偏 Rails [9]。

## 来源

1. basecamp/kamal — https://github.com/basecamp/kamal（gh 2026-10-02 采集：⭐14,625、push 2026-09-30、MIT、created 2023-01-07；releases：v1.0.0 2023-09-19、v1.9.3 2025-06-25、v2.12.0 2026-06-18 等；原始响应留档 raw/2026-10-02/gh/basecamp_kamal.json、basecamp_kamal_releases.json）
2. Kamal 官网 — https://kamal-deploy.org（访问 2026-10-02；留档 raw/2026-10-02/web/kamal-kamal-deploy.org.md）
3. 37signals Dev：Kamal 2.0 发布公告（2024-09-26）— https://dev.37signals.com/kamal-2（访问 2026-10-02；留档 raw/2026-10-02/web/kamal-dev.37signals.com.md）
4. 37signals Dev：The ONCE app server（2026-04-17）— https://dev.37signals.com/once-app-server（访问 2026-10-02；留档 raw/2026-10-02/web/kamal-once-app-server.md）
5. ECN Apps：Kamal 2 vs Coolify（2026）— https://ecn-apps.com/pages/articles/kamal-vs-coolify-2026.html（访问 2026-10-02；基准环境 Kamal v2.2.0 + Coolify v4.0.0-beta.380+ / Ubuntu 24.04；留档 raw/2026-10-02/web/kamal-ecn-apps.com.md）
6. Judoscale：Kamal vs PaaS — https://judoscale.com/blog/kamal-vs-paas（访问 2026-10-02；留档 raw/2026-10-02/web/kamal-judoscale.com.md）
7. GitHub discussion #1823：I am recommending against Kamal right now（2026-04-10）— https://github.com/basecamp/kamal/discussions/1823（访问 2026-10-02；留档 raw/2026-10-02/web/kamal-github.com-discussion1823.md）
8. basecamp/kamal-proxy — https://github.com/basecamp/kamal-proxy（gh 2026-10-02 采集：Go、MIT、⭐1,110、push 2026-10-02；官方定位 "tiny HTTP proxy"）
9. WebSearch 检索记录（2026-10-02）：语言无关采纳度（Reddit r/django、r/selfhosted、Drifting Ruby Python 集、BigMike）+ kamal-proxy discussion #222 应用容器内存；留档 raw/2026-10-02/web/kamal-websearch-multi.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（gh 一手数据 + 官方博客/三方对比当日核实） |
