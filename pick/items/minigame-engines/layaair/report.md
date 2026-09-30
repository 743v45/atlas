# LayaAir

> **TL;DR**：3D 小游戏的一等替代——微信面板直出、release 活跃（v3.4.1 2026-08-31），但社区体量与 Cocos 差一档，「90% Web3D 份额」是厂商自述。

- **结论**：trial 试用
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v3.4.1（2026-08-31 发布；v3.3.13 2026-09-17、v3.3.12 2026-07-31，release 节奏健康） | [1] |
| 许可证 | MIT（gh 2026-09-30） | [1] |
| 仓库 | https://github.com/layabox/LayaAir（⭐2,199、pushed 2026-09-24，gh 2026-09-30） | [1] |
| 商业版 | LayaAir 企业版（性能监测/3000 个 Spine/CPU 粒子/AI 生成工具），定价「联系商务」 | [3] |
| 维护活跃度 | release 月更级、pushed 2026-09-24、非 archived（gh 2026-09-30/2026-10-01） | [1] |

## 为什么选（作为 trial 而非 adopt）

- **微信通道健康**：构建面板直出微信小游戏，官方 README 把微信小游戏列为与 H5、原生 App 并列的一键发布目标 [1]；第三方指南称其「早早适配微信、把微信当一等目标」（Cinevva 2026）[4]；微信官方文档同样把 LayaAir 列入推荐引擎文档 [5]。
- **3D 叙事与真实活跃**：CEO 谢成鸿 2024-07 GameLook 演讲称「90% 的 Web3D 微信小游戏用 LayaAir」、百万开发者、坚持「永远开源、永远免费」[2]——份额是厂商自述的检测口径、无第三方复核；GitHub ⭐2,199 与「90% 份额」叙事的反差本身是选型信息：国内商业用户不上 GitHub，star 不代表市场，但也无法证伪份额 [1][2]。
- **不选为 adopt 的理由**：社区/教程体量与 Cocos 差一档（Bilibili 头部 Cocos 教程 77.8 万播放、LayaAir 无同量级公开数据，待验证，2026-09-30 检索）[4][6][7]；引擎运行时不像 Cocos 那样可分离进微信客户端插件，引擎本体占 4MB 首包预算（Cinevva 2026）[4]；同时用过两者的人常把差异描述为「口味问题而非能力问题」（Cinevva 2026）[4]——即没有压倒 Cocos 的硬优势。

## 对比

- vs Cocos Creator：同为编辑器路线、微信一等适配；Cocos 胜在生态厚度与引擎插件省包体，LayaAir 卖点在 3D 工作流偏好与企业版性能工具（3000 个 Spine 同屏等）[3][4]。2D 休闲品类社区共识 Cocos 首选（脉脉 2024-08 引擎选择指南，口径为主观综述）[6]。
- vs Unity 转换：LayaAir 是 TS 技术栈原生 Web 引擎，无转换损耗；Unity 路线面向存量 Unity 工程 [4]。

## 风险与注意

- **公司单一依赖**：引擎由 Layabox（搜游网络）一家商业公司驱动，企业版能力闭源、定价不公开（联系商务，2026-09-30 快照）；「永远免费」是承诺而非条款 [2][3]。
- **份额数据待验证**：90% Web3D 占比仅 CEO 口径（2024-07），其后未见独立统计；采信时注明出处与时间 [2]。
- 多端复用场景注意：README 列出的发布目标含 OPPO/vivo/小米等，但小米已停 Cocos 导出改推快游戏联盟标准（dev.mi.com 2026-09-30 快照）[8]——各渠道引擎支持面动态变化，发布前逐渠道核实。

## 来源

1. GitHub 仓库 — https://github.com/layabox/LayaAir（gh 2026-09-30：⭐2,199、pushed 2026-09-24、MIT；releases gh 2026-10-01：v3.4.1 2026-08-31，留档 raw/2026-10-01/gh/minigame-engines-supplement.md）
2. GameLook — Layabox CEO 谢成鸿：90% 的 Web3D 小游戏用 LayaAir — http://www.gamelook.com.cn/2024/07/548121（2024-07-02，2026-09-30 检索；厂商自述口径）
3. LayaAir 企业版介绍 — https://www.layaair.com/LayaAirEnterprise（2026-09-30：企业普通/服务/VIP 版权益，定价联系商务）
4. Cinevva — WeChat Mini Game Engines (2026) — https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines（2026-09-30 检索：LayaAir 微信一等目标、运行时占包体、与 Cocos 口味之辨）
5. 微信开放文档「学习进阶指南」— https://developers.weixin.qq.com/minigame/dev/guide/develop/develop（2026-09-30）
6. 脉脉 — 微信小游戏引擎选择指南（何永飞，2024-08-12，2026-10-01 检索，留档 raw/2026-10-01/web/cocos-vs-layaair-perf-tvly.json；个人综述口径，降权）
7. Bilibili 教程生态检索快照（2026-09-30：头部 Cocos Creator 3.8.6 教程 77.8 万播放，留档 raw/2026-09-30/web/godot-wechat.md；LayaAir 无同量级公开数据）
8. 小米开发者文档 — 小米小游戏停止 Cocos 导出、迁移快游戏联盟标准公告 — https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2165（2026-09-30 检索，留档 raw/2026-09-30/web/unity-transform-releases.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：微信通道健康+3D 工作流偏好场景可用；生态厚度与包体机制不如 Cocos，未给 adopt |
