# Render 官方定价页全量抓取（render.com/pricing）

- 来源：https://render.com/pricing
- 访问日期：2026-10-02（WebFetch 直抓被 JS 渲染拦截，改用 web_reader 渲染后取回全文）
- 用途：render 条目定价核实（2026-10 现状）

## Workspace Plans（工作区订阅）

| 计划 | 价格 | 定位 | 关键差异 |
|---|---|---|---|
| Hobby | $0/mo + compute | 个人项目/原型 | 最多 25 服务、5 GB 带宽/月、单服务预览、自定义域名 2 个（超出 $0.25/域名/月）、chat support |
| Pro | $25/mo + compute | 生产级应用与 agent 团队 | 无限席位与服务、25 GB 带宽、全栈预览、水平自动扩缩、隔离环境、OIDC、AWS PrivateLink、审计日志 |
| Scale | $499/mo + compute | 治理与合规 | 多 workspace、1 TB 带宽、HIPAA、SAML SSO & SCIM、RBAC |
| Enterprise | Custom | SLA/专属支持 | 合同 SLA、TAM、Slack 频道、响应 SLA |

无活动月份的 Pro/Scale workspace 订阅费豁免（FAQ）。

## Compute（Services & Workers）

| 规格 | 月价 | RAM |
|---|---|---|
| Free（有限制） | $0 | 512 MB |
| 0.5c-512mb | $7 | 512 MB |
| 1c-2g | $25 | 2 GB |
| 2c-4g | $85 | 4 GB |
| 2c-8g | $135 | 8 GB |
| 2c-16g | $200 | 16 GB |
| 4c-8g | $175 | 8 GB |
| 4c-16g | $225 | 16 GB |
| 4c-32g | $350 | 32 GB |
| 8c-16g | $300 | 16 GB |
| 8c-32g | $450 | 32 GB |
| 8c-64g | $1,000 | 64 GB |
| 12c-24g | $450 | 24 GB |
| 12c-48g | $800 | 48 GB |
| 12c-96g | $1,500 | 96 GB |

上限 12 CPU / 96 GB RAM。持久磁盘 $0.25/GB/月。

## Render Postgres

| 规格 | 月价 | RAM | 连接数 |
|---|---|---|---|
| Free（有限制） | $0 | 256 MB | 100 |
| 0.1c-256mb | $6 | 256 MB | 100 |
| 0.5c-1g | $19 | 1 GB | 100 |
| 1c-2g | $40 | 2 GB | 100 |
| 1c-4g | $55 | 4 GB | 100 |
| 2c-4g | $75 | 4 GB | 100 |
| 2c-8g | $100 | 8 GB | 200 |
| … | … | … | 上限 128 CPU / 1024 GB RAM / $11,000 月 |

- 含 1 GB SSD 存储；扩容 $0.30/GB；PITR：Hobby 3 天 / 付费 7 天；付费实例有逻辑备份；支持只读副本与 HA

## Render Key Value（Redis 兼容）

| 规格 | 月价 | RAM |
|---|---|---|
| Free | $0 | 25 MB |
| 256mb | $10 | 256 MB |
| 1g | $20 | 1 GB |
| 3g | $60 | 3 GB |
| 5g | $100 | 5 GB |
| … | 最高 $750（50 GB RAM） | 付费支持磁盘持久化 |

## Cron Jobs

- $0.00016/分钟（512 MB）起；按秒计费；仅运行时计费；免费层不可用
- （换算：0.5c-512mb 规格 ≈ $7/月满载）

## Workflows（新品）

- durable execution 托管：$0.20/活跃 CPU 小时 + $0.05/活跃 GB 小时（flex）；固定规格 $0.40/h（2c-4g）～ $1.50/h（4c-16g）
- 并发任务 runs：Hobby 20 / Pro 50 / Scale 100（超出 $10/mo per 50）

## Static Sites

- "Always free to deploy"：CDN、Git 连续部署、即时缓存失效、自定义域名 + 托管 TLS

## 网络 / 带宽 / 构建

- 带宽包含额度：Hobby **5 GB/月**（超额 $0.15/GB）、Pro 25 GB、Scale 1 TB、超额一律 $0.15/GB
- 自定义域名：Hobby 2 个（$0.25/域名/月 超出）、Pro 15、Scale 25
- 构建管道分钟：Hobby 500 分/月（超额 $5/千分）、Pro 1K、Scale 5K；Performance pipeline（Pro+）$25/千分
- 专用 IP $100/月/IP 组（Pro+）；Private Link $30/月（Pro+，含 3 条）
- 日志保留：Hobby 7 天 / Pro 14 / Scale 30；SSH 访问全计划有
- 零停机部署、auto-deploys、deploy hooks、pre-deploy command、即时回滚：全计划有（回滚构建保留 5/15/30/30）

## FAQ 要点（计费模型）

- "Render charges for three things: your workspace plan (flat subscription), metered features like bandwidth (usage-based), and compute for your applications (usage-based)."
- compute 按服务设定 plan、按秒 prorated；关机只付运行时段
- Free compute plans：web services / Key Value / Postgres 可免费开，有用量限制
- 首卡 $1 验证费（Stripe，退款）

## 其他观察（页面元信息）

- 页面定位语："The Zero DevOps cloud for developers and teams"、"Predictable pricing that scales with you"
- Pro 计划描述："For teams deploying production-grade apps **and agents**"（AI agent 托管是明确产品重心）
- 顶部促销：迁移奖励最高 $10K credits；Render for Startups 最高 $100K credits
- 迁移指南：Heroku Migration Guide、**Railway Migration Guide**（把 Railway 列为迁移来源）
- 官方对比页存在：vs Vercel / Heroku / Railway / Fly.io
- 新产品：Workflows（durable execution）、Sandboxes（Early Access）、Render MCP + CLI（"Deploy to Render with your coding agent"）
- 合规：SOC 2 Type II、ISO 27001、GDPR DPA；HIPAA BAA 需 +20% compute 溢价（Pro/Scale）
