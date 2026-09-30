# 小程序 UI 组件库 · 横评

> 主题：小程序的界面组件从哪来——原生 wxml 与 uni-app 两条技术栈、七个候选。
> 用户画像：通用视角按场景分流——个人快速开发 / 团队长期维护 / 多端复用；主评微信端表现。「多端能力」为对比矩阵独立参考列，不计入决策矩阵权重（见 decision.json note）。
> 数据核查日：2026-09-30（gh 快照）+ 2026-10-01（补查 gh api / npm / 官方文档）；组件规模为一手目录实测（gh 2026-10-01），价格查询 2026-09-30。原始留档 `raw/2026-09-30/`、`raw/2026-10-01/`。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| 个人快速开发 · 微信原生 | **vant-weapp** | 事实标准：教程与 AI 语料最厚，出活最快 [1] |
| 团队长期维护 · 微信原生 | **tdesign**（求稳存量选 vant-weapp） | 腾讯官方月度发版 + Skyline 官方适配唯一选项 [2] |
| 要微信官方视觉 / 主包体积敏感 | weui | 官方视觉 + 扩展库引入不占包体积 [3] |
| 个人快速开发 · uni-app | **wot-design-uni** | Vue3+TS+暗黑+AI 友好（LLMs.txt/MCP），新项目起点干净 [4] |
| 团队长期维护 · uni-app | **uni-ui** | DCloud 官方兜底，含 uni-app x 方向跟进 [5] |
| 多端复用（含存量 uView 项目迁移） | uview-plus | uView2 API 高兼容 + 36.8k npm 下载/月高频滚动 [6] |
| 要商业级模板颜值（任何场景） | 无推荐（firstui hold） | 公开停更 28 个月 + 闭源 + 商用条款严苛 [7] |

## 属性对比矩阵

| 维度 | vant-weapp | tdesign | weui | wot-design-uni | uni-ui | uview-plus | firstui |
|---|---|---|---|---|---|---|---|
| 技术栈 | 原生 wxml [1] | 原生+uni-app 双栈 [2] | 原生 wxml（扩展库）[3] | uni-app Vue3+TS [4] | uni-app（含 uni-app x）[5] | uni-app Vue2/3+nvue [6] | uni-app 双版（UNI+微信原生）[7] |
| 组件规模 | 约 68 组件目录（实测）[1] | 57 组件（官方口径）[2] | 22 组件（实测）[3] | 80+（官网口径；实测 102 目录）[4] | 60+（npm 实测 63 目录）[5] | 142 组件目录（实测，含子组件）[6] | 免费版子集，VIP 全量 [7] |
| 主题/暗黑 | CSS 变量定制，无暗黑 [1] | CSS 变量主题（暗黑待验证）[2] | 微信官方视觉，定制弱 [3] | CSS 变量+暗黑+i18n [4] | 主题定制（暗黑待验证）[5] | 主题定制（暗黑待验证）[6] | 主题定制（文档在营）[7] |
| 维护活性 | 慢修（发版止 2024-10，末次功能提交 2025-04）[1] | 活跃（1.17.0，2026-09-23）[2] | 慢（npm 1.5.6，2024-11-15）[3] | 活跃（pushed 2026-09-24）[4] | 活跃（pushed 2026-09-30；npm 2026-03-26）[5] | 高频小版本（3.8.126，2026-09-28）[6] | 停更（公开渠道止 2024-06-12）[7] |
| 许可 | MIT [1] | MIT [2] | MIT [3] | MIT [4] | MIT [5] | MIT [6] | Apache-2.0 开源版+商业闭源 [7] |
| ⭐(gh 2026-09-30) | **18,457** | 1,771 | 15,278(wxss)/2,429(mp) | 2,300 | 2,091 | 719 | 513 |
| npm 月下载(2026-08-30→09-28) | 18,870 [1] | **38,099** [2] | 2,341 [3] | 17,492 [4] | 22,778 [5] | 36,753 [6] | —（非 npm 分发） |
| 多端能力（参考列，不计权） | 微信原生为主 | 微信原生+uni-app | 微信原生（扩展库） | 微信/支付宝/钉钉小程序、H5、APP | uni-app 全端（含 uni-app x） | 全端+nvue+鸿蒙方向 | App(nvue/vue)/五家小程序/H5 |
| 微信 Skyline | 无官方适配，社区 bug 3 例开放 [1] | **官方适配中 35/57（61%）** [2] | 未声明（待验证）[3] | 不支持（issue 关闭「工作量大」）[4] | 未声明（待验证）[5] | 未声明（待验证）[6] | 未声明（待验证）[7] |
| verdict | **adopt** | **adopt** | trial | trial | trial | trial | **hold** |

## 本类别四条结构性结论（2026-09-30 快照）

1. **技术栈是第一分叉，比选库更重要**：原生 wxml（vant-weapp/tdesign/weui）与 uni-app（wot/uni-ui/uview-plus/firstui）之间不可混用——先定技术栈再谈选库；uView 谱系内部还有血统之分（uView2→uview-plus，uView1→uview-pro TS 重写），迁移前先认亲 [6]。
2. **高 star ≠ 在演进**：vant-weapp ⭐18.5k 但发版止于 2024-10、tdesign ⭐1.8k 却月度发版且 npm 月下载第一（38k vs 19k）——star 度量存量声望，pushed/发版/npm 下载才度量未来 [1][2]。
3. **Skyline 是微信端新增的隐性分叉**：跨端 web 技术路线（wot/sard）明确不支持或短期无计划；原生阵营只有 tdesign 有官方适配线（61%）——押 Skyline 的项目事实上只能在 tdesign/vant-weapp 里选 [2][4]。
4. **商业闭源组件库在免费开源供给充分时失去存在空间**：firstui 停更+¥399+商用限制，对照三家 MIT 活跃库——「付费买颜值」模式在小程序组件库赛道已被证伪 [7][8]。

## 决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖所列维度；维度外风险（Skyline 不支持、维护断层史、闭源商用条款、fork 断更风险）以各条目 verdict 为准——vant-weapp 矩阵分最高与「tdesign 才是持续演进选项」并存不是矛盾：矩阵度量「当前综合值」，verdict 度量「该场景该不该用」。

## 来源

1. vant-weapp — https://github.com/youzan/vant-weapp + npm @vant/weapp（gh 2026-09-30/10-01，npm 2026-10-01）
2. tdesign — https://github.com/Tencent/tdesign-miniprogram + Skyline issue #3149 + npm tdesign-miniprogram（gh/npm 2026-10-01）
3. weui — https://github.com/wechat-miniprogram/weui-miniprogram + https://github.com/Tencent/weui-wxss + 微信官方文档（gh 2026-10-01，文档 2026-09-30）
4. wot-design-uni — https://github.com/Moonofweisheng/wot-design-uni + https://wot-ui.cn + issue #317（gh 2026-10-01，官网 2026-09-30）
5. uni-ui — https://github.com/dcloudio/uni-ui + npm @dcloudio/uni-ui（gh/npm 2026-10-01）
6. uview-plus — https://github.com/ijry/uview-plus + npm uview-plus + 谱系 raw/2026-09-30/gh/uview1.json、uview2.json、uview-pro.json（gh/npm 2026-09-30/10-01）
7. firstui — https://github.com/FirstUI/FirstUI + DCloud 市场 + wxdoc changelog + 官网会员页（gh 2026-09-30/10-01，价格 2026-09-30）
8. sard-uniapp（观察名单）— https://github.com/sutras/sard-uniapp（gh 2026-09-30：⭐300、pushed 2026-09-11、明确不支持 Skyline）
