# Git 图形化客户端 · 横评

> 主题：macOS 上 Sourcetree 同类 GUI 客户端怎么选。用户画像：重度终端用户（zsh + Claude Code），GUI 是可视化辅助而非主战场。
> 数据核查日：2026-08-27（承接 2026-07-28 会话调研，价格全部重查）。

## 场景速配（先给结论）

| 场景 | 推荐 | 一句话理由 |
|---|---|---|
| 终端重度、GUI 只用来看 diff/历史 | **lazygit**（主）+ **Fork**（辅） | 零成本 TUI 覆盖 90% 操作，GUI 补可视化 [1][2] |
| 愿意付一次钱买最顺手的 GUI | **Fork** | $59.99 买断，轻快稳定，2026 评测共识 [2][3] |
| 大仓库 / monorepo | **Sublime Merge** | 自研 Git 读库，性能标杆 [4][5] |
| 完全免费且要全功能 GUI | **Sourcetree** | 免费参照系，代价是慢节奏与卡顿 [6][7] |
| GitHub 重度 + 新手向 | **GitHub Desktop** | 官方免费，功能基础 [3][8] |
| 学生 / 开源维护者要免费商业级 | **SmartGit**（或 Tower 教育版） | 非商业免费档覆盖全功能 [9] |
| 需要 Linux 的团队订阅 | **GitKraken** / **SmartGit** | 跨平台 + 集成，个人不推荐 [10][9] |
| 追新 macOS 原生体验 | **GitFox**（观察） | SwiftUI 原生、迭代快，待大仓库验证 [11] |

## 属性对比矩阵

| 维度 | lazygit | Fork | Sublime Merge | Sourcetree | GitHub Desktop | SmartGit | GitFox | GitKraken | Tower |
|---|---|---|---|---|---|---|---|---|---|
| 形态 | TUI | GUI | GUI | GUI | GUI | GUI | GUI | GUI | GUI |
| 许可 | **MIT 开源** | 闭源买断 | 闭源买断 | 免费闭源 | **MIT 开源** | 商业（非商业免费） | 闭源订阅 | freemium | 闭源订阅 |
| 价格 | **免费** | $59.99 一次性 | $99 一次性 | **免费** | **免费** | $5/人/月起 | €60/年 | $6.99/人/月起 | $69/年起 |
| 平台 | 全平台（TUI） | macOS/Win | macOS/Win/Linux | macOS/Win | macOS/Win | macOS/Win/Linux | **仅 macOS** | macOS/Win/Linux | macOS/Win |
| 性能 | 快（无 GUI 开销） | 轻快 | **极快**（自研 Git 库）[5] | 中（卡顿报告）[7] | 中（Electron）[4] | 好 | 快（SwiftUI 原生）[11] | 中（大仓库差）[12] | 中上 [4] |
| 大仓库 | 好 | 好 [4] | **好** [4][5] | 差 [4][7] | 差（monorepo 吃力）[4] | 好 [3] | 待验证 | 差（官方性能专页自认）[12] | 好 [4] |
| 维护活跃 | **极高**（月更，8-12 新版）[1] | 高（持续发版）[2] | 中（低频深耕，2026-04）[5] | 中低（年 4 小修）[6] | **极高**（官方团队周级）[8] | 高（syntevo 长期）[9] | 高（v4.x 快迭代）[11] | 极高（平台化厂商）[10] | 高（17.x）[13] |
| 拖拽/可视化 rebase | ✗（键位） | ✓ | ✓ | ✓ | 有限 | ✓ | ✓ | ✓（招牌分支图） | ✓（含拖拽） |
| 行级/hunk 暂存 | ✓ | ✓ | **✓（最精细）**[5] | ✓ | 有限 | ✓ | ✓ | ✓ | ✓ |
| 撤销安全网 | 部分可逆 | 有限 | 有限 | 有限 | 有限 | 有限 | 有限 | 有限 | **无限撤销任意操作（独占）**[13] |

注：✓/✗ 为功能有无速记，依据各条目报告引用；「快/中/差」性能档位依据 dev.to 2025 与 Bytestack 2026 横评分组 [4][7]。

## 价格表（查询日期 2026-08-27，均为官网现价）

| 工具 | 个人价 | 商业/团队价 | 免费档 | vs 2026-07-28 会话快照 |
|---|---|---|---|---|
| lazygit | 免费 | — | 全功能 | 不变 |
| Sourcetree | 免费 | 免费 | 全功能 | 不变 |
| GitHub Desktop | 免费 | 免费 | 全功能 | 不变 |
| Fork | **$59.99 一次性**（评估免费无时限）[2] | 同价/席 | 评估版 | 不变 |
| Sublime Merge | **$99 一次性**（评估无时限）[5] | $75/人/年 [5] | 评估版 | 个人价不变；本次新增商业价口径 |
| GitFox | **€60/年**（含 VAT；或 €8/月）[11] | Team €144/年/2 席 [11] | 30 天试用 | **7 月未收录**（本轮新晋候选；早期曾 €32 档）[11] |
| SmartGit | 非商业免费（需注册）[9] | **$5/人/月**起 或 perpetual [9] | Hobby/学生/开源/慈善 | **比 7 月预估低**（7 月参考口径「约 $99/年起」） |
| GitKraken | —（免费档仅本地+公开仓库）[10] | Pro **$6.99/席/月**（年付）、Advanced $9.99、Business $19.99 [10] | 仅本地+公开仓库 | **从「参考 $5–9」落定为确切价** |
| Tower | Basic **$69/年**、Pro $129/年 [13] | Enterprise $149/年/人；10+ 席 9 折 [13] | 30 天试用（学生计划另议） | 不变（$69/$129/$149 三档同） |

## 维护活跃度（人工核验快照，gh 采集 2026-08-27）

| 工具 | 关键证据 | 观察日期 |
|---|---|---|
| lazygit | v0.64.1（2026-08-12）；push 2026-08-26；⭐81,654 | gh 2026-08-27 |
| GitHub Desktop | 3.6.4（2026-08-13）；push 2026-08-26；⭐21,792 | gh 2026-08-27 |
| Fork | Mac 2.66.7 / Win 2.16.1（官网 CDN） | 官网 2026-08-27 |
| Sourcetree | Mac 4.2.19（2026-07-30）；2026 年 4 个小版本 | 官网 2026-08-27 |
| Sublime Merge | 稳定版 2026-04-14；dev Build 2124（2026-04-01） | 官网 2026-08-27 |
| GitFox | 4.1.4（App Store，2026-04-29） | App Store 2026-08-27 |
| Tower | Mac 17.1.1 | 官网 2026-08-27 |
| SmartGit | 定价页持续更新；版本号未公开（待验证） | 官网 2026-08-27 |
| GitKraken | 产品线扩至 CLI/GitLens/AI 全家桶 | 官网 2026-08-27 |

<!--gen:activity-table-->

## 决策树

```text
你在终端里的时间多吗？
├─ 是（主力 CLI/TUI）
│   ├─ 接受键位学习成本 → lazygit（免费，主力）
│   └─ 想要鼠标可视化兜底 → + Fork（$59.99 买断，辅助）
└─ 否（要全 GUI 工作流）
    ├─ 预算为零？
    │   ├─ 要功能全 → Sourcetree（接受慢节奏/卡顿）
    │   ├─ 要简洁/官方 → GitHub Desktop
    │   └─ 学生/开源身份 → SmartGit 非商业免费（或 Tower 教育版）
    ├─ 愿付一次钱？
    │   ├─ 大仓库/性能敏感 → Sublime Merge（$99）
    │   └─ 均衡优先 → Fork（$59.99）
    └─ 接受订阅？
        ├─ 团队 + Linux + 集成 → GitKraken（$6.99/席/月起）或 SmartGit（$5/席/月起）
        ├─ 要无限撤销/企业管控 → Tower（$69+/年）
        └─ 要 macOS 原生尝鲜 → GitFox（€60/年，先观察）
```

## 加权决策矩阵

<!--gen:decision-matrix-->

> **注记**：决策矩阵只覆盖上表所列维度（许可/成本/维护/性能/大仓库），**不包含**功能深度、交互打磨、UI 审美、团队协作能力等维度外因素；维度外风险以各条目 verdict 为准。矩阵高分与谨慎 verdict 并存时不是矛盾，是两层分工——例如 GitHub Desktop 维护分高但功能基础故仅 trial；GitFox 若矩阵分不低但大仓库无数据故 assess。

## 观察名单（未立条目，触发条件再升级）

| 候选 | 状态快照（gh 2026-08-27） | 观察理由与触发条件 |
|---|---|---|
| **GitButler** | ⭐21,572；v0.22.1（2026-08-24）；push 2026-08-26 | 「虚拟分支」新范式（并行分支栈），与传统 GUI 不可直接对比；license 非 OSI 标准（source-available）。触发：范式需求出现或 1.0 稳定 |
| **GitUp** | ⭐12,110；GPL-3.0；push 2026-07-27 | macOS 开源原生老将，但迭代慢于 GitHub Desktop。触发：想要开源+原生 mac 且接受功能取舍 |
| **Gitoryx** | 2026 年横评中出现的新买断制原生客户端 [14] | 信息尚少（厂商自评为主）。触发：独立评测出现后再核 |

## 来源

1. GitHub: jesseduffield/lazygit — https://github.com/jesseduffield/lazygit （gh 采集 2026-08-27）
2. Fork 官网 — https://fork.dev （访问 2026-08-27）
3. Rockstar Developer University: 11 Best Git Clients for Developers in 2026 — https://rockstardeveloperuniversity.com/best-git-clients-for-developers （访问 2026-08-27）
4. dev.to: Best Git GUI Clients in 2025: GitKraken, SourceTree, Fork, and More Compared — https://dev.to/_d7eb1c1703182e3ce1782/best-git-gui-clients-in-2025-gitkraken-sourcetree-fork-and-more-compared-4gjd （访问 2026-08-27）
5. Sublime Merge 官网 / Store — https://www.sublimemerge.com 、https://www.sublimehq.com/store/merge （访问 2026-08-27）
6. Sourcetree Download Archives — https://www.sourcetreeapp.com/download-archives （访问 2026-08-27）
7. Bytestack: Sourcetree, GitKraken, GitHub Desktop, and Fork Compared — https://getpi.bytestack.ai/blog/4-gui-git （访问 2026-08-27）
8. GitHub: desktop/desktop — https://github.com/desktop/desktop （gh 采集 2026-08-27）
9. SmartGit Pricing — https://www.smartgit.dev/pricing/ （访问 2026-08-27）
10. GitKraken Pricing — https://www.gitkraken.com/pricing （访问 2026-08-27）
11. Gitfox 官网 / Plans — https://www.gitfox.app 、https://www.gitfox.app/plans （访问 2026-08-27）
12. GitKraken Help: Improve GitKraken Desktop Performance（更新 2026-03） — https://help.gitkraken.com/notifications/desktop-performance/ （访问 2026-08-27）
13. Tower 官网 / Pricing / Blog — https://www.git-tower.com 、https://www.git-tower.com/pricing 、https://www.git-tower.com/blog/best-git-client （访问 2026-08-27）
14. Gitoryx: Best Git GUI Clients in 2026 — https://www.gitoryx.com （访问 2026-08-27，厂商自评为准）
15. 用户 2026-07-28 Claude 会话（初始调研与 2026-07 价格快照）— 本地会话记录
