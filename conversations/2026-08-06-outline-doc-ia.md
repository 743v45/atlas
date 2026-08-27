---
date: 2026-08-06
topic: 文档库信息架构:collection 还是层级
related:
  - ../asked/items/doc-library-information-architecture/
原始会话: ~/.claude/projects/-Users-taevas/666c3f48-2551-49df-ba92-d4e8faadc4ec.jsonl
---

# 2026-08-06 · 文档库信息架构:collection 还是层级

会话从 /outline 发布一篇 X 文章转写(AGENTS.md 八条规则,烧 60B tokens 的总结)开始。用户想把文章挂进新 collection「AI 编程实践」下的「提示词优化」分组,发现 Outline 的 collection 不能嵌套——**层级只能靠父文档→子文档实现**,由此引出给 outline skill 补层级能力的需求。中途实打实踩了一串坑:skill 用 urllib 在自签 Outline(Caddy) 上偶发 IncompleteRead,curl 实测服务端响应完整(5314B 全到)而 urllib 读到 390B 就误判 EOF,且请求其实已生效(父文档第一次报错但其实建好了);按流程脚本化规则整条链改 curl 驱动、带判重复用+重试+计时,并记入 memory。

关键转折:brainstorming 澄清三点——① CLI 用「路径 + 自动建中间节点」(--parent 支持标题/路径查找,--mkpath 显式才建)② 底层换 curl ③ 组织建议写成完整 IA 方法论。核心判断在此定稿:**进 collection 的判据是独立知识域/跨主题复用/权限可见性边界(顶层容器,创建有成本);同域细分用文档层级(建分组成本低,就是个父文档,可重组)**。深度口径以「级=含 collection 的总深度」:2 级平铺(同域 <7 篇松散笔记)、3 级 collection→分类→文章(默认推荐、知识库甜点,也是本篇的结构)、4 级封顶再深该拆 collection。何时重组:某层子项 >10 或出现「杂项」兜底桶→拆分组;层级 <2 且同 collection 文档 >15→开一层;collection >50 篇→拆两个。命名:collection 简短名词、父文档表分类名、叶子标题不重复上层路径。判据最终落盘 skill 的 SKILL.md「文档组织建议(信息架构)」一节并随 skill 发布。

后记:载体 Outline 已于 2026-08-25 弃用迁飞书,但判据本身通用,沉淀为 asked/items/doc-library-information-architecture。
