# WebSearch 社区口碑与公司融资检索

- 检索日期: 2026-10-02（WebSearch，检索词附各节）
- 性质：搜索结果摘要，原文帖未逐条点开，论断强度按「社区口碑」对待而非一手事实

## 检索 1：Railway app funding Series B announcement amount

- blog.railway.com/p/series-b：$100M Series B（后续已 WebFetch 官方原文留档）
- FinSMEs 2026-01：领投 TQ Ventures；VentureBeat：总 $124M（前轮 ~$24M）、定位 AI-native cloud 挑战 AWS；Techmeme：总 $130M+

## 检索 2：Railway.app unexpected bill hosting charges reddit complaint

社区口碑要点（2025–2026 帖）：

- r/n8n："Railway cost is 16 USD even when I'm doing absolutely nothing"——闲置也计费（RAM 常驻即计费）的体感抱怨
- r/SaaS："Avoid Railway - The Worst Customer Support I've Experienced"——支持仅工单、无电话/邮箱，账单争议时难触达
- r/node：担心 surprise charges；r/webdev "Is Railway expensive?"：半核+1GB RAM 实测可到 $20/月，定价 "less predictable"；2GB/2 核估 ~$80/月
- r/SaaS "Never host your app on Vercel or Railway"：按量计费超出原型期后不适
- r/webdev "So who's actually moving off Railway?"：可靠性+成本引发的迁离讨论
- 横评共识：Railway 按量账单 "can surprise you as you grow"，必须**主动**设 billing alerts/limits；2026 横评（"7 Railway Alternatives"）直接以 "Railway bill anxiety" 营销平价替代品
- r/webdev 帖："Railway (web app host) 'accidentally enables CDN' causing massive data breaches"——社区报道的 CDN/公开访问配置事故（与 selfhost.dev 文所述 CDN 鉴权缓存泄漏事件呼应）

## 检索 3：railway.com docs usage limit prevent charges workspace settings

- 官方 Cost Control 文档（docs.railway.com/pricing/cost-control，后续已 WebFetch 原文留档）
- station.railway.com 社区问答：hard limit 触顶 "will shut down all deployments"；入口 railway.com/workspace/usage
- Reddit r/node：用户互相推荐开 billing limit 防 surprise charge
