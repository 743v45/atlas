# Render

> **TL;DR**：托管 PaaS 中「免费起步+零运维」的默认解：git push 即部署、零停机、托管 Postgres/Redis/Cron 全家桶，Heroku 退场后承接定位明确；代价是免费层三重限制（15 分钟休眠约 1 分钟冷启动、免费 Postgres 30 天过期、2026-04 起 Hobby 带宽仅 5GB/月）与低价层政策突变史——适用 side project 与原型免费起步，长期生产托付前先核算成本与锁定。

- **结论**：trial 试用（适用域：个人 side project / 原型 / 内部小工具的零运维起步；不适用：延迟敏感的免费层对外服务、无预算审查的长期生产托付）
- **核实日期**：2026-10-02（官方 pricing/docs/changelog + CNBC 当日全量核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 全托管 PaaS（"The Zero DevOps cloud"；计算跑在 Render 管理的 AWS/GCP 容器上，用户不感知底座） | [1][4] |
| 公司 | Render（2018 年创立，旧金山，约 100 人；CEO Anurag Goel 为 Stripe 第 8 号员工） | [4] |
| 免费层 | 750 实例小时/月/workspace + 静态站永久免费 + 免费 Postgres(1GB)/Key Value(25MB)（2026-10-02 核实仍存在） | [1][2] |
| 起步价 | Starter 实例 0.5 CPU/512MB **$7/月**；1 CPU/2GB $25/月（2026-10-02 查，compute 按秒 prorated） | [1] |
| 工作区订阅 | Hobby 免费 / Pro $25 月 / Scale $499 月（2026-04-23 起的新结构） | [1][3] |
| 许可 | 商业闭源托管服务（无 GitHub 主仓，stats 不适用） | [1] |
| 合规 | SOC 2 Type II、ISO 27001；HIPAA 需 Pro/Scale 且 compute +20% 溢价 | [1] |

## 为什么选（四条论断）

1. **运维心智是同类最低**：git push 自动构建部署、零停机部署、即时回滚为全计划内置 [1]；托管 Postgres / Key Value（Redis 兼容）/ Cron Jobs / Background Workers / 静态站同在一个工作台开箱即用 [1][2]；预览环境按计划分级（Hobby 单服务预览、Pro 全栈预览）[1]。容器底座对用户完全透明，对比 Fly.io 的 machine 操作面抽象层级高一层（见对比节）。
2. **免费起步真实可用**（2026-10 现状）：每 workspace 每月 750 免费实例小时（休眠不计时、可同时跑多个免费服务分摊），静态站永久免费 [2]；免费 Postgres 1GB、免费 Key Value 25MB 让「零成本起一个全栈 demo」成立 [2]。
3. **公司健康度缓解小厂存续顾虑**：2026-02-17 宣布 $100M 融资、估值 $1.5B；收入增速 "well above 100%"，450 万开发者，客户含 Shopify、Alibaba、Base44；基础设施在 AWS+GCP 之上（近测自有服务器降本）[4]。
4. **承接 Heroku 生态的位势明确**：Salesforce 于 2026-02 表示不再为 Heroku 开发新功能，Render CEO 称用户「正在找最成熟的替代品」[4]；官方提供 Heroku/Railway 迁移指南与最高 $10K 迁移积分 [1]；OpenAI Codex 已把 Render 列为内置部署目标 [4]。

## 为什么不选 / 代价（三条论断）

1. **免费层是「免费但慢 + 数据不驻留」**：免费 web 服务 15 分钟无入站流量即休眠，唤醒约 1 分钟（官方口径，期间展示 loading 页）[2]；免费 Postgres 创建 30 天后过期，14 天宽限期后删除（无备份）[2]；免费 Key Value 25MB 纯内存、重启即丢、升级也不迁移 [2]。三者叠加意味着「免费组合」本质是试用层，不是长期免费托管。
2. **低价层政策有突变前科**：2026-04-23 工作区计划重构，官方承认新 Hobby/Pro「带宽少于 legacy」（legacy 用席位费补贴带宽）[3]；第三方口径 Hobby 含带宽 **100GB→5GB**（Pro 500GB→25GB），超额从 100GB 增量计费改 $0.15/GB，社区反应负面 [7]；存量工作区 2026-08-01 强制迁移 [3]。免费层条款与低价层包含额都可能是移动靶。
3. **涨价曲线比自有 VPS 陡**：$7 档仅 512MB 内存 [1]；带宽超额 $0.15/GB、Hobby 自定义域名超 2 个后 $0.25/个/月、构建分钟超 500 后 $5/千分 [1]——有持续外网流量的服务月账单不可控；同等月预算在自有 VPS 上能拿到的资源量级完全不同（自托管路线的运维成本是另一轴，见同类条目 dokku/caprover）。

## 对比（同类托管平台）

| 维度 | **Render** | Railway | Fly.io |
|---|---|---|---|
| 抽象层级 | PaaS：推代码即部署，不见基础设施 [1] | PaaS：同为推代码部署 [5] | 微型 VM/裸算力：Machines 按秒计量，运维面更大 [6] |
| 免费层 | 750 实例小时/月 + 免费静态站 + 免费 PG/KV（2026-10 在）[2] | 永久 Free 计划但仅 $1/月用量额度 [5] | 旧 3×256MB 免费额度已从定价页消失 [6] |
| 计价模型 | 实例规格整月固定价（$7/512MB 起），compute 按秒 prorated [1] | 低固定订阅（$5 月含 $5 额度）+ 按秒资源计（CPU $20/vCPU·月满载），停止不计费 [5] | 纯按量（shared-1x/256MB ≈ $2.19/月），无前置计划 [6] |
| 适合 | 常驻小服务要成本可预期 / 免费起步 [1][2] | 间歇性轻负载（用多少付多少）[5] | 要底层控制、多区域裸算力 [6] |

- **vs Railway** 的本质是定价模型：Render「实例月租」对常驻服务可预期、免费层更厚；Railway「订阅+计量、停机不计费」对间歇负载更省 [1][5]。
- **vs Fly.io** 的本质是抽象层级：Render 是沙箱化 PaaS（换走容易——标准构建产物 + SQL dump），Fly 给你 machine 但你要自己面对扩缩/放置 [6]。
- **vs 自托管路线**（dokku/caprover/docker，本类别其他条目）：Render 把运维门槛降到零、代价是持续付费 + 平台绑定；自有 VPS 反之。选哪边取决于「每月几美元」和「几小时运维」哪个更贵。

## 风险与注意

- **平台绑定是中等的**：服务定义（render.yaml / 工作台配置）、Cron、磁盘、托管数据库的组合迁出是手工活（PG 可标准 SQL dump，服务配置需按目标平台重写）；本次调研未发现 Render 有 config 导出为通用格式的一手证据——**待验证**。
- **免费/低价层条款是移动靶**：2026-04 已发生一次砍额 [3][7]；引用本报告价格须带「2026-10-02 查」时间戳，决策前复查官方 pricing 页。
- **延迟敏感服务勿用免费层**：约 1 分钟冷启动（官方口径）[2] 对 API/_bot 类场景不可接受；解决办法只有常驻付费实例（$7/月起）[1]。
- **免费层安全阀与限制**：750 小时耗尽即暂停至下月（不结转）；无 SSH、单实例、SMTP 端口（25/465/587）封禁、保留端口受限 [2]。
- **存续风险**：商业闭源、无自托管兜底；缓解因素为融资健康（$1.5B 估值、2026-02 新融资）与收入高增速 [4]。总融资约 $258M 为搜索聚合口径——**待验证** [7]。
- **a16z 领投传闻未核实**：本次调研（2026-10-02）未能确认早期轮领投方，CNBC 实名投资方为 01A、Addition、Bessemer、General Catalyst、Georgian Partners [4]——不采信无来源的 a16z 说法。

## 来源

1. Render 官方定价页 — https://render.com/pricing（访问 2026-10-02；全文留档 raw/2026-10-02/web/render-render.com-pricing.md）
2. Render 免费层文档 — https://render.com/docs/free（访问 2026-10-02；留档 raw/2026-10-02/web/render-render.com-free.md）
3. Render Changelog: Updated plans for Render workspaces — https://render.com/changelog/updated-plans-for-render-workspaces（访问 2026-10-02；细节留档 raw/2026-10-02/web/render-websearch-policy-history.md）
4. CNBC: Cloud startup Render raises funding at $1.5 billion valuation as AI-built apps boom — https://www.cnbc.com/2026/02/17/render-raises-100-million-at-1point5-billion-valuation.html（访问 2026-10-02；留档 raw/2026-10-02/web/render-cnbc.com-funding.md）
5. Railway 官方定价页 — https://railway.com/pricing（访问 2026-10-02；留档 raw/2026-10-02/web/render-railway.com-pricing.md）
6. Fly.io 官方定价页 — https://fly.io/pricing/（访问 2026-10-02；留档 raw/2026-10-02/web/render-fly.io-pricing.md）
7. WebSearch 聚合（2026-10-02，Z.ai web_search_prime）：checkthat.ai「April 2026 bandwidth cut」100GB→5GB 口径、Reddit r/render 社区反应、render.com/blog/better-pricing-for-fast-growing-teams、融资史（2025-01 $80M Series C，Georgian 领投）——留档 raw/2026-10-02/web/render-websearch-policy-history.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（官方 pricing/docs/changelog + CNBC 全量核实于 2026-10-02） |
