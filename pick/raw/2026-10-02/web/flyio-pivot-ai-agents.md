# Fly.io 公司转向 AI agent（WebSearch 留档）

- 来源：WebSearch "fly.io company 2025 2026 AI agents GPU pivot away from web app hosting"，检索日期 2026-10-02
- 主要出处：
  - https://daily.dev/posts/fly-io-pivots-to-ephemeral-cloud-computers-for-ai-agents-names-new-ceo-v9mpmy2bi
  - https://blog.cloud66.com/every-deployment-platform-is-pivoting-to-ai-day-2-operations-aren-t-going-anywhere
  - https://nqz.ai/blog/roast-fly-io-day1
  - https://fly.io/news/fly-io-launches-computers-for-agents （官方公告）
  - https://community.fly.io/t/gpu-migration-fly-io-gpus-will-be-deprecated-as-of-july-31-2026/27110
  - https://community.fly.io/t/will-the-apps-and-machine-platform-start-winding-down/28380/7
  - https://elixirforum.com/t/now-that-fly-are-pivoting-should-i-trust-them-for-hosting/76144

## 关键事实（检索日 2026-10-02）

- **公司全面转向「Computers for Agents」（产品名 Sprites）**：为 AI 编码 agent 提供临时云计算机。创始人 Kurt Mackey 宣布整个公司转型；官网首页 100% 以「Computers for agents」为主打，传统 app 托管平台不再出现在首屏。
- 为此方向**新融资 $25M**（官方公告：给 agent 真实的计算机——持久磁盘、安全连接、可扩到数百万实例）。
- **换新 CEO**（daily.dev 报道标题提及 names new CEO）。
- **GPU 全面弃用：2026-07-31 截止**（邮件通知客户）——社区视为平台收缩信号。
- 社区出现「apps and machine platform 会不会跟着关停」的疑问；Fly.io 员工回应：GPU 用户极少、运营成本高所以砍掉，而 **fly machines（核心 VM 平台）用户「many, many」**，暗示核心平台不会关。
- 客户信任受损实锤：Elixir Forum 出现「Now that fly are pivoting, should I trust them for hosting?」主题帖，已有用户迁往 AWS Fargate；Cloud 66 博客称「每个部署平台都在转向 AI」，传统用户的 Day 2 运维成悬问。

## 对选型的含义

- 2026-10 时点选 Fly.io 跑个人 web 服务 = 把小服务放在一家「战略重心已不在你这类客户」的公司上——存续风险与优先级风险都上调；但核心 Machines 平台用户基数仍大、官方口头承诺不关。
