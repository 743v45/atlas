# 微信小游戏引擎与渲染方案 · 横评

> 主题：微信小游戏用什么渲染——完整引擎、渲染库 DIY、裸 Canvas、Unity 存量移植四条路线六个候选。
> 用户画像：通用视角按场景分流（个人快速开发 / 团队长期维护 / 多端复用），主评微信端表现。
> 数据核查日：2026-09-30（gh API 直查 stars/pushed_at/license；license NOASSERTION 已解码 2026-10-01；口碑与定价来自 tvly 检索 + 官方文档，原始留档 `raw/2026-09-30/web/` 与 `raw/2026-10-01/{gh,web}/`）。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| 个人快速开发 · 2D 休闲 | **Cocos Creator** | 官方推荐+一键构建+教程最厚，上线确定性最高 [1][3] |
| 个人快速开发 · 3D | Cocos Creator 或 LayaAir | Cocos 省包体，LayaAir 3D 工作流口味替代 [4] |
| 团队长期维护 | **Cocos Creator** | 生态/招人/案例厚度唯一一档，引擎插件降包体运维 [1][3][4] |
| 多端复用（微信+抖音+OPPO/vivo+原生） | Cocos Creator / LayaAir | 两者皆全端发布；渠道支持面逐渠道核实（小米已停 Cocos 导出）[1][3][10] |
| 存量 Unity 项目移植 | **Unity/团结转换** | 官方五阶段方案+团结引擎双轨；新项目不适用 [2][5] |
| Web 前端团队复用 2D 资产 | PixiJS | weapp-adapter 可行但管线自担 [3][4] |
| 复用 three.js 资产的小 3D | Three.js | 官方适配层冻结 0.108，锁旧版为代价 [6] |
| 极简玩法 / 学习底层 | 原生 Canvas 直写 | 官方推荐引擎，直写只留给强定制与教学 [3] |

## 属性对比矩阵

| 维度 | Cocos Creator | LayaAir | Unity/团结转换 | PixiJS | Three.js | 原生 Canvas/WebGL |
|---|---|---|---|---|---|---|
| 形态 | 完整引擎+编辑器 | 完整引擎+IDE | WebGL 转换方案 | 2D 渲染库 | 3D 渲染库 | 裸 Canvas/WebGL |
| 2D/3D | 2D+3D 均衡 | 2D+3D（3D 优先） | 3D 见长（Unity 系） | 仅 2D | 仅 3D | 2D/3D 裸写 |
| 微信适配 | **官方推荐·引擎插件** | 面板直出·一等目标 | 官方转换工具·通道活 | weapp-adapter 自适配 | 官方适配层停更 | 平台原生·零适配层 |
| 包体表现 | 引擎入插件省首包 | 运行时占包体预算 | 4MB 首包残酷 | 库小·管线自担 | 锁旧版本·社区方案 | 最零依赖 |
| 许可/费用 | MIT·编辑器免费 | MIT·企业版商务 | 引擎订阅·个人版免费 | MIT·免费 | MIT·免费 | 无依赖·免费 |
| 上手路径 | 编辑器·中文教程最厚 | IDE·中文文档 | 限存量 Unity 项目 | 代码 DIY | 代码 DIY | 官方文档·不推荐新手 |
| 多端能力（参考列，不计权重）* | 全端：微信/抖音/OPPO/vivo/小米/原生 App（小米已停 Cocos 导出）[1][10] | 全端：微信/H5/原生+各小游戏渠道（README 自述）[4] | 微信（团结引擎另覆盖多端）[2][5] | Web 原生，小游戏端靠 adapter | Web 原生，小游戏端靠冻结适配 | 仅微信小游戏环境 |
| 引擎本体活性(pushed) | 2026-09-21 | 2026-09-24 | 团结 1.6.0 在维护 | **2026-09-30** | **2026-09-30** | —（平台能力） |
| **微信通道活性** | **活（引擎插件）** | **活（面板直出）** | **活（微信文档+Gitee）** | 民间（官方示例级） | **冻结（0.108/2023-05）** | 平台原生 |
| ⭐（gh 2026-09-30） | 9,837 | 2,199 | GitHub 封锁/Gitee 24 | 48,247 | 116,086 | — |
| verdict | **adopt** | trial | trial | trial | trial | trial |

（逐格数据出处见各条目报告文末来源；⭐/pushed 均 gh 2026-09-30。）
\* 多端口径：「多端能力」是独立参考列，不计入 decision.json 权重（口径见 decision.json note）；本类别「多端」指微信之外的发布出口，渠道支持面动态变化（小米已停 Cocos 导出改推快游戏联盟标准 [10]），多端复用场景发布前逐渠道核实。

## 本类别三条结构性结论（2026-09-30 快照）

1. **判活必须看双线：引擎本体活性 ≠ 微信通道活性**。Godot（⭐117,990 当日活跃）、Phaser（⭐40,392）、Babylon.js（⭐26,123）、Three.js（⭐116,086）引擎本体全部活跃，但微信通道分别是「作者弃维护的个人工具」「民间 shim」「通用 adapter 声量弱」「官方适配层 2023-05 冻结」——高 star 完全不保证微信可用性，这是本类别最大的选型陷阱 [6][7][8]。
2. **引擎是否被微信客户端内置是包体分水岭**：Cocos 引擎可经官方「小游戏引擎插件」留在客户端、不占 4MB 首包；LayaAir/渲染库路线的运行时占自己的包预算；Unity WebGL 转换则被 4MB 首包「残酷」对待（Cinevva 2026）[1][4][5]。
3. **路线三分决定了问题的问法**：新做（完整引擎）、DIY（渲染库/裸写）、移植（Unity 转换）回答的是三个不同问题——李卿（微信小游戏团队负责人）把「Unity 适配和 1G 包体基建的放开」列为 2023 年微信小游戏的重要突破，但它是移植工具而非微信优先工具；把它当新项目起点是最常见的错误选型 [5][9]。

## 决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖所列维度；维度外风险（Unity GitHub 商标封锁、LayaAir 份额自述无第三方复核、three/pixi 适配层无维护承诺、渠道政策变动）以各条目 verdict 为准——矩阵分与 verdict 并存差异不是矛盾，是「综合值」与「该场景该不该用」两层的分工。

## 来源

1. Cocos — https://github.com/cocos/cocos-engine（gh 2026-09-30，license 解码 2026-10-01）+ https://docs.cocos.com/creator/4.0/manual/zh/editor/publish/publish-wechatgame.html（2026-09-30）
2. 微信开放文档 Unity 适配 — https://developers.weixin.qq.com/minigame/dev/guide/game-engine/unity-webgl-transform.html（2026-09-30）
3. 微信开放文档「学习进阶指南」— https://developers.weixin.qq.com/minigame/dev/guide/develop/develop（2026-09-30：官方推荐引擎、weapp-adapter、可视化工具）
4. Cinevva — WeChat Mini Game Engines (2026) — https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines（2026-09-30 检索）
5. Unity/团结 — gh 403 封锁留档（raw/2026-09-30/gh/minigame-unity-webgl-transform.json）+ Gitee wechat-minigame/minigame-transform + unity.cn 团结 1.6.0 release note + unity.cn 服务条款（2026-10-01）+ unity.com 定价页（2026-09-30）
6. Three.js 通道 — https://github.com/mrdoob/three.js 与 https://github.com/wechat-miniprogram/threejs-miniprogram（gh 2026-09-30：0.108.0、pushed 2023-05-22）
7. Godot 通道 — https://github.com/godotengine/godot（gh 2026-09-30）+ https://github.com/yuchenyang1994/godot-love-wechat（作者弃维护声明，raw/2026-09-30/web/godot-wechat.md）
8. Phaser/Babylon 通道 — https://github.com/phaserjs/phaser、https://github.com/BabylonJS/Babylon.js（gh 2026-09-30）+ raw/2026-09-30/web/{phaser,babylon}-wechat.md（Phaser 民间 shim 线索留档见 pixi-wechat.md）
9. 虎嗅/Investing 转述李卿公开课 — https://cn.investing.com/analysis/article-200485325（2026-04，2026-09-30 检索）
10. 小米开发者文档 — 小米小游戏停止 Cocos 导出、迁移快游戏联盟标准公告 — https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2165（2026-09-30 检索，留档 raw/2026-09-30/web/unity-transform-releases.md）
