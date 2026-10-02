# raw — kamal-deploy.org（官网首页）

- 来源 URL: https://kamal-deploy.org
- 访问日期: 2026-10-02（WebFetch 提取）

## 提取要点

- 定位："Deploy web apps anywhere"；开源（Basecamp/37signals），前名 MRSK，名字取自古阿拉伯航海工具。
- **语言无关（原文）**："Originally built for Rails apps, Kamal will work with any type of web app that can be containerized."
- **工作方式（原文）**："Feed the config file a list of IP addresses with vanilla Ubuntu servers that have seen no prep beyond an added SSH key, and you'll be running in literally minutes." 服务器 "auto-provisioned with Docker, and run right away"；无需在服务器装 Ruby 等依赖（"That all lives in the Docker image now"）；底层 "just basic Docker commands being called"；Docker 层缓存加速部署。
- **功能清单**：zero-downtime deploys, rolling restarts, asset bridging, remote builds, accessory service management。
- **当前版本（官网当日显示）**：Kamal 2.12.0（另有 v1.9.2 文档线）。
- **要求**：vanilla Ubuntu（或类似）+ SSH key；Docker 自动安装。无硬件规格。
- **官方警告（原文）**："You're probably still better off with a fully managed service if basic Linux or Docker is still difficult."
- 使用方：37signals 用它在自己硬件上跑 HEY（页面提及 Basecamp、HEY、Fizzy、ONCE）。
