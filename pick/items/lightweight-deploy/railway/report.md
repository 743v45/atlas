# Railway

> **TL;DR**：全托管 PaaS 的体验标杆：GitHub push 自动构建部署、PR 自动开预览环境、模板一键拉起 Postgres/Redis，用户全程不碰服务器与容器细节，$5/月 Hobby 起步；但按量计费存在「超 $5 按全额收」的悬崖与社区公认的意外账单风险，2026 年事故记录偏多——不想运维的个人/小团队服务值得试用，账单敏感或求稳的服务须配硬限制并掂量。

- **结论**：trial（适用域：不想碰服务器的个人 side project 与小团队服务——要 PR 预览环境、要几分钟从 git 仓库到线上 URL 的体验；不适用：要可预测账单的常驻服务、要数据库备份/PITR 的有状态生产服务）
- **核实日期**：2026-10-02（官方 pricing/docs 六页 + Series B 公告当日核实；社区口碑与第三方横评同日检索）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 全托管 PaaS（底座是容器，用户不见容器/服务器） | [5][7] |
| 计划 | Trial $0（一次性 $5 额度 30 天）/ Free $0（含 $1/月）/ Hobby $5/月（含 $5 额度）/ Pro $20/月/工作区（席位不限，含 $20 额度）/ Enterprise 定制（2026-10-02 查） | [1][2] |
| 按量单价 | RAM $10/GB/月、vCPU $20/核/月、Volume $0.15/GB/月、egress $0.05/GB、构建免费；按秒计量，停止的服务不计费（2026-10-02 查） | [1][2] |
| 构建器 | Railpack 零配置默认（Nixpacks 已维护模式）；有 Dockerfile 则用 Dockerfile | [4][9] |
| 公司 | $100M Series B（2026-01-22），累计约 $124M，200 万用户 | [10][12] |
| 开源性 | 平台闭源；构建器 Nixpacks/Railpack 开源（MIT） | [9] |

## 为什么选（不想运维的前提下）

1. **部署心智最接近零**：连 GitHub 仓库后 push 即自动构建部署，Railpack 零配置从源码出镜像，无服务器、无 Dockerfile、无 CI 配置可写——「deploy 从 git push 到跑起来」全程无一步服务器操作 [4][5]。这是该类别（轻量部署）里唯一做到「零」的一档：VPS 系（dokku/caprover）最低也要装机器，Fly.io 仍暴露 machines/fly.toml，Railway 连这些概念都不出现。
2. **PR 预览环境是招牌能力**：开 PR 自动建临时环境、merge/close 自动销毁，且只部署受变更影响的服务（Focused PR Environments），官方明确支持 Dependabot/Claude Code 等机器人 PR——个人项目做 PR 工作流几乎没有对手 [6]。
3. **数据服务一键化**：PostgreSQL/MySQL/MongoDB/Redis 官方模板即点即部署，默认进项目私有网络，市场另有 ClickHouse/Dragonfly/Minio 等；服务间用 `${{service.URL}}` 变量引用连线 [7][8]。
4. **模板市场**：整套应用栈（服务+数据库）几小时点击部署，可发布自己的模板并获最高 25% 使用分成 [8]。
5. **存续风险显著缓解**：2026-01-22 宣布 $100M Series B（TQ Ventures 领投），自称 200 万用户、数万家公司客户——「小厂暴毙」风险较 2024 年代明显下降 [10][12]。

## 成本分析（2026-10-02 查，官方口径 [1][2]）

- **Hobby $5/月的实际覆盖**：含 $5/月使用额度。256MB RAM 常驻 ≈ $2.6/月、停机不计费——纯低流量小服务可压在 $5 订阅费内；但 **1GB RAM 常驻 + 半核忙 ≈ $20/月**（与社区实测帖一致 [12]），已超额度 3 倍。
- **「悬崖」条款**：Hobby 月末总用量 ≤ $5 则只收 $5；**一旦超过 $5，按总用量全额收费**（非 $5+超出部分）——小额超用会被放大成整月按量账单 [1]。
- **对策**：官方 Cost Control 支持软限制（75%/90%/100% 邮件提醒）+ 硬限制（最低 $10，触顶全部工作负载下线）；硬限制是官方明示的「possibly destructive action」[3]。

## 对比（同类托管平台）

| 维度 | Railway | Render | Fly.io | 自托管 VPS（dokku 等） |
|---|---|---|---|---|
| 计费模型 | 按量（含额度最低消费） | 订阅+每服务固定费（Pro $25/席、服务约 $7/月起） | 按量微 VM，无订阅门槛 | 固定（VPS 月租） |
| 账单可预测性 | 差（社区公认 "bill anxiety" [11][12]） | 好 [11] | 中 | 最好 |
| 抽象层级 | 容器全托管，不见机器 | 全托管 | Firecracker 微 VM，见 machines/fly.toml | 见整台机器 |
| PR 预览环境 | ✅ 自动 + Focused 部署 [6] | ✅ 有 | 需自建 | 需自建 |
| 数据库备份 | 无内置（仅 Volume ≠ 备份）[7] | 托管 Postgres 含备份/PITR [11] | 卷快照自理 | 自理 |
| 免费层 | Trial 一次性 $5/30 天 [1] | 真免费层（15 分钟休眠冷启动）[11] | 2024-10 起取消 | — |

- **vs Render**：Railway 赢在按量对突发/闲置流量更省、preview 环境更顺手；Render 赢在账单可预测、托管数据库有备份体系——第三方横评的结论分野即「突发流量选 Railway，稳定生产选 Render」（竞品撰文，注意立场 [11]）。
- **vs Fly.io**：同为按量托管，Fly 用微 VM 给更多控制权（区域、machine 配置）且无订阅下限；Railway 抽象更彻底、模板/预览环境体验更顺——「PaaS 沙箱 vs 微型 VM」的取舍。
- 类别内横评见 `../comparison.md`。

## 风险与注意

- **意外账单是头号社区风险**：闲置服务 RAM 常驻照计费（r/n8n 实测闲置 $16/月）、超 $5 全额收条款、支持仅工单无电话——2025–2026 社区口碑一致指向「必须主动设 limit」[1][3][12]。
- **可靠性记录偏多**：第三方（竞品）引 StatusGator 截至 2026-06 逾 1,134 起事故，列举 2026 年滥用误杀（约 3% 服务被终止）、CDN 鉴权响应缓存泄漏、GCP 账号暂停致停机约 8 小时——立场有偏但事件可查证，Railway 均发了复盘 [11]。
- **数据库无备份机制**：官方数据库文档只讲 Volume 持久化，无任何备份/恢复流程——有状态生产数据需自导出或改用其他托管数据库 [7]。
- **平台绑定**：应用代码是容器可迁移，但变量引用、私有网络、TCP Proxy、preview 环境这些拓扑资产不可搬 [7]。
- **默认不优雅退出**：新部署上线后旧部署默认 0 秒即 SIGKILL，长请求服务需自行配置 drain 时间 [5]。
- **免费层形同试用**：Trial 一次性 $5 限 30 天、Free 每月 $1 额度；2026-03-30 起不再支持预付卡 [1][2]。
- 待验证：Free 计划「高峰时段（8AM–8PM）拒收部署」仅见于第三方对比文，官方 plans 页未载 [11]。

## 来源

1. Railway 官方定价页 — https://railway.com/pricing（访问 2026-10-02；原始抓取留档 raw/2026-10-02/web/railway-railway.com.md）
2. Railway Docs: Pricing Plans — https://docs.railway.com/reference/pricing/plans（访问 2026-10-02；留档同上）
3. Railway Docs: Cost Control — https://docs.railway.com/pricing/cost-control（访问 2026-10-02；留档 raw/2026-10-02/web/railway-docs.railway.com.md）
4. Railway Docs: Build Configuration — https://docs.railway.com/guides/build-configuration（访问 2026-10-02；留档同上）
5. Railway Docs: Deployments — https://docs.railway.com/reference/deployments（访问 2026-10-02；留档同上）
6. Railway Docs: Environments — https://docs.railway.com/guides/environments（访问 2026-10-02；留档同上）
7. Railway Docs: Databases — https://docs.railway.com/reference/databases（访问 2026-10-02；留档同上）
8. Railway Docs: Templates — https://docs.railway.com/reference/templates（访问 2026-10-02；留档同上）
9. Nixpacks 官网（维护模式声明）— https://nixpacks.com + gh railwayapp/nixpacks、railwayapp/railpack（gh 2026-10-02 采集：⭐3,554 / ⭐1,215、均 MIT；留档 raw/2026-10-02/web/railway-nixpacks.com.md 与 railway-gh-*.json）
10. Railway Blog: Series B — https://blog.railway.com/p/series-b（2026-01-22 发布，访问 2026-10-02；留档 raw/2026-10-02/web/railway-blog.railway.com.md）
11. selfhost.dev: Railway vs Render 2026（第三方竞品横评，立场已标注）— https://selfhost.dev/blog/railway-vs-render-pricing-2026-verdict（访问 2026-10-02；留档 raw/2026-10-02/web/railway-selfhost.dev.md）
12. WebSearch 社区口碑与融资报道（reddit r/n8n、r/SaaS、r/node、r/webdev 2025–2026 帖；FinSMEs/VentureBeat 融资报道）— 检索 2026-10-02；留档 raw/2026-10-02/web/railway-websearch-reputation.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（官方 pricing/docs 六页 + Series B 公告当日核实；raw/2026-10-02/ 共 8 份留档） |
