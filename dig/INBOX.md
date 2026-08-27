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
Outline 已弃用,上述内容是否已迁 taevasidian 待查;未迁则从源对话恢复。
状态:pending

### [apprentice] 多项目 AI 上下文与隐藏关系管理 | 2026-07-29 | 8cefa2a2
原始提问:「单个项目很好管理……多个项目要一起开发,我该怎么管理?怎么让 AI 加载、又清楚各自的上下文?」「项目之间的关系、代码逻辑的关系,全是隐藏关系,不讲 AI 就不知道——除了这些还有哪些关系,全列出来」。
**待回读**:这是提问不是结论,须回读该会话结论段,结论成立且可验证才立课;与 pick/docs-code-linking 主题相邻,注意分工。
状态:pending

### [mistakes·素材] Outline 自托管 9 坑实录的下落 | 2026-07-30 | 53f490e3 + 4ac44e68
3.7MB 部署全程会话产出文章「Outline 本机自托管踩坑实录:9 个坑才跑通 Google 登录」,发布到 Outline wiki「部署踩坑」collection——**而 Outline 已于 08-25 弃用**(memory:存量/迁移留档)。
待查:文章是否已迁移到 taevasidian;若未迁,源对话 53f490e3 是恢复底稿。9 个坑若完好,可拆成 mistakes 条目素材。
状态:pending

### [维度] AI 技术科普问答(asked?) | 2026-08-03 | 48ed2ec8;+08-05/+08-06 证据
07-28 一键登录原理;08-05 端到端 AI 开发形态之问;08-06 数据库横评全景——用户问、AI 长文答、写进(已废弃的)Outline。
真空带:apprentice 收「怎么问」,mistakes 收摔跤,**「AI 给我讲过的技术课」没有馆收**。若立馆,门禁候选:须有出处对话+复述验证;且需先解决「发布地已死」问题(原发 Outline 全部沉没)。证据已 3 例,渐成型。
状态:pending

### [conversations] pick 起源对话待归档 | 2026-08-03 | 5af1327a + 7df267c2
「技术选型,最佳的技术报告该是什么样」(2.6MB)是 pick 的直接前身;同日 report 项目规则(索引文件/单向链接关联代码地址)是 pick「有理有据」体系的思想源头。
低优先:按 conversations 规则归档摘要,链接进 pick 的 README 或 DESIGN-TREE 作起源存证。
状态:pending

### [apprentice] SQLite db 文件安全迁移 | 2026-08-05 | e8b976d5
完整方法已在对话中走通:迁移前探测(lsof/ps 查占用、PRAGMA quick_check、WAL 0 字节确认一致未锁)→ 单进程完成传输+大小对比+一致性校验+耗时。
**待回读**:结论段补齐(什么情况下不能直拷、WAL 非零怎么办),可验证(校验步骤即验证)才立课。
状态:pending

### [pick/conversations] 数据库横评全景(沉没大件) | 2026-08-06 | e887ed25
「Postgres 横评,10 种数据库优先选哪些」→ AI 三梯队全景(基本盘 PG+Redis / 场景专家 Mongo+ES+CH / 领域极客 TiDB+Neo4j+InfluxDB)+ 追加四新赛道(向量/宽表/Serverless/嵌入式)+ 选型决策漏斗。用户评「写得非常好」,全文写入(已废弃的)Outline。
三重属性:①沉没清单最大件,可从源对话恢复;②pick/items/primary-database 类别的前身调研,**待查重**(pick 的 postgresql 条目 verdict 与此关系);③恢复后可拆成 pick 补充条目或 decision 素材。
状态:pending

### [apprentice/mistakes] 项目级 Z 漂移的自省 | 2026-08-20 | f804e142
原始表述:「我做这个的需求是什么。我现在光做,但是没产出,没有目的性的产出。」——同日还做了项目断舍离(13ff4727「哪些要的,哪些不要的」)。
这是 apprentice 首课「Z 三要素」的长期项目版:不是一次指令的 Z 不清,是项目的 Z 漂移——光做不问产出。**待回读**:该会话后续如何回应/修正;若走通出「定期自问产出」的方法,可立课或与 describe-the-goal 互链。
状态:pending

## 已决

(暂无)
