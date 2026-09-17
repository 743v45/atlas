# Claude Remote Control（官方）

> **TL;DR**：纯 Claude 场景的零配置官方入口，但 preview 状态口碑差（HN:「clunky and buggy prerelease」）、单会话、终端必须开着——等官方磨稳。

- **结论**：hold 观望
- **核实日期**：2026-09-17

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 许可证 | 闭源（Anthropic 官方功能） | [1] |
| 载体 | Claude App（iOS/Android/Web）内 | [1][2] |
| 形态 | 遥控本地 Claude Code 会话 + 云会话 + Dispatch 连桌面端 | [1] |

## 为什么不选（hold 理由）

- **preview 口碑差**：HN 评论概括「extremely clunky and buggy prerelease… don't try to hot fix prod from the toilet without a different mobile frontend」；停止按钮失效、UI 断连、输出显示 XML、会话加载失败等（二手汇总，2026-02 HN 主帖 [3]）。
- **单会话**：无多会话/多任务管理，编排能力为零 [3]。
- **终端必须开着**：本地会话前提是机器 + 终端存活，合盖/关终端即断——官方文档列明限制 [1][3]。
- 仅 Claude 生态；BYO 其他模型无从谈起 [3]。

## 为什么仍记录

- 零配置 + 官方信任链，是所有第三方遥控面对标的基准线；官方通道本身可信度最高 [1][3]。
- 它的市场缺口（合盖、跨代理、审批可靠性）正是第三方工具的存在理由 [3]。

## 风险与注意

- 纯 Claude + 不想装任何第三方时可用，预期要低；随 Claude App 更新快速演变，半年后重估 [1][3]。

## 来源

1. Claude Code 官方文档（mobile）— https://code.claude.com（「The Claude app for iOS and Android is a client for Claude Code sessions rather than a place where code runs」，2026-09 查）
2. 口碑调研报告 B — raw/2026-09-17/web/mobile-agent-remote-google-ai-report-b.md（2026-09-17）
3. HN 汇总 — https://hn-tldr.com/posts?page=116（HN 主帖 2026-02-25 的评论聚合）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-09-17 | hold | 首次记录：官方基准线，preview 不稳 |
