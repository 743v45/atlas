# dokku.com 安装文档（系统要求与最低内存）

- 来源 URL: https://dokku.com/docs/getting-started/installation/
- 访问日期: 2026-10-02

## 原始提取

## 1) 系统要求

**操作系统/发行版：**
- "Operating Systems: Ubuntu 22.04/24.04/26.04 or Debian 11+ x64"
- 支持架构："`AMD64` (`x86_64`) 和 `arm64` (`armv8`)"

## 2) 对 Docker 的依赖关系

页面提到了 Docker 相关组件（Dockerfile 部署、Docker 安装说明、Docker Local Scheduler），但**本页未明确说明 Docker 是否会自动安装**。仅提到：

- "Minimum Memory: Docker Scheduler: 1GB of system memory"
- Docker 安装作为单独文档存在（"Docker Installation Notes" 链接），暗示 Docker 通常需另行安装或配置。

## 3) 硬件要求数字

引用原文：

- "Docker Scheduler: 1GB of system memory, or add swap memory"
- "K3s Scheduler: 2GB of system memory on every node in the cluster"
- 安装耗时："The installation process takes about 5-10 minutes"

**总结：** 最低内存要求取决于所选调度器——Docker 调度器需 1GB（不足可加 swap），K3s 调度器每节点需 2GB。本页未说明 Docker 自动安装细节，需参阅 Docker 安装说明文档。
