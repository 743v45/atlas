---
theme: default
title: AI 用浏览器 · 选型报告 2026
info: |
  反检测浏览器 & 浏览器访问层（MCP/CLI）横评速览。
  数据采集 2026-08-27（gh 一手数据 + tvly 调研）。
  详细报告见 tlrt 仓库 tools/ 目录。
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: system-ui, -apple-system, 'PingFang SC', 'Hiragino Sans GB', sans-serif
---

# AI 用浏览器 · 选型报告 2026

### 反检测浏览器 × 访问层（MCP / CLI）

<div class="pt-8 flex items-center gap-6 text-sm opacity-70">

<span>调研 **2026-08-27**</span>
<span>·</span>
<span>gh 一手数据 + tvly</span>
<span>·</span>
<span>完整报告 `tlrt/tools/`</span>

</div>

<div class="abs-bottom-10 left-10 border-l-4 border-gray-200 pl-4 text-sm opacity-80">

核心命题：不是「哪款最强」，而是**哪款能让 AI 真正用起来**——
可被程序化驱动（API / SDK / CDP / MCP），而非只给人手的 GUI。

</div>

---
transition: slide-left
---

# 两个正交的命题

<div class="grid grid-cols-2 gap-8 pt-4">

<div class="rounded-lg border border-gray-200 p-5">

### 🛡️ 反检测浏览器

被驱动的浏览器**本体**怎么选——不被识别为 bot

`tools/anti-detect-browser/` · 12 份报告

四条路线：补丁 / 引擎 / 一体浏览器 / 商业 / 云

</div>

<div class="rounded-lg border border-gray-200 p-5">

### 🎛️ 访问层

Agent 通过什么**通道**驱动浏览器

`tools/browser-access/` · 9 份报告

四层：MCP / CLI / SDK 原语 / 自治框架

</div>

</div>

<v-click>

<div class="mt-8 rounded-lg bg-blue-50 border border-blue-200 p-4 text-sm">

**交集孤例 · Donut Browser** —— 自托管反检测浏览器、内置 MCP server。
要「反检测 且 Agent 直连」的单一方案，目前只有它（⭐3.7k，AGPL，日更）。

</div>

</v-click>

---
layout: two-cols
---

# 为什么会被检测

<v-clicks>

1. **CDP 握手痕迹** — `Runtime.enable` / `Target.setAutoAttach` 启动序列
2. **注入残留** — `window.__playwright__binding__` 可被探测
3. **HeadlessChrome 标记** — UA 与 `navigator.webdriver`
4. **指纹不一致** — JS 注入只改表层，字体 / WebGL / screen 自相矛盾

</v-clicks>

::right::

<br>

<div class="space-y-5 pt-2">

<div class="rounded-lg border border-gray-200 p-4">

**补丁派** — Chromium 上修痕迹

Patchright · nodriver

</div>

<div class="rounded-lg border border-gray-200 p-4">

**引擎派** — 改源码，指纹从引擎「长」出来

Camoufox（Firefox / C++）

</div>

</div>

---

# 反检测 · 属性对比矩阵

<div class="w-full pt-2">

<table class="w-full table-fixed text-[10.5px] leading-tight">
  <thead><tr>
    <th class="w-[8.5rem] text-left font-medium opacity-60"></th>
    <th class="text-left">Patchright</th><th class="text-left">nodriver</th><th class="text-left">Camoufox</th>
    <th class="text-left">Donut</th><th class="text-left">AdsPower / ML</th><th class="text-left">Browserbase</th>
  </tr></thead>
  <tbody>
    <tr><td class="font-bold">反检测层级</td><td>CDP 补丁</td><td>无中间层直连</td><td class="font-bold">引擎级</td><td>Profile 指纹管理</td><td class="font-bold">商业指纹库</td><td>平台内置 + 代理</td></tr>
    <tr><td class="font-bold">AI 接入</td><td>Playwright API</td><td>Python async</td><td>Playwright API</td><td>REST + MCP</td><td>REST → debug 端口</td><td>REST / SDK / MCP</td></tr>
    <tr><td class="font-bold">引擎</td><td>Chromium</td><td>Chromium</td><td>Firefox</td><td>Chromium</td><td>自研双引擎</td><td>Chromium</td></tr>
    <tr><td class="font-bold">许可</td><td>Apache-2.0</td><td class="text-amber-700">AGPL-3.0</td><td>MPL-2.0</td><td class="text-amber-700">AGPL-3.0</td><td>商业订阅</td><td>商业按量</td></tr>
    <tr><td class="font-bold">成本</td><td>免费</td><td>免费</td><td>免费</td><td>免费</td><td>€29+/mo</td><td>按量计费</td></tr>
    <tr><td class="font-bold">自托管</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>桌面端</td><td>❌（Steel 可）</td></tr>
    <tr><td class="font-bold">维护 08-27</td><td>活跃</td><td>放缓 → zendriver</td><td>断层已回魂</td><td>日更</td><td>商业稳定</td><td>商业稳定</td></tr>
  </tbody>
</table>

</div>

<div class="text-[11px] opacity-50 mt-3">琥珀色许可 = AGPL 网络服务传染，商用注意 · 维护列为 gh 2026-08-27 快照</div>

---

# 反检测 · 社区规模一览

<div class="pt-4 space-y-[11px] text-[13px]">

<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">browser-use*</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:100%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">110.8k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">crawl4ai*</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:71.6%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">79.5k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">browserless</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:12.3%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">13.6k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">udet-chromedriver</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:11.6%;background:#c9c7c0"></div></div><span class="w-14 font-mono text-[12px]">12.8k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">camoufox</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:10.3%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">11.5k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">steel-browser</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:6.8%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">7.5k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">botasaurus</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:5.1%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">5.7k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">nodriver</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:4.2%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">4.7k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">patchright</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:3.8%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">4.2k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">donutbrowser</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:3.4%;background:#2a78d6"></div></div><span class="w-14 font-mono text-[12px]">3.7k</span></div>
<div class="flex items-center gap-3"><span class="w-40 text-right font-medium">clawbrowser</span><div class="flex-1 h-[9px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:0.5%;background:#d03b3b;min-width:4px"></div></div><span class="w-14 font-mono text-[12px] text-red-700 font-bold">28</span></div>

</div>

<div class="text-[11px] opacity-50 mt-4">gh 快照 2026-08-27 · * 为相邻生态参照 · <span class="text-red-700">灰条 = 已停更</span>（udet-chromedriver push 停在 2025-07，勿选）· clawbrowser ⭐28 未达门槛</div>

---

# 访问层 · 2026 最大动态

<div class="pt-2">

**Microsoft 把重心从 Playwright MCP 转向 Playwright CLI**（Kualitatem 2026）

</div>

<div class="grid grid-cols-2 gap-8 pt-6">

<div class="rounded-lg border border-gray-200 p-5 text-sm">

### MCP server

常驻 schema 占上下文，多步往返累积

生态：Claude 原生、协议标准

适合：实时双向、IDE 集成

</div>

<div class="rounded-lg border border-blue-300 bg-blue-50 p-5 text-sm">

### CLI 子进程

**state 存磁盘不进上下文**，回传紧凑引用

生态：任何能跑 shell 的 Agent

适合：token 敏感、批处理、可组合

</div>

</div>

<v-click>

> CLI 不是 MCP 的替代，而是 **token 经济学更优的第二条主路** —— 两者长期并存。

</v-click>

---

# 访问层 · 常驻 token 成本

<div class="pt-6 space-y-4 text-[13px]">

<div class="flex items-center gap-3"><span class="w-36 text-right font-medium">DevTools MCP</span><div class="flex-1 h-[10px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:100%;background:#2a78d6"></div></div><span class="w-16 font-mono text-[12px]">≈18k</span></div>
<div class="flex items-center gap-3"><span class="w-36 text-right font-medium">Playwright MCP</span><div class="flex-1 h-[10px] bg-gray-100 rounded-r"><div class="h-full rounded-r" style="width:76%;background:#2a78d6"></div></div><span class="w-16 font-mono text-[12px]">≈13.7k</span></div>
<div class="flex items-center gap-3"><span class="w-36 text-right font-medium">Playwright CLI</span><div class="flex-1 h-[10px] bg-gray-100 rounded-r"></div><span class="w-16 font-mono text-[12px] font-bold text-green-700">≈0</span></div>
<div class="flex items-center gap-3"><span class="w-36 text-right font-medium">agent-browser</span><div class="flex-1 h-[10px] bg-gray-100 rounded-r"></div><span class="w-16 font-mono text-[12px] font-bold text-green-700">≈0</span></div>

</div>

<div class="text-[11px] opacity-50 mt-4">2025-11 公开基准（Trackingplan 2026 引述）· 运行时多步任务 MCP 成本反超（Trackingplan 2026 实测）</div>

<v-click>

<div class="mt-6 border-l-4 border-gray-200 pl-4 text-sm">

CLI 的杀手锏不只是 0 常驻——**浏览器状态留在磁盘、只回传 `@e2` 这类紧凑引用**，
多步任务的累积成本优势远大于 schema 差。

</div>

</v-click>

---

# 访问层 · 属性对比矩阵

<div class="w-full pt-2">

<table class="w-full table-fixed text-[10.5px] leading-tight">
  <thead><tr>
    <th class="w-[8.5rem] text-left font-medium opacity-60"></th>
    <th class="text-left">DevTools MCP</th><th class="text-left">Playwright MCP</th><th class="text-left">agent-browser</th>
    <th class="text-left">Playwright CLI</th><th class="text-left">Stagehand</th><th class="text-left">browser-use</th>
  </tr></thead>
  <tbody>
    <tr><td class="font-bold">形态</td><td>MCP server</td><td>MCP server</td><td>CLI（Rust）</td><td>CLI</td><td>SDK（TS/Py）</td><td>自治框架</td></tr>
    <tr><td class="font-bold">常驻 token</td><td>≈18k（最重）</td><td>≈13.7k</td><td class="font-bold text-green-700">≈0</td><td class="font-bold text-green-700">≈0</td><td>N/A（代码内）</td><td>N/A</td></tr>
    <tr><td class="font-bold">状态管理</td><td>进程内会话</td><td>进程内会话</td><td>磁盘 + @e2 引用</td><td>磁盘引用</td><td>代码控制</td><td>Agent 规划</td></tr>
    <tr><td class="font-bold">引擎覆盖</td><td>Chromium 系</td><td class="font-bold">三引擎</td><td>Chromium（CDP）</td><td>三引擎</td><td>三引擎（PW）</td><td>Chromium</td></tr>
    <tr><td class="font-bold">独占能力</td><td>trace / 网络 / console</td><td>跨引擎测试</td><td>8 个 Agent skill</td><td>微软官方方向</td><td>act/extract/observe</td><td>自治 89.1%</td></tr>
    <tr><td class="font-bold">许可</td><td>Apache-2.0</td><td>Apache-2.0</td><td>Apache-2.0</td><td>Apache-2.0</td><td>MIT</td><td>MIT</td></tr>
    <tr><td class="font-bold">star 08-27</td><td>49.7k</td><td>36.5k</td><td>41.4k</td><td>monorepo 95k</td><td>24.1k</td><td>110.8k</td></tr>
  </tbody>
</table>

</div>

<div class="text-[11px] opacity-50 mt-3">token 数据 2025-11 基准 · star 为 gh 2026-08-27 快照 · N/A = 不经上下文</div>

---

# 选型前先问：要哪一层？

<div class="grid grid-cols-3 gap-6 pt-6">

<div class="rounded-lg border border-gray-200 p-5">

### 通道

**Agent 自己看页面、亲手点**

MCP：DevTools / Playwright
CLI：agent-browser / PW CLI

</div>

<div class="rounded-lg border border-gray-200 p-5">

### 原语

**代码里调页面级操作**

Stagehand ⭐24.1k

act / extract / observe

</div>

<div class="rounded-lg border border-gray-200 p-5">

### 自治

**给目标它自己跑**

browser-use ⭐110.8k
Skyvern ⭐22.9k

</div>

</div>

<div class="pt-8 text-center opacity-70">

三者是**抽象层级而非竞争关系** —— 大型系统常三层叠用

</div>

---
layout: center
---

# 数据时间是硬规则

<div class="text-lg opacity-70 pt-2">无时间戳的数据视为无效 —— 过期数据比没有数据更危险</div>

<div class="grid grid-cols-3 gap-6 mt-10 text-sm">

<div class="rounded-lg border border-red-200 bg-red-50 p-5">

**⭐12.8k 但已死**

undetected-chromedriver

push 停在 2025-07

</div>

<div class="rounded-lg border border-gray-200 p-5">

**评测说 12k，实际 41k**

agent-browser

评测文章引用旧数据

</div>

<div class="rounded-lg border border-red-200 bg-red-50 p-5">

**⭐28 营销号**

clawbrowser

榜单声量 ≠ 社区热度

</div>

</div>

<div class="pt-10 text-center">

**star 是存量声誉，push 才是生命体征。** 本报告数据采集于 2026-08-27，复用前先核对时效。

</div>

---

# 场景速配

<div class="grid grid-cols-2 gap-8 pt-4 text-[13px]">

<div>

| 反检测场景 | 选 |
|---|---|
| 已有 Playwright 代码 | **Patchright** |
| 纯 Python 直面 CF | **nodriver** |
| 指纹一致性命门 | **Camoufox** |
| 多 Profile + MCP | **Donut** |
| 生产省心（云） | **Browserbase** |
| 多账号矩阵 | **AdsPower / ML** |

</div>

<div>

| 访问层场景 | 选 |
|---|---|
| Claude Code 日常 | **agent-browser** |
| token 敏感多步 | **Playwright CLI** |
| 调试 / 性能 / 网络 | **DevTools MCP** |
| 跨浏览器测试 | **Playwright MCP** |
| 接管现有 Chrome | **Claude in Chrome** |
| 自研 Agent 原语 | **Stagehand** |

</div>

</div>

<div class="text-[12px] opacity-60 pt-6">务实组合（2026 共识）：按任务形态分层 —— 测试 PW MCP · 日常 Claude in Chrome · 深度性能 DevTools MCP · 长任务切 CLI</div>

---
layout: center
---

# 合规边界

<div class="text-sm leading-7 max-w-2xl mx-auto pt-4">

**正当**：自有内容 · 已授权自动化 · 绕过误伤性 bot 拦截

**风险**：大规模绕过反爬 · 违反 ToS 抓取 · 账号矩阵灰色运营

<br>

> 把「目标站允许什么」当第一约束，工具只是实现层。

</div>

---

# 收尾

<div class="text-sm leading-7">

**交付物**

- 📁 `tools/anti-detect-browser/` — 12 份工具报告 + 横评
- 📁 `tools/browser-access/` — 9 份工具报告 + 横评
- 🧾 `index.html` — 索引（`refresh-stats.py` + `build-index.py` 两条命令全量保鲜）
- 规则：`RULES.md` · 本 deck：`decks/browser-selection-2026/`

**复核提醒**：verified = 2026-08-27 · 超 180 天索引自动标「待复核」

</div>

<div class="pt-8 text-sm opacity-60">

*论断必有出处，数据必带时间 —— 每份报告末节「来源」逐条可查。*

</div>
