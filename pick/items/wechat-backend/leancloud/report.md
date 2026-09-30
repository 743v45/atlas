# LeanCloud

> **TL;DR**：国内 BaaS 老兵服务仍在营（价格页活跃、商用版最低消费 30 元/天），但客户端 JS SDK 自 2023-10、服务端 leanengine 自 2021-08 起无新版，微信端无深度集成——新项目观望。

- **结论**：hold 观望
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | SDK MIT（leancloud/javascript-sdk）；服务为商业闭源托管 | [1] |
| 仓库 | https://github.com/leancloud/javascript-sdk（客户端 JS SDK） | — |
| 维护活跃度 | JS SDK ⭐341、pushed 2024-07-04、未 archived（gh 2026-09-30）；npm leancloud-storage 最新 4.15.2 发布于 2023-10-11——主版本近 3 年无新版；服务端 Node SDK leanengine 最新 3.8.0 发布于 2021-08-03——5 年无新版；聚合仓 leancloud/leancloud-sdk 已 archived | [1][2][7] |
| 公司存续 | leancloud.cn 价格页在线且含在售套餐（采集 2026-09-30）；国际版 leancloud.app 独立运营；官网宣称服务 240,000+ 开发者（营销口径） | [3][4] |
| 计费 | 开发版免费（API 请求 3 万次/天、并发 3 线程、无自动备份）；商用版按量+最低消费 30 元/天：数据存储 API 请求 1.0 元/万次、存储 0.10 元/GB/天、云引擎 512MB 2 元/天、即时通讯登录用户 15 元/万人/天、文件存储 0.16 元/GB/月、HTTPS 流量 0.36 元/GB（价格查询 2026-09-30） | [3] |

## 为什么不选（hold——新项目不推荐的原因）

- **「公司在营、SDK 冻结」的反差是核心风险**：BaaS 的价值在 SDK/API 持续演进——新微信基础库、新平台能力的适配都经 SDK 发放；客户端主版本冻结近 3 年（2023-10）、服务端 SDK 冻结 5 年（2021-08）意味着适配与新特性支持无人承诺。判断 BaaS 健康度应看包管理器最后发版时间而非公司是否存活 [1][2][7]。
- **微信集成无深度优势**：有小程序 SDK 与微信小程序解决方案页，但无免鉴权/私有协议/集成中心级别的深集成——微信集成维度被官方云开发全面覆盖；省事优势不成立 [3][6]。
- **价格模式偏旧世代**：商用版 30 元/天最低消费（≈900 元/月门槛）+按活跃用户日计费，对比云开发免费 6 个月+¥19.9/月资源点制，新项目起步成本结构劣势明显（价格均查询于 2026-09-30）[3][6]。
- 曾有的位置：AVOS Cloud 2013-09 上线、2014 年独立运营（爱分析历史报道，约 2016-2017 口径），服务知乎/新东方等中大型客户——历史口碑真实，但不改变当下 SDK 冻结的事实 [8]。

## 对比

- vs 微信云开发/CloudBase：同为国内 BaaS，云开发有私有协议免鉴权+2026 年仍在演进的 AI 工具链（AI Toolkit pushed 2026-09-30），LeanCloud 无一项 [3][6]。
- vs Supabase：镜像短板——LeanCloud 国内节点/合规无忧但 SDK 冻结；Supabase 生态活跃但国内链路不通；两者对比说明国内第三方 BaaS 路线当前没有健康选项 [3][5]。
- vs 自建：LeanCloud 省运维，但专有 API 迁移成本高，且 SDK 冻结放大锁定风险 [1][2]。

## 风险与注意

- 存量用户注意：SDK 双端冻结下，安全补丁与新基础库适配无发版承诺；续费前评估迁移路径（数据导出→Postgres/文档库）[1][2]。
- 待验证：LeanCloud 2026 年是否有 SDK 维护恢复或商业路线调整的官方公告（本次仅核到价格页与官网在营证据）[3][4]。

## 来源

1. GitHub leancloud/javascript-sdk — https://github.com/leancloud/javascript-sdk（gh 2026-09-30：⭐341、pushed 2024-07-04、MIT）
2. leancloud-storage npm — https://registry.npmjs.org/leancloud-storage（2026-09-30，留档 raw/2026-09-30/web/leancloud-npmjs.com.md）
3. LeanCloud 国内站价格页 — https://www.leancloud.cn/pricing（采集 2026-09-30，留档 raw/2026-09-30/web/leancloud-pricing-leancloud.cn.md）
4. LeanCloud 国际版 — https://leancloud.app/pricing（采集 2026-09-30，留档 raw/2026-09-30/web/leancloud-status-2026.md）
5. Supabase 条目报告 — ../supabase/
6. 微信云开发官网与价格 — https://cloud.weixin.qq.com/cloudbase + https://cloud.weixin.qq.com/cloudbase/price（采集 2026-09-30）
7. leanengine npm（服务端 Node SDK）— https://registry.npmjs.org/leanengine（2026-10-01，留档 raw/2026-10-01/web/leanengine-npmjs.com.md）+ leancloud/leancloud-sdk（gh 2026-09-30，archived）
8. LeanCloud：BaaS 端切入云服务 — 爱分析（历史背景报道，约 2016-2017 口径），留档 raw/2026-09-30/web/leancloud-status-2026.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | hold | 首次记录：公司在营但 SDK 双端冻结 3-5 年，新项目观望 |
