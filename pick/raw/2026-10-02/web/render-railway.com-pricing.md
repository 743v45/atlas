# Railway 定价页（railway.com/pricing，对比素材）

- 来源：https://railway.com/pricing
- 访问日期：2026-10-02（WebFetch）

## 计划与固定月费

- Free Trial：$0——一次性 $5 额度，30 天过期，无需信用卡
- Free：$0/mo，含 $1/月用量（永久免费层）；1 vCPU / 0.5 GB per service、1 副本、3 天日志
- Hobby：**$5/月**，含 $5 月度用量额度（不累积，每周期重置）
- Pro：**$20/月/workspace**，含 $20 月度额度；席位无限，按 workspace 计费
- Enterprise：定制（SLA、SSO、HIPAA BAA、专属 VM）

## 资源计价（容器，按秒计）

- Memory $0.00000386/GB/s（= $10/GB·月满载）；CPU $0.00000772/vCPU/s（= $20/vCPU·月满载）
- Volumes $0.15/GB·月；Egress $0.05/GB（服务）；Object Storage $0.015/GB·月（免 egress）
- 停止的服务不计费（无闲置加价）

## 对比锚点（供 render 条目对比节用）

- Railway 模型 = 低固定月费订阅 + 按用量扣额度；Render = 免费订阅 + 实例整月固定价（Free/$7/$25…）+ 少量计量（带宽/构建分钟）
- Railway 有永久 Free 层（$1 额度），比 Render 的 750 小时限制更「薄」但更简单
