# Vibe Kanban

> **TL;DR**：多 Agent 并行编排的看板天花板，但定位是任务队列而非手机审批闭环：流程重、手机仅浏览器、母公司 2026-04 倒闭后转社区维护。

- **结论**：assess 评估
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/BloopAI/vibe-kanban | — |
| 维护活跃度 | pushed 2026-09-16，⭐28,100（gh 2026-09-17） | [1] |
| 端 | 自托管 Web（手机浏览器访问） | [1][2] |
| 支持引擎 | Claude Code / Codex / Cursor 等多 CLI | [1][2] |

## 为什么关注

- **看板并行编排仍是同类最强**：任务卡（To Do → In Progress → Done）+ 每任务独立 Git worktree 并行写码互不冲突；内置浏览器预览/DevTools/设备模拟；MCP 与项目规则集中配置一次全 Agent 共享 [2][3]。
- 本地优先，代码与任务数据留本机；支持 SSH 远程连接模式 [2]。

## 为什么只是 assess

- **定位错位**：它是任务队列粒度，不承担手机端实时审批闭环——若需要「批准/拒绝这一次命令」，看板信息粒度不够 [2]。
- **手机端弱**：仅浏览器接入，无原生推送；锁屏断连是 Web 共性问题 [2][3]。
- **母公司风险已落地**：Bloop 2026-04 倒闭（外部文章佐证 [3]），转 Apache-2.0 社区维护，托管云服务下线；仓库虽仍活跃（9 月有 push），但「社区用爱发电」的长期性要打问号 [1][2]。
- 流程摩擦：顺手修一行也要建 Task/开 worktree，小改动场景负体验 [3]。

## 对比

- vs Paseo：Paseo 保留会话级审批与流式输出，Vibe Kanban 是任务级派发；两者可组合（Kanban 管队列、遥控 App 管会话）[2]。
- 「转向 Nimbalyst 等替代品」的叙事出自 nimbalyst.com 自家对比文，利益相关，不采信（见 decision-tree 落选节点）[3]。

## 风险与注意

- 曾有云同步特性随 Bloop 倒闭破裂，新多端同步方案社区打磨中——依赖多端同步前先验证当前版本 [2]。

## 来源

1. GitHub 仓库 — https://github.com/BloopAI/vibe-kanban（gh 2026-09-17：Apache-2.0、⭐28099、pushed 2026-09-16）
2. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17）
3. 口碑调研报告 A — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-a.md（2026-09-17，Bloop 倒闭时间线）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | assess | 首次记录：编排强但错位 + 公司倒闭转社区 |
