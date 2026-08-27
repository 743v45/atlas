# dig/INBOX — 候选收件箱

dig 翻阅产出中一切**等用户定夺**的候选:新维度候选(建馆/视图/收编)与馆级内容候选(课/错题/报告)。

**标记规则**(用户动手,只改「状态」行):

- `pending` → `promoted:<去向>`——转正,附一句它变成了什么(建了馆/入了哪馆哪条)
- `pending` → `dismissed:<理由>`——清理,附一句否决理由

promoted / dismissed 的条目移入「已决」区保留一行,**不删**——落选留理由,防的是以后重复提案再兴奋一遍(与 spark 的尸体规则、决策树的落选节点同构)。

AI 的边界(dig/RULES §3):spark 级可直接代录入苗圃;**凡进本收件箱的,定夺权全在用户**——收录即定案,门禁归人。

---

## 待审


### [mistakes] CLI 安装败于环境版本 | 2026-07-28 | ea55b84e
Tavily CLI 安装报错 "Python 3.10+ is required" → 同日转去装 pyenv 3.12/3.13。
根因候选:「装工具前没查依赖环境」。边缘案例,价值低——是否值得立错题,用户定。
状态:pending

### [维度] 环境与装机(setup) | 2026-07-28 起 | 3 天 6+ 例
pyenv 版本、zsh 插件缺失、CLI 依赖报错、API login 403(07-28);远程机 Go 版本损坏(08-05);tsx not found + node_modules 缺失(08-06);另 multica 跨机迁移部署(08-06)。
证据持续累积(本地+远程)。若有独立生命周期+门禁(机器配置清单?还原脚本?)才配建馆,否则 spark 念头即可。
状态:pending

### [conversations] Outline 沉没内容清单 | 07-30 起 | ✅去向已明:迁往飞书
**08-23 已执行「outline 数据全部导入飞书,用 lark-cli」**(0e78d1c6)——弃用 Outline 时的数据迁移实际去向是飞书,非 taevasidian。
- 07-30:「Outline 自托管 9 坑实录」
- 08-05:「端到端是 AI 开发终极形态吗」;SQLite WAL 机制详解
- 08-06:**数据库横评全景,最大件**
- 08-04:Apple Liquid Glass 中译副本(源在 report 项目,损失小)
后续:在飞书侧核对上述件是否完整迁达。**08-27 已从源对话恢复 3 件入 asked**(数据库全景/WAL 详解/一键登录);端到端与九坑实录仍待恢复。
状态:pending

### [apprentice] 多项目 AI 上下文与隐藏关系管理(tacit) | 2026-07-29 | 8cefa2a2 ✅已回读
提问「多个项目 AI 怎么加载、隐藏关系怎么讲」→ 当场演进为设计并实现 **tacit 插件**(taevas-plugins):默会知识显式化——`.tacit/` 登记跨文件约束(改 A 必改 B/不变量/红线/why),hook 编辑时自动注入提醒,`/tacit init|add|audit`。命名取自 Polanyi「我们能知道的,远多于我们能说出来的」,与 implicit-coupling、强制优于记忆同脉。
**方法已走通,artifact 已存在**(tacit 插件),验证方式=端到端测试+真实项目实测注入。立课条件齐备,artifacts 指向插件目录即可——等用户 promoted。
状态:pending

### [mistakes·素材] Outline 自托管 9 坑实录的下落 | 2026-07-30 | 53f490e3 + 4ac44e68
3.7MB 部署全程会话产出文章「Outline 本机自托管踩坑实录:9 个坑才跑通 Google 登录」,发布到 Outline wiki「部署踩坑」collection——**而 Outline 已于 08-25 弃用**(memory:存量/迁移留档)。
后续:文章应已随 08-23「outline 数据全部导入飞书」落地飞书(见上条,非 taevasidian);在飞书侧核对是否完整迁达,若未达,源对话 53f490e3 是恢复底稿。9 个坑若完好,可拆成 mistakes 条目素材。
状态:pending


### [conversations] pick 起源对话待归档 | 2026-08-03 | 5af1327a + 7df267c2;+08-21
「技术选型,最佳的技术报告该是什么样」(2.6MB)是 pick 的直接前身;同日 report 项目规则(索引文件/单向链接关联代码地址)是 pick「有理有据」体系的思想源头。
**+08-21**:knowledge-base 类别起源(99faa8a0);**+08-24**:asr-subtitle-tools 起源「有没有好用的识别视频音频的字幕,免费的,或者本地能部署的」(fce485e7);**同日 apprentice 前身之问**:「教教我,这个项目怎么写。怎么设计出来,设计哲学。出一份教程,顺序教学」(3475e2c2→e8f845e1 调研一手材料)。
低优先:按 conversations 规则归档摘要,链接进 pick 的 README 或 DESIGN-TREE 作起源存证。
状态:pending

### [apprentice] SQLite db 文件安全迁移 + WAL 红线 | 2026-08-05 | e8b976d5 ✅已回读
完整方法已走通并验证:迁移前探测(lsof/ps 查占用、PRAGMA quick_check、WAL 0 字节确认一致未锁)→ 单进程传输+大小对比+一致性校验+耗时。
回读补充**两条红线**:WAL 为 0 字节才可单独拷 `.db`;非空 `-wal` 绝不能丢下。同会话还产出了「SQLite WAL 机制详解」自洽长文(checkpoint/崩溃恢复/与 rollback journal 对比)——沉于 Outline,可恢复。立课素材齐备。
状态:pending


### [mistakes] 项目级 Z 漂移:「光做没产出」 | 2026-08-20 | f804e142 ✅已回读
原始表述:「我做这个的需求是什么。我现在光做,但是没产出,没有目的性的产出。」
回读结论:自省当场转化为修正——同会话后半以 TDD 交付 `export bundle` 消费端闭环(5 任务 5 commit、243/243 测试绿、真库冒烟命中 3136 视频、面试题场景实测),收尾即「真正的产出时刻」。
**建议形态:mistakes 条目**(经过=光做没产出;根因=项目 Z 漂移,做了大量采集基建却无消费端;修正=自问产出→立即转向消费端闭环)。素材齐全,等用户定夺。
状态:pending

### [apprentice] 批量文档翻译流水线 | 2026-08-04 | 17959ecc 等 10 会话 ✅已回读
Apple Liquid Glass 官方文档全套中译走通的模式:**一篇文档一个会话** + 标准化翻译 prompt + goal 挂机采集前置。**08-24 最大规模实例:mattpocock-skills 整仓中译,85+ 文件编队(「一次一个 subagent 只翻译一个文件」,指挥会话 448387f6)**。模板已定型:
```
读取:md/<slug>.md → 写出:md/<slug>.zh.md
这是什么(一句话) + 翻译要求:
- 术语映射表(Material→材质/vibrancy→虚化…每篇定制)
- 保持不变:> 来源区块 / ```代码块 / API·类型名 / URL / markdown 结构
```
**立课就绪,亦可直接固化成 skill**(固化光谱的公路档)。
状态:pending


### [维度/方法论] AI 原生数据访问(CLI for AI) | 2026-08-11 起 | 跨项目六现
「有没有 cli 查询数据的功能。希望做一个 cli 给 ai 查询使用」(lucent 08-11);subtitle-collector 的 collector-cli+SKILL.md;pick/knowledge-base 核心命题「AI 对存储层的原生访问权」;08-25「没法用 cli 的话,需要实现功能的」;**08-27 第五现**:「subtitle-collector 需要 skill 做这个事情,方便我调度」(e3533f06);**08-24 第六现**:「增加手动翻译功能…留给大模型使用。cli 化」(325c89be)——给 AI 的接口持续升维(CLI→skill→功能准入)。
贯穿五个项目。六现=超成熟,建议直接立课或写入 PHILLOSOPHY(与「图纸与公路」互链)。
状态:pending

### [mistakes] virtiofs 宿主机直读 SQLite 损库 | 2026-08-24 翻车 | ✅已定位
**经过**:2026-08-24 两次 SQLITE_CORRUPT——旧 bind mount 走 virtiofs,宿主机进程直触挂载库(哪怕只读)引发 mmap 一致性损坏。
**根因**:macOS Docker 的 virtiofs 与 SQLite mmap 不兼容,「只读无害」假设错误。
**修正(已产物化)**:迁 named volume 根除路径;docker-compose 文件头红线注释;备份四层化(15min RPO,VACUUM INTO 滚动)+ verify-deployed 自检 + sqlite-rescue 工具。
原始会话 76ec3aae(08-24,在 dig-0824 队覆盖内)。**素材完整,立条就绪**。
状态:pending

### [apprentice] 调查/审计驱动的开发工作流 | 2026-08-21/22/25/26 | 四日多处 ✅已回读(模板已存证)
家族模式:动手前先派只读调查摸清现状——08-21 四视角审计+P0-P3 分批 TDD 修复;08-22 **审-修流水线日常化**(审查员基于 git diff「找真实 bug 不是风格意见」→ 修复会话逐条 [S1/medium] 精确修)+ **adversarial 拷问者**(对抗审视架构政策一致性/产品路线决策,只读);08-25 平台维度四层调查+前置调查;08-26 CLI 完计度审计+ASR 设计前置。
审查 prompt 模板(79f2c8f8 原文,可直接固化 skill):
```
审查 <路径> 的「<视角>」设计,找设计不合理之处。只读代码、报告发现,不修改任何文件。
## 项目背景(架构速览,一段)
## 审查视角(N 条:职责划分/数据流/单点假设/故障恢复…)
## 输出格式(按严重度排序:标题/文件:行号/为什么不合理——具体后果,不要泛泛/建议方向一句)
约束:只报核实过的;附「已检查无问题」清单;≤12 项,宁缺毋滥
```
**立课就绪**:三段式(审计→分级→TDD 分批修复)+模板+验证方式(测试)俱全。与「并行编队」(08-23)互为姊妹。
状态:pending

### [apprentice] 「降级凑合为失败」:工具降级的表达课 | 2026-08-27 | 82106df1 ✅素材完整
原始三问:「没指定 playwright 且没安装,让 AI 访问网站,结果只会用 curl,效果不好——我该怎么表达,能让 AI 先来一层元思考?」「降级凑合为失败。那我应该补充『不降级凑合』就行了对吧?」「那我该怎么表达,又很方便的,没提到标准,然后 AI 自动会不选择 curl 呢?」
**这是 Z 三要素的姊妹课**:表达里隐含的质量底线——AI 会自作主张降级工具(curl 替 playwright),纠法不是罗列标准,而是给出「不降级凑合」这类否决性原则+触发元思考。对话三问三答结构完整,立课素材即成。
状态:pending

### [apprentice] 并行 agent 编队作战 | 2026-08-23 | 当日 30+ 会话 ✅样本完整
ds-phoneness 原生 App 会战 + subtitle-collector 测试质量会战,模式定型:
- **文件级隔离分工**:每个 agent 限一两个文件,「禁止动其它文件,并发同事在写别的文件,统一由主线集成构建」
- **多视角审查编队**:标准审查/规格符合性/对抗性(correctness·robustness·security)并行
- **轮次制验收**:「第 5 轮验收:对抗复核这批修复本身有没有引入新缺陷或修错」——复核修复,不是复核原始代码
与「调查/审计驱动工作流」(08-21)互为姊妹:那个串行深挖,这个并行分治。立课素材齐备。
状态:pending

### [pick] 31 条 meta.sources 为不可解析文本引用 | 2026-08-27 | 审查发现
pick 门禁承诺「有据可溯」,但全库 78 条中 31 条的 meta.sources 存在既非 URL 亦非 raw/ 实路径的纯文本引用(如「Claude 历史会话(2026-08-25)——提取源」)——可溯性承诺未兑现,需重新溯源为 URL 或实路径(raw/ 留档)。
状态:pending

## 已决

- [维度] asked(08-27)→ promoted:建馆 atlas/asked(五馆齐);首批 4 篇恢复入库:两种雾/数据库全景/WAL/一键登录;其余 4-5 例(类型系统/审美/gherkin/双向链接/AI 深度幻觉)待回读源对话后补录

- [pick] Sourcetree 选型调研(07-28)→ dismissed:重复——pick/git-gui-clients 已 9 条目含 sourcetree(trial),调研成果已被完整覆盖(2026-08-27 查重)
- [pick] prd-tools 调研(08-26)→ dismissed:重复——pick/prd-tools 已 7 条目(chatprd/claude/feishu/kiro/notion-ai/productboard/spec-kit)(2026-08-27 查重)
- [pick] 数据库横评全景(08-06)→ dismissed:重复——pick/primary-database 已 8 条目,PG/SQLite 双 adopt,三梯队结论已入库;**全景综述原文仍是 asked 沉没件**(见沉没清单)(2026-08-27 查重)
