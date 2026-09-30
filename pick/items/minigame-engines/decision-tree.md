# 微信小游戏引擎与渲染方案 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

微信小游戏用什么渲染——完整引擎、渲染库 DIY、还是移植转换？（2026-10-01 会话；画像注记：通用视角按场景分流——个人快速开发 / 团队长期维护 / 多端复用三场景，主评微信端表现）

## 分叉与决策

### D1 新做，还是移植存量 Unity 项目？

- 有 Unity 存量工程与 Unity 技能栈时，转换路线的全部价值才成立；它回答「怎么把已有游戏搬上微信」，不回答「新游戏用什么写」（Cinevva 2026「移植工具而非微信优先」）[unity-transform 报告/来源 5]。
- 叶：[Unity / 团结引擎 微信小游戏转换](unity-transform/) trial（官方五阶段方案+团结引擎双轨、通道活；但 4MB 首包残酷、调优链长、Unity 订阅制费用）
- （无存量 → 走 D2）

### D2 新做：要编辑器/IDE，还是接受代码 DIY？

- 微信官方口径：推荐直接用已适配小游戏的引擎（编辑器、平台适配、分包由引擎代劳）；PixiJS/ThreeJS「可以做但不推荐无经验开发者」；裸 Canvas 仅留给强定制与学习（官方「学习进阶指南」）[comparison 来源 3]。
- 要编辑器 → 走 D3；接受 DIY → 走 D4。

### D3 编辑器路线：默认 Cocos，还是 3D 工作流偏好 LayaAir？

- Cocos 胜在生态厚度（教程/案例/招人）与引擎插件省首包；LayaAir 是微信一等适配的 3D 工作流替代，「用过两者的人说是口味问题」——没有压倒性硬优势时不偏离默认 [cocos-creator/layaair 报告]。
- 叶：[Cocos Creator](cocos-creator/) adopt（官方推荐位+引擎插件+一站式构建，2D/3D 默认答案）
- 叶：[LayaAir](layaair/) trial（release 活跃 v3.4.1 2026-08-31；社区体量差一档、运行时占包预算、90% 份额为厂商自述）

### D4 DIY 路线：复用什么资产？

- DIY 的正当性全部来自复用：有 pixi 2D 资产选 pixi，有 three 3D 代码选 three（代价是锁 0.108），什么都不是复用、只要极简玩法就裸 Canvas——三条路都别当新项目默认 [pixijs/threejs/canvas-native 报告]。
- 叶：[PixiJS](pixijs/) trial（本体 ⭐48k 极活跃；weapp-adapter 官方示例级、管线自担）
- 叶：[Three.js（微信小游戏）](threejs/) trial（本体当日活跃但微信适配层停在 0.108/2023-05，three-platformize 亦停 2021——通道冻结是硬约束）
- 叶：[原生 Canvas/WebGL 直写](canvas-native/) trial（平台原生零依赖；官方明确推荐引擎，直写只留给极简/学习/强定制）

## 落选节点（不立条目的死分支）

- **Egret（白鹭）**：引擎本体死了——egret-labs/egret-core ⭐4,022、pushed 2022-07-20（gh 2026-09-30）；egret.com 官网首页原文「白鹭科技公司于 2022 年 2 月已经停止运营，白鹭引擎也停止了官方技术团队的维护和更新」（raw/2026-09-30/web/egret-status.md）；CEO 2022-06 公开称面临破产清算。第一波微信小游戏的主力引擎，公司停运=通道与维护双死，不立目。
- **Godot**：引擎本体极健康（⭐117,990、pushed 2026-09-30，gh 2026-09-30），但微信通道死——godot-love-wechat 作者原话「本人已不研究微信小游戏了，也无力维护和更新本项目」（raw/2026-09-30/web/godot-wechat.md）；社区后继工具（适配 4.4、分包）是个人作品，另有实测记录记录到降版本/黑屏/仅 Windows 导出等坑。引擎活+通道死=结构性结论的样本，不立目。
- **Phaser**：⭐40,392、pushed 2026-08-21 本体活跃，但无官方微信通道，民间 shim（littlee/wechat-small-game-phaser 等 weapp-adapter 包装）年久；2D DIY 场景被 PixiJS 覆盖，不重复立目（raw/2026-09-30/web/phaser-wechat.md；littlee shim 留档见 pixi-wechat.md）。
- **Babylon.js**：⭐26,123、pushed 2026-09-30、Apache-2.0 本体活跃，微信适配靠通用 adapter（WeApp-Adapter/minigame-std 一类），中文小游戏社区声量弱、无成功案例群；3D 引擎需求已被 Cocos/Laya/Unity 三线覆盖，不立目（raw/2026-09-30/web/babylon-wechat.md）。

## 观察名单（下次复核触发器）

- threejs-miniprogram 或其后继复活（适配层离开 0.108）→ threejs verdict 重估
- 微信包体上限现行值（主包 4MB/分包合计 30MB，2026-10 快照）或高性能模式内存政策调整 → 全类别包体列刷新
- 团结引擎专业版人民币定价公开（2025-06 起收费政策已实施、价格未公示，待验证）→ unity-transform 费用格更新
- LayaAir 90% Web3D 份额出现第三方统计（现为 2024-07 CEO 自述）→ layaair verdict 复核
- Cocos 编辑器/企业授权口径变化（2026-10-01 快照：编辑器免费、无分成）→ cocos-creator 费用格复核
- 渠道引擎支持面变动（小米已停 Cocos 导出改快游戏联盟标准，2026-09-30 快照）→ 多端复用场景横评列复核
