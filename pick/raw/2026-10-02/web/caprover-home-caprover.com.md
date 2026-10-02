# CapRover 官网首页

- 来源：https://caprover.com/
- 访问日期：2026-10-02（WebFetch 提取）

## 定位

- "Scalable, Free and Self-hosted PaaS"
- "Deploy apps. Own your infrastructure."
- "Free forever" / "No vendor lock-in" / "Production ready"

## 核心功能

- **Web 面板**：管理端口、持久目录、环境变量、实例数量
- **CLI**：`caprover deploy`（检测源码→构建镜像→推送→部署→启动容器）
- **一键应用**：数据库、WordPress、监控工具等（官网称数十种秒级部署；实际清单 360 个，见 caprover-one-click-apps 仓库 raw 留档）
- **集群**：基于 Docker Swarm，"Add nodes to your Docker Swarm cluster and let CapRover handle load balancing"
- 自动 HTTPS（Let's Encrypt 签发与续期）、任意语言（Node/Python/PHP/Java/Ruby/.NET）、多种部署入口（面板/CLI/webhook/Git）

## 商业化

- 首页未提任何付费服务/商业版本；资金来源为 OpenCollective 社区捐赠（"Keep CapRover independent"）
- 开源协议：Apache 2.0（官网口径；仓库 LICENSE 为 Apache-2.0 + 附加条款 appendix，见 gh raw 留档）
