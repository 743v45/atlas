# Unity / 团结引擎 微信小游戏转换

> **TL;DR**：存量 Unity 项目的移植通道——官方转换工具+团结引擎双轨可用，但 4MB 首包残酷、调优链长；新项目不要为此从 Unity 起步。

- **结论**：trial 试用（场景限定：已有 Unity 存量）
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 方案形态 | Unity WebGL 小游戏适配（快适配）：WASM 转换+微信运行时+WX C# SDK，官方五阶段接入流程（兼容性评估→转换→平台能力→调优→上线） | [2] |
| 支持引擎 | Unity 2018~2022、团结引擎（微信官方文档口径） | [2] |
| 官方仓库 | GitHub `Unity-Technologies/minigame-unity-webgl-transform` 已被商标理由封锁（block reason: trademark，2025-09-16，gh 2026-09-30 留档）；文档社区迁 Gitee 官方组织 `wechat-minigame/minigame-transform`（MIT，24⭐，无 release）与个人 fork（NoahZuo，8⭐） | [1][3] |
| 团结引擎 | Unity 中国版，1.6.0 起内置 MiniGame 平台（微信为原生构建目标而非 WebGL 转换）；下载量超 50 万（Cinevva 2026 转述） | [4][5] |
| 费用 | Unity Personal 免费（年收入+融资 <20 万美元）；Pro $2,310/席/年（2026-01-12 起 +5%）；团结引擎个人版免费（近 12 个月财务规模 ≤150 万元人民币，超阈须专业版；专业版阈值 150 万~2 亿元） | [6][7][8] |

## 为什么选（作为 trial 而非更多）

- **它是存量通道，不是新项目起点**：Cinevva 2026 的结论可作定论——「它是移植现有游戏的工具，不是优先做微信的工具」；Unity WebGL 构建体量大，4MB 首包对非按此设计的引擎「极其残酷」，要在裁剪、代码拆分、分包上花实打实的功夫 [5]。微信官方也把流程定义为五阶段的适配工程而非一键导出 [2]。
- **但通道本身是活的一等方案**：微信小游戏团队负责人李卿公开将「Unity 适配」列为 2023 年小游戏（中重度化）爆发的两大技术突破之一（另一为 1G 包体基建放开）[9]；官方维护五阶段文档、转换案例（我叫 MT2/谜题大陆/热血神剑等）与 WX C# SDK [2]；2025 年中更新起支持一键导出，配套 minigame-adaptor 宣称微信优化渲染路径比纯 WebGL 快约 3 倍（厂商宣称，待独立实测）[5]。
- **GitHub 封锁是渠道风险样本**：官方仓库 2025-09-16 被以商标理由封锁（gh API 403 留档）[1]，文档迁 Gitee/微信开放文档——工具可用性不受影响（微信开放文档+Gitee 官方组织仍在），但 GitHub 生态位（issue/PR/star 信号）丢失，判活要看微信文档与 Gitee 提交而非 GitHub [1][3]。

## 对比

- vs Cocos/LayaAir：新项目无需比较——转换方案的价值全部建立在「已有 Unity 工程与 Unity 技能栈」上；从零起步选转换路线等于主动吃 4MB 首包与调优链成本 [2][5]。
- vs 团结引擎直出：团结把微信做成原生构建目标（MiniGame 平台），绕过 WebGL 转换层，是 Unity 肌肉记忆团队的中国市场正解；但团结个人版要资质审核、超 150 万门槛转专业版（订阅费）[4][8]。

## 风险与注意

- **包体与启动性能是主战场**：首资源包下载直接决定买量场景的「即点即玩」留存，官方要求自建启动留存数据上报；首帧/首场景优化是必做项 [2]。
- **版本兼容边界**：转换插件理论支持 Unity 2018~2022 与团结引擎；Unity 6（6000.x）项目的兼容性有社区疑问（团结 MuseChat 回复「可能还不支持」，2026-09-30 检索，待验证）[3]。
- **价格水位**：Unity Pro 2026-01-12 起 $2,310/席/年、月付 $210（unity.com 官方，2026-09-30 检索）[7]；团结引擎专业版人民币定价未见公开页（待验证，bilibili 2025-04 分析称当时未公布）[8]。
- 商标封锁后若微信文档站调整，fork 链路（NoahZuo 等）是脆弱备份 [1][3]。

## 来源

1. gh api repos/Unity-Technologies/minigame-unity-webgl-transform → 403 Repository access blocked（reason: trademark，created 2025-09-16，留档 raw/2026-09-30/gh/minigame-unity-webgl-transform.json）
2. 微信开放文档「微信小游戏适配解决方案（支持 Unity/团结引擎）」+「Unity 游戏接入微信小游戏指南」— https://developers.weixin.qq.com/minigame/dev/guide/game-engine/unity-webgl-transform.html（2026-09-30：支持版本、五阶段、转换案例、WX SDK）
3. Gitee wechat-minigame/minigame-transform（24⭐、MIT、1153 commits，2026-09-30）+ NoahZuo/minigame-unity-webgl-transform（8⭐）+ unity.cn MuseChat 问答（留档 raw/2026-09-30/web/unity-transform-releases.md）
4. 团结引擎 1.6.0 Release Note — https://unity.cn/editor1-6-0/release-note（2026-09-30：MiniGame 平台同步 Unity WebGL Audio 修复等）
5. Cinevva — WeChat Mini Game Engines (2026) — https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines（2026-09-30 检索：移植工具定位、4MB 残酷、团结引擎下载 50 万、adaptor 3x 宣称）
6. unity.com/cn/products/pricing-updates — Unity 定价变更（2026-09-30 检索：Personal 免费 <20 万美元、Pro $2,310/席/年自 2026-01-12）
7. 80.lv / CG Channel（2025-11）：Unity 2026 涨价 5% 报道，与官方页互证（2026-09-30 检索，留档 raw/2026-09-30/web/unity-china-pricing.md）
8. unity.cn 团结引擎服务条款 — https://unity.cn/tuanjie/legal/terms-of-service（2026-10-01：个人版阈值 150 万元、专业版 150 万~2 亿元、企业版 ≥2 亿元；留档 raw/2026-10-01/web/tuanjie-pricing-tvly2.json）
9. 虎嗅/Investing.com 转述微信小游戏负责人李卿公开课 — https://cn.investing.com/analysis/article-200485325（2026-04 微信公开课报道，2026-09-30 检索：Unity 适配与 1G 包体基建是 2023 爆发关键）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：存量 Unity 移植通道，通道活但成本结构决定只服务移植场景 |
