# Coolify 官方安装文档（coolify.io）

- 来源 URL：https://coolify.io/docs/installation
- 访问日期：2026-10-02（web_reader 抓取）
- 用途：最低资源要求 / 安装方式 / Docker 依赖核实

## 原文关键内容

### Server Requirements
- You need a server with SSH access. This can be: A VPS / A Dedicated Server / A VM in Proxmox / A Raspberry Pi / Any other server with SSH access

### Supported Operating Systems
- Debian based (Debian, Ubuntu, etc.) / Redhat based (CentOS, Fedora, Redhat, AlmaLinux, Rocky, Asahi, etc.) / SUSE based (SLES, SUSE, openSUSE, etc.) / Arch Linux / Raspberry Pi OS 64-bit (Raspbian) / Alpine Linux

### Supported Architectures
- 仅 64 位：AMD64 / ARM64

### Minimum Hardware Requirements（Server Requirements for Coolify）
- **2 Core CPU**
- **2 GBs memory (RAM)**
- **30+ GB of storage for the images**

> If you build and host on the same server as Coolify and your builds are utilizing all available memory, this may cause the server to become unresponsive or even crash. To prevent this, consider enabling swap space on your server (or paying for more resources).

> Hosting `Supabase`, `Appwrite` or `Posthog` requires more resources than hosting a static site (waay more).

### Installation Methods

#### 1. Quick Installation (Recommended)
```
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```
The installer does the following:
- Installs required tools (`curl wget git jq openssl`)
- **Installs Docker Engine (26+)**
- Configures Docker logging
- Configures Docker daemon with default address pools
- Creates directory structure at `/data/coolify`
- Sets up SSH keys for server management
- Installs and starts Coolify

> It is recommended to use the PrivateIP to access coolify as it is more secure (a VPN setup to your Server is needed for that to work).

#### 2. Manual Installation
- Install Docker Engine (24+)
- Create `/data/coolify/{source,ssh,applications,databases,backups,services,proxy,webhooks-during-maintenance}` 等目录
- 生成 SSH key（coolify 通过 SSH 管理服务器，包括本机 → 自己）
- 从 CDN 取 `docker-compose.yml`、`docker-compose.prod.yml`、`.env.production`、`upgrade.sh`
- **启动命令：`docker compose --env-file ... -f docker-compose.yml -f docker-compose.prod.yml up -d --pull always --remove-orphans --force-recreate`**
- UI 端口 `http://<ip>:8000`

#### 3. Docker Desktop Installation
- 仅用于本地开发测试（Windows）

### Debugging（附注）
- GitHub PAT 过期会导致 ghcr.io 拉镜像 401
- Raspberry Pi 2GB RAM 可能崩溃（SD 卡慢），建议 4GB+ RAM 的机型

## 采集备注
- 官方描述（repo tagline）：280+ one-click services
- Coolify 自身 = 一组 docker compose 容器（含 4 个 helper 容器架构），印证「微型 PaaS 藏起 Docker 而非绕开」
