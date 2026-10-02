# Docker Hub 政策变动（2025-04 生效的新限速体系）

- 来源：WebSearch（Z.ai web_search_prime 聚合），查询词「Docker Hub policy change 2025 2026 pull rate limits uncapped subscription organizations retirement」
- 访问日期：2026-10-02

## 新限速表（2025-04-01 起生效）

| 计划 | 拉取限额 |
|---|---|
| Business / Team / Pro（付费） | 无限（uncapped，受 fair use 约束） |
| Personal（免费认证） | **100 pulls/小时**（从最初宣布的 40 上调） |
| 未认证（匿名） | **10 pulls/小时** |

- 按月拉取数上限与按量计费被**移除**，只保留小时限速；限速按 6 小时滚动窗口计算（docs.docker.com/docker-hub/usage/pulls）
- 存储限额执行推迟到 2026（Reddit r/kubernetes 传述）

## 来源链接（搜索结果给出）

- https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience （官方公告）
- https://docs.docker.com/docker-hub/usage/pulls / https://docs.docker.com/docker-hub/usage （官方文档）
- https://thenewstack.io/revised-docker-hub-policies-unlimited-pulls-for-all-paying-customers （The New Stack 报道）
- https://www.reddit.com/r/kubernetes/comments/1iudj0d/docker_hub_will_only_allow_an_unauthenticated （未认证 10/h 与存储限额推迟）
- Blacksmith / Medium：未认证 10/h 对 CI/CD 冲击最大

## 解读

- 对个人小服务的实际影响很小：自己 VPS 上 `docker compose pull` 登录一下就是 100/h，付费无上限
- 真正痛点是 CI/CD 无认证拉取（10/h）；个人场景可用认证或镜像代理绕开
- 政策方向 2025 转向「对开发者友好」：上调免费额度 + 移除月度上限，此前 2024-2025 初的紧缩（40/h 提案）引发反弹后回调
