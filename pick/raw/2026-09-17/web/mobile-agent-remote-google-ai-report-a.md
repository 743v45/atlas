# 口碑原始留档 · 谷歌 AI 调研报告 A(逐个工具版)

> 采集方式:用户以 Claude Code 提供的提示词在谷歌 AI 搜索执行,原文粘贴回会话。
> 采集日期:2026-09-17。采集者:taevas。
> 可信度注记:本报告为 AI 聚合产物,部分来源为低权重聚合站(如 github-wiki.com、skillsllm.com、cask.news),关键论断已在本类别各条目报告中用 GitHub API 直查复核(issue 存在性、stars、pushed_at、license)。**KKCode=Shellby 的说法经复核为混淆,不成立。** 与报告 B 冲突时以 B + GitHub API 为准。

---

🛠 逐个工具口碑调研报告

A. 开源遥控 App（手机客户端 + 桥接本机 Agent）

1. Happy (slopus/happy)
社区定位一句话： 支持端到端加密（E2EE）与实时语音的 slopus/happy 移动/Web 远端控制面。
好评 TOP3：实时语音功能极其惊艳，用户反馈："散步时直接对着手机讲两句，Claude Code 就能在后台把活干完。"开源且支持全链路端到端加密，对企业用户和注重资产保护的独立开发者非常友好。桌面端与移动端无缝协同，文件变更、diff 对比及终端预览同步速度较快。
差评/踩坑 TOP3：iOS 偶现 Machine 丢失 Bug：在最新 Issues 中，用户吐槽在 iOS 上 Happy Agent 机器经常从 Machine 列表中消失，无法被选为生成目标。CLI 依赖迁移历史（原 happy-coder 包名变更）导致老用户更新时需要全局重新安装。口碑样本指出在低网速环境下，端到端加密的 Relay 服务器有时会出现握手延迟。
高频使用场景： 散步/通勤时的语音远程派发任务、盯长任务进度、随时通过 Web/手机查看实时编译产物。
安全隐私口碑： 口碑极佳。核心卖点即为 End-to-End Encryption (E2EE)，且支持自托管 Relay 服务器，代码完全不流经第三方服务器。
稳定性口碑： 长会话保持良好，但在网络切换（如 Wi-Fi 变 5G）时会偶尔触发上述 iOS 节点丢失问题。
社区推荐位次： 在手机遥控 Claude Code 对比中稳居前三。因支持语音和强加密，常在"高隐私需求"与"移动语音办公"场景中被首推。
信息日期： 2026 年 3 月 - 9 月。

2. T3 Code (pingdotgg/t3code)
社区定位一句话： 由 Theo 团队打造、拥有 22k+ Stars 的全生态多 Agent 大一统遥控控制面。
好评 TOP3：生态极其庞大：通吃 Claude Code, Codex, Cursor CLI, Grok Build, OpenCode 等几乎所有主流 CLI 引擎。UI/UX 极度丝滑，渲染性能极强，高频渲染大文件列表或复杂的 CSS 动画时完全不掉帧。社区热度极高，背靠著名技术网红 Theo 团队，更新频繁且周边生态活跃。
差评/踩坑 TOP3：严重的 Token/费用消耗 Bug：在 Issue #7338 中，用户爆料使用 T3 Code 配合 Claude Code 时，其 API Token 消耗量竟比原生高出 3x-5x，直接导致工作阻断。目前项目处于极早期，官方明确表示（暂时）不接受大型社区 PR，一切以核心团队意志为准。手机端偶尔会与本机 Server 出现版本同步脱节，需要频繁更新 CLI。
高频使用场景： 极其适合重度全栈开发者，用于在家中/外出时统一操控公司的多轨 Agent、远程审 Diff 和紧急合并分支。
安全隐私口碑： 本地运行优先。但作为网红项目，部分极客在 Reddit 讨论其是否有"隐蔽的遥测或体验数据回传"，官方主打纯开源但早期监管严格。
稳定性口碑： 渲染不卡顿，但网络差时可能导致长会话桥接断开，加上 API 消耗异常的 bug，稳定极客仍持观望态度。
社区推荐位次： 讨论度第一，但因处于早期（Expect bugs）经常被劝退作为生产力，属于"观望与尝鲜首选"。
信息日期： 2026 年 8 月 - 9 月。

3. Paseo (getpaseo/paseo)
社区定位一句话： 主打多 Agent 智能编排、零追踪的纯粹隐私优先自托管 Daemon 控制台。
好评 TOP3：跨 Harness 编排无敌：独创 /paseo-handoff 等 Skill 指令，支持用 Claude 规划全局，然后自动交棒给 Codex 去写代码，多 Agent 协同极其震撼。真正的自托管（Homelab 友好），支持多端（Mac、iPhone、Android）随时接入同一个持久化 Session。极致克制：完全没有任何 Telemetry（遥测）、无跟踪、不强制登录。
差评/踩坑 TOP3：没有美观的云端一键登录，纯靠自托管和 WebSocket 配置，对于非运维型开发者门槛稍高。移动端（Expo 开发）在长对话下，内存占用偶尔会飙升，导致低配手机卡顿。偶尔在并行运行 4 个以上 Agent 时，本机的守护进程（daemon）会因底层并发冲突而崩溃。
高频使用场景： Homelab 长期挂载、多 Agent 委员会评审（/paseo-committee）、手机端随时切入多模型并行的编码大工程。
安全隐私口碑： 顶流级别。承诺零 telemetry、无日志上传、代码完全不出个人局域网或私有加密 Relay。
稳定性口碑： 极为坚固，长会话保持优秀，手机休眠后重连机制非常合理（基于持久化 daemon）。
社区推荐位次： 在 Hacker News 上备受资深黑客推崇，常在"如何优雅地在私有云调度多模型"对比中排名第一。
信息日期： 2026 年 9 月。

4. CC Pocket (K9i-0/ccpocket)
社区定位一句话： 专为手机优化的 Flutter 轻量级 Claude Code/Codex 遥控桥接客户端。
好评 TOP3：手机 UI 极其直观，审批流（Approval flow）体验好，一键允许/拒绝 Agent 的高危操作。网络配置透明，官方直接给出通过 Tailscale 穿透远端桥接的完美指南，简单粗暴易上手。安全控制严格，可在配置文件中通过 BRIDGE_ALLOWED_DIRS 严格锁死 Agent 只能访问特定目录。
差评/踩坑 TOP3：跨网重连摩擦：如果不用 Tailscale 而是用原生 wss:// 连接，手机休眠唤醒后极易断连，需要重扫 QR 码。功能相对单一，无法像 Paseo 那样做复杂的跨 Agent 调度，只是一个纯粹的 Terminal 会话镜像。移动端由 Flutter 编写，部分极客在 iOS 上抱怨键盘弹出时偶尔会遮挡输入框。
高频使用场景： 在外吃午饭或通勤时，用手机监控家里的电脑跑 Claude Code，进行文件差异审查和快速审批授权。
安全隐私口碑： 优秀。代码不离本地，API Key 存放在手机原生安全区（iOS Keychain / Android Keystore），支持设置 BRIDGE_API_KEY 验证连接。
稳定性口碑： 中规中矩。在本机不休眠且使用 Tailscale 的情况下长会话极稳；若电脑进入休眠则连接彻底死掉。
社区推荐位次： 属于小而美的代表，常在"不想折腾复杂大框架、只想手机纯粹遥控 Claude"的推荐帖中名列前茅。
信息日期： 2026 年 9 月。

5. Omnara (omnara-ai/omnara)
社区定位一句话： 主打托管云与多 Agent 指挥台的商业级开源替代品。
好评 TOP3：提供官方 Managed Cloud（Omnara Cloud），一键省去自托管的繁琐网络配置。自带强大的审批策略引擎，可以对高危 Tool 动作进行多级拦截和手机推送。支持语音和 Apple Watch 联动控制（通过特定的云端通道）。
差评/踩坑 TOP3：如果使用其云端版本（Managed Cloud），虽然方便，但代码和会话数据不可避免会流经其托管服务器，引起隐私洁癖者的反感。免费额度有限，后期商业化转化推得较死。社区用户反馈其官方容器有时在拉取非主流 MCP 工具时会遇到权限被卡死的情况。
高频使用场景： 远程盯长任务、团队共享 Agent 审批台、无视本地机器硬件的纯云端 Agent 调度。
安全隐私口碑： 存在争议。由于主推云版本，代码资产防线需要妥协。虽然开源版可独立部署到私有 VPC，但多数人冲着云版去，隐私口碑弱于 Happy 和 Paseo。
稳定性口碑： 由于底层有云端基础设施支撑，手机断连重连率极低，网络平滑度属于全场第一梯队。
社区推荐位次： 在"无需 Laptop/VPS 的一键式开箱即用"对比中通常排第一；但在开源纯极客圈容易被劝退。
信息日期： 2026 年 2 月 - 6 月。

6. ClaudeCodeUI / CloudCLI (siteboon/claudecodeui)
社区定位一句话： 针对 Claude Code 官方 CLI 的自托管响应式 Web UI 镜像。
好评 TOP3：纯粹的 Web/PWA 路线，部署完直接用手机浏览器访问，无需下载任何原生 App 安装包。版本迭代极其疯狂，在 GitHub 上紧跟 Anthropic 官方的脚步，几乎每周都在解决黑屏或断连问题。界面像素级致敬云端 IDE 体验，在平板（iPad）上的体验远超小屏手机。
差评/踩坑 TOP3：手机端键盘极度难用：由于是 Web 响应式布局而非原生 App，在 iPhone 浏览器上唤起虚拟键盘时，极其容易触发页面整体往上顶、输入框被截断的恶性体验。缺乏原生的手机推送通知（Push Notification），只能靠一直开着网页死守。当终端输出（Stdout）过大时（例如跑了一个几万行的测试包），手机浏览器会直接崩溃卡死。
高频使用场景： 在 iPad 或备用机上打开网页远程管理家里的 Claude Code 进程，审视轻量级 Diff。
安全隐私口碑： 纯自托管，数据安全取决于你如何暴露这个 Web 端口，若裸奔公网极易被扫。
稳定性口碑： 较弱。手机休眠或锁屏后，网页的 WebSocket 会被 iOS/Android 操作系统无情杀掉，解锁后 100% 需要刷新重新初始化。
社区推荐位次： 在"免安装 App 临时凑合用"的方案里排名靠前，但长期生产力推荐中往往被劝退。
信息日期： 2026 年 9 月。

7. Zedra (tanlethanh/zedra)
社区定位一句话： 纯 Rust 开发、基于 Zed 同款高性能 GPUI 渲染引擎与 QUIC P2P 直连的移动端全功能代码编辑器。
好评 TOP3：性能无敌（120FPS）：基于 GPU 渲染，用户在 Hacker News 和 Reddit 狂赞："在 iPhone 上滑 20 万行的巨型代码库居然比刷 Twitter 还丝滑，Tree-sitter 高亮和 LSP 完全不卡顿！"完美的 P2P 直连：集成 Iroh 协议，通过 QUIC/UDP 实现出站优先的纯内网穿透，无需任何公网 IP 或繁琐端口转发，在外随时连回电脑。不是网页套壳，它是在手机上塞入了一个真正的自研原生代码编辑器与全功能终端。
差评/踩坑 TOP3：生态绑定和编译问题：由于 GPUI 目前在移动端的中文输入法适配有瑕疵，部分中文用户反馈打字会出现吞字或无法选词。极客向严重，配置和自定义主题需要对 Rust/GPUI 体系有一定了解，不适合小白。当前被部分用户认为"更像一个带 AI 的硬核移动终端编辑器"，在多 Agent 高级看板编排上略显单薄。
高频使用场景： 移动端硬核 Coding、在外远程穿透回工作机调用全量环境编译、查看完整的 LSP 语法高亮及 LSP 诊断。
安全隐私口碑： 顶级。全链路 QUIC P2P 加密，真正的端到端直接通信，不经过任何中间服务器中转代码。
稳定性口碑： 得益于 QUIC 协议的高效重连特性，手机切网或短时间休眠后，网络恢复时几乎能"瞬间无感重连"。
社区推荐位次： 2026 年中旬发布后迅速在 Reddit r/rust 和 Hacker News 爆火，被称为"最具有技术极客含金量的移动 AI 编码工具"。
信息日期： 2026 年 6 月 - 8 月。

8. Octrix (andforce/octrix)
社区定位一句话： 主打国产大模型适配、在 V2EX 独立开发者圈小有名气的 iOS 遥控 App。
好评 TOP3：对国内网络环境友好，对 DeepSeek、Qwen 等国产开源/闭源 Agent 控制面做到了原生级别的深度缝合。V2EX 上用户反馈："UI 充满中式极简美学，功能克制，没有多余的恶心付费策略。"自带简易的二维码扫码配对机制（Host + Relay 架构）。
差评/踩坑 TOP3：仅限苹果生态（iOS/iPadOS/Mac M1+），完全不支持 Android，受众面被死死卡住。社区整体声量较小，在 Reddit 等国际社区近乎查无此人（口碑样本极度集中在国内 V2EX 圈子）。审批提示在处理高吞吐并发任务时，偶尔会丢失长文本日志（truncated 现象）。
高频使用场景： 国内独立开发者在地铁上通过手机遥控本机的 DeepSeek 编码智能体进行修 Bug 和局部重构。
安全隐私口碑： 干净透明。支持本地局域网直连或私有私钥 Relay，无第三方数据拦截。
稳定性口碑： 手机锁屏后重连较为平稳，但在 iOS 18 强力后台限制下，如果长会话挂载超过 20 分钟未交互，偶发断连。
社区推荐位次： 国内特定圈子的心头好，在"适合国内直连/DeepSeek 遥控生态"的本土讨论里被高频提及。
信息日期： 2026 年下半年（最新活跃）。

B. OpenCode 生态（自带引擎，BYO 任意模型）

9. OpenCode 官方 serve + Web UI 手机访问体验
社区定位一句话： OpenCode 官方原生提供的公网服务挂载与自适应网页端。
好评 TOP3：绝对的根正苗红，不需要安装任何第三方插件或软件，一句 opencode serve 即可原生起飞。兼容性完美，永远不用担心第三方客户端更新导致的 API 破裂或控制字段缺失。对响应式排版支持良好，Markdown 预览和基本的多选一审批按钮能正常点按。
差评/踩坑 TOP3：完全没有后台保活与推送：一旦手机锁屏，网页即刻变死狗，如果 Agent 在跑一个 10 分钟的大任务，你必须保持手机屏幕常亮干等。纯 Web 终端的输入延迟非常高，特别是在弱网或通过免费内网穿透（如 Localtunnel）时，打字就像在泥潭里爬。不支持手机端任何原生手势（如滑屏切换 Session），容易误触返回导致页面刷新。
高频使用场景： 开发者在没有带电脑的周末，临时通过手机浏览器登录家里的 OpenCode 节点进行极其紧急的代码审查。
安全隐私口碑： 极高（纯 BYOK 与纯自托管，官方完全不碰数据）。
稳定性口碑： 极差（受制于手机浏览器内核的墓碑机制，锁屏即断）。
社区推荐位次： 属于底座基石，但在"Mobile 最佳体验"对比中通常只作为"保底垫底的无奈之选"。
信息日期： 2026 年 8 月。

10. OpenCode 第三方手机客户端 (doza62/opencode-mobile, Shahfarzane/opencode-mobile 等)
社区定位一句话： 群雄逐鹿的 OpenCode 生态第三方 React Native / Expo 移动大军。
社区实际推荐： 综合推荐度和迭代完成度，dzianisv/opencode-mobile 被社区推荐最多且最稳（由 VIBE TECHNOLOGIES 维护，已上架 Google Play）；而 doza62/opencode-mobile 则是 iOS App Store 上最火的 unofficial 开源客户端。
好评 TOP3：dzianisv 版：自带绝妙的"离线 Demo 模式"，30 秒内完整模拟一键解决 Grep/Diff/权限提示全流程，onboarding 极其清晰。doza62/Shahfarzane 版：在手机上完美集成了全功能的 iOS 触觉反馈（Haptic）、Face ID 生物解锁以及原生 Git 自动 AI Commit 功能。插件生态好：结合 opencode-mobile 电脑端 Companion 插件，能通过 Cloudflare/ngrok 隧道极速完成免注册穿透。
差评/踩坑 TOP3：iOS 版 reconnection 顽疾：doza62 的 App Store 版本被疯狂吐槽："有时切换回后台再回来直接白屏断连，必须彻底杀掉 App 重新冷启动才能连上。"核心特性缺失：在处理 OpenCode 抛出的多选一选择题时（Multiple choice question），部分版本无法在手机聊天流中渲染出来，导致任务直接在后台静默卡死。部分版本在长会话（Long session）下滚动会产生极其明显的卡顿和掉帧。
高频使用场景： 彻底抛弃 Laptop，在咖啡馆或地铁上用手机审查 OpenCode 生成的每一行 Diff，并进行手势一键审批。
安全隐私口碑： 极佳。明确承诺全链路零 Telemetry（或仅限 opt-in 的 Sentry 崩溃数据），不代劳任何 API Key，纯薄客户端，不搞代码代理。
稳定性口碑： Android 版（dzianisv）由于打磨时间长，在 F-Droid/Google Play 体验相对扎实；iOS 版目前仍处于"功能很美，但 reconnection bug 搞人心态"的 Beta 期。
社区推荐位次： 只要提及"Best Android client for OpenCode"，dzianisv 版必排第一；iOS 侧目前用户普遍还在期待 Agent Labs 正在闭门造车的官方标准版。
信息日期： 2026 年 7 月 - 9 月（处于激烈迭代期）。

11. opencode-telegram-bot (grinev)
社区定位一句话： 另辟蹊径、将 Telegram 变成 OpenCode 遥控控制面的极客聊天机器人路线。
好评 TOP3：保活无敌：得益于 Telegram 庞大且极其强悍的后台常驻网络，它是全场完全不会漏掉任何一条 Agent 推送的方案。极其轻量，只要你有 Telegram，任何破手机甚至智能手表都能秒速查看 Agent 的进展。部署简单，本机的 bot daemon 跑起来之后，直接在 TG 聊天框里输命令。
差评/踩坑 TOP3：Diff 审查体验灾难：TG 的纯文本或者 Markdown 块根本无法优雅呈现复杂的代码红绿 Diff，遇到大改动时直接刷屏，体验极其痛苦。安全风险较高：虽然 TG 自身有加密，但你的代码资产、项目上下文以及交互过程不可避免地全部上传并存储到了 Telegram 的云端服务器。缺乏原生的文件树浏览和复杂的 LSP 交互支持。
高频使用场景： 纯粹作为"重度离线通知器"，当 OpenCode 跑出大结果或遇到中断时，在 TG 上敲个 /approve 或者 /deny。
安全隐私口碑： 隐私敏感型团队的禁区。绝大多数公司由于严格的合规政策，严禁使用 TG 机器人来中转任何公司私有代码。
稳定性口碑： 稳定性顶级（TG 的连接鲁棒性无人能敌）。
社区推荐位次： 在"最佳推送与保活方案"中名列前茅，在"正式的手机编码客户端"对比中被劝退。
信息日期： 2026 年上半年。

12. KKCode、FlyCode
社区定位一句话： 在中国本土技术社区（如 V2EX）曾被广泛讨论的、偏底层的 iOS 精品终端/SSH/开发流桥接客户端。
现状确认与口碑： KKCode 目前已深度融入/演变为更成熟的独立 SSH 与智能开发终端产品（如著名的 Shellby 生态，在 App Store 持续霸榜）；而 FlyCode 的口碑样本极少，大多已处于半停更状态。
【复核注记(2026-09-17,主会话):此"KKCode=Shellby"说法为混淆——所引链接全部指向无关 SSH 客户端 Shellby 的 App Store 页面。采信报告 B:KKCode 是 OpenCode 的 iOS 第三方伴侣客户端(V2EX 作者驱动,免费,需自备 Tailscale);FlyCode 样本极少。】

C. 特殊路线

13. Vibe Kanban (BloopAI/vibe-kanban)
社区定位一句话： 将 AI 编程智能体由"聊天框"彻底革命为"异步 Trello 看板"的自托管并行大师。
好评 TOP3：极其震撼的异步多轨并行：彻底告别无脑聊天，采用 Trello 看板式（To Do -> In Progress -> Done），你可以手机一键派发 4 个不同任务，看它们在不同的 Git 工作树（Worktree）里并行写代码，互不打扰，零冲突！自带极其惊艳的内置浏览器、DevTools 调试面板和设备模拟器（Device emulation），在手机/平板上能直接看运行效果。Centralized MCP：所有的 MCP 插件和项目规则只需配置一次，所有并发 Agent 共享。
差评/踩坑 TOP3：惊天巨变：母公司 Bloop 于 2026 年 4 月宣布倒闭关闭！由于找不到免费用户的商业变现模式，商业公司停运，项目目前全盘转交为社区用爱发电的纯 Apache 2.0 开源维护状态，部分托管云服务已在 2026 年中旬正式下线，现已全面缩回纯本地/私有网架构。流程过重：对于只想改一行代码的"顺手修 Bug"场景，强行建 Task、开独立 Branch 和 Worktree 反而带来了极大的操作摩擦。手机端目前主要依赖远端浏览器的 Web Access 接入，缺乏高度优化的精细化原生移动皮肤。
高频使用场景： 当你需要扮演"硅谷赛博主管"，在咖啡厅同时给几位"AI 实习生"分配不同模块的重构工作，并异步进行 Diff 评审。
安全隐私口碑： 转型后完全回归纯本地/纯局域网，隐私极高，但失去了商业大厂的安全合规背书。
稳定性口碑： 架构稳健，但因为公司倒闭导致一些高级云端同步特性破裂，目前社区版正在打磨新的多端同步方案。
社区推荐位次： 曾是绝对的革命性全场第一，在 Bloop 倒闭后，社区在"震撼其多规并行实力"的同时，普遍开始转向 Nimbalyst 等有全职团队维护的替代品。
信息日期： 2026 年 1 月爆火，2026 年 4 月 - 5 月宣告转型社区版。
【复核注记:Bloop 倒闭说法有 nimbalyst.com 等外部文章佐证,采信;但"转向 Nimbalyst"叙事来自 nimbalyst.com 自营销,降权。】

14. Catnip
社区定位一句话： 走 iOS + GitHub Codespaces 官方容器直连路线的轻量云端 companion。
口碑样本少： 社区样本较为稀缺。作为特定小众路线，其好评在于能借用 GitHub Codespaces 的巨型云端算力，免去了用户自己家里开电脑的麻烦；差评在于资费完全受制于 GitHub 容器，且对于非 Codespaces 用户而言没有任何灵活 BYO 服务器的空间。通常在"轻度 GitHub 深度绑定党"中流传，2026 下半年声量渐小。
【复核注记:报告 B 称仓库为 github.com/wandb/catnip,经 gh API 直查 404,wandb org 下亦无 catnip 仓库;开源状态无法验证,故本类别不立条目。】

15. Cosyra、Nimbalyst (新一代工作区 + 手机 companion)
社区定位一句话： 2026 年当下风头最劲、全面接管 Vibe Kanban 倒闭后市场的两大顶流多 Agent 现代移动协同 workspace。
Direct Comparison: Cosyra vs Nimbalyst
维度 | Cosyra (Portable Software Corp) | Nimbalyst (Open-source / MIT)
核心定位 | 纯云端托管的 AI 移动 Linux 终端：给手机配一个不熄灭的云 Ubuntu 24.04 容器（30GB 存储），内置所有主流 Agent，彻底解放 Laptop。 | 本地优先的超强全功能工作区：在电脑端管理 Session/图表/设计稿，配合极致完美的 iOS 原生控制 Companion App。
手机好评 | 外出/通勤完全不需要电脑开机！Agent 在云端永远在线，用手机给它一个大任务，断网坐完地铁，到站代码已经推到了 GitHub。 | 原生 iOS 体验天花板：卡片式 Session 看板，滑动红绿 Diff，智能检测如果你的 Mac 处于活跃状态，手机就会智能静默防止打扰。
主要踩坑 | 收费较贵：固定月费 $29.99/月（虽然自带机器，但模型 API Key 还得自己出）。目前尚无 Android 版（仅限 iOS Beta），且完全依赖你本机的电脑不能休眠断电。 | ——
安全隐私 | 代码不可避免地常驻其云端托管 Ubuntu 镜像中，大厂合规难以通过。 | 极高。AES-256-GCM 消息级别加密，密钥在首次配对扫 QR 码时本地交换，绝对不碰服务器。
推荐位次 | 2026 年"无 Laptop 极简出行党/iPad Pro 生产力党"心目中的绝对第一。 | 2026 年下半年"Vibe Kanban 倒闭后最佳全功能开源替代品"第一名。
信息日期 | 2026 年 4 月 - 7 月。 | 2026 年 2 月 - 8 月。
【复核注记:本节"前三/第一"叙事大量来自 nimbalyst.com 自家对比文,利益相关,全部降权为线索;Nimbalyst/Cosyra 均不立条目,进 decision-tree 落选节点。】

D. 官方对照（简要）

16. Claude 官方移动 (Remote Control / 云会话)
口碑现状： 虽然官方在 2026 年极大地强化了移动端的 Web 控制力，但它缺乏真正的本地文件系统深度 Tool 操作与编译环境镜像。社区普遍认为，Claude App 适合聊天和出点子，但要论"让它在手机上直接遥控改写你 Mac 上的工程并跑通测试"，官方移动端完全无法替代 Claude Code 配合第三方遥控面。

17. ChatGPT Codex 手机端
口碑现状： 遭遇了与 Claude 官方类似的尴尬。即便底层模型推理极强，但官方 App 并没有给出像 T3 Code 或 Paseo 那样强大的"全栈多并发文件树工作区（Worktree）"操作权限。

18. Cursor iOS
口碑现状： 2026 年 Cursor 在桌面端依然是统治级地位，但其 iOS 客户端由于受到苹果沙盒的严重限制，目前主要功能仍局限于"远程审阅代码"与"查看会话历史"，无法做到像 Zedra 或 Paseo 那样进行激进的底层 P2P 远端控制或复杂的跨 Harness 编排调度。

🏁 横向热点问题解答(摘要)
1. 社区公认前三(该报告版):Zedra / Nimbalyst / Paseo——注意此排名大量引用 nimbalyst.com 自家对比文,降权采信。
2. Happy vs Paseo vs CC Pocket vs Omnara:跨模型调度 Paseo 完胜;上手极简与审批流 CC Pocket 胜;免设备免折腾 Omnara 胜;移动语音办公 Happy 独占。
3. OpenCode 第三方客户端:Android 推荐 dzianisv(双渠道上架+离线 Demo);iOS 推荐 doza62(App Store unofficial 扛把子)。
4. 翻车/停更:Vibe Kanban 母公司 Bloop 2026-04 倒闭转社区;T3 Code #7338 token 放大 3-5x;新星 Zedra。
5. 遗漏新工具(该报告版,未复核):Crush(Android)、Shellby(实为无关 SSH 客户端,剔除)。
6. BYO/本地模型需求:拒绝托管云,走纯自托管薄客户端或纯 P2P(Zedra / Paseo / CC Pocket + Tailscale)。
