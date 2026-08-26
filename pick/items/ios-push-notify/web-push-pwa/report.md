# Web Push + PWA（自建）

> **TL;DR**：唯一证书完全自控的路线：自生成 VAPID 密钥、不依赖任何 App 开发者的推送证书，iOS 16.4+ 主屏幕 PWA 可收锁屏通知；但无静默推送、自定义声音 iOS 17 才补齐、订阅页面与推送服务全要自己搭——彻底自持者再评估，暂不结论。

- **结论**：assess（评估——架构上最彻底，工程与 iOS 限制未实测）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 自建订阅页 + Service Worker + Web Push（VAPID）协议栈 | [1][4] |
| 许可 | W3C 开放标准，栈自选（web-push 库等均开源） | [1] |
| 平台门槛 | iOS 16.4+，且必须「添加到主屏幕」的 PWA——Safari 标签页内不推送 | [1][2] |

## 为什么（assess）

- **自持上限最高的路线**：自己生成 VAPID 密钥对，不依赖任何 App 开发者的推送证书——是唯一完全自控证书链的方案（会话 2026-08-25 方案 3：「最彻底的自持」；Bark 自建仍依赖 Finb 的 APNs 证书）[4]。APNs 在这条路上只搬运加密后的标准 Web Push 载荷。
- **iOS 支持是「能用」而非「好用」**：Web Push 仅对主屏幕 Web App 开放（2023 年 iOS 16.4 起）；不支持静默推送（无后台代码执行）、无自动安装提示；自定义声音缺失——ntfy 官方 known-issues 记录 Safari 将 Web Push 一律按无声处理，iOS 17/Safari 17 才修复 [1][2][3]。
- **工程量是独立小项目**：订阅落地页（iPhone 上触发权限弹窗并收集 endpoint）+ 推送服务 + 密钥管理都要自己搭，会话估计「几十行代码起步」但需长期维护 [4]；对比 Bark 的「装 App 即得 URL」，成本差一个量级。
- **EU 市场曾有反复**：2024 年 Apple 因 DMA 一度调整 EU 区 PWA 处理方式，相关限制随 iOS 版本多次变动（MobiLoud 2026 指南仍单列 EU 注意事项）[1]——**待验证**：本场景在中国区 Apple ID，影响面需按当前 iOS 版本实测。

## 对比

- 与 Bark：Bark 10 分钟落地、体验原生（铃声/重要警告/加密全有），代价是信任 Finb 的证书；PWA 证书全自控，代价是自建工程 + iOS 通知能力打折（无声等）[1][2][4]。见 `../bark/report.md`。
- 逐维度对比见 `../comparison.md`。

## 风险与注意

- iOS 对 PWA 的后台执行限制意味着通知点击前不能做任何本地处理（无 NotificationServiceExtension 等价物）[1][2]。
- 推送延迟通常及时，但 iOS 对低频使用的 Web Push 存在节流/清理订阅的报道（7 天不活跃清理订阅一类机制，MobiLoud 2026 综述口径）[1]——**待验证**：告警场景可靠性需实测。
- 通知无声 + 无徽章刷新的场景下，重要告警可能被漏看 [1][3]。

## 来源

1. Do Progressive Web Apps Work on iOS? The Complete Guide for 2026（MobiLoud）— https://www.mobiloud.com/blog/progressive-web-apps-ios（访问 2026-08-27）
2. PWA iOS Limitations and Safari Support（MagicBell，2026）— https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide（访问 2026-08-27）
3. ntfy Known issues（Safari Web Push 无声、iOS 17 修复记录）— https://docs.ntfy.sh/known-issues（访问 2026-08-27）
4. Claude 会话 13bf0e5c（2026-08-25）——方案 3（Web Push + PWA 最彻底自持）来源

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | assess | 首次记录（2026-08-25 会话方案 3 + iOS 支持现状核验） |
