# Three.js（微信小游戏）

> **TL;DR**：引擎极活跃但微信通道冻结——官方适配层停在 0.108（2023-05），社区方案也已停更，仅限复用既有 three 代码的场景。

- **结论**：trial 试用（场景限定：复用既有 three.js 代码、非关键路径）
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 引擎本体 | mrdoob/three.js（⭐116,086、pushed 2026-09-30、MIT，gh 2026-09-30） | [1] |
| 微信官方适配 | wechat-miniprogram/threejs-miniprogram：Three.js 小程序 WebGL 适配版，**锁版本 0.108.0**，README 自述「如要更新 threejs 版本可发 PR 或 fork 自行修改」；⭐799、pushed 2023-05-22（gh 2026-09-30） | [2] |
| 社区适配 | deepkolos/three-platformize（适配微信/淘宝/头条，⭐592、pushed 2021-12、无 LICENSE 文件，gh 2026-10-01） | [3] |
| 通用垫片 | weapp-adapter（微信官方示例级 DOM/BOM 桩） | [4] |

## 为什么选（作为 trial 而非 adopt/hold）

- **「引擎活、通道死」的标本**：three.js 本体是 Web 3D 事实标准、当日仍在推提交 [1]；但微信官方适配层 0.108.0 停在 2023-05——落后主线数年（0.108 上游发布于 2019-08，npm 2026-10-01 查询）[6]，官方明示不再跟进版本 [2]；最著名的社区平台化方案 three-platformize 也停在 2021-12 且无 license 文件 [3]。想用新版本只能 fork 自扛适配 [2]。
- **仅存的真实场景**：团队已有 three.js 代码/技能要复用到体积敏感的小 3D 玩法（Cinevva 2026：适合小而定制、对体积敏感的游戏，或团队本来就活在 Three.js 里）[5]；此时锁 0.108 旧版本是可接受的折衷。
- **不给 adopt 的原因**：新项目走此路 = 主动选一个无维护通道、版本冻结的 3D 栈；同为 DIY 路线，pixi（2D）的适配负担小一个量级，3D 完整需求应选引擎路线（Cocos/Laya）[4][5]。
- **不给 hold 的原因**：适配层虽冻结但可用（小程序 canvas + createScopedThreejs 模式文档齐全）[2]，存量复用场景下它仍是正解。

## 对比

- vs Cocos/LayaAir 引擎：引擎路线有微信一等适配+编辑器+分包方案；three 路线全部自担 [4][5]。
- vs Unity 转换：同为 3D，Unity 转换面向存量 Unity 工程、有微信官方五阶段支持；three 路线面向存量 Web 3D 代码、支持只有冻结的适配层 [5]。
- vs 裸 WebGL：three 提供场景图/材质/加载器抽象，裸写连这些都要自建 [5]。

## 风险与注意

- **版本冻结是硬约束**：0.108 之后的功能/修复全数缺席；配套类库（Controls、loader）需自行传入 THREE 实例，部分缺失（Controls 未适配，2020 年使用记录与 README 口径一致）[2]。
- three-platformize 无 LICENSE 文件——商用前法律状态待验证 [3]。
- 微信端 3D 性能调优（内存上限、高性能模式）无官方 three 指引，参照小游戏通用性能文档 [4]。

## 来源

1. GitHub 仓库 — https://github.com/mrdoob/three.js（gh 2026-09-30：⭐116,086、pushed 2026-09-30、MIT）
2. GitHub 仓库 — https://github.com/wechat-miniprogram/threejs-miniprogram（gh 2026-09-30：⭐799、pushed 2023-05-22、MIT、版本 0.108.0；README 原文见 raw/2026-09-30/web/three-wechat-adapter.md）
3. GitHub 仓库 — https://github.com/deepkolos/three-platformize（gh 2026-10-01：⭐592、pushed 2021-12-12、license null，留档 raw/2026-10-01/gh/minigame-engines-supplement.md）
4. 微信开放文档「学习进阶指南」— https://developers.weixin.qq.com/minigame/dev/guide/develop/develop（2026-09-30）
5. Cinevva — WeChat Mini Game Engines (2026) — https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines（2026-09-30 检索：Three.js 与裸 WebGL 路线定位）
6. npm — three 0.108.0 上游发布时间（npm view three time，2026-10-01 查询：2019-08-28，留档 raw/2026-10-01/web/three-0108-npm-date.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | trial | 首次记录：本体活跃+通道冻结（0.108/2023-05），存量复用场景限定 |
