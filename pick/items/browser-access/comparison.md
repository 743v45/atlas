# 浏览器访问层横评（MCP 与 CLI）

> 调研时间 2026-08-27，方法 tvly（Tavily）+ gh（GitHub CLI 一手数据）。
> 核心命题：**AI Agent（Claude Code / Codex / Cursor 等）要通过什么通道驱动浏览器**——MCP server、CLI 子进程，还是 SDK 原语？2026 年最大动态是 Microsoft 把重心从 Playwright MCP 转向 Playwright CLI，**token 经济学正在改写这条赛道**。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| Claude Code 里的日常通用浏览器操作 | [agent-browser](agent-browser/report.md) | Rust CLI，`@e2` 元素引用极省 token，官方 skill 一行装 |
| 自研 Agent 要页面级原语 | [Stagehand](stagehand/report.md) | act/extract/observe 三原语 SDK |
| token 敏感的多步任务 | [Playwright CLI](playwright-cli/report.md) | state 存磁盘不进上下文，微软官方演进方向 |
| 调试/性能分析、看网络瀑布 | [Chrome DevTools MCP](chrome-devtools-mcp/report.md) | trace/insight 能力独占 |
| 跨浏览器测试 | [Playwright MCP](playwright-mcp/report.md) | 唯一成熟跨引擎选项 |
| 接管你**正在用**的 Chrome | [Claude in Chrome](claude-in-chrome/report.md) | 官方扩展，同 profile 登录态 |
| 自治执行（给目标它自己跑） | [browser-use](browser-use/report.md) | 自治层顶流，WebVoyager 89.1% |
| 云端托管、免本地浏览器 | Browserbase MCP（观察名单） | 云会话 + Stealth，与反检测复合 |
| 反检测 + MCP 一步到位 | [Donut Browser 内置 MCP](../anti-detect-browser/donut-browser/report.md) | 自托管反检测浏览器自带 MCP |

## 一、两条路线的本质差异

| 维度 | MCP server | CLI 子进程 |
|------|-----------|-----------|
| 形态 | 常驻进程，暴露结构化工具 schema | 按需 spawn 的命令，输出即结果 |
| 上下文成本 | **schema 常驻上下文**（Playwright MCP ≈13.7k；DevTools MCP ≈18k，2025-11 基准），多步任务运行时往返累积 | 零常驻 schema；`--help` 按需加载；**state 存磁盘不进上下文** |
| 状态管理 | server 内维持会话 | 文件系统即状态（snapshot 引用如 `@e2`），可组合、可断点续传 |
| 生态 | Claude Desktop/Code 原生，协议标准化 | 任何能跑 shell 的 Agent 都能用 |
| 适用 | 实时双向交互、IDE 集成、复杂会话 | token 敏感、批处理、可脚本化组合 |

2026 年动向：微软发布 Playwright CLI 并明示重心迁移（Kualitatem 2026）；Vercel agent-browser 从另一头（Rust 性能 + CLI 组合性）印证同一趋势。**CLI 不是 MCP 的替代，而是 token 经济学更优的第二条主路**；两者长期并存。

## 二、通道 / 原语 / 自治：先想清楚要哪层

| 层 | 回答的问题 | 代表 | 特征 |
|---|---|---|---|
| 通道 | Agent 自己看页面、亲手点 | MCP（DevTools/Playwright）、CLI（agent-browser、playwright-cli） | 通用、可控性最强、每步 token 成本敏感 |
| 原语 | 代码里调页面级操作 | [Stagehand](stagehand/report.md) | act/extract/observe，确定性与效率的折中 |
| 自治 | 给目标它自己跑 | [browser-use](browser-use/report.md)、[Skyvern](skyvern/report.md) | LLM 规划，不确定性最高 |

三者是**抽象层级而非竞争关系**，大型系统常三层叠用。

## 三、token 成本速查

| 方案 | 常驻成本 | 运行时特征 |
|------|---------|-----------|
| Playwright MCP | ≈13.7k（schema） | 多步任务往返累积，长 journey 成本高 |
| Chrome DevTools MCP | ≈18k（schema） | 同上；换来 trace/网络独占能力 |
| Playwright CLI | ≈0 | state 存磁盘，回传紧凑引用 |
| agent-browser | ≈0（skill 按需） | `@e2` 元素引用 + Web 调试 UI 压缩快照 |

（MCP schema 数据：2025-11 公开基准，Trackingplan 2026 引述；运行时结论：Trackingplan 2026 实测。）

## 三·五、属性对比矩阵

| 维度 | Chrome DevTools MCP | Playwright MCP | agent-browser | Playwright CLI | Stagehand | browser-use |
|---|---|---|---|---|---|---|
| 形态 | MCP server | MCP server | CLI（Rust） | CLI | SDK（TS/Python） | 自治框架（Python） |
| 常驻 token | ≈18k（最重） | ≈13.7k | **≈0** | **≈0** | N/A（代码内调用） | N/A |
| 状态管理 | 进程内会话 | 进程内会话 | **磁盘 + `@e2` 引用** | **磁盘引用** | 代码控制 | Agent 规划 |
| 引擎覆盖 | Chromium 系 | **三引擎** | Chromium（CDP） | 三引擎 | 三引擎（PW 底座） | Chromium |
| 独占能力 | trace / 网络瀑布 / console | 跨引擎测试 | 8 个 Agent 官方 skill | 微软官方演进方向 | act/extract/observe 三原语 | 自治执行（WebVoyager 89.1%） |
| 许可 | Apache-2.0 | Apache-2.0 | Apache-2.0 | Apache-2.0 | MIT | MIT |
| star（gh 2026-08-27） | 49,749 | 36,492 | 41,373 | monorepo 95,165 | 24,065 | 110,792 |

## 决策矩阵（加权）

<!--gen:decision-matrix-->

## 四、GitHub 活跃度速查

<!--gen:activity-table-->

（跨类别与观察项另见观察名单：Donut Browser（反检测类）、stealth-browser-mcp、Browserbase MCP 等。microsoft/playwright 本体 95,165 即 `@playwright/cli` 所在 monorepo；browser-use ⭐110k+ 见反检测横评。选型门槛 ≥1k star。）

## 五、选型决策树

```
Agent 要驱动浏览器
│
├── 环境里有 MCP 生态（Claude Desktop/Code）?
│   ├── 要调试/性能/网络 → Chrome DevTools MCP
│   ├── 要跨浏览器测试 → Playwright MCP
│   ├── 要接现有登录态会话 → Claude in Chrome（mcp-chrome 放缓，暂 hold）
│   ├── 要云端+反检测 → Browserbase MCP
│   └── 要持久 profile 长任务 → Browser Use MCP
│
├── token 敏感 / 长任务 / 可组合?
│   ├── Playwright 生态 → Playwright CLI
│   └── 通用 CLI Agent → agent-browser（Vercel）
│
└── 反检测也是需求?
    └── Donut Browser / stealth-browser-mcp（MCP 自带）或 agent-browser + 云端 stealth

前置问题：要通道（MCP/CLI）、原语（Stagehand）还是自治（browser-use/Skyvern）？
三者是抽象层级而非竞争关系，大型系统常三层叠用。
```

务实组合（2026 共识，Medium/Lalatendu 综述口径）：**测试与预发验证用 Playwright MCP，日常开发调试用 Claude in Chrome，深度性能网络分析加 Chrome DevTools MCP，长任务与 token 敏感场景切 CLI**——按任务形态分层，而非一门工具打天下。

## 六、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| Browser Use MCP | browser-use 本体的通道之一 | 主打持久 profile 与长任务，本体见 browser-use 报告 |
| Browserbase MCP | ⭐3,409，push 2026-07-20 | 云会话 + Stealth；本体见反检测横评 |
| Webfuse MCP | 小众 | 面向「线上用户会话」实时协作场景 |
| stealth-browser-mcp | ⭐1,667，push 2026-07-24 | 反检测×MCP 交集，Donut 的轻量替代 |
| BrowserMCP/mcp | ⭐7,018，push 2025-04-24 | ❌ 停更一年余，勿选 |

## 数据时间说明

本页所有 star / push / license 为 gh 2026-08-27 采集快照；token 成本为 2025-11 公开基准（Trackingplan 2026 引述）；评测结论均标注评测方与年份。复用前先核对时效（RULES.md 第 3 节）。
