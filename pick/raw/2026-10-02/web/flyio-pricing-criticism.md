# Fly.io 定价复杂度/意外账单口碑（WebSearch 留档）

- 来源：WebSearch "fly.io pricing complexity surprise bill criticism reddit hacker news 2025"，检索日期 2026-10-02
- 主要出处：
  - https://www.reddit.com/r/selfhosted/comments/1pri1wo/is_flyio_that_bad_or_were_we_that_stupid_or_is （$1,200–1,500/月账单 + 差 uptime 的用户）
  - https://www.reddit.com/r/elixir/comments/1h8ajm2/is_flyio_ridiculously_expensive （r/elixir 定价吐槽；<$5/月不收费；Pay As You Go）
  - https://news.ycombinator.com/item?id=48688835 （对比固定 $1.94/月的竞品；带宽是唯一不可控变量）
  - https://news.ycombinator.com/item?id=31390506 （「Heroku 魔法继承者」帖：billing UI「weird and cobbled together」）
  - https://news.ycombinator.com/item?id=41985410 （Fly 用 Metronome 解决 usage-based billing；网友承认其定价变量多：区域×机型×带宽）
  - https://community.fly.io/t/why-is-my-bill-so-ridiculously-high/19164
  - https://community.fly.io/t/how-concerned-should-i-be-about-a-surprise-bill/5811

## 口碑三主题

1. **带宽/用量的不可预测性导致意外账单**（bandwidth 是最常被点名的变量；出站 $0.02/GB 起，但亚太/南美 $0.04、非洲 $0.12——流量型服务在偏远区会痛）
2. **多变量定价的心智负担**：区域加价（1.0–1.615）× 机型 × 带宽分区（granular vs non-granular 组织）× 快照/卷/IP 附加费——账单构成复杂
3. **可靠性差评与高账单叠加放大不满**（与故障史记录互证）

## 缓解面（同一批讨论里也提到）

- <$5/月的小账单不收费（Pay As You Go 下小微用户实际常月付 $2–5）
- 个人小服务（低流量）场景下费用高度可预测（~$2–5/月/台），恐怖账单故事多来自流量型/多机型业务
