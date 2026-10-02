# raw — judoscale.com（Kamal vs PaaS）

- 来源 URL: https://judoscale.com/blog/kamal-vs-paas
- 访问日期: 2026-10-02（WebFetch 提取；正文无明确发布日，讨论 Rails 8 + Kamal 2，约 2024 末–2025）

## 提取要点

- 定位："a deployment tool built to make shipping Docker-based apps to the web even easier, 'No PaaS Required'"；"deployment-as-code, not quite infrastructure-as-code"。
- **语言无关**："While Kamal works for more than just Rails apps"（未点名具体语言）。
- **功能**：kamal-proxy 单机多应用 + 零停机 + 复用旧构建快速回滚；setup 后 "a simple `kamal deploy` is all it takes"；accessories（Redis/DB/队列）配置文件管理，或接托管服务。
- **Kamal 缺口（对比 PaaS）**：不 provision 服务器；要求 Docker 容器；本地构建镜像（"uses your local Docker environment to build images"）；需要容器 registry；不配负载均衡器；**不支持 autoscaling**。
- **成本**："Running your app on a VPS provider like Hetzner or DigitalOcean is undeniably cheaper than using a PaaS at scale"；proxy 对 "a bunch of small 'hobby' apps" 省钱；注意 Docker Hub 免费层只含 1 个私有仓库。
- 对照 PaaS 名单：Heroku、Render、Railway、Fly.io（未提 Dokku）。
