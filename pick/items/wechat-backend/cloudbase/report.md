# 微信云开发 / CloudBase

> **TL;DR**：微信小程序后端的官方 serverless 默认（并入腾讯云 CloudBase 后转型 AI 原生一体化平台）——免鉴权+集成中心把微信支付/公众号接入压到最低成本，个人快速开发首选；代价是腾讯专有栈锁定与计费口径更迭。

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 官方 Serverless BaaS：云函数（微信私有协议天然鉴权）/云数据库（文档型）/云存储/静态托管/扩展能力；微信侧入口 cloud.weixin.qq.com/cloudbase，平台侧为腾讯云 CloudBase | [1][6] |
| 计费 | 免费云环境 40,000 资源点/月（可体验 6 个月，不支持按量付费）；基础套餐 ¥19.9/月（原价 ¥39，含 40,000 资源点/月，支持加购资源包与按量付费）；1 资源点 = ¥0.001（价格查询 2026-09-30） | [1][2] |
| 资源点模式 | 2026-01-16 上线，替代「套餐额度+加购资源」固定额度模式，覆盖全套现网套餐；2026-06-17 起内置 AI 模型调用转资源点计费 | [3][6][7] |
| 维护活跃度 | 平台更新日志持续月度发版（2026-06 AI 开发工具/2026-05-28 集成中心/2026-03-30 ICP 备案）；npm @cloudbase/js-sdk 最新 3.10.1（2026-09-23 发版，距核查日 7 天） | [3][4] |
| AI 工具链 | CloudBase AI Toolkit（MIT，⭐1,129，pushed 2026-09-30）：面向 AI coding agents 的数据库/认证/云函数接入，经 Plugin、Skills 与 MCP | [5] |

## 为什么选（作为 adopt——个人/快速开发场景默认）

- **免鉴权是微信集成深度的天花板**：云函数走微信私有协议天然鉴权，免维护 access_token 与证书、免鉴权调用微信开放接口；云数据库/云存储可在小程序端直接调用——这三件事在自建路线里分别是鉴权工程、凭证管理与 API 封装 [1][6]。
- **微信支付/公众号接入成本被压到最低**：2026-05-28 上线集成中心，微信支付（小程序/JSAPI/Native）与公众号封装为开箱即用的「集成」——凭证统一托管、回调代收代验、一键部署云函数；自建路线里支付回调验签与凭证安全是数天的合规工程 [3]。
- **免费层真实可用、起步价低**：新用户免费云环境体验 6 个月，基础套餐 ¥19.9/月；官方案例口径「月花费数百元实现千万销售额」（营销案例，打折采信）[1][2]。
- **多端与合规路径在打通**：2026-03-30 起云开发环境可作为云资源进行 ICP 备案；官网定位除小程序外支持公众号、网页等多形态业务 [3][6]。
- **AI 原生转型带来新的工程价值**：AI Toolkit 活跃维护（pushed 2026-09-30），2026-06 上线插件生态（Codex/Claude Code 一键装）+ PostgreSQL 支持 + API Key 认证；微信「AI 应用及线上工具小程序成长计划」激励期 2026 全年，云开发资源与 AI 算力在激励包内 [5][3][8]。

## 对比

- vs 微信云托管：同属官方体系、同享私有协议免鉴权；云开发管「新建轻应用」（函数+文档库+BaaS 一件套），云托管管「存量服务/自定义运行时」（容器，任意语言）[1][9]。
- vs 自建后端：自建的优势是资产自有与多端通用；但要过 ICP 备案+HTTPS+域名白名单三关，且支付/公众号接入全部手工——云开发用专有 API 换掉三关，也换掉了可迁移性 [9][10]。
- vs Supabase：Supabase 是 Postgres 生态与出海正解；但免鉴权/支付集成/备案链路它一个都没有，国内小程序直连连域名白名单都过不了（详见 ../supabase/）[10]。

## 风险与注意

- **锁定是结构性的**：专有数据模型与云函数 API，迁出要重写数据层与调用层；官方工具链有拆旧建新史——cloudbase-cli、cloudbase-framework 均已 archived（gh 2026-09-30），选型按平台能力投而不是按单个工具投 [11]。
- **计费口径 2026 年内两次更迭**：2026-01-16 资源点制替代套餐额度；2026-06-17 内置模型调用转资源点；微信侧文档仍存在旧「基础配额」口径（调用次数 20 万次/容量 2GB/云函数资源使用量 10 万 GBs，价格同为 ¥19.9/月）与资源点口径并存——成本模型按资源点口径算，交叉核对两份官方文档 [1][2][3][7]。
- 免费环境 6 个月到期转付费；免费层超量不可用（不支持按量付费），需升基础套餐 [1][2]。
- 待验证：云函数冷启动对 C 端体验的量化影响（无 2026 年官方数据）；云托管可设常驻消除冷启动，云开发函数侧无对等公开选项 [9]。

## 来源

1. 微信云开发价格计算器 — https://cloud.weixin.qq.com/cloudbase/price（采集 2026-09-30，留档 raw/2026-09-30/web/wechat-cloudrun-cloud.weixin.qq.com.md）
2. 微信云开发计费说明（微信开放文档）— https://developers.weixin.qq.com/minigame/dev/wxcloud/billing/price.html（采集 2026-09-30，留档同上）
3. CloudBase 平台更新日志 — https://docs.cloudbase.net/changelog（采集 2026-09-30，留档 raw/2026-09-30/web/cloudbase-changelog-docs.cloudbase.net.md）
4. @cloudbase/js-sdk npm — https://registry.npmjs.org/@cloudbase/js-sdk（2026-09-30，留档 raw/2026-09-30/web/cloudbase-npmjs.com.md）
5. CloudBase AI Toolkit — https://github.com/TencentCloudBase/CloudBase-AI-Toolkit（gh 2026-09-30：⭐1,129、pushed 2026-09-30、MIT）
6. 微信云开发官网 — https://cloud.weixin.qq.com/cloudbase（采集 2026-09-30，留档 raw/2026-09-30/web/wechat-cloudbase-merge-tencent.com.md）
7. CloudBase 价格文档（腾讯云官方）— https://cloud.tencent.com/document/product/876/75213（采集 2026-10-01，个人版 ¥19.9 与免费体验/AI 小程序成长计划章节在页；留档 raw/2026-10-01/web/cloudbase-price-cloud.tencent.com.md——微信侧 vs 腾讯云侧交叉核对：资源点口径以微信侧价格页全文为准）
8. AI 应用及线上工具小程序成长计划（激励期 2026 全年）— 阿思达克财经/Yahoo 财经报道，留档 raw/2026-09-30/web/ant-design-mini-wechat.md
9. 微信云托管官网与产品定价 — https://cloud.weixin.qq.com + https://developers.weixin.qq.com/minigame/dev/wxcloudrun/src/Billing/price.html（采集 2026-09-30）
10. 小程序网络使用规范 — https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html（采集 2026-10-01，留档 raw/2026-10-01/web/wechat-network-doc-developers.weixin.qq.com.md）
11. gh api — TencentCloudBase/cloudbase-cli、Tencent/cloudbase-framework（2026-09-30，均 archived，留档 raw/2026-09-30/gh/）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：个人/快速开发场景默认答案；锁定与计费口径更迭为主要代价 |
