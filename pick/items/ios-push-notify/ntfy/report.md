# ntfy

> **TL;DR**：开源 HTTP pub-sub 推送全家桶（iOS/Android/Web，Apache-2.0，⭐33,772.8k 高活跃），多端告警场景最强；硬伤在 iOS：自建服务器的即时推送必须经官方 ntfy.sh 转发 poll_request，不配 upstream 则退化为分钟级轮询（几分钟～约 20 分钟一档）——iPhone 单机场景让位 Bark，多端场景值得试用。

- **结论**：trial（试用——多端场景在非关键路径试用；iPhone 单机不推荐当主力）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | HTTP pub-sub：`curl -d "内容" ntfy.sh/你的topic` 即推，iOS/Android/Web 客户端订阅 | [1] |
| 许可证 | Apache-2.0 | [1] |
| 仓库 | github.com/binwiederhier/ntfy ⭐33,772、push 2026-08-25（gh 2026-08-27） | [1] |
| 官方服务 | ntfy.sh 免费托管：每 visitor 250 条/天，另有并发限流（60 并发、每 5 秒回填 1 次；docs 配置口径，访问 2026-08-27） | [2][3] |
| iOS App | App Store 免费（© 2026 Philipp Heckel，访问 2026-08-27） | [7] |

## 为什么（trial 而非 adopt）

- **多端与生态是它最强的地方**：一个 topic 语法覆盖 iOS/Android/桌面 Web，Docker 一行自建，社区热度远超同类（⭐33,772，gh 2026-08-27；对比 Gotify ⭐33,772、bark-server ⭐33,772）[1]。会话（2026-08-25）将其列为免费方案第二顺位 [6]。
- **iOS 是结构性短板，不是 bug**：官方文档明说——iOS 严格限制后台处理，自建服务器**不可能**不经中央服务器实现即时推送；要做即时，必须把 `poll_request` 转发到官方 ntfy.sh（或任何 APNs/Firebase 连接的 upstream），由它唤醒 iOS App 再回头拉取（docs.ntfy.sh/config，访问 2026-08-27）[2]。也就是说自建 ntfy 的 iOS 即时推送仍依赖官方基础设施——与「自建绕过第三方」的目标相悖（会话方案 2 的 ⚠️ 判定）[6]。
- **不配 upstream 的退化行为**：iOS App 退回周期性轮询（会话口径默认几分钟一次 [6]，社区记录可达约 20 分钟一档 [4][5]）+ 只显示「New message」占位，需手动刷新才见内容（2018 起 issue #363 讨论、2025-03 issue #1305 仍有「无推送、下拉才出现」报告）[4][5][8]。
- **隐私面**：upstream 转发的 poll_request 只含消息 ID 不含内容，消息正文留在自建服务器 [2]——比全量过云好，但元数据（何时推、推给哪个 topic）仍经 ntfy.sh。

## 对比

- 与 Bark：Bark 自建后**完全不经第三方服务器**（镜像内置 APNs 证书直连 Apple），ntfy 自建 iOS 必须挂官方 upstream；Android 上 ntfy 是完美方案、iPhone 上不推荐当主力（会话 2026-08-25 同口径）[6]，见 `../bark/report.md`。
- 官方 ntfy.sh 托管则无此问题（即时、免费），代价是 250 条/天限额 + 内容过官方服务器 [2][3]。
- 逐维度对比见 `../comparison.md`。

## 风险与注意

- `base-url` 必须与 iOS App 里填的 Default Server **完全一致**，否则 iOS 只见「New message」（官方 known-issues，访问 2026-08-27）[8]——自建排查时先核对这个。
- iOS 上游链路依赖 Firebase/APNs，官方文档自述「weird and buggy」，偶发掉订阅需重加 topic [8]。
- 免费 250 条/天对个人告警足够，但脚本风暴（如 for 循环里逐条推）会触顶 [3]。

## 来源

1. binwiederhier/ntfy — https://github.com/binwiederhier/ntfy（访问 2026-08-27）
2. ntfy Configuration 文档（iOS instant notifications / upstream-base-url）— https://docs.ntfy.sh/config（访问 2026-08-27）
3. ntfy Sending messages 文档（rate limits / 250 条/天）— https://docs.ntfy.sh/publish（访问 2026-08-27）
4. Self-Hosted Push Notifications with Ntfy on iOS（Noted，实测 walkthrough）— https://noted.lol/ntfy（访问 2026-08-27）
5. binwiederhier/ntfy issue #1305（2025-03-30：iOS 自建无推送、仅手动刷新可见）— https://github.com/binwiederhier/ntfy/issues/1305
6. Claude 会话 13bf0e5c（2026-08-25）——候选与「iOS 有坑」判定来源
7. ntfy（App Store）— https://apps.apple.com/us/app/ntfy/id1625396347（访问 2026-08-27）
8. ntfy Known issues（base-url 匹配 / New message / Firebase 抖动）— https://docs.ntfy.sh/known-issues（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录（2026-08-25 会话候选 + 官方文档核验 iOS upstream 限制） |
