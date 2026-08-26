# Git 图形化客户端 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

类似 Sourcetree 的 Git 图形客户端有哪些、最好用的是哪个、价格多少？（2026-07-28 会话；用户画像：macOS、重度终端用户——GUI 是辅助）

## 分叉与决策

### D1 主力形态：终端还是 GUI？

- 用户重度终端（Claude Code/zsh）——lazygit（TUI ⭐81k、月更）是日常主力，GUI 按需辅助。
- 叶：[lazygit](lazygit/) adopt（决策矩阵 4.88 第一：免费+MIT+月更全满）

### D2 免费参照系？

- 会话结论「免费选 Sourcetree」承接；2026 年 Sourcetree 仅 4 个小版本（维护态），GitHub Desktop 官方周级更新但功能基础，SmartGit 非商业免费且跨平台。
- 叶：[Sourcetree](sourcetree/) trial · [GitHub Desktop](github-desktop/) trial · [SmartGit](smartgit/) trial（价格修正：官网现价 $5/人/月起 或 perpetual，低于 7 月预估）

### D3 付费买断还是订阅？

- **Fork $59.99 一次性买断**（终身更新，公认体验最顺）vs Tower 年订阅（$69-149，功能最全但个人性价比低）vs GitKraken 订阅（免费档仅本地+公开仓库，Pro $6.99/席/月已落定）。
- 决策：付费 GUI 选 Fork 买断；订阅制对个人不划算。
- 叶：[Fork](fork/) adopt · 落选节点：[Tower](tower/) hold · [GitKraken](gitkraken/) hold

### D4 性能标杆？

- Sublime Merge：大仓库性能标杆，「停更」传言不实（2026-04 仍发版）；个人 $99、商业 $75/人/年。
- 叶：[Sublime Merge](sublime-merge/) trial（决策矩阵 4.35 第二）

### D5 2026 新变量（会话未覆盖、调研新增）？

- GitFox：macOS 原生 SwiftUI 新秀，€60/年——大仓库表现待验证。
- 叶：[GitFox](gitfox/) assess · 观察名单：GitButler（⭐21.6k、v0.22.1 2026-08-24 活跃）、GitUp、Gitoryx
