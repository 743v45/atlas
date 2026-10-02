# Fly.io 免费额度/计划变动（WebSearch 留档）

- 来源：WebSearch "fly.io free allowances discontinued new users pay-as-you-go"，检索日期 2026-10-02
- 主要出处：
  - https://fly.io/docs/about/discontinued-plans （官方 Discontinued Plans 文档）
  - https://community.fly.io/t/free-tier-is-dead/20651 （官方社区解释 Pay As You Go 过渡）
  - https://www.saaspricepulse.com/tools/flyio
  - https://www.withorb.com/blog/flyio-pricing

## 关键事实

- **2024-10-07 起 Fly.io 对新用户取消永久免费层（legacy free allowances）**：新注册不再送「最多 3 台 shared-cpu-1x 256MB 机器 + 3GB 卷存储」的免费额度。
- 新用户改为**短期试用**（2 machine-hours 或 7 天，先到为准），定位是评估而非永久免费。
- 仅 **2024-10-07 之前购买 Legacy Hobby 计划的老组织**仍保留 3 台 shared-cpu-1x 免费机器 + 3GB 存储（grandfathered）。
- 旧 Hobby 计划（要求 $5/月承诺）被 **Pay As You Go** 取代：无预付、无月度最低消费，按实际用量计费。
- Launch / Scale 计划也已停售（2024-10-07 前购买者可继续用，除非主动转换）。
- Orb 博客指出：官方文档部分页面仍引用 free tier 字样，但新组织实际拿不到——文档与现实有漂移，读文档时要注意。

## 对选型的含义

- 2026 年评估 Fly.io 跑个人小服务，默认假设是**纯按量付费、零免费额度**；「白嫖 3 台 256MB」只属于老用户。
