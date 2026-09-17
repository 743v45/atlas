# OpenCode Mobile (dzianisv)

> **TL;DR**：Android 上「免费 + 开源 + 任意 BYO 模型 + 原生 App」的唯一全满足解：直连自托管 opencode server、无中继、持续更新、被官方收录。

- **结论**：adopt 推荐
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v0.4.15（2026-08-14 发布） | [1][2] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/dzianisv/opencode-mobile | — |
| 维护活跃度 | pushed 2026-08-20，⭐169（gh 2026-09-17）；2026 年发布记录连续 | [1] |
| 上架渠道 | Google Play + F-Droid 双渠道稳定签名 | [1][3] |

## 为什么选

- **BYO 模型自由度全场最高**：OpenCode 服务端侧 75+ provider（OpenAI/Anthropic/Gemini/DeepSeek/本地 Ollama），客户端只是薄前端，模型完全由自己的 `opencode serve` 决定 [1][3]。
- **无中继架构**：官方页面明确 "no middleman, no cloud relay"，直连用户自己的 opencode server（LAN / Cloudflare Tunnel / ngrok / Tailscale），凭证存 Android Keystore，支持生物识别 [1]。
- **社区验证度最高**：被 OpenCode 官方仓库收录（sst/opencode#669）；"Best Android client for OpenCode" 讨论中一致排第一 [2][3]。
- **功能闭环完整**：多服务器管理、流式输出、Diff 查看、工具调用审批、离线 Demo 模式（30 秒无服务器模拟全流程 onboarding）[1][3]。

## 对比

- iOS 侧无对等物：doza62 版半年未更新（2026-02-25 后无 push，见其条目）；Shahfarzane 版 2026-01 后停更 [3]。
- 与遥控桥接派（Happy/CC Pocket）的本质差异：本条目配 OpenCode 引擎，模型任意换；桥接派的模型锁定在底层 CLI 的订阅上 [3]。

## 风险与注意

- **仅 Android**：官方明确 iOS 不在当前版本范围（Roadmap 项），iOS 用户无对等选择 [1][3]。
- 依赖上游 `opencode serve` API，上游大版本变更时有失配风险（第三方客户端共性）[3]。
- 需自备网络路径：出门用要 Tailscale 或 Cloudflare Tunnel，勿把端口裸暴露公网 [1][3]。

## 来源

1. GitHub 仓库 — https://github.com/dzianisv/opencode-mobile（gh 2026-09-17：MIT、⭐169、pushed 2026-08-20）
2. OpenCode 官方收录 PR — https://github.com/sst/opencode/pull/669
3. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（谷歌 AI 检索汇总，关键论断经 GitHub API 复核，2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | adopt | 首次记录：四条件（免费/开源/BYO/原生App）全满足且口碑扎实 |
