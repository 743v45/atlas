# raw — dev.37signals.com（Kamal 2.0 发布公告）

- 来源 URL: https://dev.37signals.com/kamal-2
- 访问日期: 2026-10-02（WebFetch 提取）

## 提取要点

- **发布日期**：2024-09-26（作者 Donal McBreen，37signals SIP 团队）。
- **版本史定位**：Kamal 1.0 为 37signals 自用场景而生——"an application across multiple hosts, served with an external load balancer"；Kamal 2 面向任意规模："50 servers or deploying 5 apps to a single server"。
- **Traefik → kamal-proxy**：Traefik 的 "declarative discovery model made it a poor match for Kamal's imperative design"；自研 proxy 实现 "1-1 mapping between kamal commands and proxy commands"。
- **kamal-proxy 功能**：gapless（零停机）部署、Let's Encrypt 自动 HTTPS、单机托管多个应用、内置维护模式与请求暂停；canary 部署"coming to Kamal soon"。
- **secrets 管理**：简化，提供从密码管理器拉取 secrets 的命令。
- **生产使用**："We are already running HEY deployments on Kamal 2"（HEY 已跑在 Kamal 2 上）。
- **Rails 8 关系**：Kamal 2.0 "will be installed by default in Rails 8.0"，但适用于 "web apps written in any language or framework"；提供 1→2 升级指南。
