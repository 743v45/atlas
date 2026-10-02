# raw — dev.37signals.com（The ONCE app server）

- 来源 URL: https://dev.37signals.com/once-app-server
- 访问日期: 2026-10-02（WebFetch 提取）

## 提取要点

- **日期**：2026-04-17（RECORDABLES 系列）；ONCE 是 37signals 开源 app server，DHH 比作游戏机："Cartridge out, cartridge in, it just works"，单条 copy-paste 命令安装，TUI「80's aesthetic」。
- **与 Kamal/kamal-proxy 关系**：复用 kamal-proxy——"that proxy would fit really well if we could put it into the ONCE setup"，提供 "that nice no downtime deployment"；ONCE 在一个 Docker network 上装 proxy + 一或多个应用；kamal-proxy 的 Prometheus 指标驱动 dashboard 流量统计（对客户端 IP 做 HyperLogLog）。
- **分工定位**："Kamal is really for deploying your own private applications in a more sort of involved manner"，ONCE 则是单机 console 式部署公开可分享应用。
- **单机多应用**：核心升级点；应用按 hostname 自动路由；约束单机、数据统一放 `/storage`（SQLite 为主）。
- **支持应用**：内置 Campfire / Writebook / Fizzy；可带任意第三方公开 Docker 镜像（要求：响应 `/` up、最好 SQLite in /storage）。
- **受众与规模**：面向半技术 self-hoster；笔记本/ closet 旧 PC/小云 VM 均可，单机支撑数千用户；数据自主（EU hosting）；Omarchy 将预装 ONCE。
- **采信点**：kamal-proxy 已作为独立组件被 ONCE 生态复用 → proxy 本身轻量的旁证。
