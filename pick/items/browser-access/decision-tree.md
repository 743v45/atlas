# 浏览器访问层 · 选型设计树

> 根问题的决策路径。叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

AI Agent（Claude Code / Codex / Cursor 等）要通过什么通道驱动浏览器——MCP server、CLI 子进程，还是更上层的 SDK 原语 / 自治框架？（调研 2026-08-27）

## 分叉与决策

### D1 先想清楚要哪一层（通道 / 原语 / 自治）

- 三者是**抽象层级而非竞争关系**，大型系统常三层叠用——这是本类别的选型框架。
- 通道层叶：[Chrome DevTools MCP](chrome-devtools-mcp/) adopt · [Playwright MCP](playwright-mcp/) trial
- 原语层叶：[Stagehand](stagehand/) adopt
- 自治层叶：[browser-use](browser-use/) adopt · [Skyvern](skyvern/) trial

### D2 token 经济学：MCP 还是 CLI？

- 2026 最大动态：微软把重心从 Playwright MCP 转向 Playwright CLI（state 存磁盘不进上下文）。
- CLI 路线零常驻 schema、`@e2` 紧凑引用——token 敏感多步任务首选；MCP 换来实时双向与生态原生。
- 决策：CLI 是第二条主路而非替代，按任务形态分层。
- 叶：[agent-browser](agent-browser/) adopt · [Playwright CLI](playwright-cli/) trial（太新，官方方向但生态待观察）

### D3 要独占能力还是通用覆盖？

- 调试 / 性能 / 网络瀑布 → DevTools MCP（trace/insight 独占，代价 schema 最重 ≈18k）。
- 跨浏览器测试 → Playwright MCP（唯一成熟三引擎）。
- 8 个 Agent 一键集成 → agent-browser（官方 skill 生态一等公民）。

### D4 要接管正在用的 Chrome（登录态）？

- 官方扩展路线：Claude in Chrome（side panel + debugger API，同 profile 同 tab）。
- 落选节点：[mcp-chrome](mcp-chrome/) hold（push 停 2026-01 放缓 7 个月，同类被更活跃项覆盖）；BrowserMCP ⭐7k 停 2025-04 勿选（观察名单）。
- 叶：[Claude in Chrome](claude-in-chrome/) trial（场景限定日常调试，不适合无人值守）

### D5 反检测也是需求？

- 交集孤例：Donut Browser 内置 MCP（见反检测类别 D3）；或 agent-browser + 云端 stealth 组合。

## 决策矩阵一致性

加权排序（comparison.md）：Stagehand 105 > Playwright CLI 99 > agent-browser 98——与 verdict 分层一致（三层各有 adopt）。
