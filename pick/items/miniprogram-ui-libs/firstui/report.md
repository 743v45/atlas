# FirstUI

> **TL;DR**：商业闭源 uni-app 组件库——免费版功能受限、VIP ¥399/永久且商用条款严苛，UNI 版与微信版公开渠道均停更于 2024-06——新项目不建议采用

- **结论**：hold 观望
- **核实日期**：2026-10-01

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 开源免费版 Apache-2.0；商业版闭源（VIP 源码不公开分发） | [1][5] |
| 仓库 | https://github.com/FirstUI/FirstUI（⭐513、pushed 2024-06-12，gh 2026-09-30）；微信原生版 FirstUI-weixin（⭐88、pushed 2024-06-12，gh 2026-10-01） | [1][2] |
| 最新版本 | UNI 版 v2.4.01（2024-06-12，DCloud 插件市场）；微信小程序版 V2.4.0（2024-06-12，官方 changelog 页顶条） | [3][4] |
| 价格 | VIP ¥399/永久（官网会员权益页，查询 2026-09-30）；SaaS/外包批量授权 ¥2,999～¥16,999/永久（官方 FAQ，查询 2026-09-30） | [5][6] |
| 维护活跃度 | 公开渠道全停：GitHub org 各仓 push 止于 2024-06-12（uni-app x 方向 FirstUI-uvue 至 2025-02-24）、DCloud 市场与官方 changelog 同日（2024-06-12）——至今 28 个月无公开更新 | [1][2][3][4] |

## 为什么不选（hold）

- **公开停更 28 个月**：三条公开证据链同日指向 2024-06-12——GitHub org（FirstUI 与 FirstUI-weixin 均 pushed 2024-06-12）、DCloud 插件市场最新 v2.4.01（2024-06-12）、官方 changelog 最新 V2.4.0（2024-06-12）。「付费才有的 VIP 渠道是否仍在私下更新」无法验证——「待验证」，但对新项目而言付 ¥399 买一个无法验证活跃度的闭源组件库，风险收益不成立 [1][2][3][4]。
- **付费墙切割核心组件**：官方更新日志与 FAQ 组件表显示 Calendar、Cascader、Select、Upload、Qrcode、Barcode、Waterfall、Table、Poster、Charts 等大量常用组件为 VIP 专属——免费版是残缺体验（2026-09-30 留档）[3][6]。
- **商用条款严苛**：官方 FAQ 明确——不可用于开源项目、不可发布到公开渠道、不可用于外包项目（除非双方均为 VIP）、不可转让/出售源码；SaaS/外包需按用户数买断（¥2,999～¥16,999）[6]。
- **口碑长期负面**：知乎官方文章评论区（2022–2025）高频差评：「更新有点慢」「跑路了，没有更新了」「开源收费 吃相难看」「不要买。被坑」（2025-03-11）——与停更证据链互相印证 [7]。
- **替代充分**：同类 uni-app 库（wot-design-uni / uni-ui / uview-plus）全部 MIT 免费且 2026-09 仍在活跃更新——FirstUI 的差异化只剩模板颜值，不足以对冲闭源+停更风险（gh 2026-09-30～10-01 核实）[8]。

## 对比

- vs wot-design-uni / uni-ui / uview-plus：三者免费开源且活跃；FirstUI 组件颜值与物料商城是差异点，但停更+闭源+商用限制使其在所有三场景（个人快速开发/团队长期维护/多端复用）均出局 [8]。
- 若确需其模板：单次买断拿源码做一次性参考，不作为依赖引入——此用法也需接受其不可用于开源/外包的条款约束 [6]。

## 风险与注意

- **VIP 私下更新可能性**——「待验证」：向官方会员群求证 2024-06 后是否有会员源码更新；有则可将本条降级评估，但公开证据不足时 hold 维持 [1][3][4]。
- **uni-app x 方向尝试停滞**：FirstUI-uvue（uni-app x 版）pushed 2025-02-24 后未再更新（gh 2026-10-01）——新架构方向同样失速 [2]。
- 复核触发：官网/插件市场出现 2026 年新版本，或官方公告恢复更新。

## 来源

1. GitHub 仓库 — https://github.com/FirstUI/FirstUI（gh 2026-09-30：Apache-2.0、⭐513、pushed 2024-06-12）
2. FirstUI org — https://github.com/FirstUI（gh 2026-10-01：FirstUI-weixin ⭐88 pushed 2024-06-12；FirstUI-uvue ⭐59 pushed 2025-02-24；留档 raw/2026-10-01/web/firstui-repos.md）
3. DCloud 插件市场 — https://ext.dcloud.net.cn/plugin?id=7646（访问 2026-09-30：最新 v2.4.01，2024-06-12；VIP 组件清单，留档 raw/2026-09-30/web/firstui-dcloud-market.md）
4. 微信小程序版 changelog — https://wxdoc.firstui.cn/docs/log.html（访问 2026-10-01：最新 V2.4.0，2024-06-12，留档 raw/2026-10-01/web/firstui-wxdoc-log.md）
5. 官网会员权益 — https://www.firstui.cn/right（查询 2026-09-30：「免费开源版本组件」「¥399/永久 VIP会员版」，留档 raw/2026-09-30/web/firstui-price.md）
6. 官方 FAQ（版权与价格）— https://wxdoc.firstui.cn/docs/FAQ.html（查询 2026-09-30：商用限制条款、SaaS 授权 ¥2,999/¥8,999/¥16,999、VIP 组件对照表，留档 raw/2026-09-30/web/firstui-changelog.md）
7. 知乎评论区 — https://zhuanlan.zhihu.com/p/504348632（2022-05～2025-06 评论，留档 raw/2026-09-30/web/firstui-changelog.md）
8. 同类对照 — https://github.com/Moonofweisheng/wot-design-uni、https://github.com/dcloudio/uni-ui、https://github.com/ijry/uview-plus（gh 2026-09-30～10-01：均 MIT、2026-09 有 push）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-01 | hold | 首次记录：公开渠道停更 28 个月 + 闭源 + 商用条款严苛（预判 assess，依证据修正为 hold） |
