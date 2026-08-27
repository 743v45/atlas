# 反检测浏览器 · 选型设计树

> 根问题的决策路径。叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

哪款反检测浏览器能让 AI（Agent/LLM）真正用起来——可被程序化驱动（API/SDK/CDP/MCP），而非只给人手的 GUI？（调研 2026-08-27，tvly + gh）

## 分叉与决策

### D1 对抗思路：补丁派还是引擎派？

- **补丁派**（Chromium 上修痕迹）：成本最低，改 import 即生效——已有 Playwright 代码的最低成本升级。
- **引擎派**（改浏览器源码，指纹从引擎「长」出来）：一致性理论最强，但接受 Firefox 引擎差异 + 维护断层史风险。
- 决策：两条都留，按场景分流（已有代码走补丁、指纹命门走引擎）。
- 叶：[Patchright](patchright/) adopt · [Camoufox](camoufox/) trial（断层史已回魂但 README 警告未撤，压级）

### D2 Python 直面 Cloudflare 的场景？

- 直连 DevTools WebSocket、控制平面无中间层 → undetected-chromedriver 官方继任。
- 前作已死（push 停 2025-07）→ 继任者维护也放缓 → fork 备选。
- 叶：[nodriver](nodriver/) trial · 落选节点：[undetected-chromedriver](undetected-chromedriver/) hold（⭐12.8k 但停更一年余——star 是存量、push 是生命体征）

### D3 需要多 Profile + Agent 直连？

- 开源界唯一自带 REST API + MCP server 的反检测浏览器，反检测 × Agent 一步到位。
- 叶：[Donut Browser](donut-browser/) trial · 落选节点：[Clawbrowser](clawbrowser/) hold（榜单声量大但 ⭐28，营销>社区，未达 ≥1k 门槛）
- 轻量备选：stealth-browser-mcp（观察名单，⭐1.7k）。

### D4 不想碰浏览器运维？

- 开源自托管：Steel（Apache-2.0）或 Browserless（老牌多 API）。
- 托管省心：Browserbase（业界安全默认）；成功率优先预算足：Bright Data（AIMultiple 97，观察名单）。
- 叶：[Browserbase](browserbase/) trial · [Steel Browser](steel-browser/) trial · [Browserless](browserless/) trial

### D5 商业指纹浏览器？

- 多账号矩阵（电商/社媒）场景才需要：AdsPower（中文/性价比）、Multilogin（指纹口碑/自研引擎）。
- 决策：个人 Agent 开发用不上，场景外 hold（能力未被否定）。
- 叶：[AdsPower](adspower/) hold · [Multilogin](multilogin/) hold

### D6 要的是整体爬虫而非精细控制？

- 一体化打包（反检测+代理+验证码）→ botasaurus。
- 叶：[botasaurus](botasaurus/) assess

## 决策矩阵一致性

加权排序（见 comparison.md 决策矩阵节）：Camoufox 110 > Patchright 105 > Donut 104 > Steel 102——矩阵高分与 verdict 分层的差异属正常分工（维度外风险以 verdict 为准）。
