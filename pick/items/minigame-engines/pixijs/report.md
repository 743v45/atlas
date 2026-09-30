# PixiJS

> **TL;DR**：2D 渲染库 DIY 路线——引擎本体极活跃，微信端靠 weapp-adapter 适配、管线自担，仅适合已有 pixi 资产的前端团队。

- **结论**：trial 试用（场景限定：Web 前端团队复用 pixi 资产）
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | pixijs/pixijs（仓库已由 pixi.js 改名 pixijs），持续发布中 | [1] |
| 许可证 | MIT（gh 2026-09-30） | [1] |
| 仓库 | https://github.com/pixijs/pixijs（⭐48,247、pushed 2026-09-30，gh 2026-09-30） | [1] |
| 维护活跃度 | pushed 与采集日同日，头部活跃（gh 2026-09-30） | [1] |

## 为什么选（作为 trial 而非 adopt/hold）

- **引擎本体一流但通道是民间的**：⭐48k、pushed 2026-09-30 的顶级 2D 渲染器 [1]；微信官方对 PixiJS 的口径是「可以发布到小游戏，只需引入 weapp-adapter 并做一些适配调整，但并不推荐没有经验的开发者学习使用」——即官方承认可行、不给支持承诺 [2]。
- **DIY 的真实成本**：没有编辑器、没有场景/资源/分包管线，渲染循环、素材管线、分包、每个适配边角都自己扛（Cinevva 2026：最灵活也最费劲，适合小而定制、对体积敏感的游戏或本来就活在 Three.js/pixi 里的团队）[3]。
- **不给 hold 的理由**：weapp-adapter 模拟 DOM/canvas 的路子成熟（官方示例 + 社区文章覆盖 PixiJS/ThreeJS/Babylon 三家）[2][4]，库本体小、2D 场景包体友好；对已有 pixi 代码与技能的前端团队，复用收益是真实的。

## 对比

- vs Cocos Creator：Cocos 给编辑器+引擎插件+官方适配，PixiJS 给裸渲染器+自适配；同一 2D 休闲游戏，Cocos 路径的上线确定性显著更高 [2][3]。
- vs Three.js：同为渲染库 DIY，pixi 只做 2D；weapp-adapter 路线两者同门（ThreeJS 亦可走此路）[2][4]。
- vs 裸 Canvas：pixi 提供 WebGL 批渲染/精灵图集性能层，裸 Canvas 无这些但零依赖 [3]。

## 风险与注意

- **适配层无维护承诺**：weapp-adapter 是官方示例级代码，微信基础库或 pixi 大版本升级后回归靠团队自测 [2]。
- **无微信平台能力封装**：登录/支付/开放数据域等 wx API 全部自封装（引擎路线里由 Cocos/Laya 构建模板代劳的部分）[2][3]。
- 团队若无 pixi/WebGL 经验，选它纯属负重——官方文档明确不推荐无经验者走此路 [2]。

## 来源

1. GitHub 仓库 — https://github.com/pixijs/pixijs（gh 2026-09-30：⭐48,247、pushed 2026-09-30、MIT）
2. 微信开放文档「学习进阶指南」— https://developers.weixin.qq.com/minigame/dev/guide/develop/develop（2026-09-30：PixiJS/ThreeJS 走 weapp-adapter、不推荐无经验开发者）
3. Cinevva — WeChat Mini Game Engines (2026) — https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines（2026-09-30 检索：最灵活最费劲、适用场景）
4. CSDN — WeApp-Adapter 终极指南 — https://blog.csdn.net/gitblog_00206/article/details/155330412（2026-09-30 检索：adapter 覆盖 PixiJS/ThreeJS/Babylon；个人博客口径）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：本体活跃+通道民间，复用 pixi 资产的前端团队限定 |
