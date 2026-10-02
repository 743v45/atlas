# Fly.io

> **TL;DR**：「真机器手感」托管平台的代表：Firecracker 微 VM 按秒计费（最小 256MB ≈ $2.23/月，2026-10 查），fly.toml + fly deploy 免服务器运维、Anycast 多区分布与自动 HTTPS 开箱即用；但 2024-10 起新用户免费额度取消、2024 Q4 连环重大故障、2026-07 公司整体转向 AI agent——个人非关键路径服务值得试用，关键服务慎押。

- **结论**：trial（适用域：个人/小团队的**非关键路径**服务——要「自己的机器感」而非 PaaS 沙箱、想白捡全球分布、按量付费可接受；不适用域：关键业务重押、流量型服务的成本敏感场景、想要零平台绑定的人）
- **核实日期**：2026-10-02（官方定价/架构/公告页当日抓取；故障史与社区口碑当日检索）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 商业闭源托管平台；`flyctl` CLI 开源（superfly/flyctl） | [1][8] |
| 计算底座 | Firecracker microVM（Fly Machines），硬件虚拟化，启动 ~300ms | [2][5] |
| 网络入口 | Anycast IPv4/IPv6 全域广播、流量就近落地 microVM；数据中心间 WireGuard 隧道回程 | [2] |
| 计费 | Pay As You Go：按秒计费、无月费承诺、无预付；新用户无免费额度（2024-10-07 起） | [1][3] |
| 规模口径 | 37,000+ 客户（2026-07 官方公告口径，其中 8,000+ agent-native） | [4] |
| 公司动向 | 2026-07-24 官宣转向「Computers for Agents」，新 CEO Scott Johnston（前 Docker CEO），$25M Series D | [4][7] |

## 为什么选（轻量部署视角）

1. **资源心智最轻的一档**：装 `flyctl` → `fly launch`（生成 `fly.toml`）→ 之后每次 `fly deploy`，全程不碰服务器 [8]。构建既可以吃本地 Docker daemon，也可以 `--remote-only` 甩给远程 builder，或 `--image` 直接推现成 OCI 镜像——本地机器可以完全不参与构建 [8]。
2. **「真机器」手感**：跑的是硬件虚拟化 microVM 而非受限沙箱，有持久磁盘（Volume）、能跑任意语言/任意 Dockerfile；官方定位就是「给应用一台真计算机」[2][4]。
3. **成本对个人小服务极友好**：最小机型 shared-cpu-1x/256MB ≈ **$2.23/月**（2026-10-02 查，iad 无区域加价；按区域系数线性折算，东京 ≈ $2.9/月，圣保罗 ≈ $3.6/月）；停机只收 rootfs 存储费（每 GB 停 30 天 $0.15）——挂着的闲置服务也能很便宜 [1]。
4. **全球分布白送**：Anycast 就近路由 + 多区域部署 + 自动 TLS；每应用送共享 IPv4 + 无限 Anycast IPv6，前 10 个单主机名证书免费，入站流量全免费 [1][2]。
5. **秒级弹性**：Machines API 约 300ms 启动，代理可按请求拉起机器、空闲关停（auto-stop/start），流量极小的服务可以只付「有请求的时间」[5]。

## 为什么不选 / 谨慎（同样真实）

1. **公司战略重心已离开你这类客户（2026 最大变量）**：2026-07-24 官宣整体转向「Computers for Agents」（为 AI 编码 agent 提供计算），融资叙事、官网首页、新 CEO 全部押注 agent 负载；**GPU 产品 2026-07-31 全面弃用**是首个收缩实锤。官方称核心 Machines 平台用户「many, many」不会关——而新 agent 业务恰好也跑在同一套 Machines 上，这是平台存续的最强保证，但传统 web 托管客户从此是第二叙事，社区已有迁移与信任讨论 [4][7]。
2. **可靠性记录平平**：2024-10-22 全网编排故障（Consul root key 签名密钥过期，官方称「记录在案的最长重大故障」）、2024-11-25 全球故障（交换机饱和）、2025-02 Tigris 存储故障（约一周）；第三方监控 121 天实测 94.41% uptime、约 13 起事件/月（2026-10 检索口径）。透明度高（infra log 全量公开）救不了可用率 [6][10]。
3. **新用户免费额度已死**：2024-10-07 起 legacy free allowances（3 台 256MB + 3GB 存储）不再发给新用户，只剩短期试用；「白嫖」时代结束，同价位自托管 VPS 的控制权优势凸显 [3]。
4. **定价复杂度口碑差**：区域加价 1.0–1.615 × 机型 × 出站流量分区（北美 $0.02/GB 至非洲 $0.12/GB）× 卷/快照/IP 附加费；HN/Reddit 有意外账单案例（多来自流量型/多机型业务，个人低流量服务月账单通常稳定在 $2–5）[1][9]。且定价仍在持续变动：2026-01-01 起新增快照存储收费 [1]。
5. **平台绑定中度**：部署产物是标准 OCI 镜像（可搬走），但 fly.toml、Anycast 网络、Machines API、远程构建、Volume 都是平台专属；迁出成本 ≈ 换一家托管平台重新接线 [8]。

## 对比

同类别八条路线的逐维度对比见 `../comparison.md`（如存在）。Fly.io 在坐标系里的位置：

| 对比对象 | 关键差异 |
|---|---|
| Docker/Podman + 自有 VPS | 同价位（$2–5/月 VPS）但控制权完整、无绑定；代价是自己管服务器、自己搞证书/网络/备份，无全球分布 |
| Kamal（VPS 编排工具） | 同样容器化、同样 fly.toml 式声明，但落在自己的 VPS 上——「省心」程度低一档、绑定也低一档 |
| Heroku 类 PaaS | Fly 给的是完整 microVM（有磁盘、任意进程），不是 dyno 沙箱；计费粒度更细（按秒）但账单心智更重 |
| 裸 systemd/pm2 | 零平台费、零绑定，但运维门槛高数档——Fly 的存在意义就是替你省掉这些 |

## 风险与注意

- **平台优先级风险（本条目最大风险）**：pivot + GPU 弃用先例俱在；持续观察信号 = Machines 平台的定价与产品动向、agent 收入占比变化 [4][7]。
- **可靠性**：只放非关键路径；需要多副本时记住 2024 Q4 那两次是**平台级**故障，多区域救不了 [6]。
- **账单护栏**：出站流量按区计费（亚太 $0.04/GB、非洲 $0.12/GB，2026-10 查），流量型服务先算这笔账；快照 2026-01 起计费，默认每日自动快照开着——不想要要手动关 [1][9]。
- **fly.toml 重置坑**：`fly deploy` 会把手动改过的机器配置拉回 fly.toml 所声明状态——改配置要改文件而不是只改线上 [8]。
- 文档与现实漂移：部分官方页面仍引用 free tier 字样，新组织实际没有——以账单为准 [3]。

## 来源

1. Fly.io 官方定价文档 — https://docs.fly.io/about/pricing（访问 2026-10-02；费率/区域系数/流量分区/快照收费全文留档 raw/2026-10-02/web/flyio-docs.fly.io.md）
2. Fly.io 官方架构文档 — https://docs.fly.io/reference/architecture（访问 2026-10-02；Firecracker microVM/Anycast/WireGuard 原文留档 raw/2026-10-02/web/flyio-architecture-reference.md）
3. Fly.io Discontinued Plans 与免费额度变动 — https://fly.io/docs/about/discontinued-plans、https://community.fly.io/t/free-tier-is-dead/20651（检索 2026-10-02；留档 raw/2026-10-02/web/flyio-web-search-result.md）
4. Fly.io 官方公告「Computers for Agents」 — https://fly.io/news/fly-io-launches-computers-for-agents（访问 2026-10-02；$25M Series D/新 CEO/37,000 客户口径全文留档 raw/2026-10-02/web/flyio-fly-io-news.md）
5. Fly Machines 产品页与博客（~300ms 启动、按需拉起/空闲关停） — https://fly.io/machines、https://fly.io/blog/fly-machines（检索 2026-10-02；留档 raw/2026-10-02/web/flyio-fly-io-architecture.md）
6. Fly.io 故障史（infra-log 及 postmortem） — https://fly.io/infra-log、https://fly.io/infra-log/2024-10-26、https://community.fly.io/t/psa-postmortem-for-the-nov-25-outage/22933、https://fly.io/infra-log/2025-02-22（检索 2026-10-02；时间线留档 raw/2026-10-02/web/flyio-outage-history.md）
7. 公司转向报道与社区反应 — https://daily.dev/posts/fly-io-pivots-to-ephemeral-cloud-computers-for-ai-agents-names-new-ceo-v9mpmy2bi、https://community.fly.io/t/gpu-migration-fly-io-gpus-will-be-deprecated-as-of-july-31-2026/27110、https://community.fly.io/t/will-the-apps-and-machine-platform-start-winding-down/28380/7、https://elixirforum.com/t/now-that-fly-are-pivoting-should-i-trust-them-for-hosting/76144（检索 2026-10-02；留档 raw/2026-10-02/web/flyio-pivot-ai-agents.md）
8. 部署工作流（fly launch/deploy、本地与远程构建、fly.toml） — https://fly.io/django、https://hexdocs.pm/phoenix/1.6.4/fly.html、https://community.fly.io/t/build-images-with-nixpacks/6169（检索 2026-10-02；留档 raw/2026-10-02/web/flyio-deploy-workflow.md）
9. 定价复杂度口碑（Reddit r/selfhosted、r/elixir、HN） — https://www.reddit.com/r/selfhosted/comments/1pri1wo/、https://www.reddit.com/r/elixir/comments/1h8ajm2/、https://news.ycombinator.com/item?id=48688835（检索 2026-10-02；留档 raw/2026-10-02/web/flyio-pricing-criticism.md）
10. 第三方可用性监控口径 — https://www.pulsapi.com/services/fly-io/uptime（94.41%/121 天）、IsDown 统计约 609 起事件（检索 2026-10-02；留档 raw/2026-10-02/web/flyio-outage-history.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（定价/架构/官方公告当日抓取，故障史与社区口碑当日检索；全部原始数据留档 raw/2026-10-02/web/flyio-*.md） |
