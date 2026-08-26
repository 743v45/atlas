# lazygit

> **TL;DR**：终端内零成本最高效：MIT 开源 TUI，81.7k star、月更活跃，重度终端用户的主战场，GUI 只补它不擅长的可视化。

- **结论**：adopt 推荐
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v0.64.1（2026-08-12 发布） | [2] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/jesseduffield/lazygit | — |
| 维护活跃度 | ⭐81,655（gh 采集 2026-08-27）；最近 push 2026-08-26；发布节奏稳定月更级 | [1][2] |

## 为什么选

1. **开源、免费、极活跃**：MIT 许可，81.6k star，仓库 2026-08-26 仍有 push，v0.64.1 于 2026-08-12 发布（gh 2026-08-27）[1][2]。star 规模在本类别所有开源项中断层第一（对照：GitHub Desktop 21.8k、GitUp 12.1k，同日采集）。
2. **与用户画像完全重合**：重度终端用户（zsh + Claude Code）日常工作流本就在终端里，lazygit 的键位驱动 staging/hunk 拆分/rebase/amend 效率高于任何鼠标 GUI；2026-07-28 会话结论亦为「终端用户装 lazygit，零成本、效率最高」[4]。7 月底搜索受限未核数据，本次已用 gh 一手核验补齐。
3. **性能无忧**：TUI 形态天然轻量，无 Electron/WebView 开销；同类横评将终端系客户端归入大仓库友好一档 [3]。

## 对比

它不是 Sourcetree 的「图形化」同类，而是该问题的另一解：放弃图形、换取速度与零成本。分支图可视化、拖拽式交互 rebase、外部 diff 工具集成这些 GUI 擅长的场景才需要 Fork/Sublime Merge 补位。逐维度对比见 `../comparison.md`。

## 风险与注意

- 学习曲线：键位体系需要上手期（官方 cheat sheet 可缓解）[1]。
- 无图形化分支拖拽、无内置 GUI merge 工具——复杂冲突可视化解算需配外部工具或 GUI 客户端。
- v0.x 版本号：作者刻意不大版本化，功能仍在演进（2026-08 观察 v0.64.x）[2]。

## 来源

1. GitHub: jesseduffield/lazygit — https://github.com/jesseduffield/lazygit （gh 采集 2026-08-27）
2. lazygit Releases（v0.64.1, 2026-08-12） — https://github.com/jesseduffield/lazygit/releases （gh 采集 2026-08-27）
3. dev.to: Best Git GUI Clients in 2025 — https://dev.to/_d7eb1c1703182e3ce1782/best-git-gui-clients-in-2025-gitkraken-sourcetree-fork-and-more-compared-4gjd （访问 2026-08-27）
4. 用户 2026-07-28 Claude 会话（Sourcetree 同类调研，价格快照 2026-07 官网抓取）— 本地会话记录

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（承接 2026-07-28 会话「终端用户首选」结论） |
