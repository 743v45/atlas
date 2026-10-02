# Railway 官方文档抓取（六页合并）

- 来源 URL:
  - https://docs.railway.com/guides/build-configuration（构建配置）
  - https://docs.railway.com/reference/deployments（部署机制）
  - https://docs.railway.com/guides/environments（环境）
  - https://docs.railway.com/reference/databases（数据库）
  - https://docs.railway.com/reference/templates（模板）
  - https://docs.railway.com/pricing/cost-control（成本控制）
- 访问日期: 2026-10-02（404 的 /reference/build、/guides/build、/reference/config-from-code、/reference/pricing/{plans 下 usage-limits、cost-controls} 不留档）

## 构建配置（build-configuration）

- 默认构建器 Railpack："Railway uses Railpack to build your code. It works with zero configuration"
- "Railway will build and deploy your code with zero configuration"
- 配置可经环境变量或 railpack config file 定制；Railway 自身配置文件 railway.json/railway.toml（不跟随 Root Directory，需绝对路径）
- 覆盖构建命令：在 service settings 设值；`RAILPACK_INSTALL_CMD`/`RAILPACK_PACKAGES`（Mise 包）/`RAILPACK_BUILD_APT_PACKAGES`/`RAILPACK_DEPLOY_APT_PACKAGES`
- `NO_CACHE=1` 禁缓存；"cache hit on builds is not guaranteed"（构建系统按需伸缩）
- Watch paths：gitignore 风格；Procfile 自动检测 start command（官方更推荐 settings 指定）

## 部署机制（deployments）

- 服务源变更即构建："when changes are detected in the service source"
- 打包："Railway will build the service and package it into a container with Railpack or a Dockerfile if present"；源为 Docker 镜像时跳过构建
- 单例部署："Railway maintains only one deploy per service"，新部署上线后旧部署收 SIGTERM，**默认 0 秒后强制 SIGKILL**
- 旧部署清理：Active/Completed/Crashed 状态的旧部署最终被移除

## 环境（environments）

- "All projects in Railway are created with a `production` environment by default."
- "All changes made to a service are scoped to a single environment."
- PR 预览环境（temporary）："created when a Pull Request is opened on a branch and are deleted as soon as the PR is merged or closed."
- Focused PR Environments："only deploy services affected by files changed in the pull request"
- 支持机器人 PR："works with any GitHub bot, including Dependabot, Renovate, GitHub Copilot, Claude Code, Devin, Jules"
- Fork 环境弃用（2024-01 起）："forked environments have been deprecated in favor of Isolated Environments with the ability to Sync."同步后服务标记 New/Edited/Removed，审查后再部署
- staging 惯用法："maintain a `staging` environment that is configured to auto-deploy from a `staging` branch"
- 变量：复制环境时随服务复制；服务间依赖经变量引用 `${{service.URL}}`

## 数据库（databases）

- 官方模板："PostgreSQL, MySQL, MongoDB, Redis"；声称 "Railway can support any type of Database service required for an application stack."
- 部署途径："from a template, or by creating one through the service creation flow"
- 市场另有 Minio、ClickHouse、Dragonfly、Chroma、ParadeDB；官方模板带 Database View
- "Railway services are containers deployed from a Docker Image or code repository"；外部访问需 "enabling TCP Proxy on the service"——数据库默认在项目私有网络内
- **该页未提及任何备份机制**；持久化仅 Volume："data can be persisted between rebuilds of the container by attaching a Volume"（Volume ≠ 备份）

## 模板（templates）

- "Templates provide a way to jumpstart a project by packaging a service or set of services into a reusable, distributable format."
- "Deploy a service or set of services in a few clicks. Choose a template from the marketplace"（railway.com/templates）
- "you can create and publish templates for others to use"
- 开源伙伴计划分成："Earn commission from template usage, up to 25% as part of the partner program"

## 成本控制（cost-control）

- 入口：Workspace Usage 页 "Set Usage Limits"（Compute 与 Agent 分开配）；CLI：`railway usage limit set --target workspace --soft 75 --hard 125`
- 权限："You must be a workspace admin to configure usage limits."
- 软限制：仅邮件提醒，"Your resources will remain unaffected."
- 硬限制：达到后 "all your workloads will be taken offline to prevent them from incurring further resource usage."；最低 $10；75%/90%/100% 三档提醒
- 恢复：提高/删除限制后自动重新部署，失败可手动；"Setting a hard limit is a possibly destructive action"
- Compute 触顶→工作负载下线；Agent（Railway Agent 的 LLM 消耗）触顶→Agent 停用；Agent 默认硬限 Hobby $5 / Pro $20，可调不可移除
