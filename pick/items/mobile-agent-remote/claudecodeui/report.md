# ClaudeCodeUI (CloudCLI)

> **TL;DR**：免装 App 的自托管 Web 路线代表（iPad 体验尚可），但锁屏必断、明文 WebSocket issue、大会话 CPU 130%——临时凑合可以，不做生产力主力。

- **结论**：hold 观望
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | AGPL-3.0 | [1] |
| 仓库 | https://github.com/siteboon/claudecodeui | — |
| 维护活跃度 | pushed 2026-09-16，⭐13,709（gh 2026-09-17） | [1] |
| 接入 | Claude Code / OpenCode / Cursor CLI / Codex | [1] |

## 为什么不选（hold 理由）

- **安全模型要自己补齐**：#190 HTTPS 代理后走未加密 WebSocket——直接冲击「自托管更安全」前提；部署必须自配 TLS + 强认证，端口不可裸公网 [2]。
- **性能坑实锤**：#204 大量会话文件时 CPU 130%+；手机浏览器跑大输出会崩（聚合口碑）[2][3]。
- **Web 墓碑机制**：手机锁屏即断 WebSocket，解锁需刷新重初始化；无原生推送——这些是路线级缺陷，非版本 bug 可修 [3]。
- #206 Windows `process.env.HOME` 未定义启动崩溃（跨平台未稳）[2]。

## 对比

- Web 路线唯一优势是零安装 + iPad 大屏体验可接受；作为「临时凑合」场景里排名靠前，长期生产力被口碑一致劝退 [3]。

## 风险与注意

- 若部署：VPS 放 UI、Tailscale/HTTPS 进网、最小端口、默认禁用的工具权限保持禁用 [1][3]。

## 来源

1. GitHub 仓库 — https://github.com/siteboon/claudecodeui（gh 2026-09-17：AGPL-3.0、⭐13,709、pushed 2026-09-16）
2. Issues #190/#204/#206 — https://github.com/siteboon/claudecodeui/issues/190 等（均已复核存在）
3. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | hold | 首次记录：路线级缺陷（锁屏断/无推送），非执行问题 |
