# Fly.io 故障史与可靠性（WebSearch 留档）

- 来源：WebSearch "fly.io outage incident history 2024 2025 uptime reliability"，检索日期 2026-10-02
- 主要出处：
  - https://fly.io/infra-log （官方 infra log，自称对内部事件 100% 忠实公开）
  - https://fly.io/infra-log/2024-10-26 （10-22 编排故障 postmortem）
  - https://community.fly.io/t/psa-postmortem-for-the-nov-25-outage/22933 （11-25 全球故障 postmortem）
  - https://fly.io/infra-log/2025-02-22 （Tigris 存储故障）
  - https://www.pulsapi.com/services/fly-io/uptime （第三方监控）
  - Kuberns（LinkedIn）对 fly.io 全部事件报告的分析；IsDown 统计

## 大事件时间线

- **2024-07-13**：老物理机下线 + Machine 迁移 + 宿主误标记不健康，容量受限
- **2024-10-09**：SEA 区域 BGP4 上游误配置，流量被引向 LON
- **2024-10-22** ⚠️ 最大事故：**全网编排故障（fleetwide orchestration outage）**。根因：**Consul root key signing key 过期**，双向认证连带把连通性整个打挂。官方称「记录在案的最长重大故障」，发布完整 postmortem
- **2024-11-25** ⚠️ **全球故障**：交换机饱和、API 不可用、全球客户应用宕机；复合根因（其一与 10 月编排故障同型）
- **2025-02-16~22** ⚠️ **Tigris 存储故障**（2-16 宣布，~2-22 缓解）
- 2025-01：builders / logging 故障（infra log 周报）；2025-09-26：AMS 网络故障 ~22min、GRU 状态库问题

## 第三方口径

- PulsAPI 实测：观测 121 天内 **94.41% uptime**（第三方探测点口径，非官方 SLA；Fly 不提供正式 SLA 给普通客户）
- IsDown：2022-06 以来 **609 起已记录事件 ≈ 13 起/月**
- Kuberns 分析模式：**遗留系统迁移问题反复引发事件**，postmortem 收尾永远是「继续排干遗留系统」
- 官方立场：「记录的事件很多，但严重持续故障不常见」
- 正面：透明度高（infra log 全量公开，业界少见）

## 对选型的含义

- 2024 Q4 连环重大故障 + 遗留系统迁移反复出事是真实记录；个人小服务可接受（本来就非关键路径），但「全球分布当卖点」时要掂量区域级故障频率。
