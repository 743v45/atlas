# Fly.io Firecracker microVM 架构（WebSearch 留档）

- 来源：WebSearch "fly.io Firecracker microVM architecture machines fast boot"，检索日期 2026-10-02
- 主要出处：
  - https://fly.io/machines （Fly Machines 产品页）
  - https://fly.io/learn/firecracker-vm （Firecracker microVM 讲解）
  - https://fly.io/docs/reference/architecture （官方架构文档）
  - https://fly.io/blog/fly-machines （Machines API 博客）
  - https://firecracker-microvm.github.io （Firecracker 官方）
  - https://ritza.co/articles/gen-articles/cloud-hosting-providers/aws-vs-fly-io （2025 对比文）

## 关键事实

- 应用代码运行在 **Firecracker microVM** 中：基于硬件虚拟化（Linux KVM）的轻量安全 VM，不是容器沙箱。
- Fly Machines = 快速启动 VM 的 REST API，**启动约 300ms**；代理可在请求到达时按需拉起机器、空闲时关停（auto-stop/start 模式）。
- Firecracker 单宿主可跑数千 microVM，每个毫秒级启动、无传统 VM 的内存开销（AWS 出品，也是 AWS Lambda/Fargate 底座）。
- 部署形态是「每应用一组 microVM」而非传统容器编排——Ritza 2025 对比文指出这带来比容器更强的隔离。
- Machines 是平台上所有应用的计算底座（web 服务、后台任务都能跑）。
