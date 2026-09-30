# 小程序 UI 组件库 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

小程序的界面组件从哪来——按技术栈选哪家组件库？（2026-10-01 会话；用户画像注记：通用视角按场景分流——个人快速开发 / 团队长期维护 / 多端复用，主评微信端表现；「多端能力」为参考列不计决策权重）

## 分叉与决策

### D1 原生 wxml 还是 uni-app/taro 生态？

- 技术栈锁定先于库选型：原生与 uni-app 组件互不通用；taro 生态（React 系）域外，见落选节点。
- 选 **原生 wxml** → 进 D2a
- 选 **uni-app 生态** → 进 D2b

### D2a 原生赛道：要官方设计系统还是自由定制？

- 微信官方视觉（weui）是「视觉一致性」诉求，与「组件广度/持续演进」诉求（vant-weapp/tdesign）不同轴。
- 叶：[vant-weapp](vant-weapp/) adopt（原生事实标准：⭐18.4k、教程与 AI 语料最厚、v1.11.7 稳定；代价是 2024-10 起慢修——个人快速开发与求稳存量首选 [1]）
- 叶：[TDesign 小程序](tdesign/) adopt（腾讯官方月度发版（1.17.0，2026-09-23）+ Skyline 官方适配唯一（35/57，61%）——团队长期维护与押 Skyline 首选 [2]）
- 叶：[WeUI](weui/) trial（微信官方视觉 + 扩展库零包体积独门；22 组件只够轻量界面 [3]）

### D2b uni-app 赛道：官方标配还是现代体验/存量延续？

- DCloud 官方兜底（uni-ui）、Vue3+TS 新架构（wot-design-uni）、uView 存量延续（uview-plus）回答的是三个不同问题；后两者进入 D3。
- 叶：[uni-ui](uni-ui/) trial（DCloud 官方 + uni-app x 方向跟进最稳；GitHub releases 通道失灵，判活看 npm [5]）
- 叶：[wot-design-uni](wot-design-uni/) trial（Vue3+TS+暗黑+AI 友好工具链，新项目体验最优；不支持 Skyline 是硬边界 [4]）
- 叶：[uview-plus](uview-plus/) trial（uView 官方双仓冻结（2025-01）后的社区接棒：uView2 API 高兼容 + 36.8k npm 下载/月；存量 uView 项目迁移首选 [6]）

### D3 接不接受商业闭源？

- 即便接受付费，闭源供给仍需「持续在营」作前提——firstui 三条公开证据链停更于 2024-06-12，前提不成立。
- 叶：[FirstUI](firstui/) hold（免费版组件受限 + VIP ¥399/永久 + 商用条款严苛（不可开源/外包需双 VIP）+ 公开停更 28 个月——颜值模板不足以对冲 [7]）

## 落选节点（不立条目的死分支）

- **ColorUI**（weilanwl/coloruicss，⭐12,374）：pushed 2024-04-08 停更（gh 2026-09-30），且本质是样式库（class 库）而非组件库——无交互组件可维护性差，双死因。
- **Lin UI**（logamee/lin-ui，⭐4,142）：pushed 2023-08-11 停更（gh 2026-09-30），原生赛道被 vant-weapp/tdesign 覆盖。
- **iView Weapp**（TalkingData/iview-weapp，⭐6,600）：pushed 2023-03-01 停更（gh 2026-09-30；LICENSE 解码 MIT，raw/2026-10-01/gh/），TalkingData 已无投入。
- **Ant Design Mini**（ant-design/ant-design-mini，⭐552）：仍活跃（pushed 2026-06-01）但官方描述自证定位——「for **Alipay** mini programs that is **also compatible with** WeChat」，支付宝优先、微信为辅；主评微信端的画像下不收（gh 2026-09-30/10-01：releases 止于 3.1.6，2025-02-26）。
- **uv-ui**（@climblee/uv-ui）：uView2 的另一条社区 fork，npm 月下载 1,719（2026-10-01），声量与更新均弱于 uview-plus——uView 谱系记一条即可，不重复立目。
- **uview-pro**（anyup/uView-Pro，⭐555）：活跃（v0.6.19，2026-09-07；MIT）但是 uView1 血统的 TS 重写（非 uView2 延续），且版本号未到 1.0——与 uview-plus 同谱系不同源，正文已讲清双线，暂不独立立目（观察名单）。
- **Taro 生态（NutUI-tenant 等）**：React 系跨端，与主评的微信原生/uni-app 两栈不同轨；TDesign 亦有 React/Taro 版但归前端框架域问题，本类别不展开。

## 观察名单（下次复核触发器）

- **sard-uniapp**（sutras/sard-uniapp，⭐300、pushed 2026-09-11、tag v1.30.6）：Vue3+TS、96+ 组件、单测覆盖 80%（掘金 2025 文章，raw/2026-09-30/web/sard-ui-search.md），但明确不支持 app-nvue/uni-app-x/Skyline 且社区未验证——触发器：star 破 1k 或出现生产案例 → 立目评估。
- **tdesign Skyline 进度**：61%（35/57）→ 复核时查 issue #3149 是否接近全覆盖；全覆盖后可上调其在原生赛道的首选位。
- **vant-weapp 是否恢复发版**：若 2027 年仍无新版本，下轮复核降 trial 并在树中把 tdesign 提为原生唯一 adopt。
- **wot-design-uni / uni-ui / weui 的 Skyline 官方表态**：任何一家给出适配路线图 → 更新矩阵 Skyline 行。
- **uview-pro 0.x → 1.0**：正式版 + 持续半年活跃 → 考虑与 uview-plus 并列立目或替换。
- **firstui 恢复更新**：官网/DCloud 市场出现 2026 年新版本 → hold 重估（同时验证 VIP 渠道是否有私下更新）。

## 引用

1. raw/2026-09-30/gh/vant-weapp.json + releases/commits 补查 raw/2026-10-01/gh/ui-libs-releases.md、ui-libs-commits-tags.md（gh 2026-10-01）
2. raw/2026-09-30/gh/tdesign-miniprogram.json + Skyline issue #3149（raw/2026-10-01/gh/ui-libs-skyline-issues.md）
3. raw/2026-09-30/gh/weui-miniprogram.json、weui-wxss.json + LICENSE 解码 raw/2026-10-01/gh/weui-wxss-license-decode.md
4. raw/2026-09-30/gh/wot-design-uni.json + issue #317（raw/2026-10-01/gh/ui-libs-skyline-issues.md）
5. raw/2026-09-30/gh/uni-ui.json + npm 实测 raw/2026-10-01/gh/ui-libs-uniui-firstui.md
6. raw/2026-09-30/gh/uview-plus.json、uview1.json、uview2.json、uview-pro.json + 谱系 raw/2026-10-01/web/uview-lineage-tavily.json
7. raw/2026-09-30/gh/firstui.json + raw/2026-09-30/web/firstui-dcloud-market.md、firstui-price.md、firstui-changelog.md + raw/2026-10-01/web/firstui-wxdoc-log.md、firstui-repos.md
8. raw/2026-09-30/gh/sard-uniapp.json + raw/2026-09-30/web/sard-ui-search.md
