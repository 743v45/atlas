# dig/INBOX — 候选收件箱

dig 翻阅产出中一切**等用户定夺**的候选:新维度候选(建馆/视图/收编)与馆级内容候选(课/错题/报告)。

**标记规则**(用户动手,只改「状态」行):

- `pending` → `promoted:<去向>`——转正,附一句它变成了什么(建了馆/入了哪馆哪条)
- `pending` → `dismissed:<理由>`——清理,附一句否决理由

promoted / dismissed 的条目移入「已决」区保留一行,**不删**——落选留理由,防的是以后重复提案再兴奋一遍(与 spark 的尸体规则、决策树的落选节点同构)。

AI 的边界(dig/RULES §3):spark 级可直接代录入苗圃;**凡进本收件箱的,定夺权全在用户**——收录即定案,门禁归人。

---

## 待审

### [pick] Sourcetree 替代品选型调研 | 2026-07-28 | 5b13ef50
「Sourcetree 一样的软件有哪些,最好用的是哪个。以及价格」——git GUI 客户端对比。
**待查重**:pick/items/git-gui-clients 类别已存在,可能是同期同一调研的产物;若已覆盖则 dismissed:重复。
状态:pending

### [mistakes] CLI 安装败于环境版本 | 2026-07-28 | ea55b84e
Tavily CLI 安装报错 "Python 3.10+ is required" → 同日转去装 pyenv 3.12/3.13。
根因候选:「装工具前没查依赖环境」。边缘案例,价值低——是否值得立错题,用户定。
状态:pending

### [维度] 环境与装机(setup) | 2026-07-28 起 | 3 天 6+ 例
pyenv 版本、zsh 插件缺失、CLI 依赖报错、API login 403(07-28);远程机 Go 版本损坏(08-05);tsx not found + node_modules 缺失(08-06);另 multica 跨机迁移部署(08-06)。
证据持续累积(本地+远程)。若有独立生命周期+门禁(机器配置清单?还原脚本?)才配建馆,否则 spark 念头即可。
状态:pending

### [conversations] Outline 沉没内容清单 | 07-30 起 | 待查
- 07-30:「Outline 自托管 9 坑实录」(53f490e3 底稿可恢复)
- 08-05:「端到端是 AI 开发终极形态吗」(a5699e87)
- 08-06:**数据库横评全景,最大件**(e887ed25)
- 08-04:Apple Liquid Glass 全套文档中译副本(cc58980a 采集)——**源在 report/projects/apple-liquid-glass/md/,损失小**,仅 Outline 副本沉没
- 08-05:SQLite WAL 机制详解(e8b976d5,含备份红线)
Outline 已弃用,上述内容是否已迁 taevasidian 待查;未迁则从源对话恢复。
状态:pending

### [apprentice] 多项目 AI 上下文与隐藏关系管理(tacit) | 2026-07-29 | 8cefa2a2 ✅已回读
提问「多个项目 AI 怎么加载、隐藏关系怎么讲」→ 当场演进为设计并实现 **tacit 插件**(taevas-plugins):默会知识显式化——`.tacit/` 登记跨文件约束(改 A 必改 B/不变量/红线/why),hook 编辑时自动注入提醒,`/tacit init|add|audit`。命名取自 Polanyi「我们能知道的,远多于我们能说出来的」,与 implicit-coupling、强制优于记忆同脉。
**方法已走通,artifact 已存在**(tacit 插件),验证方式=端到端测试+真实项目实测注入。立课条件齐备,artifacts 指向插件目录即可——等用户 promoted。
状态:pending

### [mistakes·素材] Outline 自托管 9 坑实录的下落 | 2026-07-30 | 53f490e3 + 4ac44e68
3.7MB 部署全程会话产出文章「Outline 本机自托管踩坑实录:9 个坑才跑通 Google 登录」,发布到 Outline wiki「部署踩坑」collection——**而 Outline 已于 08-25 弃用**(memory:存量/迁移留档)。
待查:文章是否已迁移到 taevasidian;若未迁,源对话 53f490e3 是恢复底稿。9 个坑若完好,可拆成 mistakes 条目素材。
状态:pending

### [维度] AI 技术科普问答(asked?) | 2026-08-03 起 | 6 例
一键登录原理(07-28);端到端 AI 开发形态(08-05);数据库横评全景(08-06);类型系统/形式化验证(08-04);**如何积累审美、临摹就忘(08-25 2c395067);双向链接 wiki 选型追问(08-25 be457b46);gherkin 验收测试(08-25 f9c829d3)**。
注意:后三例已从「技术原理」扩展到「学习方法/方法论之问」——asked 的真实边界可能是「我问、AI 长答、值得留存的一切」。若立馆,门禁候选:出处对话+复述验证;且需先解决发布地长存问题(atlas 即答案)。
状态:pending

### [conversations] pick 起源对话待归档 | 2026-08-03 | 5af1327a + 7df267c2;+08-21
「技术选型,最佳的技术报告该是什么样」(2.6MB)是 pick 的直接前身;同日 report 项目规则(索引文件/单向链接关联代码地址)是 pick「有理有据」体系的思想源头。
**+08-21**:knowledge-base 类别起源「个人知识库,和 ai 共建,用什么工具管理」(99faa8a0, 3MB)。
低优先:按 conversations 规则归档摘要,链接进 pick 的 README 或 DESIGN-TREE 作起源存证。
状态:pending

### [apprentice] SQLite db 文件安全迁移 + WAL 红线 | 2026-08-05 | e8b976d5 ✅已回读
完整方法已走通并验证:迁移前探测(lsof/ps 查占用、PRAGMA quick_check、WAL 0 字节确认一致未锁)→ 单进程传输+大小对比+一致性校验+耗时。
回读补充**两条红线**:WAL 为 0 字节才可单独拷 `.db`;非空 `-wal` 绝不能丢下。同会话还产出了「SQLite WAL 机制详解」自洽长文(checkpoint/崩溃恢复/与 rollback journal 对比)——沉于 Outline,可恢复。立课素材齐备。
状态:pending

### [pick/conversations] 数据库横评全景(沉没大件) | 2026-08-06 | e887ed25
「Postgres 横评,10 种数据库优先选哪些」→ AI 三梯队全景(基本盘 PG+Redis / 场景专家 Mongo+ES+CH / 领域极客 TiDB+Neo4j+InfluxDB)+ 追加四新赛道(向量/宽表/Serverless/嵌入式)+ 选型决策漏斗。用户评「写得非常好」,全文写入(已废弃的)Outline。
三重属性:①沉没清单最大件,可从源对话恢复;②pick/items/primary-database 类别的前身调研,**待查重**(pick 的 postgresql 条目 verdict 与此关系);③恢复后可拆成 pick 补充条目或 decision 素材。
状态:pending

### [mistakes] 项目级 Z 漂移:「光做没产出」 | 2026-08-20 | f804e142 ✅已回读
原始表述:「我做这个的需求是什么。我现在光做,但是没产出,没有目的性的产出。」
回读结论:自省当场转化为修正——同会话后半以 TDD 交付 `export bundle` 消费端闭环(5 任务 5 commit、243/243 测试绿、真库冒烟命中 3136 视频、面试题场景实测),收尾即「真正的产出时刻」。
**建议形态:mistakes 条目**(经过=光做没产出;根因=项目 Z 漂移,做了大量采集基建却无消费端;修正=自问产出→立即转向消费端闭环)。素材齐全,等用户定夺。
状态:pending

### [apprentice] 批量文档翻译流水线 | 2026-08-04 | 17959ecc 等 10 会话 ✅已回读
Apple Liquid Glass 官方文档全套中译走通的模式:**一篇文档一个会话** + 标准化翻译 prompt + goal 挂机采集前置。模板已定型(首轮抽取即见结构完全一致):
```
读取:md/<slug>.md → 写出:md/<slug>.zh.md
这是什么(一句话) + 翻译要求:
- 术语映射表(Material→材质/vibrancy→虚化…每篇定制)
- 保持不变:> 来源区块 / ```代码块 / API·类型名 / URL / markdown 结构
```
**立课就绪,亦可直接固化成 skill**(固化光谱的公路档)。
状态:pending

### [pick] prd-tools 调研查重 | 2026-08-26 | d77eeed3
「prd 最佳工具」(grilling 逼问式)——pick/items/prd-tools 类别已存在,待查重是否同源;同源则 dismissed:重复。
状态:pending

### [维度/方法论] AI 原生数据访问(CLI for AI) | 2026-08-11 起 | 跨项目四现
「有没有 cli 查询数据的功能。希望做一个 cli 给 ai 查询使用」(lucent 08-11);subtitle-collector 的 collector-cli+SKILL.md;pick/knowledge-base 核心命题「AI 对存储层的原生访问权」;**08-25 第四现**:「cli 收集 b 站近半年 ai 面试题内容。没法用 cli 的话,需要实现功能的」(08ac9a07)——以「AI 能否直接用」为功能开发的准入标准。
贯穿四个项目的设计哲学。四现=立课时机成熟,建议用户考虑立 apprentice 课或并入 PHILoSOPHY。
状态:pending

### [mistakes] virtiofs 宿主机直读 SQLite 损库 | 2026-08-24 翻车 | ✅已定位
**经过**:2026-08-24 两次 SQLITE_CORRUPT——旧 bind mount 走 virtiofs,宿主机进程直触挂载库(哪怕只读)引发 mmap 一致性损坏。
**根因**:macOS Docker 的 virtiofs 与 SQLite mmap 不兼容,「只读无害」假设错误。
**修正(已产物化)**:迁 named volume 根除路径;docker-compose 文件头红线注释;备份四层化(15min RPO,VACUUM INTO 滚动)+ verify-deployed 自检 + sqlite-rescue 工具。
原始会话 76ec3aae(08-24,在 dig-0824 队覆盖内)。**素材完整,立条就绪**。
状态:pending

### [apprentice] 调查/审计驱动的开发工作流 | 2026-08-21/25/26 | 三日多处
家族模式:动手前先派只读调查摸清现状——08-21 四视角审计+P0-P3 分批 TDD 修复(deepseek-harness 目录 8 会话);08-25 平台维度四层调查(server/web/CLI/扩展各一会话)+开发者前置调查(存量回填 CLI 先例);08-26 CLI 完整度审计+ASR 设计前置。
共同结构:**只读调查(带 file:line 引用的事实清单)→ 确认问题/设计 → 分批实现(TDD)**。强候选,「CLI for AI」是该工作流的接口层。待回读定型。
状态:pending

## 已决

(暂无)
