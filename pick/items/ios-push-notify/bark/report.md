# Bark

> **TL;DR**：iOS 专属推送 App，完全免费、装好即得一个 URL，任何脚本 curl 一下就弹锁屏通知；官方服务器即开即用，有 NAS 可 Docker 自建 bark-server + E2E 加密把业务数据留在内网——「脚本→iPhone 弹通知」的默认答案。

- **结论**：adopt（推荐——2026-08-25 会话首推，本类默认选择）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | iOS App（免费）+ HTTP API（GET/POST 一条 URL 即推） | [1][2] |
| 许可证 | MIT（App 与 bark-server 双双开源） | [1][3] |
| 仓库 | github.com/Finb/Bark ⭐8,947（gh 2026-08-27） | [1] |
| 服务端 | bark-server v2.3.5（2026-05-21 发布），Go 单二进制 / Docker，⭐8,947（gh 2026-08-27） | [3][4] |
| 维护活跃度 | App 仓库 push 2026-08-18、bark-server push 2026-07-07，均已适配 iOS 26（App Store 更新日志，访问 2026-08-27） | [2][4] |
| 用户历史 | 2026-08-25 会话纯咨询：首推 Bark 与自建 bark-server 路线，**无部署/采纳记录** | [5] |

用法即一个 URL：

```bash
curl https://api.day.app/你的key/标题/内容
# 自建后换成 http(s)://你的服务器:8080/你的key/标题/内容
```

## 为什么选

- **免费且零门槛**：App Store 免费下载，装好直接用官方服务器 api.day.app，不需要任何注册 [1][2]。会话（2026-08-25）中列为首推：装好拿到 URL，任何地方 curl 一下就能推 iPhone [5]。
- **iOS 体验是同类最强档**：依托 APNs 系统推送，App 无需常驻、不耗电 [1]；支持通知分组、自定义图标/铃声、时效性通知、穿透勿扰的重要警告（critical alerts）、图片推送、更新/撤回已发通知（App Store 更新日志，访问 2026-08-27）[2]——这些是 PWA 和 IM 机器人路线给不了的。
- **自托管路线成熟且够轻**：bark-server 一个 Docker 容器即可自建，镜像内置 Bark App 的 APNs 证书，自建服务器直连 Apple 推送 [3][5]。对有 Synology NAS 的本库环境，10 分钟级别即可完成（会话方案 1，2026-08-25）[5]；生产建议前置 TLS 反代（Caddy/nginx 两行自动证书）[4][5]。
- **隐私可做到密文落 APNs**：支持自定义密钥端到端加密（2026 年更新为 AES-GCM combined 模式），推送内容在 Bark 服务器与 Apple APNs 上均为密文；消息历史经 NotificationServiceExtension 仅存本机 [2][5]。自建 + 加密 = 业务数据不出内网，只剩加密指令经 Apple——这是 iOS 平台上隐私上限第二高的路线（第一是自控证书的 Web Push，但代价见 web-push-pwa 报告）。

## 对比

- 与 ntfy：ntfy 多端通吃且更火（⭐8,947 vs ⭐8,947，gh 2026-08-27），但 **iOS 自建即时推送必须经官方 ntfy.sh 转发**，Bark 自建后完全不经第三方服务器 [3][5]，见 `../ntfy/report.md`。
- 与飞书群机器人：飞书零额外 App、卡片富文本，但消息内容经飞书云、呈现受飞书 App 通知策略约束；Bark 是独立通知通道、不受 IM 影响。两者可并存（脚本告警走 Bark、工作流告警走飞书），见 `../lark-webhook/report.md`。
- 与 Pushover：Pushover 体验口碑最佳但 $4.99/平台买断（2026-08-27 官网报价）[6]，Bark 免费且可自托管。
- 逐维度对比见 `../comparison.md`。

## 风险与注意

- **最后一跳必经 Apple**：iOS 锁屏通知必须走 APNs，这是系统层设计，绕不过；「自建」的实际含义是业务数据不经过任何第三方服务器，只有（加密后的）推送指令经过 Apple [5]。
- **自建仍依赖 Finb 的 APNs 证书**：bark-server 镜像内置的是 Bark App 的推送证书，证书生命周期不在自己手里；要完全自控证书只有 Web Push/VAPID 路线 [5]。待验证：Finb 证书若失效对自建实例的影响面。
- 官方服务器 api.day.app 的限流策略未见公开文档——**待验证**；重度使用建议直接自建。
- HTTP 明文调用（含自建内网地址）会把推送内容暴露在链路上，公网自建务必套 TLS [4][5]。

## 来源

1. Finb/Bark（GitHub README）— https://github.com/Finb/Bark（访问 2026-08-27）
2. Bark - Custom Notifications（App Store 页及更新日志）— https://apps.apple.com/us/app/bark-custom-notifications/id1403753865（访问 2026-08-27）
3. Finb/bark-server — https://github.com/Finb/bark-server（访问 2026-08-27）
4. bark-server: Self-Hosted iOS Push Notifications（DEV.co，v2.3.5/2026-05-21 快照）— https://dev.co/devops/open-source/bark-server（访问 2026-08-27）
5. Claude 会话 13bf0e5c（2026-08-25）——需求来源与自建方案讨论
6. Pushover: Pricing — https://pushover.net/pricing（查询 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（2026-08-25 会话首推 + gh/App Store 核验） |
