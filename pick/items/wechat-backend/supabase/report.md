# Supabase

> **TL;DR**：开源 Postgres BaaS 头部（⭐111k，pushed 2026-09-30）——出海场景的默认后端；国内无节点、直连偏慢但不用梯子可用，且 *.supabase.co 过不了小程序域名备案关——国内主线不选。

- **结论**：trial 试用
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0（supabase/supabase 仓库） | [1] |
| 仓库 | https://github.com/supabase/supabase | — |
| 维护活跃度 | ⭐110,941、pushed 2026-09-30（gh 2026-10-01 刷新） | [1] |
| 能力面 | Postgres 数据库 + Auth + Storage + Realtime + Edge Functions + 自动 REST/GraphQL API + RLS 行级安全 | [1][2][5] |
| 计费 | 免费档（最多 2 项目）；Pro $25/月才有自定义域名（一手博客口径，价格采集 2026-09-30）；支付走 Visa/MasterCard（营销来源印证，打折采信） | [2][4] |

## 为什么选（作为 trial——出海/海外用户场景）

- **出海正解**：用户在海外时，海外节点+OAuth 全家桶+Postgres 生态是最顺组合——竞品 CloudBase 官方博客也这么分流（出海产品推荐 Next.js+Supabase+Vercel+Stripe，利益相关但方向与第三方一手体验互证）[3]。
- **Postgres 是迁移保险**：数据层是标准 Postgres，标准 SQL/迁移工具链成熟；自托管路径存在（开源），阿里云 AnalyticDB 已推 Supabase 兼容服务（帮助文档 2026-07-01 更新）——国内兼容生态在出现 [1][6]。
- **零运维+RLS 数据层安全模型**：行级安全策略在数据库层隔离用户数据，Auth/Storage/Realtime 一体 [5]。

## 为什么不是国内主线

- **域名合规关就过不了**：小程序 request 合法域名必须 ICP 备案且不支持 IP/无法备案的境外域名（官方规则 + API 层 45082 错误码硬拦截）——*.supabase.co 无法成为合法域名，国内小程序直连在配置层就卡死；只能经自有中转层（云函数/云托管/自建网关），「BaaS 免后端」价值被架空 [1][7]。
- **国内无节点是物理问题**：数据库与 API 全在海外，前端在国内也要跨境调用；Pro 也改变不了（CloudBase 官方博客口径）[3]。
- **实测口碑**：一手体验（kuizuo.me 博客）——国内请求偏慢但不用梯子、慢点可接受（个人项目口径；博客无发布日期，以采集日 2026-09-30 为准）。具体延迟数值：跨境 300-800ms 是同博客生态的 Vercel 前端对照数据，Supabase 本体无系统实测；YesApi 营销页称 200-500ms+（营销来源打折采信）——**待验证**：2026 年国内直连拨测 [2][3][4]。
- **微信集成零原生**：无 openid 免鉴权、无支付集成、无域名豁免；企业级授权欠缺——不支持 OIDC 提供者与原生 RBAC（Logto 博客口径），多租户 SaaS 场景需外挂身份层 [5]。

## 对比

- vs 微信云开发：镜像对手——云开发有微信私有协议/支付/备案链路而无 Postgres 生态，Supabase 反之；选型问句是「用户在国内还是海外」[3][7]。
- vs LeanCloud：同为第三方 BaaS，LeanCloud 国内合规无忧但 SDK 冻结（详见 ../leancloud/）；Supabase 生态活跃但国内链路不通——国内第三路线目前没有健康选项 [3][6]。
- 自托管替代路径：开源可自托管到国内云，但 CloudBase 博客观点成立——自托管等于把免运维初衷搬回来，且失去托管生态 [3]。

## 风险与注意

- 跨境延迟不可通过配置消除（物理距离）；高峰期波动是常态口径 [3]。
- 数据出境合规：涉及个人信息的境内业务数据存境外有合规风险——国内 C 端业务直接排除 [3][4]。
- 免费档限制与暂停策略的 2026 现状**待验证**（免费 2 项目口径来自博客，无官方快照留档）[2]。

## 来源

1. 小程序网络使用规范 + 域名配置 API 错误码 — https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html、https://developers.weixin.qq.com/doc/oplatform/openApi/miniprogram-management/domain-management/api_modifyserverdomaindirectly.html（采集 2026-10-01，留档 raw/2026-10-01/web/）
2. 将 Supabase 作为下一个后端服务 — kuizuo.me 一手体验博客（采集 2026-09-30，留档 raw/2026-09-30/web/supabase-cn-latency.md）
3. 2026 一人公司技术架构：替掉 Next.js+Supabase+Vercel 这套 — CloudBase 官方博客 2026-04-22，https://tcb.cloud.tencent.com/blog/2026/04/22/solo-company-tech-stack-2026（竞品立场，与 [2] 互证；留档同上）
4. YesApi「Supabase 国内替代」营销页 — https://www.yesapi.cn/blog/supabase-china-alternative.html（营销来源，数据打折采信；留档同上）
5. 为什么 AI 初创公司选择 Supabase 以及它的不足之处 — Logto 博客，https://blog.logto.io/zh-CN/supabase-ai-limitation（采集 2026-09-30）
6. 阿里云 AnalyticDB Supabase 兼容文档 — https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/supabase（页面更新 2026-07-01）
7. GitHub — https://github.com/supabase/supabase（gh 2026-10-01 刷新：⭐110,941、pushed 2026-09-30、Apache-2.0；首次采集 2026-09-30 ⭐110,932 留档 raw/2026-09-30/gh/）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：出海场景默认；国内主线因域名备案关+无节点不选 |
