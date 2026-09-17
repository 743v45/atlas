# 手机端遥控 Coding Agent 客户端 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

手机上远程查看/审批/驱动本机 AI 编程 Agent（Claude Code / Codex / OpenCode）的客户端选哪个？（2026-09-17 会话；用户画像：免费 + 开源 + BYO 任意模型 + 手机原生 App 优先）

## 分叉与决策

### D1 自带引擎还是桥接本机 CLI？

- 用户核心条件「用自己的模型」→ 带 OpenCode 引擎的薄客户端（BYO 任意 provider/Ollama）优先于桥接派（模型锁在底层 CLI 订阅上）。
- 叶：[OpenCode Mobile (dzianisv)](opencode-mobile-dzianisv/) adopt（决策矩阵 4.42 第一：四硬条件全满足 + 双渠道上架 + 官方收录）
- 叶：[OpenCode Mobile (doza62)](opencode-mobile-doza62/) hold（功能最全但 2026-02-25 后停更半年 + beta 重连问题史——**iOS BYO 路线由此塌方**）

### D2 桥接派里信不信任中继？

- 不信任第三方中继 → 本机 Bridge/直连架构；能接受加密中继 → 体验层产品。
- 叶：[CC Pocket](ccpocket/) trial（本机 Bridge + 目录锁死 + Tailscale，安全工程最规矩；缺独立长测口碑）
- 叶：[Happy](happy/) trial（E2EE + 语音独门、赛道声量第一；Codex 移动审批失灵 issue 史 #489/#503 压住 adopt）
- 叶：[Paseo](paseo/) trial（/paseo-handoff 异构编排独一档；订阅额度折损 + license 文件非标准）
- 叶：[Zedra](zedra/) assess（QUIC P2P 零中继技术上最彻底；官方自认早期 + 中文输入法适配待自测）
- 叶：[T3 Code](t3code/) hold（多 CLI 包装广度第一但 token 消耗 3~5x 放大 bug #7338 + 官方自认极早期，等磨稳）

### D3 编排走会话级还是任务级？

- 多 Agent 并行：会话级审批编排（Paseo）vs 任务队列看板（Vibe Kanban）——后者粒度粗、无手机审批闭环。
- 叶：[Vibe Kanban](vibe-kanban/) assess（⭐28.1k 看板天花板，但 Bloop 2026-04 倒闭转社区维护 + 流程重）

### D4 国产模型场景？

- Codex/Claude 官方 App 均不遥控国产模型 CLI，iOS 侧空白位。
- 叶：[Octrix](octrix/) assess（V2EX 圈内唯一填充者；仓库无 LICENSE 文件，「全栈开源」宣称待补证）

### D5 Web/Bot/云托管轻路线值不值得当主力？

- Web 锁屏必断 + 无推送是路线级缺陷；TG 通道保活最强但代码过第三方云；云托管免运维但代码默认出本机。
- 叶：[ClaudeCodeUI](claudecodeui/) hold（明文 WebSocket #190 + CPU 130% #204 + 锁屏必断——临时凑合可以）
- 叶：[opencode-telegram-bot](opencode-telegram-bot/) hold（只当通知器，不当遥控器——合规雷 + diff 体验灾难）
- 叶：[Omnara](omnara/) trial（云托管免运维第一 + Watch 联动；代码默认过第三方云是隐私代价——「停更」传言已证伪，2026-09 仍活跃）

### D6 官方入口当基准线？

- 零配置 + 官方信任链，但 preview 不稳、单会话、终端须常开。
- 叶：[Claude Remote Control（官方）](claude-remote-official/) hold（HN:「clunky and buggy prerelease」——它解决不了的三件事正是第三方存在的理由）

## 落选节点（不立条目的死分支）

- **Catnip（W&B）**：iOS + GitHub Codespaces 路线，合盖党最优之一；但报告所引仓库 `wandb/catnip` gh API 直查 **404**，wandb org 下无此仓库——开源状态无法验证，GITHUB_TOKEN 过其后端的说法无法溯源。观察信号：仓库公开/官方文档落地后重审。
- **Cosyra**：$29.99/月闭源云 Ubuntu 容器，「合盖党」体验第一但违反免费+开源硬条件；官方页面自述（无独立审计）。价格与闭源不变则永不入选。
- **Nimbalyst**：freemium 闭源桌面工作区 + iOS companion；**「社区前三」「Vibe Kanban 最佳替代」叙事全部出自 nimbalyst.com 自家对比文，利益相关降权**。若开源核心落地可重审。
- **KKCode / FlyCode**（OpenCode iOS 第三方）：口碑样本极少，作者自认「App 没有 AI、Mac 必须开着、自搭 Tailscale」；FlyCode 疑似半停更。样本沉淀后再看。
- **Shahfarzane/opencode-mobile**（iOS Expo）：2026-01-15 后无提交，停更，被 doza62 覆盖。
- **ChatGPT Codex 移动 / Cursor iOS**：闭源官方对照——read-only/chat-first，不能接管本地 CLI，不满足 BYO；仅作能力基准线。
- **报告 A 提及的「Crush」**：口碑报告称 Android 专属本地 Agent 终端，未找到可靠一手来源，存疑不收录；「Shellby 演变自 KKCode」说法经复核为混淆（Shellby 是无关 SSH 客户端），剔除。

## 观察名单（下次复核触发器）

- T3 Code：#7338 token 放大修复确认 + 稳定版 → 重估（hold → trial）
- doza62/Shahfarzane：任何一方恢复 push → iOS BYO 重估
- Zedra：GPUI 中文输入法适配确认 + 脱离 "early" 声明 → trial
- Octrix：补 LICENSE 文件 → verdict 升一级的前提
- Vibe Kanban 社区版：多端同步方案落地 → 重估手机浏览器路线
