# 反检测浏览器横评（AI Agent 可用方案）

> 调研时间 2026-08-27，方法 tvly（Tavily）+ gh（GitHub CLI 一手数据）。
> 核心命题：**不是「哪款反检测浏览器最强」，而是「哪款能让 AI（Agent/LLM）真正用起来」**——即提供 API/SDK/CDP/MCP 接口、可被程序化驱动，而不是只给人手的 GUI。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 个人/AI Agent 自动化，自托管，零成本起步 | [Patchright](patchright/report.md) | Playwright drop-in 替换，改一行 import 即生效 |
| Python 爬虫，直面 Cloudflare | [nodriver](nodriver/report.md) | undetected-chromedriver 官方继任，直连 DevTools WebSocket |
| 指纹一致性要求高，能接受 Firefox | [Camoufox](camoufox/report.md) | 引擎级改造，指纹从引擎「长」出来 |
| 多 Profile 管理 + AI 接口，自托管 | [Donut Browser](donut-browser/report.md) | 自带 REST API + MCP server，天生给 Agent 用 |
| 团队生产，要稳定性和观测 | [Browserbase](browserbase/report.md)（云） | 托管会话 + Stealth，最省心 |
| 多账号运营（电商/社媒矩阵） | [AdsPower](adspower/report.md) / [Multilogin](multilogin/report.md) | 商业指纹库 + REST API → debug 端口接管 |

## 一、为什么 AI 驱动的浏览器会被检测

反检测的前提是理解检测。Agent 驱动浏览器（Playwright/Puppeteer/Selenium）被识别的主要信号：

1. **CDP 协议握手痕迹**：启动时的 `Runtime.enable`、`Target.setAutoAttach` 调用序列，反机器人系统可在协议层识别（Patchright 修补的核心）。
2. **注入残留**：`window.__playwright__binding__` 等 JS 可被页面探测（Camoufox 把这些操作隔离在页面外作用域）。
3. **HeadlessChrome 标记**：UA 与 `navigator.webdriver` 等 headless 指纹。
4. **指纹不一致**：字体、WebGL、screen 属性自相矛盾——JS 注入式伪装只改表层，天然易露馅。

对抗思路分两派：**补丁派**（Patchright/nodriver：Chromium 上修痕迹）与**引擎派**（Camoufox：改浏览器源码，指纹一致性天然成立）。

## 二、跨方案属性对比

| 维度 | Patchright | nodriver | Camoufox | Donut | AdsPower/Multilogin | Browserbase/Steel 等 |
| ----- | -------------- | ------------ | -------------- | -------------- | ------------------- | ---------------------- |
| 形态 | 驱动库 | 驱动库 | 驱动库+定制浏览器 | GUI+API 浏览器 | GUI+API 商业浏览器 | 云 API |
| 反检测层级 | CDP 补丁 | 无中间层直连 | 引擎级（最强理论） | Profile 指纹管理 | 商业指纹库（最强商业） | 平台内置+代理 |
| AI 接入 | Playwright API | Python async | Playwright API | REST + **MCP** | REST → debug port | REST/SDK/MCP |
| 引擎 | Chromium | Chromium | Firefox | Chromium | 自研 Mimic/Stealthfox | Chromium |
| 许可 | Apache-2.0 | ⚠️ AGPL-3.0 | MPL-2.0 | ⚠️ AGPL-3.0 | 商业订阅 | 商业按量 |
| 成本 | 免费 | 免费 | 免费 | 免费 | €29+/mo | 按量/订阅 |
| 自托管 | ✅ | ✅ | ✅ | ✅ | 桌面端 | Steel/Browserless 可，余否 |
| star（gh 2026-08-27） | 4,189 | 4,698 | 11,449 | 3,717 | —（闭源） | —（Steel 7,542） |
| 最后 push（同上） | 2026-08-19 | 2026-05-13 | 2026-08-26 | 2026-08-26 | — | Steel 2026-08-25 |
| 维护风险 | 中 | 中（fork zendriver 备选） | 高（断层史，2026-08 已回魂） | 低（活跃） | 低（商业） | 低（商业） |

## 二·五、决策矩阵（加权）

<!--gen:decision-matrix-->

## 三、GitHub 活跃度速查

<!--gen:activity-table-->

（相邻生态另见观察名单：UI-TARS-desktop、crawl4ai、browser-use 等。选型门槛 ≥1k star。）

## 四、选型决策树

```
要反检测的浏览器给 AI 用
│
├── 已有 Playwright 代码?
│   └── 是 → Patchright（改 import，零迁移）
│
├── 纯 Python、直面 Cloudflare?
│   └── 是 → nodriver（停摆时切 zendriver）
│
├── 需要多 Profile / 多账号 / 指纹轮换?
│   ├── 自托管、要 MCP 直连 → Donut Browser（或 stealth-browser-mcp，观察名单）
│   └── 商业级稳定、付费 → AdsPower（中文/性价比）/ Multilogin（指纹口碑）
│
├── 指纹一致性是命门、接受 Firefox?
│   └── Camoufox（盯紧维护状态）
│
└── 不想碰浏览器运维?
    ├── 开源自托管 → Steel / Browserless
    └── 托管省心 → Browserbase；成功率优先且预算足 → Bright Data
```

## 五、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| zendriver | ⭐1,409，push 2026-08-16 | nodriver 社区 fork，nodriver 停摆时切换 |
| stealth-browser-mcp | ⭐1,667，push 2026-07-24，MIT | 「反检测×MCP」轻量封装，Donut 的备选 |
| Bright Data（云） | AIMultiple 2026 综合 97（成功率 95%） | 企业级、代理网络加成，贵但能打 |
| Kernel（云） | 官方口径浏览器创建 30ms p50 / 105ms p99（kernel.sh 2026 自述）；SigNoz 案例从 140ms 优化至 30ms | 极速沙箱，内置观测遥测 |
| Hyperbrowser（云） | AIMultiple 2026 综合 62 | Agent 品牌最强但综合分落后 Steel（72） |
| BrowserAI / Anchor（云） | AIMultiple 2026 综合 87 / 82 | 新兴，关注即可 |
| GoLogin / BitBrowser（商业） | 同 AdsPower/Multilogin 模式 | 中文圈常用，未单独评估 |
| UI-TARS-desktop | ⭐38,708，push 2026-08-05 | 字节出品 GUI/视觉 Agent，相邻生态 |
| crawl4ai | ⭐79,463 | LLM 友好爬虫（非反检测），常与本赛道组合用 |

## 六、合规边界

反检测工具用于**访问自己拥有的内容、已授权的自动化、绕过误伤性 bot 拦截**是正当用途；用于大规模绕过目标站反爬、违反 ToS 抓取、账号矩阵灰色运营则有法律与封号风险。指纹浏览器商业方案的合规责任同样由使用者承担。选型时把「目标站允许什么」当第一约束，工具只是实现层。

## 数据时间说明

本页所有 star / push / license 为 gh 2026-08-27 采集快照；评测结论均标注评测方与年份；价格以标注查询日期为准。**过期数据比没有数据更危险**——复用本页前先核对时效（RULES.md 第 3 节）。
