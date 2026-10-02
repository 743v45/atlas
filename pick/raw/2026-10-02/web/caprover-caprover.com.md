# CapRover 官方入门文档（服务器要求）

- 来源：https://caprover.com/docs/get-started
- 访问日期：2026-10-02（经 WebFetch 提取）
- 用途：caprover 条目（lightweight-deploy 类别）资源占用与依赖核实

## 原文要点

1. **RAM**：512MB 可能不够——"the build process sometimes consumes too much RAM, and 512MB RAM might not be enough"；多数服务商 $5 档最低提供 1GB RAM。
2. **CPU 架构**：镜像支持 "AMD64 (x86-64) and ARM64"；32 位 ARMv7 镜像不再发布。
3. **操作系统**："CapRover is tested on Ubuntu 24.04 and Docker 25+"。
4. **Docker**：必须有 Docker，"your Docker version needs to be, at least, version 25.x+"。DigitalOcean 一键镜像自动安装；手动装需 Docker CE，文档明确警告避免 snap 方式安装。
5. **Docker Swarm**：页面提到多节点 Swarm 端口的防火墙设置链接，未给具体版本号。
6. **防火墙端口**（单节点 Ubuntu）：80/tcp、443/tcp、443/udp、3000/tcp（CapRover 面板）。

## 解读备注

- 安装方式是 `docker run caprover/caprover`（老牌安装脚本），即 CapRover 本身以 Docker 容器运行——微型 PaaS 路线 = Docker 被藏起来，不是绕开。
- 最低资源口径：官方文档以「1GB RAM」为实际起步线（512MB 警告不够，构建期吃内存）。
