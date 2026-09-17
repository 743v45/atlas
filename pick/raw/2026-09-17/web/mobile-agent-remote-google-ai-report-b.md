# 口碑原始留档 · 谷歌 AI 调研报告 B(带引用来源版)

> 采集方式:同报告 A(同一会话第二次查询,产出更严谨)。
> 采集日期:2026-09-17。采集者:taevas。
> 可信度注记:本报告引用一手 issue 编号/release notes/App Store 原话,经主会话 gh API 直查复核:**happy #489/#496/#503、t3code #7338、claudecodeui #190/#204/#206、paseo release v0.1.65 全部真实存在**。已知错误:「Omnara 2025-09 后停更」系引用过时第三方索引(ecosyste.ms),gh API 直查 pushed_at=2026-09-16,不成立;「Zedra 迁至 deltaqdev/zedra」——gh API 显示 canonical 名仍为 tanlethanh/zedra(MIT,pushed 2026-09-15),迁移说法待验证。

---

# 手机端遥控 Claude Code / Codex / 编程 Agent 客户端口碑调研报告

## 摘要

截至 **2026 年 8 月 17 日**，这个赛道已经从"手机能不能连上"转向三个更难的承诺：**笔记本合盖后续航、审批交互是否可靠、第三方中继能否被信任**。社区公开讨论仍高度碎片化，最可靠的"排名信号"来自更新频率、issue 可见度和应用商店少量评价，而不是可信的"我把所有 App 都试了一遍"第三方横评。按现有证据，综合推荐位次可概括为：**Happy 仍是 Claude/Codex 双代理、BYOK 和推送审批的高频默认；Paseo 是多代理编排的第一选择；Claude Code 官方 Remote Control 是纯 Claude 场景的零配置入口，但不解决合盖问题。** Omnara 的仓库索引显示 2025-09 后未更新，已不能按活跃项目推荐。【复核注记:此 Omnara 结论已证伪】

若只遥控 OpenCode，实际可验证的推荐是 **dzianisv/opencode-mobile（Android，2026-08-14 仍在更新、无第三方中继）**；doza62 的 iOS/跨端方案评价样本极少，但作者自己在 3 月承认仍是 beta、重连和通知不稳定；Shahfarzane 版本自 2026-01-15 后未见提交。"用自己的 API Key / 本地模型"这一需求下，社区最明确的技术组合不是某个最热的 App，而是 **Tailscale/VPN + 自托管 OpenCode/Claude/Codex + 原生客户端或手机 Web UI**，因为数据流、密钥和运行环境都可以留在用户控制范围内。

## 一、赛道不是"又一个 App 排名"，而是三种架构之争

**所谓"手机遥控"，其实至少有三种不同的产品承诺。** 第一类是"本地代理中继"：开发机运行 Claude Code 或 Codex，手机经 App、浏览器或中继连接并接管会话；第二类是"手机或云端工作区"：容器、Codespaces 或云端运行环境持续承载 Agent，手机只是入口；第三类是"聊天入口/自托管看板"：Telegram、Web UI、看板或任务面板显示进度并接受输入。三类产品都可以被用户泛称为"remote control"，但其失败模式完全不同：本地代理失败于机器休眠、终端关闭和网络抖动；云端产品失败于持续费用、镜像可信度与 vendor lock-in；看板类则未必能完整传递审批权限。

**"合盖后继续运行"是比 App Store 评分更有效的筛选标准。** Happy、Paseo、CC Pocket、T3 Code、Zedra、Claude Code UI、Octrix、多数 OpenCode 客户端都把 Agent 运行在开发机或用户自己的服务器上。Catnip 依赖 GitHub Codespaces/Devcontainer，Cosyra 直接提供持久云容器；这两类在"设备不在身边"时结构性优于纯本地客户端。反过来，它们要求用户接受代码、运行环境或 API Key 进入额外云边界。官方 Claude Code Remote Control 同样只能在本地会话存在时继续；其社区 TL;DR 总结也把"终端必须保持打开"列为明确限制。

**公开讨论与代码活跃度之间有明显脱节。** Happy、Paseo、Claude Code UI、Zedra、OpenCode 第三方客户端等都有公开仓库与近期提交；但大量中文营销文章、聚合站和 AI 生成内容在重复官方 README，并未提供真实长周期使用。因此本报告把"官方声称""作者自述""issue 报告""应用商店原话""社区评论"分开处理。尤其是搜索结果中声称"938 条评分、4.9 分"的文章没有附 App Store 可验证页面，不能用于正式推荐。

## 二、Happy：Claude/Codex 高频默认，但近期审批故障是最大红旗

### Happy

- **社区定位一句话：** MIT 开源、E2EE 中继的 Claude Code/Codex 专用遥控器，强调推送、语音和跨设备切换。
- **好评 TOP3：**
  1. "The DX and the amount of things you can set your workflow up to do and leverage Happy is absolutely cracked."——第三方复盘文引述的 App Store 评论，标注 2026 年 3 月；原文未提供 App Store 直链，证据等级低于一手评论。
  2. "The first time I used Happy I was blown away… In line at TSA pre-check, I finished another 20% of a magic link app."——同一第三方复盘文引述，日期亦为 2026 年 3 月，缺少商店原页。
  3. 官方 README 声称端到端加密、无遥测、支持 iOS/Android/Web、按键即可从手机切回桌面；这是**官方声称**，不是用户口碑。
- **差评/踩坑 TOP3：**
  1. `Mobile app unable to approve Happy Codex commands`（#503，2026-01-31）与 `Unable to Approve Commands When Using Codex Remotely on Mobile`（#489，2026-01-28）：确认/拒绝按钮无响应，直接破坏 Codex 移动审批闭环。【复核:两 issue 真实存在,状态 closed】
  2. `Session not preserved when switching from mobile to Windows PC - new session created instead`（#496，2026-01-30），挑战"一键跨设备"核心承诺。【复核:真实,closed】
  3. `iOS26.6` 兼容报错（#494，2026-01-30）、`failed to connect to terminal`（#482，2026-01-27）、`When happy is running, loops /rate-limit-options till tokens run out`（#490，2026-01-29）；连接、版本兼容和失控循环同时存在。
- **高频使用场景：** 外出时查看 Claude/Codex 进度；接收权限、错误或完成提醒；从手机临时追加指令；用语音输入。
- **安全隐私口碑：** 官方明确宣传 E2EE、MIT、无遥测；但**没有发现独立安全审计或正式威胁模型**。仓库包含 Happy Server，意味着默认并非纯 P2P；是否"零知识"需要核对中继密钥协商、备份和元数据。截至本报告日期，仓库已迁移/合并线索显示存在 `slopus/happy` 与 `rootux/happy` 两个外观相近仓库，主 README 以 `slopus/happy` 为准，安装命令仍可见旧的 `happy-coder` 名称，存在包名迁移混淆风险。
- **稳定性口碑：** 中高活跃但中高风险。2026-06-11 仍有提交，活跃度强；可验证 issue 中审批、连接、跨设备恢复问题密集，说明早期高评价不等于生产级稳定。
- **社区推荐位次：** 综合第一候选；纯 Claude/Codex、重视推送和 BYOK 时优先试。
- **信息日期：** 仓库核验 2026-08-17；代表性 issue 主要集中于 2026-01；口碑原话多为二手聚合，缺少独立大样本。

**Happy 的优势不是"功能最多"，而是把审批和通知做成了产品。** 官方 README 把它包装为本地 CLI 的替换入口：`happy claude` 与 `happy codex` 在手机接管时把会话转入 remote 模式，键盘按键可切回桌面。对用户而言，这种"继续已有会话"的体验明显优于在手机浏览器里重新配置终端。问题在于，公开 issue 显示 Codex 审批恰好是它最不稳定的地方；如果手机端不能可靠批准，它就会从遥控器退化成一个只读进度窗口。

## 三、T3 Code：跨代理覆盖面最大，但尚不能称为成熟默认

### T3 Code（pingdotgg/t3code）

- **社区定位一句话：** Theo 团队开源的"Agent harness control surface"，目标是用一个本地服务端统一 Claude Code、Codex、Cursor、OpenCode、Grok Build、Antigravity。
- **好评 TOP3：**
  1. 官方 README 称 iOS、Android、Web 与 Electron 客户端可用，并支持用户已经配置好的订阅。
  2. `npx t3@latest` 可启动本地服务端和 Web UI，降低首次尝试门槛；这是官方声称。
  3. 中文社区转述认为它是"Agent 驾驶舱"，可纵览多 Agent 而不在多个终端间切换；但检索到的材料是营销转载，不是原始长测。
- **差评/踩坑 TOP3：**
  1. 0.0.28 连接故障：用户 ramifara 在 issue 下说回退到 0.0.27 后"all works perfectly"，并形容 0.0.28 的体验"disappointing"；GoblinRules 于 2026-07-12 附和"since .28 it became unusable"。【复核:#7338 "[Bug]: Extremely high usage" 真实存在】
  2. 同类评论认为最新 nightly 0.0.29 仍有断连，只是"does not fully get stuck"。
  3. 有用户解释当双向连接环境中某台机器断网时，T3 Code 会持续尝试重连并冻结当前机器所有线程；Sensei85 于 2026-07-12 提出这是阻塞线程问题。项目 README 同时明确"We are very very early… Expect bugs"和"(mostly) not accepting contributions"。
- **高频使用场景：** 同时使用 Claude Code、Codex、Cursor、OpenCode 的开发者；桌面上的多代理编排；偶尔用手机审批、查看或追加任务。
- **安全隐私口碑：** 本地服务端架构利于 BYOK 和保留本地工具链；官方没有找到完整审计、E2EE 中继或企业权限文档。作为聚合层，它需要获得多个 CLI 的认证状态，密钥范围值得审计。
- **稳定性口碑：** 2026-09-09 仓库记录显示 3,774 次提交、更新频繁，但用户评论揭示 0.0.28 引入明显回归；这是典型的"快速迭代、兼容性风险高"。
- **社区推荐位次：** 多代理需求第一，稳定需求暂不列默认。
- **信息日期：** 2026-08-17；用户评论为 2026-07-11/12。

**T3 Code 的野心和可靠性之间存在明显时间差。** 它的价值是把 Claude、Codex、Cursor、OpenCode 等现有 CLI 统一到一个控制面，而不是再创造一个 Agent 提供商。但当前公开负面证据正是 2026 年 7 月的连接与冻结问题；早期访问用户只能回退版本，且项目不愿大规模接收外部贡献。因此它在"想在一个屏幕里管理所有 Agent"的场景排名最高，在"今天就要稳定陪我过夜"的场景排名低于本地中继方案。

## 四、Paseo：多代理编排能力领先，手机端偏"监督台"

### Paseo（getpaseo/paseo）

- **社区定位一句话：** 本地 daemon 调度 Claude Code、Codex、Copilot、OpenCode、Pi 等代理，提供 iOS/Android/Web/CLI 的跨端控制面。
- **好评 TOP3：**
  1. App Store 用户 vinnyxiong 于 2026-05-31："非常好用，直连的速度快，功能丰富。"
  2. App Store 用户"民族可以咩"于 2026-06-15："体验无敌 绝对的强，移动编程第一。"
  3. App Store 用户"怎么办昵称占用了"于 2026-04-15："移动CC天花板 速度快，指令支持好。"
- **差评/踩坑 TOP3：**
  1. App Store 用户 bighunhun 于 2026-05-16："click always ask option will crash"，表明权限策略入口存在崩溃，而非普通功能请求。
  2. v0.1.65 release notes（2026-05-03）修复了 daemon WebSocket 中途断线、relay 重连循环、终端 worker 稳定性及崩溃无日志问题；这些"修复项"反向证明此前稳定性存在缺口。【复核:release 真实,published 2026-05-03】
  3. 同一 release 还修复 Apple Silicon 错误安装 Intel build 导致渲染器 CPU 100%+、Codex 计划审批面板重复等。
- **高频使用场景：** 并行跑多个异构 Agent；按任务挑选 provider；语音控制；从电脑启动、手机检查；共享本地开发环境而非上传代码。
- **安全隐私口碑：** 官方提供本地 daemon、TCP/Tailscale/VPN 直连以及可选 E2E relay；声明无遥测、无强制登录。这些属于官方架构主张，未见独立审计。
- **稳定性口碑：** 多代理赛道最强。近期 release 系统地修连接、重连、终端 worker、CPU 与构建错误；但 App Store 仅有 38 个评分，不能据此宣称大规模稳定。
- **社区推荐位次：** 多代理第一；纯 Claude/Codex 简易需求则次于 Happy。
- **信息日期：** 2026-08-17；App Store 评论 2026-04—06，release 2026-05-03。

**Paseo 更像"Agent 编排层"，而不是 Claude Code 的手机皮肤。** 它能覆盖五个 Agent 提供商并允许 `paseo run --provider claude/opus-4.6` 一类调用，手机只是跨端界面之一。这意味着它的配置和概念复杂度天然高于 Happy。Paseo 的另一个关键风险是 Anthropic 对程序化订阅调用的额度限制；社区所引维护者回应称，Paseo 内 Claude Code 订阅仍可用，但会消耗不同 credit 池，实际使用可能只剩一部分额度。

## 五、CC Pocket：跨平台与 Tailscale 路径清楚，但社区样本不足

### CC Pocket（K9i-0/ccpocket）

- **社区定位一句话：** Flutter 跨平台 Codex/Claude 遥控器，靠本地 Bridge Server 与 WebSocket，把代码留在用户机器上。
- **好评 TOP3：**
  1. 官方文档将 macOS/Linux/Windows 桌面版列为可用，但明确 Windows/Linux 为实验性。
  2. 官方支持 QR、mDNS、手工 ws/wss 及 Tailscale，给出可复现的自托管连接模型。
  3. 官方称 Bridge 可用于批准流程、提示历史、Git 操作、文件浏览、图片/Diff 查看。
- **差评/踩坑 TOP3：**
  1. 聚合追踪器称其 GitHub 社区讨论"minimal"，Hacker News 只有 2026-03 的 Show HN，Reddit 活动为零；可信用户原声未找到。
  2. 官方自己说明 Claude OAuth 支持需要 `BRIDGE_ALLOW_CLAUDE_OAUTH=1`，并承认 Anthropic 官方指南的 scope 不清晰。
  3. Windows/Linux 实验性支持、Claude OAuth 默认关闭意味着跨平台承诺不应被理解为均等质量。
- **高频使用场景：** 出门前让 Codex/Claude 跑任务，手机上读流式输出、审 Diff、Git 操作和批准。
- **安全隐私口碑：** 架构上比强制云端中转更适合私有代码：代码留在本机，Tailscale 直连为默认建议。没有找到独立安全审计。
- **稳定性口碑：** 仓库追踪显示 2026 年 5—6 月仍有版本更新，但公开社区原声不足。
- **社区推荐位次：** 多代理赛道第三候选；因样本少不能进入前三总榜。
- **信息日期：** 2026-08-17。

**CC Pocket 的工程路径比营销口碑更值得肯定。** 它把 Bridge、审批、Git、文件浏览和自托管明确写出来，并给出 Tailscale 的 `ws://host:8765` 模式。对已有 Tailscale 的开发者，这是一个低信任中继的方案；但公开搜索没有找到能确认长时稳定、断线重连或审批体验的真实评论，因此应把它列为"可试点"，而不是"已被社区验证"。

## 六、Omnara：产品方向有价值(报告误判停更,经复核 2026-09 仍活跃)

### Omnara（omnara-ai/omnara）

- **社区定位一句话：** Python/Apache-2.0 的 AI Agent "mission control"，把 Claude Code 会话同步到终端、Web 和移动端。
- **好评 TOP3：** 官方 README 描述实时观察 Agent、即时回答 Agent 问题、远程监控和 human-in-the-loop；生态索引归类为 Claude Code 的"alternative client";官方提供 iOS App、Web dashboard 和 `pip install omnara`。
- **差评/踩坑 TOP3：**
  1. 【复核注记:报告依据第三方索引称 2025-09-03 后无更新——**已证伪**,gh API 直查 pushed_at=2026-09-16】
  2. 2025-08 的 Windows issue #72 报告 `termios` 缺失导致无法启动；官方建议 WSL 或等待二进制。
  3. 官方仓库明确依赖终端/PTY，Linux/macOS 优先；手机端主要同步 Claude Code 会话，并非跨 Agent 通用工作区。
- **高频使用场景：** 只使用 Claude Code；想让一个 dashboard 同时显示本地终端、Web 与手机。
- **安全隐私口碑：** 本地运行与账号/云端同步并存；云版代码过第三方,可自托管 VPC。
- **社区推荐位次：** 云托管开箱即用第一;隐私敏感者慎选云版。
- **信息日期：** gh 复核 2026-09-17。

## 七、Claude Code UI / CloudCLI：自托管 Web 路线有价值，但安全与性能都未成熟

### ClaudeCodeUI / CloudCLI（siteboon/claudecodeui）

- **社区定位一句话：** 自托管 Web UI，把 Claude Code/Cursor 的会话、文件、终端、Git 和任务管理搬进响应式网页。
- **好评 TOP3：** 官方 README 宣称响应式移动设计、交互式聊天、内置 shell、文件树、Git 操作和会话恢复;官方默认禁用所有 Claude Code 工具;可接入 Claude Code 和 Cursor CLI。
- **差评/踩坑 TOP3：**
  1. issue #190（2025-09-01）：在 HTTPS 代理后使用未加密 WebSocket。【复核:真实】
  2. issue #206（2025-10-04）：Windows 上 `process.env.HOME` 未定义导致启动崩溃。【复核:真实】
  3. issue #204（2025-10-02）：大量会话文件时 CPU 使用超过 130%。【复核:真实】
- **稳定性口碑：** 手机休眠或锁屏后 WebSocket 被系统杀掉,解锁后需刷新重初始化。
- **信息日期：** 2026-08-17。

## 八、Zedra：P2P 信任模型有潜力，但仍是实验性补丁桥

### Zedra（tanlethanh/zedra）

- **社区定位一句话：** Rust + GPUI + Iroh QUIC/UDP 的 P2P 移动远程编辑器。
- **好评 TOP3：** 官方 README 称直接 P2P、TLS 1.3、凭证不离开设备;支持 Claude Code 与 Codex 的 `zedra setup` hooks、二维码扫码;GPU 加速、文件浏览、Markdown、Git 与终端组合为"移动优先"。
- **差评/踩坑 TOP3：**
  1. README 明确"Zedra is early… bugs, rough edges, and breaking changes should be expected"，安全零信任模型是"near future"。
  2. 对称 NAT/CGNAT 下会回退到 relay。
  3. 第三方测评认为它适合个人长任务与终端 Agent 监督，但公开 traction 有限，Android 仍是 beta 分发路径。
- **高频使用场景：** 对中继信任敏感;需要在手机上查看 diff/文件/Git;Claude/Codex 本地跑、手机只做轻量干预。
- **信息日期：** 2026-08-17。【复核:仓库 canonical 名 tanlethanh/zedra,MIT,pushed 2026-09-15】

## 九、Octrix：国产模型/多 CLI 场景有真实需求，但评测样本很少

### Octrix（andforce/octrix）

- **社区定位一句话：** 面向国内用户、开源 iOS 客户端，把十余种 CLI（包括 Codex、Claude 与国产模型接入）桥接到手机聊天界面。
- **好评 TOP3：** 2026-02-03 的 V2EX 主帖作者说明，国产模型用户无法用 Codex 官方手机 App 遥控，Octrix 的聊天对话框由此产生价值;主帖声称全栈开源;官方支持语音输入、长按查看文件/图片。
- **差评/踩坑 TOP3：** 未找到可信的第三方差评原话;架构依赖后端中继把手机与 Mac 配对，安全、隐私、可用区和数据留存均缺少公开审计;跨 CLI 兼容性风险高。
- **信息日期：** V2EX 主帖 2026-02-03。【复核:仓库无 LICENSE 文件(gh API license=null),"全栈开源"宣称与实际不符,待验证】

## 十、OpenCode 官方 Web：最低依赖，但官方 UI 并非移动优先

- **好评:** `opencode serve --hostname 0.0.0.0 --port 4096` 可用密码认证;BYOK,官方完全不碰数据。
- **差评:** 官方 UI"Not mobile responsive / Limited mobile experience";Basic authentication 密码只是 Base64;公网直接开放端口不符合最佳实践,推荐 Tailscale/VPN。
- **社区推荐位次：** 底座;dzianisv 第三方 Android 客户端为移动端第一。

## 十一、OpenCode 第三方客户端：dzianisv 是资料上最可验证的选择

- **dzianisv/opencode-mobile:** 官方页面明确"no middleman, no cloud relay";支持多服务器、流式输出、Diff、工具调用审批、生物识别和 Android Keystore；截至 2026-08-14 仍在发布（v0.4.15）。【复核:MIT,pushed 2026-08-20】被 OpenCode 官方仓库收录(sst/opencode#669)。Android-only。
- **doza62/opencode-mobile:** 作者 2026-03-16 称"finally working (still beta quality)";权限请求截断、问答界面问题、会话状态不自动刷新、重连键盘隐藏。【复核:MIT,pushed 2026-02-25,半年未动】
- **Shahfarzane/opencode-mobile:** 最新可见提交 2026-01-15,不能按活跃推荐。

## 十二、opencode-telegram-bot（grinev）

- **好评:** /status /new /abort /sessions /projects /worktree /messages /revert /fork /task 命令全;/task 支持预定任务;本地机器运行、Bot 只做入口。
- **差评:** Docker 部署下 /open /ls /attach 不能直接使用;Bot token、user ID 和 OpenCode Basic Auth 都是敏感凭据;SSE/long polling 不自动重启。
- **信息日期：** 2026-08-17。【复核:MIT,pushed 2026-09-13,⭐1159】

## 十三、KKCode 与 FlyCode

- **KKCode:** V2EX 主帖称 Claude/GPT/Gemini 取决于服务端配置、流式输出不强制滚动、代码高亮/Markdown、图片发送;作者自认:App 没有 AI、Mac 必须开着 opencode、外网需自搭 Tailscale、只认 OpenCode;暂未收费。
- **FlyCode:** 可连接自托管 opencode server、查看项目、恢复会话;依赖 opencode serve,兼容性风险高;样本极少。

## 十四、Vibe Kanban（BloopAI/vibe-kanban）

- **定位:** 自托管 AI 任务看板,多 Agent 并行任务编排,非手机原生遥控器。
- **好评:** 本地优先、代码与任务数据留在本地、支持 SSH 远程连接模式;可创建任务、指派 AI 工具、设置优先级。
- **差评:** 母公司 Bloop 2026-04 倒闭(转 Apache-2.0 社区维护,云同步基建已废);不是手机原生客户端;若目标是实时批准权限、断线恢复,看板信息粒度可能不足。
- **信息日期：** 2026-08-17。【复核:pushed 2026-09-16,⭐28.1k,社区维护活跃】

## 十五、Catnip（W&B Catnip）

- **好评:** Docker/Apple Container、worktree、隔离环境、终端、端口代理和移动 UI;移动访问通过 catnip.run 登录 GitHub 自动启动 codespace。
- **差评:** 启动时向 catnip.run 发送 codespace 和 repo 名称；临时 GITHUB_TOKEN 存在后端（24 小时清理承诺）;依赖 GitHub Codespaces 费用与生命周期;口碑样本少。
- **【复核注记:github.com/wandb/catnip 404,wandb org 下无此仓库;开源状态无法验证,不立条目】**

## 十六、Cosyra / Nimbalyst

- **Cosyra:** 每用户独立 Ubuntu 24.04 容器、预装 Claude Code/Codex CLI/OpenCode/Gemini CLI、30GB 持久存储，Pro 可休眠后恢复;API Key 官方称设备端加密;$29.99/月;闭源;均为官方声称,无独立审计。
- **Nimbalyst:** 官方称桌面端支持 Codex/Claude/OpenCode 并行 worktree、可视化 diff、看板、任务、终端及移动端推送和语音回复;iOS companion 围绕桌面 daemon 运行。注意:关于本工具的对比文均出自 nimbalyst.com 自家,利益相关。

## 十七、官方三件套

- **Claude Code Remote Control:** HN TL;DR「extremely clunky and buggy prerelease… don't try to hot fix prod from the toilet without a different mobile frontend」;停止按钮失效、UI 断连、单会话、终端必须开着;HN 主帖 2026-02-25。
- **ChatGPT Codex 手机端:** Mobile 是 preview,在 ChatGPT App 内 read-only/chat-first,不能执行完整 agentic 任务;不能接管本地 Codex CLI。
- **Cursor iOS:** 局限于远程审阅代码与会话历史,无法激进远控或跨 Harness 编排。

## 十八、横向结论(原文要点)

1. 社区公认的"前三"不存在;按证据条件化:Happy(Claude/Codex 高频默认)、Paseo(多 Agent 编排)、官方 Remote(纯 Claude 零配置)。
2. 四方对比:今天出门看 Claude/Codex→Happy;长期管理多种 Agent→Paseo;不信任第三方中继→CC Pocket;继续得到维护→排除停更项(Omnara 判断已证伪)。
3. OpenCode 第三方:dzianisv 第一(Android);iOS 无公认冠军。
4. 停更风险:Omnara 判断证伪;安全方面无 CVE,但 ClaudeCodeUI 有明文 WebSocket issue;普遍缺独立审计。
5. 遗漏工具(未达一手标准,未推荐):VibeTunnel、Agent Deck、OpenClawdex、OpenACP。
6. BYOK 路线:自托管 server + VPN + 原生前端;第一选择自己机器跑 Agent,第二 Tailscale 而非公网,第三 dzianisv/Paseo 直连/CC Pocket Tailscale/ClaudeCodeUI HTTPS;合盖需求迁 Cosyra/Catnip/VPS。

## 引用来源(原始 URL 清单,复核状态见各处注记)

[1] https://github.com/slopus/happy
[2] https://github.com/getpaseo/paseo
[3] https://github.com/dzianisv/opencode-mobile
[4] https://github.com/Shahfarzane/opencode-mobile
[5] https://hn-tldr.com/posts?page=116 (Claude Remote Control HN 评论:"extremely clunky and buggy prerelease")
[6] https://codeongrass.com/blog/is-there-a-mobile-app-for-claude-code
[7] https://github.com/slopus/happy/issues (#489/#496/#503 等,已复核存在)
[8] https://github.com/rootux/happy
[9] https://github.com/pingdotgg/t3code
[10] 微信转载文章(营销转载,仅线索)
[11] https://github.com/pingdotgg/t3code/issues (#7338 "[Bug]: Extremely high usage",已复核存在)
[12] https://apps.apple.com/cn/app/paseo-remote-coding-agents/id6758887924 (用户评论原文)
[13] https://github.com/getpaseo/paseo/releases/tag/v0.1.65 (已复核,2026-05-03)
[14] https://arceapps.com/blog/paseo-orchestrator-multi-provider-2026 ("Practically speaking you will be able to use only a fraction of your usage in Paseo")
[15] https://github.com/K9i-0/ccpocket
[16] https://cask.news:2096/cask/cc-pocket (聚合追踪,低权重)
[17] https://awesome.ecosyste.ms/projects/github.com%2Fomnara-ai%2Fomnara (过时索引,Omnara 停更判断来源,已证伪)
[18] https://github.com/omnara-ai/omnara/issues/72
[19] https://github.com/siteboon/claudecodeui
[20] https://www.togithub.com/siteboon/claudecodeui/issues (#190/#204/#206 已复核存在)
[21] https://github.com/deltaqdev/zedra
[22] https://vibecodinghub.org/tools/zedra
[23] https://www.v2ex.com/t?q=Octrix (V2EX 主帖 2026-02-03 的搜索入口,具体帖 URL 未取得)
[24] http://github.es/hosenur/portal ("Not mobile responsive / Limited mobile experience")
[25] https://foxdata.com/fr/app-marketing-analytics/6757406313/as/US/opencode-mobile-app ("finally working (still beta quality tho)")
[26] https://github.com/sst/opencode/pull/669 (dzianisv 客户端被官方仓库收录)
[27] https://github.com/grinev/opencode-telegram-bot
[28] https://www.v2ex.com/t?q=KKCode (作者自述:App 没有 AI、Mac 必须开着、自搭 Tailscale)
[29] https://ima.qq.com/wiki/?shareId=54beb0ae... (Vibe Kanban 中文转述,低权重)
[30] https://github.com/wandb/catnip (**已复核 404**,"GITHUB_TOKEN 存后端 24h 清理"说法无法溯源)
[31] https://cosyra.com ("On Pro, the container hibernates after ten minutes idle and resumes with state intact")
[32] https://github.com/nimbalyst/nimbalyst
[33] https://aiunpacking.com/review/openai-codex ("Mobile is preview-only… read-only and chat-first")
[34] https://startupfortune.com/?p=9955/ (ChatGPT Android 远控 Codex 传闻)
