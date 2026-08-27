# 个人知识库 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

个人知识库，和 AI 共建，用什么工具管理？（2026-08-20 首问；08-25 落地为 taevasidian；08-27 高强度复核）

## 分叉与决策

### D1 核心命题：AI 共建的本质是什么？

- 决策：**AI 对存储层的原生访问权**——AI 能直接无缝读写知识库全文。一切工具按此裁决。

### D2 存储形态：本地纯文本还是应用数据库？

- 本地纯 Markdown + Git：读写/搜索/批量重构无门槛、共建历史可回溯（Git 记录人和 AI 各自改了什么）、可 diff/grep/发布。
- 数据库型：块级引用更细（思源）或 Web 多端（Trilium），但牺牲 AI 文件直写通用性——落选主因。
- SaaS：API 批量读写慢、数据不本地——落选主因。
- 叶：[Markdown + Git 仓库工作流](markdown-git-vault/) adopt
- 落选节点：[Notion](notion/) hold（AI 锁 Business $20/席/月 + agent 批量 API 慢）

### D3 双链怎么来：手动 Zettelkasten 还是机器织网？

- 用户主用法是「页面阅读 + 全文搜索」——双链价值在「能检索的知识库」而非卡片盒思考流。
- 决策：AI 写入时自动织 `[[链接]]`，反链由阅读器自动算；双链只写一次。
- 落选节点：RAG/向量库方案（黑盒检索、token 效率低，千条内 ripgrep 够——Khoj ⭐36.7k 属此路线，观察名单）。

### D4 阅读器层：数据之上用什么看？

- Obsidian：本地纯 md、不锁格式不建数据库、双链/反链/图谱核心功能——**只当阅读器，不做写入通道**（随时可换、数据零迁移）；2026 官方 CLI（1.12，101 命令）+ CEO 发布 agent skills（⭐47k）——架构方向获官方背书。
- Logseq：大纲/日记流范式与「页面阅读」错位；2.0（2026-07）转 SQLite 数据库版、OG/2.0 双轨添变数——选它须锁 OG 模式。
- 思源：2026 AI 转向最激进（v3.8.0 内置 MCP+Agent、语义搜索），但通道仍是 API 层非文件直写；若出纯 md 存储模式值得重评。
- Trilium：**更正**——非死项目，是 fork（2025-06 归档）并回原名 TriliumNext/Trilium 的整合（v0.105.0 活跃）；仍因数据库形态落选。
- 叶：[Obsidian](obsidian/) adopt · [Logseq](logseq/) assess · [思源笔记 SiYuan](siyuan/) assess · [Trilium / TriliumNext](trilium-next/) assess

### D5 存量迁移：Outline 何去何从？

- 完整生命周期样本（详见其报告四幕）：2026-07 三条件选型（最火+AI 接入+好看）胜出 → 部署踩 9 坑（详单小天会话 53f490e3）→ 使用约一月 → 2026-08-25 弃用。弃用主因：排版硬伤 + 无 `[[` 式双链（只有文档跳转）补不上需求。
- 数据两路迁出：「技术设计」collection 08-23 经 lark-cli 迁飞书；个人知识 105 篇 08-25 迁入 taevasidian。
- 教学价值：选型矩阵全 ✅ 的胜者仍被生命周期淘汰——选型要看全生命周期，不止选型时刻。
- 落选节点：[Outline](outline/) hold（个人场景已废弃；云版免费档消失、$10/月起，团队 Wiki 场景仍合格）

## 终态与验证

taevasidian：272 篇、重名 0、孤儿链接 0、三通道备份；「notes as agent context」被第三方研究列为 2026 笔记赛道新轴线（Bear CLI+MCP、ZenNotes）——本方案提前踩中方向。竞品扫描：无值得新增的 AI 原生知识库（Reor 停更勿选、Memos 无双链、AFFiNE 数据库形态——观察名单）。
