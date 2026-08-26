# Pushover

> **TL;DR**：体验口碑最佳的商业推送：$4.99/平台一次性买断、终身有效、30 天全功能试用（2026-08-27 官网报价），但试用后必付费且闭源不可自托管——与「免费」硬约束直接冲突；哪天愿意付这 5 美元它就是体验上限。

- **结论**：hold（观望——不满足免费硬约束；仅质量问题会重评）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 商业 SaaS：HTTP API + 各平台官方 App（iOS/Android/桌面） | [1] |
| 许可 | 闭源商业服务，无自托管选项 | [1][2] |
| 价格 | $4.99（US）一次性/平台，该平台下个人所有设备终身可用；30 天免费全功能试用（pushover.net/pricing，查询 2026-08-27） | [1][3] |

## 为什么（hold）

- **体验是行业标杆**：2026-08-25 会话评价「体验最好」，跨平台一致、API 稳定多年 [4]；各竞品评测（如 DEV.co 2026 对比表）也默认它为体验基准 [5]。
- **唯一否决项是价格结构**：个人版 30 天试用后必须 $4.99/平台买断（无订阅）[1][3]。需求原点是「免费的 webhook 通知工具」[4]——Bark 免费提供了同级别的 iOS 原生体验（含重要警告、E2E 加密），Pushover 的付费无法用体验差距正当化。
- **闭源不可自托管**：与「有 NAS、想数据不出内网」的自建诉求完全相悖 [4]。

## 对比

- 与 Bark：同为 APNs 原生体验，Bark 免费 + 可自建 + E2E 加密；Pushover 胜在多平台一致性（一套 API 覆盖 iOS/Android/桌面且各端体验统一）与十年级商业稳定性。多平台且愿意付费时 Pushover 才反超——见 `../bark/report.md`。
- 逐维度对比见 `../comparison.md`。

## 风险与注意

- 价格口径为 2026-08-27 官网快照，购买前重新核对 [1]。
- Teams 版 $5/用户/月（含全平台），团队场景另算 [1]。

## 来源

1. Pushover: Pricing — https://pushover.net/pricing（查询 2026-08-27）
2. Pushover: Licensing — https://pushover.net/licensing（查询 2026-08-27）
3. How much does Pushover cost?（Pushover Support 官方问答）— https://support.pushover.net/i8-how-much-does-pushover-cost-is-there-a-subscription（访问 2026-08-27）
4. Claude 会话 13bf0e5c（2026-08-25）——「体验最好但 $5、不符合免费要求」判定来源
5. bark-server: Self-Hosted iOS Push Notifications（DEV.co，2026，含 Bark/FCM/OneSignal/Pushover 对比表）— https://dev.co/devops/open-source/bark-server（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录（2026-08-25 会话候选；官网核验价格结构） |
