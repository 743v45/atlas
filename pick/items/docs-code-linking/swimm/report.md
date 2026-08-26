# Swimm

> **TL;DR**：锚点级最强——token/AST 锚点随重构自动跟随+swimm-verify CI 卡点；但核心闭源、按代码行数计价、2026 已转向企业现代化服务，对个人/小团队过重。

- **结论**：hold（观望——个人场景外；锚点级机制仍是最强参照系）
- **核实日期**：2026-08-27（官网/定价/GitHub org 复核）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 形态 | 文档平台 SaaS + IDE 插件（VS Code/JetBrains）+ GitHub App | [1][5] |
| 许可 | 核心闭源（swimmio org 仅辅助仓库：swimm-verify-action ⭐3 MIT、pre-commit hooks ⭐5；gh 2026-08-27） | [4] |
| 定价 | 官方口径「按要理解的代码行数计价」，销售驱动（Get a demo / Book a call）；查询 2026-08-27 | [2] |
| CI 组件 | swimm-verify GitHub Action：⭐3 / MIT / 最后 push 2024-07-30（gh 2026-08-27） | [4] |
| 文档存储 | 入仓：`.swm` 目录，现为 sw.md（Markdown+frontmatter）格式，git 同步 | [3] |

## 为什么（未 pick，但承认其机制最强）

- **锚点级价值是真的**：文档引用以 token/AST 锚点定位代码，重构时代码怎么挪文档引用自动跟随——这是六级方案里唯一解决「标识随代码演进」的层级；配合 swimm-verify 在 CI 里校验文档新鲜度并卡 PR，四支柱全部拉满（2026-08-25 会话结论）[6]。第三方评测同样以其「代码耦合 + 漂移检测 + CI 校验」为核心卖点 [5]。
- **商业与形态不合个人场景**：
  1. 定价按代码行数、销售驱动（demo/Book a call 入口遍布官网），面向企业（Akamai/Merck/Optum 等客户墙、Gartner Cool Vendor）[1][2]。第三方报价口径互相冲突且可信度存疑：AutomaDocs 2026 称「个人免费、团队 ~$19/用户/月」[5]，Research.com 2026 称「$15/月含免费档」——与官方现行「按代码行数计价」不符，**待验证**（历史免费档或已收缩）。
  2. IDE 插件、playlists、onboarding 流程是团队知识管理设计，单人使用徒增流程重量 [6]。
  3. **2026 年主业已转向**：官网现主打「Agentic modernization」——评估/规约/现代化/移交四阶段固定价的企业现代化服务（含 mainframe），文档平台成为其中一环 [1]。供应商战略重心偏移对单一功能用户的长期保障是实际风险。
  4. 核心闭源：锚点引擎无法自托管或审计；swimm-verify-action 自 2024-07 后未再更新（gh 2026-08-27）——动作本身简单（包装 CLI），但维护信号平淡 [4]。
- **被组合方案替代的判断**：CI 卡点（正确性保障）可用 exit 1 脚本等价实现；损失的只是 IDE 内漂移提醒与锚点自动跟随（体验增益）。个人场景下「一天成本的简化版 Swimm」覆盖了 90% 价值——见 [ci-drift-combo](../ci-drift-combo/report.md) [6]。

## 对比

与组合方案/Docusaurus/TypeDoc 的逐维对比见 `../comparison.md`。

## 风险与注意

- 定价透明度低：官方无公开价目表，第三方数据互相矛盾（见上，均注明来源与年份）[2][5]。
- 供应商方向漂移：企业现代化服务化的 2026 转向，意味着产品投入可能向大客户场景倾斜 [1]。
- 内容无锁定但流程有：sw.md 文件在仓、纯文本可读 [3]；锚点系统与创作/校验流程深度绑定其平台，迁出即退化成普通 Markdown。
- 若未来出现开源锚点级工具（AST 锚点 + CI 校验的 CLI 实现），本条目应立即重评。

## 来源

1. Swimm 官网（2026 主打 Agentic modernization）— https://swimm.io（访问 2026-08-27）
2. Swimm Pricing（「Pricing is based on the number of lines of code」）— https://swimm.io/pricing（访问 2026-08-27）
3. Docs as Code: understanding Swimm's sw.md Markdown format — https://swimm.io/blog/docs-as-code-understanding-swimm-sw-md-markdown-format（访问 2026-08-27）
4. Swimm Verify Action / swimmio org 仓库 — https://github.com/swimmio/swimm-verify-action（gh 2026-08-27 快照）；GitHub Marketplace — https://github.com/marketplace/swimm-io（访问 2026-08-27）
5. Swimm Review 2026（The CTO Club）/ AutomaDocs Best Documentation Tools 2026 — https://thectoclub.com/tools/swimm-review（访问 2026-08-27）
6. Claude 历史会话（2026-08-25）——锚点级分析与否决结论提取源

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录（历史会话结论 + 2026-08-27 复核官网转型/定价/org 仓库） |
