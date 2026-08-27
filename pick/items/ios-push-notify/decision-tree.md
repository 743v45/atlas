# iPhone Webhook 通知 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

iPhone 有没有免费的 webhook 工具用于接收通知；自建、绕过第三方服务器的方案？（2026-08-24/25 会话；用户环境：Synology NAS、Docker/caddy 熟练、重度飞书）

## 分叉与决策

### D1 免费是不是硬约束？

- 是。Pushover 体验口碑最好但 $4.99/平台买断——直接出局。
- 落选节点：[Pushover](pushover/) hold · [Telegram Bot](telegram-bot/) hold（大陆网络双端被墙）

### D2 iOS 推送的硬天花板？

- 锁屏通知最后一跳必须走 Apple APNs，绕不过——「绕过第三方」的实际含义只是**业务数据不过第三方**（加密推送指令仍过 Apple）。这条天花板写进所有方案的风险节。

### D3 首选通道？

- Bark：iOS 免费+开源（⭐8,947），官方 api.day.app 一个 URL curl 即推；2026 年更新密集（iOS 26 适配、AES-GCM、通知撤回）。
- 自建诉求 → 自建 bark-server（Docker 镜像内置 APNs 证书、E2E 加密、Caddy 套 TLS、10 分钟）。
- 叶：[Bark](bark/) adopt

### D4 要和工作流合并？

- 重度飞书用户：群自定义机器人零成本（限额 100 条/分、5 条/秒，无数据访问权限）——通知即消息流，可检索可归档。
- 叶：[飞书群机器人](lark-webhook/) adopt（环境契合）

### D5 自建即时性陷阱？

- **ntfy 的坑**：自建服务器在 iOS 是轮询模式（分钟级～约 20 分钟），即时推送必须 upstream-base-url 转发到官方服务器（只含消息 ID 不含正文）——自建的意义打折，故 trial 非 adopt。
- 叶：[ntfy](ntfy/) trial（⭐33,772 极活跃，Android/桌面场景仍是好选择）

### D6 完全自控证书的路线？

- Web Push + PWA（VAPID）：唯一不过任何第三方推送服务器的路线（iOS 16.4+），但工程量大 + iOS 无声推送受限。
- 叶：[Web Push + PWA](web-push-pwa/) assess

## 备注

会话为纯咨询、无部署记录（与 ASR/知识库类别的「实际采纳」形成对照）；观察名单：Gotify（无官方 iOS App）、Overpush、Home Assistant（能穿透勿扰但太重）。
