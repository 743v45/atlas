# Cocos Creator

> **TL;DR**：微信小游戏的默认答案——官方文档推荐+引擎插件（引擎可留客户端）+一站式构建，2D/3D 全覆盖、编辑器免费，新项目首选。

- **结论**：adopt 推荐
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 引擎版本 | Cocos Creator 3.8.x 稳定线，3.8.6 发布于 2025-04-02；docs 已上线 4.0 手册 | [3][6] |
| 许可证 | MIT（仓库 LICENSE.md 全文为 MIT 文本，署名 Chukong/Yaji；GitHub API 标 NOASSERTION/Other，已人工解码 2026-10-01，留档 `raw/2026-10-01/gh/minigame-engines-supplement.md`） | [1] |
| 仓库 | https://github.com/cocos/cocos-engine（⭐9,837、pushed 2026-09-21，gh 2026-09-30） | [1] |
| 编辑器授权 | 免费下载；企业支持/定制工具/更多授权类型走商务合作（cocos.com 2026-10-01） | [2] |
| 维护活跃度 | 引擎仓库 pushed 2026-09-21、非 archived（gh 2026-09-30） | [1] |

## 为什么选（作为 adopt）

- **微信端事实标准**：微信官方「学习进阶指南」把 Cocos Creator 与 LayaAir 列为推荐直接阅读文档的游戏引擎，并明确说引擎已针对小游戏平台做好适配、开发者无需关注底层 [7]；Cocos 官方文档提供微信小游戏一键构建（Build 面板选平台、AppID、开放数据域模板、引擎原生代码分包、分离引擎即微信小游戏引擎插件、高性能模式开关）[3]。
- **包体分水岭优势**：引擎可经「微信小游戏引擎插件」分离——引擎部分由微信客户端内置，不占游戏包体；而 LayaAir 等引擎运行时要占自己的包预算（Cinevva 2026：对 4MB 里每一 KB 都要抠的 3D 游戏，Cocos 内置插件可能是决定性因素）[4]。现行包体口径：主包 ≤4MB、超出走远程资源（微信官方限制，经 Cocos 文档转述，2026-09-30 快照）[3]；主包+所有分包合计 ≤30MB、单个普通分包不限制大小（微信「分包加载」官方文档，2026-10-01 快照）[9]。
- **教程与生态最厚**：Bilibili 上 Cocos Creator 3.8 系统教程播放量 77.8 万（2026-09-30 快照检索）[6]；微信 2026 年 IAP 首发 110% 激励（基础 70%+首发 40%，上限 400 万）等商业化政策生态亦以 Cocos 教程覆盖最全 [5][8]。
- **多端出口宽**：一套工程发布微信/抖音/支付宝/OPPO/vivo/小米及原生 App（引擎 README 自述 + 各平台构建文档）[1][3]——多端能力见 comparison.md 参考列，不计入决策权重。

## 对比

- vs LayaAir：同为微信一等适配+编辑器路线；差异在 Cocos 引擎可入微信插件省首包、社区体量大一档，LayaAir 主打 3D 工作流叙事（详见 `../layaair/`）[4]。
- vs Unity 转换：Unity 路线是「存量项目移植工具」，4MB 首包对 Unity WebGL 构建极其残酷；新项目无 Unity 存量时不构成对手（详见 `../unity-transform/`）[4]。
- vs 渲染库（pixi/three）与裸 Canvas：微信官方对 PixiJS/ThreeJS 路线的口径是「可以做但要自己适配、不推荐无经验开发者」[7]。

## 风险与注意

- **引擎与编辑器是两回事**：GitHub 上开源的是引擎（MIT）；编辑器本体闭源免费分发，企业服务/定制授权走商务——商用前核对 cocos.com 当时口径（2026-10-01 快照：无按席订阅、无流水分成）[2]。
- **高性能模式是双刃剑**：iOS 高性能模式显著提 FPS 但内存上限收紧（2GB RAM 机型限 1GB、3GB 机型限 1.4GB，超限崩溃；eastondev 2026-05 实测记录，待官方一手复核）[5]。
- **渠道端政策变动**：小米澎湃 OS 已公告停止 Cocos 导出、要求迁移快游戏联盟标准（dev.mi.com，2026-09-30 快照检索）[10]——多端复用场景发布前逐渠道核实现状。
- 微信小游戏发布需要版号/资质流程（IAP 变现），技术选型之外的时间成本要预留 [5]。

## 来源

1. GitHub 仓库 — https://github.com/cocos/cocos-engine（gh 2026-09-30：⭐9,837、pushed 2026-09-21；license 解码 2026-10-01 留档 raw/2026-10-01/gh/minigame-engines-supplement.md）
2. Cocos 官网产品页 — https://www.cocos.com/creator（2026-10-01：免费下载、企业服务/授权商务入口）
3. Cocos Creator 4.0 手册「发布到微信小游戏」— https://docs.cocos.com/creator/4.0/manual/zh/editor/publish/publish-wechatgame.html（2026-09-30：主包 4MB、分离引擎/引擎插件、高性能模式、开放数据域）
4. Cinevva — WeChat Mini Game Engines (2026) — https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines（2026-09-30 检索：引擎烘焙进微信客户端、与 LayaAir/Unity 对比；第三方指南，作口碑参照）
5. Easton 开发日志 — Cocos Creator 微信小游戏构建调试完全指南 — https://eastondev.com/blog/zh/posts/dev/20260522-cocos-wechat-mini-game-build（2026-05-22 发布/2026-07-14 修改，2026-09-30 检索：高性能模式实测、2026 激励政策、包体与内存限制）
6. Cocos Creator 3.8.6 发布公告（cocos.com，2025-04-02，留档 raw/2026-09-30/web/cocos-creator-wechat.md）+ Bilibili 教程生态检索（2026-09-30，留档 raw/2026-09-30/web/godot-wechat.md）
7. 微信开放文档「学习进阶指南」— https://developers.weixin.qq.com/minigame/dev/guide/develop/develop（2026-09-30：官方推荐 Cocos Creator/LayaAir 文档；PixiJS/ThreeJS 需 weapp-adapter 不推荐新手）
8. 微信开放文档「2026 年微信小游戏虚拟支付激励政策」— https://developers.weixin.qq.com/minigame/introduction/commercialization/guide/virtual-payment.html（2026-09-30）
9. 微信开放文档「分包加载」— https://developers.weixin.qq.com/minigame/dev/guide/base-ability/subPackage/useSubPackage.html（2026-10-01：主包+分包 ≤30M、主包 ≤4M；留档 raw/2026-10-01/web/wechat-minigame-package-limit-tvly.json）
10. 小米开发者文档 — 小米小游戏停止 Cocos 导出、迁移快游戏联盟标准公告 — https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2165（2026-09-30 检索，留档 raw/2026-09-30/web/unity-transform-releases.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | adopt | 首次记录：微信端事实标准，引擎插件包体优势+生态最厚 |
