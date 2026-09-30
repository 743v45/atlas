# 原生 Canvas/WebGL 直写

> **TL;DR**：无引擎基线——平台原生但官方文档明确推荐用引擎，仅适合极简 2D/自绘玩法，渲染循环与分包全部自担。

- **结论**：trial 试用（场景限定：极简玩法/学习底层/强定制）
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 小游戏 = 只有一个全屏 Canvas 的页面：无 DOM、无 CSS、只能执行 JS，`game.js` 单入口；Canvas 2D 或 WebGL 直绘 + wx API | [1][2] |
| 运行限制 | 不支持 eval / new Function（动态执行 JS 被禁）；ES 标准差异靠基础库 core-js polyfill 抹平 | [3] |
| 适配设施 | weapp-adapter（官方示例级 DOM/BOM 桩）；社区现代替代 minigame-std（wx API 标准化封装，自称微信 100% 测试通过，JSR 发布） | [2][4] |
| 官方态度 | 「我们更推荐直接阅读游戏引擎的文档……开发者无需关注底层技术」——官方把直写定位为有经验者的可选项 | [2] |

## 为什么选（作为 trial 而非 hold）

- **它是理解平台的基线**：小游戏环境的一切差异（无 DOM/CSS、eval 禁止、包体 4MB/30MB、分包、远程资源）在直写时暴露得最彻底——学习价值与排查能力都从这里来 [1][2][3]。
- **极简玩法的真实可行域**：纯 2D 自绘（计时器、点触、翻牌类）直写代码量小、零引擎依赖、包体最优；现代封装（minigame-std 等）已把 wx API/DOM 差异的相当部分标准化 [4]。
- **不给 adopt 的原因**：微信官方明确推荐引擎路线（可视化编辑器、平台适配、分包方案都是引擎代劳）[2]；一旦游戏有场景管理/动画/音频/分包需求，直写的隐藏成本迅速超过引擎学习成本。

## 对比

- vs 引擎路线（Cocos/Laya）：引擎给出编辑器、资源管线、分包模板与平台能力封装；直写路线换来的是零依赖、零黑盒与最小包体 [2]。
- vs PixiJS：pixi 介于两者之间——给 2D 渲染性能层，不给场景/资源管线 [4][5]。
- 微信还有《小游戏可视化制作工具》（无代码拖拽）作为不写代码的官方出口 [2]。

## 风险与注意

- **性能优化无护栏**：WebGL 层的批渲染、纹理图集、脏矩形等全靠自修；引擎内置的这些优化在直写时都是可选项而非默认 [2]。
- 动态执行 JS 被禁意味着部分热更新/脚本化方案直接不可行 [3]。
- weapp-adapter 是示例级代码，无维护承诺；minigame-std 社区项目体量小，采用前评估其维护节奏（2026-09-30 快照）[4]。

## 来源

1. 微信开放文档「开发指南 / 小游戏介绍」— https://developers.weixin.qq.com/minigame/dev/guide/（2026-09-30）
2. 微信开放文档「学习进阶指南」— https://developers.weixin.qq.com/minigame/dev/guide/develop/develop（2026-09-30：全屏 Canvas 模型、引擎推荐、weapp-adapter、可视化制作工具）
3. 微信开放文档「JavaScript 支持情况」— https://developers.weixin.qq.com/minigame/dev/guide/runtime/js-support.html（2026-09-30：eval/new Function 禁止、core-js polyfill）
4. JSR @happy-js/minigame-std — https://jsr.io/@happy-js/minigame-std（2026-09-30：与 Adapter 的关系、微信小游戏 100% 测试自述）
5. Cinevva — WeChat Mini Game Engines (2026) — https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines（2026-09-30 检索：裸 WebGL 路线定位）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：基线条目，极简/学习场景可行，官方推荐引擎 |
