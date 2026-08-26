# Sublime Merge

> **TL;DR**：$99 买断的性能标杆：自研 Git 读库极快、行级暂存精细，2026 年仍在活跃更新，大仓库场景首选。

- **结论**：trial 试用
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 稳定版构建发布于 2026-04-14；dev 通道 Build 2124（2026-04-01，含 LFS lock 支持等） | [2] |
| 许可证 | 闭源；个人 $99 一次性（无限期免费评估）；商业版 $75/人/年 订阅 | [1] |
| 仓库 | 无公开仓库（Sublime HQ，悉尼） | — |
| 维护活跃度 | 稳定/dev 双通道 2026-04 均有发版；「已停更」传言与官网发版记录不符（2026-08-27 核验） | [2] |

## 为什么值得试用

1. **性能是它的立身之本**：官网明确宣传自研高性能 Git 读取库 + 自绘跨平台 GUI 工具包（vendor 口径）[2]；SourceForge 三方对比页用户评价「sets the bar for performance」[4]；dev.to 2025 横评将其列入大仓库友好一组 [3]。
2. **买断制 + 无限期免费评估**：$99 一次性（与 2026-07 会话快照一致，价格未变）；评估期不设时限，慢用户可以一直白嫖试用 [1][5]。
3. **行级/hunk 级暂存是招牌**：可按行拆 hunk、拖拽上下文扩展，commit 粒度控制全类别最精细之一 [2]。
4. **跨平台含 Linux**：Mac/Win/Linux 三平台齐备，是买断制里唯一覆盖 Linux 的 [2]。

## 为什么不是 adopt（对本人画像）

- 用户主力在终端（lazygit 已覆盖行级操作的键盘流），GUI 需求集中在「看」而非「精细拆提交」时，Fork 的交互更顺手、还便宜 $39 [6]。
- Sublime 系 UI 是「键盘优先的极简风」，与 Sourcetree 式「鼠标友好」预期有落差，上手体验两极（社区长期反馈）。

## 对比

与 Fork：同为买断，$99 vs $59.99，Sublime 性能与行级操作更强、跨平台更广，Fork 交互更常规讨喜。与 GitKraken/SmartGit 的订阅制相比无年付压力。逐维度对比见 `../comparison.md`。

## 风险与注意

- 更新节奏缓慢但未死：2026-04 后至 2026-08-27 官网无新构建记录（间隔 4 个月+），属于「低频深耕」模式，介意者标「待验证」。
- 许可升级政策（如 3 年后升级是否需付费）以官网 FAQ 为准，本次未逐条核验，待验证。
- 商业用途是 $75/人/年 订阅而非买断，公司采购需区分 [1]。

## 来源

1. Sublime HQ Store: Buy Sublime Merge — https://www.sublimehq.com/store/merge （访问 2026-08-27）
2. Sublime Merge 官网 / 下载页（版本与性能宣传） — https://www.sublimemerge.com （访问 2026-08-27）
3. dev.to: Best Git GUI Clients in 2025 — https://dev.to/_d7eb1c1703182e3ce1782/best-git-gui-clients-in-2025-gitkraken-sourcetree-fork-and-more-compared-4gjd （访问 2026-08-27）
4. SourceForge: GitKraken vs SourceTree vs Sublime Merge 用户对比 — https://sourceforge.net/softwarecomparison/GitKraken-vs-SourceTree-vs-Sublime-Merge/ （访问 2026-08-27）
5. 用户 2026-07-28 Claude 会话（价格快照 $99，2026-07 官网抓取）— 本地会话记录
6. Fork 官网 — https://fork.dev （访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录 |
