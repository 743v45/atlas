# pick · 项目设计树

> 本文件是项目自身的架构决策记录（design tree / ADR 性质）：每个节点 = 问题 → 选择 → 理由（含被否方案）。
> **同步规则（RULES.md 第 7 节）：任何架构级变更必须当日加节点——先改树再动手是推荐顺序。**

## 根问题

如何组织「技术选型」的知识，让每次选择有理有据、可追溯、可复用？

定位演进：~~工具报告库（tlrt = tool-report）~~ → **选型对比决策库（pick）**——对象不限于软件工具，表现形式、方案、任何「要从中挑一个」的东西都是条目；宽表、对比矩阵、决策矩阵是方法层。

## 架构决策

### D1 目录结构 — 索引 + 类别/条目两级

- 选择：`items/<类别>/<条目>/{meta.json, report.md}`，索引页聚合导航。
- 否决：单一大目录平铺（无类别语义）；数据库驱动（违背零依赖）。
- 背景：2026-08-27 立项，同日 `tools/` 更名 `items/`（定位泛化）。

### D2 元信息机制 — 脚本聚合，单一事实来源

- 选择：meta.json 是条目元信息唯一来源，`build-index.py` 聚合生成全部 HTML。
- 否决：索引内嵌 JSON 手动维护（必然漂移）；运行时 fetch（file:// 下被 CORS 拦）。

### D3 报告呈现 — md 唯一源 + 构建期渲染 HTML

- 选择：build 时渲染每份 report.md / comparison.md 为同名 HTML（面包屑 + 类别内上下篇导航），md 是源。
- 否决：保持裸 md（索引美、报告断崖）；运行时 JS 渲染（iframe/file:// 限制）；引入 mkdocs/docsify（破坏零依赖）。
- 渲染器为**零依赖手写 markdown 子集**（模板语法封闭集合，~120 行）。

### D4 数据管线 — stats 字段 + refresh 脚本

- 选择：meta.stats（source_repo/stars/pushed_at/license/collected_at）由 `refresh-stats.py` 从 gh 自动刷新；stale 判定基于 collected_at。
- 否决：数据散落正文手工维护（star 更新要改 3 处）；deck 自动同步数据（收益配不上复杂度——见 D9）。

### D5 数据时间规则 — 无时间戳视为无效（用户规则）

- 选择：所有数据显式标注观测时间（star 注采集日期、评测注评测方与年份、价格注查询日期）；正文 ⭐ 与 stats 一致性由 build 校验（warn）。
- 动机：undetected-chromedriver ⭐12.8k 已死、clawbrowser ⭐28 营销号、agent-browser 评测 12k 实际 41k——**star 是存量声誉，push 才是生命体征**。

### D6 索引形态 — 宽表（类别自定义维度列）

- 选择：每类别一张宽表：条目 | 结论 | <类别 columns 维度列> | star | push；`_meta.json.columns` 定义列，条目 `meta.matrix` 存值。
- 否决：卡片墙 + 三行 summary（信息密度低、无对比性）；「场景→名字」推荐表（用户明确否决：要属性对比）。
- 术语约定（用户）：宽表 = wide format；对比矩阵 = comparison/feature matrix；决策矩阵 = decision matrix。

### D7 决策矩阵 — decision.json 权重评分

- 选择：类别级 `{weights, scores}`（1-5），build 注入 `<!--gen:decision-matrix-->` 占位处；**强制注记**「矩阵只覆盖所列维度，维度外风险以 verdict 为准」。
- 否决：评分拍脑袋（映射口径必须写入 note，如 Apache=5/AGPL=3）。
- 分工语义：矩阵高分与谨慎 verdict 并存不是矛盾，是两层的分工（例：Camoufox 矩阵第一但 trial——断层史属维度外）。

### D8 展示规范 — dataviz 色板

- 选择：verdict 徽章 = status 色板（good/warning/neutral/critical）**色点 + 文字标签**（文字承载识别，永不只靠颜色）；边框 hairline 级；数字 tabular-nums；deck 条形图单 hue + 端点数值直标。
- 依据：dataviz skill 规范，颜色不靠眼睛估。

### D9 演示层 — Slidev 纪律化

- 选择：deck 放 `decks/<主题>/`，只链接报告不复制结论；**不自动生成**，规则要求引用数据带采集日期、meta 更新后人工核对。
- 否决：deck 数据页从 meta 生成（16 页里只有 2 页数据页，自动化收益低）。

### D10 设计树机制 — 两级树 + 门禁同步（本文件）

- 选择：项目级 DESIGN-TREE.md（架构决策）+ 类别级 decision-tree.md（选型路径）；**类别树叶子（`- 叶：[名](slug/) verdict`）由 build 校验与 meta 一致**——verdict 变更必须同步树。
- 否决：只有规则没有校验（必然漂移）。

### D11 协作模式 — 主题级 subagent 高强度调研

- 选择：每个选型主题派一个 general-purpose agent：读规则 → 挖历史会话 → gh/WebSearch 高强度调研 → 写全套（条目/横评/决策矩阵/设计树）；agent 禁跑 build（并行写 index 会互相覆盖），主会话统一重建。
- 教训：7 agent 并行撞账户 429 限流——错峰唤醒恢复；会话提取先行（db-picker/doc-picker）再派主题 agent 并把提取结果转发，效率最高。

### D12 知识参考类条目 — 双层结构（常用速查 + 全量图谱）

- 选择：「查一个」而非「选一个」的条目（标准 / 图谱 / 速查类）在单份报告内分层——『常用速查』在前（核心矩阵 + 速查规则代码块）、『全量图谱』在后；首个实践：typography/char-forms（16 类字符表现形式，四条差异轴收束）。
- 否决：拆成两个条目（全量必然包含常用 → 内容重叠 + 双头维护）；强制所有非工具条目双层（小体量知识条目负担过重）——进 RULES 第 3 节第 7 条，建议性措辞（2026-08-27 与 owner 确认）。

### D12 域聚合层 — 三层结构（用户反馈）

- 选择：根级 `domains.json` 定义域（虚拟层，不动 items/ 目录）；顶层索引只列域（短页），每域一页 `domains/<slug>.html` 装类别宽表；报告/横评面包屑加域层。
- 否决：74 条铺单页（用户明确反馈太长）；物理目录重组 `domains/<域>/<类别>/`（74 条目路径全变、树与横评链接全断，成本不成比例）。
- 校验：类别必须归属域、域不得引用未知类别（build 门禁）。
- 动机：浏览器×2、知识库+文档本就是姊妹主题——关联紧密的类别在域层聚合，天干编号随之上移到域。

### D13 膨胀支持 — 预案先于需要（用户指令）

- 选择：**先支持再膨胀**——① 界（kingdoms）机制就绪（domains.json 声明即启用，索引按界分组，校验强制域归属唯一界）；② 膨胀预警门禁（类别 >30 条 warn 并系拆分、域 >9 个 warn 启用界）；③ 顶层全站搜索（内嵌条目级轻量索引，即时建议直跳，千条仅几十 KB）；④ refresh-stats 并发 8 线程（49 项 6 秒，原串行分钟级）。
- 否决：等触发条件出现再加（用户明确：项目一定会膨胀，先支持上就对了）。
- 附带：新增 info-architecture 类别——「信息组织方案」本身成为被 pick 的对象（浅三层 adopt、扁平多面/深分类学树 assess、网络图 trial），pick 用自己选出了自己的结构。

### D14 原始数据留档 — raw/ 采集即存档（用户规则）

- 选择：`raw/<日期>/{gh,web,sessions}/` 三通道留档；**机制化**——refresh-stats.py 每次 gh 调用自动落盘完整 API 响应（不靠自觉）；web/sessions 靠规则（subagent prompt 必备条款）。
- 否决：只存提炼后的 meta（原始丢失后不可复核、不可二次加工）；事后补采（star 会变、网页会消失、会话会被清理——原始数据是一次性资产）。
- 红利：跨日目录 = star/push 时间序列；报告可引用 raw/ 路径作可复核出处。
