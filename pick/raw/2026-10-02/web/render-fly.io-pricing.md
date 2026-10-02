# Fly.io 定价页（fly.io/pricing，对比素材）

- 来源：https://fly.io/pricing/
- 访问日期：2026-10-02（WebFetch）

## 计费模型

- Machines 按秒计费（"Billed by the second while a Machine runs"）；Volumes 按预分配容量计费
- 无前置计划费（"No plans to pick up front on Machines or Sprites"）
- **旧的免费层（3 台 shared-cpu-1x 256MB VM）已从页面消失**——免费口径只剩「每月前 10GB 快照免费」+ 每 app 一个共享 IPv4 / 无限 Anycast IPv6

## 示例价（Ashburn）

- shared-cpu-1x 256MB：$0.0030/h ≈ $2.19/月
- performance-1x 2GB：$0.0458/h ≈ $33.00/月
- 加内存 $6/GB·月（至 128GB）；停止的 Machine 按 rootfs $0.15/GB·月
- Volumes $0.15/GB·月；egress $0.02/GB（NA/EU）～ $0.12/GB（非洲/印度）
- 预留算力省 40%（$36/yr shared 起）
- 区域乘数：东京 1.308、圣保罗 1.615

## 定位信号

- 页面主打裸算力（Machines / Sprites），不是「推代码即部署」的 PaaS 叙事
- Sprites：纯计量新形态（$0.03825/CPU-h、$0.021875/GB-h）
- Managed Postgres 固定套餐（$38～$1,922/月）；付费支持档 $29/$199/$2,500+
- 对比锚点：Fly = 微型 VM/裸算力按秒计量，运维面比 Render 大；无免费层（2024-2026 间退场）
