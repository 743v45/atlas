# Telegram Bot

> **TL;DR**：Bot API 免费强大、客户端成熟，但大陆网络 Telegram 全线被墙：发送端服务器要可达 api.telegram.org、接收端 iPhone 都需常驻代理，把一个通知通道变成两个外部依赖——不推荐新采用，网络环境变化再重评。

- **结论**：hold（观望——工具本身优秀，网络可达性在本库环境不成立）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | Bot API（sendMessage 等）+ Telegram 客户端接收；也支持 webhook 回调 | [1] |
| 许可 | API 免费；客户端开源；服务端闭源云 | [1] |
| 官方文档 | core.telegram.org/bots（访问 2026-08-27） | [1] |

## 为什么（hold）

- **工具本身几乎无可挑剔**：完全免费、无注册门槛、Bot API 文档完善（会话 2026-08-25 评价「免费、无门槛」[4]）；客户端通知体验成熟。若网络无障碍，这是第一梯队候选。
- **大陆网络是决定性否决项**：Telegram 在中国大陆被防火长城整体封锁，访问需常驻 VPN（MyChina Guide 2026；Trip.com 2026 等多源一致）[2]。落到本场景是**双重依赖**：① 发送端（NAS/服务器上的脚本）要可达 api.telegram.org——国内服务器直连不可达，常见解法是境外节点/隧道回源（Pinggy 2025-05 实操记录）[3]；② 接收端 iPhone 的 Telegram 客户端本身也要翻墙——通知通道的最下游挂在一个需要代理才在线的 App 上，告警可靠性不成立。
- **会话判定一致**：2026-08-25 会话将其归入「其他：免费、无门槛，但国内网络要处理」[4]。本报告将「要处理」量化为双端依赖后，升级为 hold。

## 对比

- 与飞书机器人：同为「IM App 收通知」，飞书在国内直连、零额外 App（本库环境已装）；Telegram 表达力相当但被墙——见 `../lark-webhook/report.md`。
- 逐维度对比见 `../comparison.md`。

## 风险与注意

- 若未来主要基础设施在境外（VPS + 境外网络），否决项消失，可重评为 trial/adopt。
- 境外服务器中转 + 回源隧道的架构（Cloudflare Tunnel 等）可行 [3]，但为一条通知通道维护一条跨境隧道，复杂度收益比远差于 Bark/飞书。

## 来源

1. Telegram Bot API / Webhooks 官方文档 — https://core.telegram.org/bots/webhooks（访问 2026-08-27）
2. Does Telegram Work in China?（MyChina Guide，2026）— https://mychina.guide/blog/does-telegram-work-in-china（访问 2026-08-27）
3. How to Set Up and Test Telegram Bot Webhook（Pinggy Blog，2025-05-22）— https://pinggy.io/blog/how_to_set_up_and_test_telegram_bot_webhook（访问 2026-08-27）
4. Claude 会话 13bf0e5c（2026-08-25）——候选与网络限制判定来源

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录（2026-08-25 会话候选；核验大陆被墙为双端依赖） |
