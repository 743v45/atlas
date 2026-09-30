# 自建后端

> **TL;DR**：自建后端是团队长期维护与多端复用场景的默认——代码与数据资产完全自有、语言框架不限；但要过 ICP 备案+HTTPS+域名白名单三道合规关，运维与安全全部自担。

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 路线条目：云服务器/容器 + Node/Go/Python/Java 等自选框架（Express/NestJS/Gin/Django/Spring Boot 均可），无单一 vendor；小程序经 wx.request/HTTPS 调用 | [1] |
| 合规三关 | 域名 ICP 备案（API 层硬校验：错误码 45082 need icp license）+ 仅 https/wss（错误码 86100）+ 合法域名白名单制（超限错误码 85016；修改频率限制 86102 每月 50 次） | [1][2] |
| 微信集成 | 手动接入：access_token 管理、消息加解密、支付回调验签均自行实现；登录态经 code2session 换取 openid 自管 | [1] |
| 维护活跃度 | —（路线不依赖单一 repo；约束来自微信平台规则，规则页现行有效，采集 2026-10-01） | [1] |

## 为什么选（作为 adopt——团队长期维护/多端复用场景默认）

- **资产完全自有**：代码、数据、部署管线不随小程序生态与任何云厂商政策摆布；后端服务同时服务 App/H5/Web 时是天然形态，小程序只是接入端之一——多端复用场景下「微信专用 API」反而是负债。
- **语言与工具链无抽象损耗**：任意 AI coding 工具、任意框架、任意数据库直接可用；不像 BaaS 有平台 API 抽象边界，也不像云开发有专有数据模型。
- **长期成本确定性**：固定租用成本随包年折扣递减，规模化后固定成本对按量常驻（云托管 1 核 2G 常驻约 85 元/月/实例 [3]）的优势放大——成本结构可预算。

## 合规三关（硬约束，选型前先确认能过）

1. **ICP 备案**：官方网络文档明文「域名必须经过 ICP 备案」，且域名配置 API 直接报错拦截（45082）；第三方文章（百度智能云 2025-10，社区口径）补充：备案主体须与小程序主体一致、海外服务器需走微信特殊申请流程 [1][4]。
2. **HTTPS**：仅支持 https/wss；TLS 1.2+（第三方口径，与官方「https」要求一致），新备案域名 24h 后才可配置 [1][4][5]。
3. **域名白名单**：request/socket/uploadFile/downloadFile 分类别白名单制；官方文档未标数量上限数值——**修正**：流传的「最多 5 个」出自百度智能云 2025-10 文，与官方指引冲突不采信；腾讯云 CloudBase 官方指引写明单类最多 20 个、且修改次数受限（mp 后台 API 每月 50 次 [2]、扫码授权路径每月 5 次 [3]）[1][3][4]。

## 对比

- vs 微信云托管：同为容器/运行时自由；自建多拿机器级控制权与成本确定性，少买「免运维+免白名单+微信就近接入」——团队已有运维能力时自建长期更省 [3]。
- vs 微信云开发/CloudBase：云开发把支付/公众号/鉴权封装成集成（2026-05-28 集成中心），自建这些全是手工合规工程；换来的是数据模型自由与可迁移性 [6]。
- vs Supabase/LeanCloud 等 BaaS：省事维度 BaaS 占优，但资产自有维度全部落败；国内 BaaS 另有 SDK 活性风险（详见 ../leancloud/）。

## 风险与注意

- 运维/安全/证书续期/备份/扩容全自担——三场景中只有「团队长期维护」场景养得起这份负担 [1]。
- 微信侧新能力无法白拿：免鉴权调用开放接口、消息推送免加解密是官方体系特权；access_token 安全保存（官方明文要求存后台服务器）与支付验签自行实现 [1][6]。
- 域名白名单修改有频率限制（每月 50 次 [2]），多环境/灰度域名规划要前置。

## 来源

1. 小程序网络使用规范 — https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html（采集 2026-10-01，留档 raw/2026-10-01/web/wechat-network-doc-developers.weixin.qq.com.md）
2. 快速配置小程序服务器域名 API（错误码表）— https://developers.weixin.qq.com/doc/oplatform/openApi/miniprogram-management/domain-management/api_modifyserverdomaindirectly.html（采集 2026-10-01，留档 raw/2026-10-01/web/wechat-domain-api-errcode-developers.weixin.qq.com.md；错误码数值原文另见 raw/2026-10-01/web/wechat-domain-limit-tavily.json）
3. CloudBase 小程序域名配置指引（单类 20 个/每月修改次数）— https://docs.cloudbase.net/lowcode/practices/miniapp-guide/downloadfile-guide（采集 2026-10-01，留档 raw/2026-10-01/web/wechat-domain-limit-tavily.json）
4. 服务器与业务域名配置全解析 — 百度智能云社区 2025-10-31，https://cloud.baidu.com/article/4626869（第三方：备案主体一致/TLS1.2/海外服务器特殊流程采信为社区口径；「最多 5 个」与官方指引冲突不采信）
5. 微信小程序配置服务器域名和业务域名 — 掘金，https://juejin.cn/post/7023712285273112606（HTTPS+ICP 备案、新备案域名 24h 后可配；采集 2026-09-30，留档 raw/2026-09-30/web/selfhosted-backend-developers.weixin.qq.com.md）
6. 微信云开发官网/集成中心 — https://cloud.weixin.qq.com/cloudbase + https://docs.cloudbase.net/changelog（采集 2026-09-30）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：团队长期/多端复用场景默认；三道合规关与全自担运维为代价 |
