# 手机端遥控 Coding Agent 客户端 · 横评

> 主题：手机上远程查看/审批/驱动本机 AI 编程 Agent（Claude Code / Codex / OpenCode）的客户端怎么选。
> 用户画像：免费 + 开源 + BYO 任意模型 + 手机原生 App 优先；闭源官方产品仅作对照。
> 数据核查日：2026-09-17（gh API 直查 stars/pushed_at/license；口碑来自两份谷歌 AI 调研报告，关键论断已复核，原始留档 `raw/2026-09-17/web/`）。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| Android + BYO 任意模型（标准答案） | **OpenCode Mobile (dzianisv)** | 四条件全满足，直连无中继，双渠道上架仍在更新 [1] |
| 不信任一切中继（求稳） | **CC Pocket + Tailscale** | 本机 Bridge + 目录锁死，安全工程最规矩 [2] |
| 不信任一切中继（求彻底） | **Zedra** | QUIC P2P 零中继，但官方自认早期 + 中文输入法适配待自测 [3] |
| Claude/Codex 订阅党要体验最顺 | **Happy** | E2EE + 语音独门；接受 Codex 审批偶发失灵史 [4] |
| 多 Agent 异构编排（homelab） | **Paseo** | /paseo-handoff 跨 harness 交棒独一档；注意订阅额度折损 [5] |
| iOS + BYO 模型 | **无可靠解**（doza62 停更半年） | iOS 是本类别当前最大空白，见 decision-tree [6] |
| 只当通知器 | **opencode-telegram-bot** | 保活推送全场最强；代码过 TG 云是硬代价 [7] |
| 多 Agent 并行任务队列 | **Vibe Kanban** | 看板 worktree 并行天花板；流程重、转社区维护 [8] |
| 零运维云托管 | **Omnara** | 一键即用 + Watch 联动；代码默认过第三方云 [9] |
| 纯 Claude 零配置 | Claude Remote Control（官方） | 官方信任链但 preview 不稳，基准线 [10] |

## 属性对比矩阵

| 维度 | dzianisv mobile | CC Pocket | Happy | Paseo | Zedra | tg-bot | Vibe Kanban | T3 Code | doza62 mobile | Omnara | ClaudeCodeUI | Octrix | Claude 官方 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 形态 | 原生App客户端 | 原生App桥接 | 原生App桥接 | daemon编排 | 原生App编辑器 | TelegramBot | 自托管看板 | 控制面转交CLI | 原生App客户端 | 云指挥台 | Web自托管 | 原生App桥接 | 官方App |
| 许可 | **MIT** [1] | **MIT** [2] | **MIT** [4] | Apache-2.0* [5] | **MIT** [3] | **MIT** [7] | **Apache-2.0** [8] | **MIT** [11] | **MIT** [6] | **Apache-2.0** [9] | AGPL-3.0 [12] | **无LICENSE** [13] | 闭源 [10] |
| 成本 | 免费·BYO | 免费·BYO | 免费·BYO | 免费·BYO | 免费·BYO | 免费·BYO | 免费·BYO | 免费·订阅绑定 | 免费·BYO | 免费+云额度 | 免费·BYO | 免费·BYO | Claude订阅 |
| 模型接入 | **任意BYO** | Claude·Codex | Claude·Codex | 多CLI包装 | Claude·Codex | **任意BYO** | 多CLI包装 | 多CLI包装 | **任意BYO** | Claude系 | Claude·CursorCLI | 多CLI包装 | Claude系 |
| 手机端 | Android | iOS/Android | iOS/Android/Web | iOS/Android/Web | iOS/Android | Telegram | 浏览器 | iOS/Android/Web | iOS/Android/Web | iOS/Web | 浏览器/PWA | iOS | ClaudeApp |
| 代码路径 | **直连无中继** | 本机Bridge | E2E中继(可自托管) | 直连或E2E中继 | **P2P直连** | 过TG云端 | 纯本地内网 | 本地server+relay | 直连无中继 | 云同步(可自托管) | 纯自托管 | LAN/私钥中继 | Anthropic通道 |
| 维护活跃(pushed) | 2026-08-20 [1] | 2026-09-15 [2] | 2026-09-16 [4] | 2026-09-16 [5] | 2026-09-15 [3] | 2026-09-13 [7] | 2026-09-16 [8] | 2026-09-16 [11] | **2026-02-25** [6] | 2026-09-16 [9] | 2026-09-16 [12] | 2026-09-11 [13] | 官方持续 [10] |
| ⭐(2026-09-17) | 169 | 1,069 | 23,805 | 17,468 | 223 | 1,159 | 28,100 | 22,865 | 271 | 2,852 | 13,709 | 117 | — |
| 审批闭环口碑 | 工具调用审批可 [1] | **最规矩** [2] | Codex偶发失灵 [4] | 好但early crash史 [5] | 待自测 [3] | 命令式,弱 [7] | 任务粒度,弱 [8] | 依赖底层 [11] | beta问题史 [6] | 策略引擎+Watch [9] | 锁屏必断 [12] | 样本少 [13] | preview差 [10] |
| 独立安全审计 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无(官方背书) |
| verdict | **adopt** | trial | trial | trial | assess | hold | assess | hold | hold | trial | hold | assess | hold |

*注：Paseo license 文件带自定义版权头，GitHub 识别 NOASSERTION，正文为 Apache-2.0（gh 2026-09-17 解码确认）。*

## 本类别三条结构性结论（2026-09-17 快照）

1. **审批闭环是第一筛选标准**：Happy 的 Codex 审批失灵 issue（#489/#503）、ClaudeCodeUI 锁屏必断、官方 Remote「停止按钮失灵」——演示视频看不出按钮可靠性，必须自测 [4][12][10]。
2. **本机休眠杀全场桥接派**：Happy/Paseo/CC Pocket/T3 Code 全部要求 daemon 机器不睡；合盖续跑只有云工作区路线（本类别外：Catnip/Cosyra/VPS，见 decision-tree 落选节点）[4][5]。
3. **iOS BYO 路线塌方**：doza62 停更半年、Shahfarzane 停更、KKCode/FlyCode 样本极少——Android 有 adopt，iOS 无一可推 [6]。

## 决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖所列维度；维度外风险（token 放大 bug、停更、审批失灵史、license 缺失）以各条目 verdict 为准——矩阵高分与 hold verdict 并存不是矛盾，是两层分工。

## 来源

1. https://github.com/dzianisv/opencode-mobile（gh 2026-09-17）
2. https://github.com/K9i-0/ccpocket（gh 2026-09-17）
3. https://github.com/tanlethanh/zedra（gh 2026-09-17）
4. https://github.com/slopus/happy + issues #489/#496/#503（gh 2026-09-17 复核）
5. https://github.com/getpaseo/paseo + release v0.1.65（gh 2026-09-17 复核）
6. https://github.com/doza62/opencode-mobile（gh 2026-09-17）
7. https://github.com/grinev/opencode-telegram-bot（gh 2026-09-17）
8. https://github.com/BloopAI/vibe-kanban（gh 2026-09-17）
9. https://github.com/omnara-ai/omnara（gh 2026-09-17）
10. https://code.claude.com + https://hn-tldr.com/posts?page=116
11. https://github.com/pingdotgg/t3code + issue #7338（gh 2026-09-17 复核）
12. https://github.com/siteboon/claudecodeui + issues #190/#204/#206（gh 2026-09-17 复核）
13. https://github.com/andforce/octrix（gh 2026-09-17，license=null）
14. 口碑原始留档 — `raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md`、`raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md`
