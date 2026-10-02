# Railway 定价页（官方）原始抓取

- 来源 URL: https://railway.com/pricing 与 https://docs.railway.com/reference/pricing/plans（两次抓取合并留档）
- 访问日期: 2026-10-02
- 抓取方式: WebFetch（官方 pricing 页 + 官方 docs plans 页，两源交叉一致）

## 计划费用（官方 pricing 页）

- Free Trial：$0，一次性赠送 **$5 额度，30 天有效**，无需信用卡
- Free：$0/月，含 **$1/月** 使用额度
- Hobby：**$5/月**，含 $5/月 使用额度
- Pro：**$20/月**（按 workspace 计，席位不限），含 $20/月 使用额度
- Enterprise：定制价格

## 按量计费单价（容器服务，按秒计）

- 内存：$0.00000386 /GB/秒 ≈ **$10/GB/月**
- CPU：$0.00000772 /vCPU/秒 ≈ **$20/vCPU/月**
- 磁盘卷：$0.00000006 /GB/秒 ≈ $0.15/GB/月
- 出站流量（服务）：**$0.05/GB**
- 对象存储：$0.015/GB-月，流量免费

## VM/沙箱单价（与容器费率分列）

- 内存：$0.00001929 /GB/秒 ≈ **$50/GB/月**
- CPU：$0.00001929 /vCPU/秒 ≈ **$50/vCPU/月**
- 出站流量：$0.05/GB
- 按实际 CPU 使用和运行中持有的内存计费，非挂钟时间；销毁后不产生费用

## 计费方式

- 资源按**秒**计量，按实际使用计费；"stopped services cost nothing"（停止的服务不计费）
- 计划费覆盖包含额度，超出部分按上述费率计
- Hobby 计划：月末总用量 ≤ $5 则不多收，超过 $5 则按总用量收费；额度不累积，每周期重置
- Upgrade 立即生效，downgrade 下个周期生效；Trial 剩余额度升级后结转
- 支付方式：信用卡；Enterprise 支持发票付款
- **自 3 月 30 日起不再支持预付，需绑定后付卡**（docs 页）
- **额度用尽时订阅被取消并停止所有工作负载**（docs 页）

## docs 页补充数字

- 构建免费（构建 CPU、内存、基础镜像下载、镜像导出与存储均不收费）
- RAM 单价原文："$10 / GB / month ($0.000231 / GB / minute)"
- CPU 单价原文："$20 / vCPU / month ($0.000463 / vCPU / minute)"
- Network Egress 原文："$0.05 / GB"
- Volume Storage 原文："$0.15 / GB / month"

## 各计划资源上限（两源合并，docs 页为准）

| 计划 | 副本数 | RAM | CPU | 临时存储 | 卷存储 | 镜像大小 | 日志保留 | 项目/服务数 | 并发构建 | 自定义域名 |
|---|---|---|---|---|---|---|---|---|---|---|
| Trial | 2 | 1 GB | 2 vCPU | 1 GB | 0.5 GB | 4 GB | 7 天 | 2 项目/5 服务 | 3 | 1 |
| Free | 1 | 0.5 GB | 1 vCPU | 1 GB | 0.5 GB | 4 GB | 3 天 | 1 项目/3 服务 | 1 | 0 |
| Hobby | 6 | 48 GB | 48 vCPU | 100 GB | 5 GB | 100 GB | 7 天 | 50/50 | 3 | 2 |
| Pro | 42 | 1 TB | 1,000 vCPU | 100 GB | 1 TB* | Unlimited | 30 天 | 100/100 | 10 | 20 |
| Enterprise | 50 | 2.4 TB | 2,400 vCPU | 100 GB | 5 TB* | Unlimited | — | — | — | — |

*Pro 及以上可自助扩容卷至 1 TB。

- 协作：Pro 与 Enterprise "allow you to add members to their workspace and manage their permissions"
- 镜像保留期：Free/Trial 24h，Hobby 72h，Pro 120h，Enterprise 360h
- 下线后数据保留：Free/Trial 过期后 30 天，Hobby 取消后 60 天，Pro 取消后 90 天
