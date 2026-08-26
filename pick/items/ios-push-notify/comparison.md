# iPhone Webhook 通知横评

> 调研时间 2026-08-27，方法 gh（GitHub 一手数据）+ tvly（Tavily）+ 官方文档核验；需求原点：2026-08-25 会话「iPhone 有没有免费的 webhook 通知工具」+ 追问「自建绕过的方案」。
> 核心命题：**脚本/CI/服务器告警 → iPhone 锁屏弹通知，选哪条通道**。硬约束两条：免费、（进阶）数据不出自己手里。天花板一条：**iOS 锁屏通知的最后一跳必经 Apple APNs，谁也绕不过**——「自建」的真实含义是业务数据不经过第三方服务器，只剩加密推送指令经 Apple（2026-08-25 会话结论，全部候选均受此约束）。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 「脚本跑完/CI/告警 → iPhone 弹通知」 | [Bark](bark/report.md) | 免费全功能，一个 URL 即推；官方服务器即开即用 |
| 有 Synology/服务器，要数据不出内网 | [Bark 自建 bark-server](bark/report.md) | Docker 一容器 + E2E 加密，APNs 上全是密文 |
| 已重度用飞书，工作流结果汇报 | [飞书群自定义机器人](lark-webhook/report.md) | 零额外 App、卡片富文本、100 条/分钟免费 |
| iOS + Android + 桌面多端告警 | [ntfy](ntfy/report.md)（试用） | 多端生态最强；iOS 注意 upstream 依赖 |
| 不在乎 5 美元、要多平台一致体验 | [Pushover](pushover/report.md)（观望） | 体验上限，但违反免费硬约束 |
| 要完全自控推送证书 | [Web Push + PWA](web-push-pwa/report.md)（评估） | 唯一 VAPID 自控路线，工程量大 |
| 大陆网络直连（无代理） | 排除 [Telegram Bot](telegram-bot/report.md) | 双端都要代理，告警可靠性不成立 |

**务实组合（2026-08-25 会话建议，贴合本库环境 Synology + 重度飞书；纯咨询、尚未部署）**：Bark（自建 bark-server 于 Synology）做主力告警通道 + 飞书群机器人做工作流汇报——两者互补不互斥。

## 一、先认清天花板：iOS 推送的最后一跳

无论选谁，锁屏通知都必须经 Apple APNs（iOS 系统层设计，2026-08-25 会话结论）。各候选的差别只在**谁的服务器能看到你的业务数据**：

| 路线 | 你的数据经手方 |
|------|---------------|
| Bark 自建 + E2E 加密 | 只有自己（APNs 见密文）[见 bark 报告] |
| Web Push + PWA | 只有自己（自控 VAPID 证书）[见 web-push-pwa 报告] |
| Bark 官方服务器 | Finb 的 api.day.app |
| ntfy 自建（iOS 即时） | 自建服务器 + ntfy.sh（仅消息 ID 元数据）[见 ntfy 报告] |
| 飞书机器人 / Telegram / Pushover | 对应厂商云 |

## 二、属性对比矩阵

| 维度 | Bark | ntfy | 飞书自定义机器人 | Telegram Bot | Pushover | Web Push + PWA |
|---|---|---|---|---|---|---|
| 形态 | iOS App + URL | App + HTTP pub-sub | 群机器人 webhook | IM 机器人 API | 商业 SaaS App | PWA + VAPID |
| 自托管 | ✅ bark-server(Docker)，iOS 直连 APNs | ⚠️ iOS 即时推送需官方 ntfy.sh 转发 poll_request | ❌ 飞书 SaaS | ❌ 依赖 TG 云 | ❌ 闭源 | ✅ 全自持（唯一自控证书路线） |
| 免费额度 | 完全免费（官方/自建均无文档限额） | ntfy.sh 250 条/天/visitor；自建无限 | 免费，100 条/分、5 条/秒 | 完全免费 | 30 天试用 → $4.99/平台买断（2026-08-27 官网价） | 完全免费（自建成本=工程时间） |
| iOS 体验 | 原生锁屏 + 重要警告 + 铃声/图标 + E2E 加密（AES-GCM） | 原生（官方服务器时）；自建退化见下 | 经飞书 App 通知，卡片富文本；受群免打扰约束 | 原生但客户端需代理 | 原生（口碑基准） | ⚠️ 无声（iOS 17 前无声，此后有限）、仅主屏幕 PWA、无静默推送 |
| 延迟 | APNs 秒级 | 官方/配 upstream 秒级；**自建无 upstream 分钟级轮询**（几分钟～约 20 分钟，issue #363/#1305 记录） | 秒级（待验证） | 秒级（双端代理在线为前提） | 秒级 | 及时，iOS 有节流风险（待验证） |
| 大陆直连 | ✅（自建内网更佳） | ✅ | ✅ | ❌ 全线被墙（MyChina Guide 2026） | ✅ | ✅（APNs 通道正常） |
| 多端覆盖 | 仅 iOS | iOS/Android/Web（最强） | 全飞书端 | 全 TG 端 | iOS/Android/桌面 | 任何支持 Web Push 的平台 |
| 许可 | MIT（App+server 双开源） | Apache-2.0 | 专有（免费功能） | API 免费/客户端开源 | 专有（商业） | 开放标准 + 自选栈 |
| star（gh 2026-08-27） | ⭐8,947（server ⭐3,595） | ⭐33,772 | —（SaaS） | —（平台） | —（闭源） | —（标准） |

（每格数据的来源与时间见对应条目报告；价格为 2026-08-27 官网快照。）

## 决策矩阵（加权）

<!--gen:decision-matrix-->

> 注记：决策矩阵只覆盖上表所列维度。lark-webhook 的 adopt 是**环境契合 verdict**（重度飞书 → 零成本零安装），该维度未入矩阵权重；矩阵高分与条件性 verdict 并存时，以各条目报告为准——这是两层的分工（RULES.md 第 5 节）。

## 三、GitHub 活跃度速查

<!--gen:activity-table-->

（仅两段式开源项目有 stats：Bark / ntfy。飞书、Pushover 为 SaaS 无仓库；Telegram 为平台 API；Web Push 为 W3C 标准。）

## 四、选型决策树

```
要 iPhone 收脚本/CI 告警
│
├── 预算 = 0？（硬约束）
│   └── 否，愿意 $4.99 买断多平台一致体验 → Pushover（hold：等付费意愿）
│
├── 数据能不能出内网？
│   ├── 不能，且要完全自控证书 → Web Push + PWA（assess：先实测 iOS 无声/节流）
│   ├── 不能，接受 Finb 证书 → Bark 自建 bark-server + E2E 加密（adopt·主力）
│   └── 无所谓 → 继续
│
├── 要不要多端（Android/桌面）？
│   ├── 要 → ntfy（trial：iOS 端配 upstream 或用官方 ntfy.sh）
│   └── 只要 iPhone → Bark（adopt）
│
├── 通知要不要进飞书工作流？
│   └── 要 → 叠加飞书群自定义机器人（adopt·补充通道）
│
└── 网络环境在大陆且无代理？
    └── 排除 Telegram Bot（hold：双端被墙）
```

## 五、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| Home Assistant Companion | iOS 推送稳、支持穿透勿扰的 critical alerts（2026-08-25 会话） | 为了通知装 HA 太重；已有 HA 者直接用 |
| Gotify | ⭐15,799、push 2026-08-26（gh），活跃 | **无官方 iOS App**（issue #87，2018 开至今）；第三方 iGotify 需额外组件——iOS 场景劣于 ntfy/Bark |
| Overpush（mrusme/overpush） | ⭐83、push 2026-01-13（gh） | 自托管 Pushover 平替，早期项目，观察成熟度 |
| Bark 官方服务器限流 | 未见公开文档 | **待验证**；重度使用建议自建 |
| Bark 的 Finb APNs 证书依赖 | 生命周期不透明 | **待验证**：证书失效对自建实例影响面 |

## 数据时间说明

本页所有 star / push / license 为 gh 2026-08-27 采集快照；价格为 pushover.net 2026-08-27 查询价；飞书限流为开放平台文档 2026-08-27 访问口径；iOS PWA 限制为 MobiLoud/MagicBell 2026 指南与 ntfy 官方 known-issues；Telegram 大陆被墙为 MyChina Guide 2026。复用前先核对时效（RULES.md 第 3 节）。
