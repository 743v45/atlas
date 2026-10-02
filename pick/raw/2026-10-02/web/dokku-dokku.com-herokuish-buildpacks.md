# dokku.com Herokuish Buildpacks builder 文档

- 来源 URL: https://dokku.com/docs/deployment/builders/herokuish-buildpacks/（由 https://dokku.com/docs/deployment/methods/buildpacks/ 302 重定向）
- 访问日期: 2026-10-02

## 原始提取

## 1) dokku 支持哪些 buildpack/builder

页面侧边导航显示 Builders 包括：Herokuish Buildpacks、Cloud Native Buildpacks、Dockerfile、Lambda、Nixpacks、Railpack、Null。

- Herokuish 使用 Heroku buildpacks，页面链接指向 Heroku 文档。
- Cloud Native Buildpacks 对应 `pack` builder，文中提到 "Dokku will only select the `dockerfile` builder if both the `herokuish` and `pack` builders are not detected"

## 2) 检测机制

原文引用：

> "This builder will be auto-detected in either the following cases"

- 设置了 `BUILDPACK_URL` 环境变量（通过 `dokku config:set` 或仓库根目录的 `.env` 文件）
- 应用仓库根目录存在 `.buildpacks` 文件

也可显式指定：`dokku builder:set node-js-app selected herokuish`

另有警告："A specified `BUILDPACK_URL` will always override a `.buildpacks` file or the buildpacks plugin."

## 3) 用户需要懂 Dockerfile 吗

**不需要**。Dokku 默认使用 buildpacks 部署：

> "Dokku normally defaults to using Heroku buildpacks for deployment"

Dockerfile 只是可选项——如果提交了 Dockerfile 才会触发 Dockerfile 部署；要避免该自动检测，可设置 `BUILDPACK_URL` 或创建 `.buildpacks` 文件。

## 4) 常见语言支持

本页面未列举具体编程语言支持列表（仅示例应用名如 node-js-app、python-sample、ruby-sample 暗示 Node.js/Python/Ruby 均可通过 Heroku buildpacks 支持）。页面主要覆盖：

- 自定义 stack 镜像：`dokku buildpacks:set-property node-js-app stack gliderlabs/herokuish:latest`
- 非 amd64 平台需设置 `allowed` 属性才能启用 herokuish
- `curl` 超时可设 `CURL_TIMEOUT=1200` 等配置
- 通过 Procfile 指定进程命令

具体语言列表需查看 Heroku 官方 buildpacks 文档（页面外部链接）。

## 关键判断素材

- builder 可插拔清单：herokuish / pack(CNB) / dockerfile / lambda / nixpacks / railpack / null——七种
- 默认路径 buildpack：push 代码即可，无需写 Dockerfile
