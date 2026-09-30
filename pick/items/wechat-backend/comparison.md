# 微信小程序后端方案 · 横评

> 主题：小程序的后端放哪——官方 serverless、官方容器托管、自建、第三方 BaaS 四路线五个条目。
> 用户画像：通用视角按场景分流——个人快速开发 / 团队长期维护 / 多端复用三场景；主评微信端表现。
> 数据核查日：2026-09-30（gh/npm 一手数据、价格页与官方文档当日采集；域名规则补充采集 2026-10-01）。原始留档 `raw/2026-09-30/` 与 `raw/2026-10-01/`。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| 个人快速开发（默认答案） | **微信云开发 / CloudBase** | 免鉴权+集成中心把支付/公众号接入压到最低，免费 6 个月+¥19.9/月起 [1][8] |
| 存量服务迁移 / 任意语言运行时 | **微信云托管** | 容器免改造上云，callContainer 免鉴权且免域名白名单 [2][3] |
| 团队长期维护 / 多端复用（默认答案） | **自建后端** | 资产完全自有、后端不随平台政策摆布；三道合规关是固定成本 [3][4] |
| 出海 / 海外用户 | **Supabase** | Postgres 生态+零运维；国内小程序主线不选（域名备案关+无节点）[3][5] |
| 国内第三方 BaaS 补位 | LeanCloud 观望 | 服务在营但 SDK 双端冻结 3-5 年，新项目无理由入坑 [6] |

## 属性对比矩阵

| 维度 | 云开发/CloudBase | 微信云托管 | 自建后端 | Supabase | LeanCloud |
|---|---|---|---|---|---|
| 形态 | 官方 Serverless BaaS [1] | 官方容器托管 [2] | 云服务器+自选框架 [4] | 开源 BaaS（Postgres）[5] | 国内老牌 BaaS [6] |
| 微信集成 | **免鉴权·原生最深**：云函数私有协议+集成中心微信支付/公众号一键接入 [1][7] | **免鉴权·免域名白名单**：callContainer 私有协议 [2][3] | 手动：三道合规关+access_token/验签自管 [3][4] | 无：*.supabase.co 过不了备案关，须中转层 [3][4] | 有小程序 SDK，无免鉴权深集成 [3][6] |
| 计费（2026-09-30 查询） | 免费环境 6 个月；基础套餐 ¥19.9/月（40,000 资源点/月，1 点=¥0.001）[1][8] | 按量：实例 ¥0.02975/时起、数据库算力 ¥0.0855/时起；免费额度 3 个月 [2] | 服务器固定租用+域名/证书/备份自购 | 免费档（2 项目）；Pro $25/月有自定义域名 [5] | 开发版免费；商用版最低消费 30 元/天、API 1.0 元/万次 [6] |
| 运维负担 | 零运维 | 低（免运维，冷启动可设常驻消除） | 高（部署/证书/备份/安全全自管） | 零运维 | 零运维 |
| 锁定风险 | 高（专有数据模型/云函数 API） | 中（容器镜像可迁） | 低（资产自有） | 低-中（Postgres 标准接口） | 中高（专有 API，SDK 冻结放大） |
| 多端能力（参考列，不计权） | 中：公众号/Web/多端 SDK 支持但走云开发专用 API [1] | 中：容器即通用服务，天然多端可接 [2] | 高：API 自定义，任何端可接 | 高：Postgres+REST，任何端可接 [5] | 中：多端 SDK 齐全但均为专有 API [6] |
| AI 工具链（2026） | **活跃**：AI Toolkit MIT ⭐1,129 pushed 2026-09-30，Skills/MCP/插件生态 [9] | 无专门工具链 | 任意 AI coding 直接可用 | 社区 MCP 生态丰富 | 无 |
| 维护活跃（2026-09-30） | 平台月度发版（2026-06 AI 工具/2026-05-28 集成中心）[7] | 官网/定价页现行口径在线 [2] | —（路线条目） | pushed 2026-09-30，⭐110,941（gh 2026-10-01）[10] | SDK 双端冻结：JS 2023-10 / leanengine 2021-08 [6][11] |
| verdict | **adopt** | trial | **adopt** | trial | hold |

## 结构性结论（2026-09-30 / 10-01 快照）

1. **后端层与前端框架层正交**：Taro/uni-app/原生等任何前端框架都能配任何后端；唯一的例外级差异是微信原生集成深度——云开发免鉴权、云托管 callContainer 免域名白名单是平台特权，其余路线都要过 ICP 备案+HTTPS+白名单三关 [1][2][3][4]。
2. **「官方 serverless」与「腾讯云产品」的边界已变化**：微信云开发与腾讯云 CloudBase 同栈同计费（资源点模式、同一份更新日志），平台定位转型「AI 原生后端一体化平台」，2026-05-28 上线集成中心（微信支付/公众号一键接入）；微信侧入口保留但叙事升维——配合微信「AI 应用及线上工具小程序成长计划」（激励期 2026 全年，云开发资源/AI 算力在激励包内），官方后端从「小程序配套」变成「AI 后端入口」[1][7][12]。
3. **合规三关是自建路线的真实门槛，官方两条线全部绕开**：ICP 备案（API 层 45082 硬拦截）+ 仅 https/wss + 合法域名白名单（修改限频）[3][4]；云托管 callContainer 被官方文档明文豁免域名配置 [3]。选型本质是「用锁定换合规」。
4. **BaaS 看 SDK 活性不看公司存续**：LeanCloud 公司在营（价格页活跃）但 SDK 双端冻结 3-5 年；对照 CloudBase 旧工具链（cloudbase-cli/cloudbase-framework 已 archived）与 npm SDK 2026-09 仍在发版——判断健康度的指标是包管理器最后发版时间 [6][9][11]。

## 决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖所列维度；维度外风险（工具链拆旧建新、SDK 冻结、跨境延迟、锁定）以各条目 verdict 为准——自建后端矩阵分低于云托管而「团队长期场景 adopt」并存不是矛盾：矩阵度量通用画像综合值（微信集成权重最高），verdict 按三场景分流。

## 来源

1. 微信云开发官网与价格计算器 — https://cloud.weixin.qq.com/cloudbase + https://cloud.weixin.qq.com/cloudbase/price（采集 2026-09-30，留档 raw/2026-09-30/web/）
2. 微信云托管官网与产品定价 — https://cloud.weixin.qq.com + https://developers.weixin.qq.com/minigame/dev/wxcloudrun/src/Billing/price.html（采集 2026-09-30，留档 raw/2026-09-30/web/）
3. 小程序网络使用规范（callContainer 免域名/域名规则原文）— https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html（采集 2026-10-01，留档 raw/2026-10-01/web/wechat-network-doc-developers.weixin.qq.com.md）
4. 域名配置规则与第三方解析 — https://developers.weixin.qq.com/doc/oplatform/openApi/miniprogram-management/domain-management/api_modifyserverdomaindirectly.html（错误码表，留档 raw/2026-10-01/web/wechat-domain-api-errcode-developers.weixin.qq.com.md）、https://docs.cloudbase.net/lowcode/practices/miniapp-guide/downloadfile-guide（采集 2026-10-01，留档 raw/2026-10-01/web/wechat-domain-limit-tavily.json）、百度智能云 2025-10 文（第三方，留档 raw/2026-09-30/web/selfhosted-backend-developers.weixin.qq.com.md）
5. Supabase — https://github.com/supabase/supabase（gh 2026-09-30）+ kuizuo.me 一手体验 + CloudBase 官方博客 2026-04-22（留档 raw/2026-09-30/web/supabase-cn-latency.md）
6. LeanCloud — https://www.leancloud.cn/pricing（2026-09-30）+ npm leancloud-storage/leanengine（2026-09-30 / 2026-10-01）
7. CloudBase 平台更新日志 — https://docs.cloudbase.net/changelog（采集 2026-09-30，留档 raw/2026-09-30/web/cloudbase-changelog-docs.cloudbase.net.md）
8. 微信云开发计费说明 — https://developers.weixin.qq.com/minigame/dev/wxcloud/billing/price.html（采集 2026-09-30）
9. CloudBase AI Toolkit + @cloudbase/js-sdk npm — https://github.com/TencentCloudBase/CloudBase-AI-Toolkit（gh 2026-09-30）+ https://registry.npmjs.org/@cloudbase/js-sdk（2026-09-30）
10. supabase/supabase — gh 2026-09-30
11. leancloud/javascript-sdk gh + leanengine npm — gh 2026-09-30 / npm 2026-10-01（留档 raw/2026-10-01/web/leanengine-npmjs.com.md）
12. AI 应用及线上工具小程序成长计划（激励期 2026 全年）— 阿思达克财经报道，留档 raw/2026-09-30/web/ant-design-mini-wechat.md
