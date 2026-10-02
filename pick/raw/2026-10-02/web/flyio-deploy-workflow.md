# Fly.io 部署工作流：flyctl / fly deploy 本地与远程构建（WebSearch 留档）

- 来源：WebSearch 'fly.io docs "fly deploy" remote builder local Docker image fly.toml'，检索日期 2026-10-02
- 主要出处：
  - https://fly.io/django （官方 Django 页：install flyctl → fly launch → 每次改动 fly deploy）
  - https://hexdocs.pm/phoenix/1.6.4/fly.html （--remote-only 用法）
  - https://community.fly.io/t/build-images-with-nixpacks/6169 （无本地 Docker（Apple ARM64）时 --remote-only 走远程 builder；--nixpacks）
  - https://agdia-597e782f.mintlify.app/platforms/fly （fly.toml 与机器配置关系）

## 关键事实

- 标准流：装 `flyctl` CLI → `fly launch`（首次：检测应用、生成 `fly.toml`、建应用）→ 之后每次改动 `fly deploy`。
- **构建两条路**：
  - **本地构建**（默认）：`fly deploy` 用本地 Docker daemon 构建（`--local-only` 控制）；本机没装 Docker 则失败。
  - **远程构建**：`fly deploy --remote-only` 把构建丢给 Fly 的 remote builder（本机无 Docker 的典型场景，如 Apple ARM64 上常见）；也支持 `--nixpacks`（buildpack 路线，免写 Dockerfile）与 `--image`（直接推已有 OCI 镜像）。
- **fly.toml 是声明式应用配置**（应用名、region、[[services]]、[http_service]、env 等）；注意：deploy 时部分手动改过的机器配置会被 fly.toml 重置——「以文件为准」是其声明式哲学的体现，也是配置漂移的常见坑。
- 部署产物最终是跑在 Firecracker microVM（Fly Machines）里的镜像。

## 对选型的含义

- 上手路径 = 写代码 + fly.toml，不需要碰服务器；构建可以完全不吃本地资源（--remote-only），也可以复用本地已有镜像（--image）。
