# dokku.com 首页（定位与核心特性）

- 来源 URL: https://dokku.com/
- 访问日期: 2026-10-02

## 原始提取

**1) 自我定位**
- 标题："An open source PAAS alternative to Heroku."
- 副描述："Dokku helps you build and manage the lifecycle of applications"
- 页面头部称其为 "The smallest PaaS implementation you've ever seen"

**2) 部署方式**
通过 Git 推送部署："you can push Heroku-compatible applications to it via Git"（可通过 Git 向其推送与 Heroku 兼容的应用）。

**3) 核心特性（页面明确提到的）**
- 基于 Docker："Powered by Docker" —— 构建后在隔离容器中运行："run in isolated containers"
- 单机版 Heroku："your own, single-host version of Heroku"
- 无厂商锁定："No vendor lock-in"，可安装在任何硬件/廉价云服务商上
- 插件系统："Write dokku plugins in any language"（任意语言编写插件），"Dokku itself is built out of plugins"（Dokku 本身由插件构成）
- 生命周期管理：从构建到扩缩容（页面导航含 Create / Deploy / Scale）
- 商业版（Pro）提供开源版之外的功能

页面**未提及** nginx 或 Let's Encrypt（这些在文档中，非本主页）。

**4) 语言/构建方式**
- 构建方式："They'll build using Heroku buildpacks"（使用 Heroku buildpacks 构建）
- 插件可用任意语言编写
- 主页未列出具体支持的应用语言（由 buildpack 决定）
