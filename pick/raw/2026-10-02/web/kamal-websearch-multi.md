# raw — WebSearch 检索记录（资源占用 + 采纳度，多域）

- 来源: WebSearch（Z.ai web_search_prime），查询两组
- 访问日期: 2026-10-02

## 组1：kamal-proxy 资源占用

- [kamal-proxy discussion #222](https://github.com/basecamp/kamal-proxy/discussions/222)：小 Rails 应用容器 ~150–300MB/容器；讨论 idle shutdown/wake-up 进一步降耗 → proxy 自身占用相对可忽略。
- [basecamp/kamal-proxy](https://github.com/basecamp/kamal-proxy)：官方定位 "a tiny HTTP proxy, designed to make it easy to coordinate zero-downtime deployments"；Go，跑 80/443。
- [ecn-apps Kamal 2 vs Coolify 2026](https://ecn-apps.com/pages/articles/kamal-vs-coolify-2026.html)：kamal-proxy "~15MB RAM"（已单独留档 kamal-ecn-apps.com.md）。
- [nts.strzibny.name/kamal-proxy](https://nts.strzibny.name/kamal-proxy)：换掉 Traefik 的理由包括"想要更轻"。

## 组2：37signals ONCE / 语言无关采纳度

- [basecamp/once](https://github.com/basecamp/once)：ONCE 自述 "a platform for installing and managing Docker-based web applications"，内置 37signals 应用 + 任意自定义 Docker 容器。
- 语言无关三方佐证：BigMike（"language-agnostic: if an application can be built into a Docker image, it can be deployed"）；Drifting Ruby《Kamal with Non-Rails Apps》演 Python 部署；judoscale（"works for more than just Rails apps"）；matiassalles99.codes（"any language, not just Rails"）。
- 非 Ruby 采纳信号：r/django 讨论「Deploying multiple Django apps to a single server」用 Kamal；r/selfhosted 有面向自托管社区（非 Rails 群体）的 Kamal 书。
- 反面信号：GitHub discussion #1823「I am recommending against Kamal right now」（2026-04-10，已单独留档 kamal-github.com-discussion1823.md）。
- 相关检索：Reddit r/rails「Kamal deployment memory usage」——1GB RAM 跑完整部署是否够的讨论（瓶颈在应用容器非 proxy）。
