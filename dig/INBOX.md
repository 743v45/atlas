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

---

## 待审 · 本机 MacBook Air 批(2026-08-27 dig,15 会话日 194 文件)

> 本批全部来自 MacBook Air 本机存量(与小天 progress 记录分机器统计,互不覆盖)。以下均为新立条;既有条目的本机新证据见本批末尾「+N 例汇总」。

### [mistakes] fud3 集群编号被误当 k8s DNS 域后缀(连环两日) | 2026-08-17/18 | 94e8bf7d + ef20cf99(本机)
grpc 报 `Name resolution failed for target dns:order.holdcloud-backend.svc.cluster.fud3:8443`;同输入对比:长后缀 ENOTFOUND、短后缀 `.svc` 解析 192.168.70.158。根因:集群真实 DNS 域是 `cluster.local`(resolv.conf search 列表可证),fud3/fud4 只是内部集群编号被误写进配置。修正:统一改短形式 `shinichi.holdcloud-backend.svc:8443`。**用户当时坚信错误结论的原话**:「为什么要改成 cluster.local。明明应该是 fud3」。三段俱全+验证,**立条就绪**。
状态:pending

### [mistakes] whisper 逐词时间戳必崩:模型仓库变体选错 | 2026-08-06/07 | 2801380a(本机)
原文「Model outputs must contain cross attentions to extract timestamps...not exported with output_attentions=True」。根因:transformers.js 逐词路径要求 `_timestamped` 变体模型仓库,turbo 用的无后缀仓库不带 cross-attentions,一开逐词即 crash。修正:turbo 禁逐词开关 + 全模型 try/catch 自动降级逐句带警告。
状态:pending

### [mistakes] urllib 自签 HTTPS 长响应截断(已固化) | 2026-08-05→07 | b0872007→666c3f48→9e00e9e0(本机)
outline skill 的 `resp.read()` 在自签 HTTPS 上 ~15KB 即 IncompleteRead;修=`_request` 原地换 curl(subprocess,-sk+双重重试),签名不变全调用者受益。**翻车→修 skill→新会话用新 API 发布成功 704ms,三段链完整且修正已固化进 taevas-plugins outline skill,可直录**。
状态:pending

### [mistakes] 纸面样板冒充生产经验 | 2026-08-07 | c002eaf1(本机)
xiaopacai 的「全套 K8s/Helm/Prometheus」是从未跑过的纸面样板:三套互相矛盾 CD 管线、`*.example.com`、`wc -h<<EOF` typo、PM2 与 k8s 并存。「读过模板=会生产运维」是误导学习方向的最危险幻觉;修正=学习路线图阶段 3 专破(跑通一次真部署)。
状态:pending

### [mistakes] E2E 绿灯掩盖配置缺失 | 2026-07-27→30 | 5086a366(本机)
原文「No entry point found for electron app, please add a "main" field」。根因:E2E 用 `electron out/main/main.js` 直接指定入口**绕过了** package.json main 字段,而 `electron-vite dev` 走 main 字段——验收路径与真实启动路径不一致,测试全过但 dev 起不来。通用根因:**测试通过 ≠ 能跑,当测试路径绕过配置时**。
状态:pending

### [mistakes] CLI 凭据采集无验证闭环 | 2026-07-28 | 41f4fc3f(本机)
原文:「你不验证一下吗。我随便填写的。账号密码。」——随手填 "123" 也提示「已保存网关 cookie」。修正=login 即打真实接口验证+密码隐藏输入,后续已落地。
状态:pending

### [mistakes] subagent 长报告回传截断只剩尾句 | 2026-07-28 | a14286de(本机)
coordinator 原话:「你的审查完成了,但返回的内容只剩最后一句(--force 无效)。请输出完整的 final review 报告」——final review 险些以一句残片收场。根因方向:subagent 回传通道对长输出有截断,长报告应落盘文件+回传路径而非全靠 final text。
状态:pending

### [mistakes] task 级 gate 拦不住全局 lint 溃败 | 2026-07-28 | 41f4fc3f(本机)
原文「lint 全是问题。修复」——28 agent 各过各的 task gate,合并后 lint 全挂。根因:**全局质量门禁须独立于分发单元**,分片各自达标≠整体达标。
状态:pending

### [mistakes] 小件三则 · 本机合计立一条或并入相关条均可 | 2026-07-28/08-03/08-05 | 41f4fc3f 等
①commander required option 报错输出两遍+确认清单 `#undefined`(41f4fc3f,07-28);②kubectl -n 误传 workload 路径 `deploy/holdon`(bcbd5d97,08-03);③AI 凭印象断言 Surge 配置「语法对」被打脸,认错原话「这次我查官方文档确认准确写法,不猜了」(c03ea2ba,08-05——AI 的错非用户的错,收否由用户定)。
状态:pending

### [apprentice·大案例] holdon 支付链调查→对账系统会战 | 2026-08-03 | 22c19544(本机,4 小时一会话)
完整链:问句「有没有主动处理支付完成的方式」→ Explore 结论「100% 依赖 Webhook、无补偿对账、QueryOrder 定义了从未被调用」→ brainstorming →「A,B,C 都做」→ 13 subagent 按 G1-G4 编队实施(DAO/对账脚本/回调改造/测试)→「会不会重复充值」幂等追问 → 最小上线三步清单;对账形态拍板「不要接口,用脚本」。**调查→设计→编队实施→上线清单完整链,建议以案例形态收编**(与「调查驱动」「并行编队」两候选互为表里)。
状态:pending

### [apprentice] CLI 鉴权幂等状态机 | 2026-07-28 | 41f4fc3f(本机)
用户口述设计原文:「gwsupyun 先认证的吧。认证完,就可以记录进配置,每次 auth 看看配置里的可不可用,可用就没必要再配置,除非 force 更新,如果账号已经登录,也没必要再登录,除非 logout,每一步确认鉴权通过」——落地 feature/auth-idempotent 分支并合 develop;配套「配置不存密码存 cookie + salt」「状态码必展示 + 401 关联登录提醒 + 增删改二次确认」三则 UX/安全决策。
状态:pending

### [apprentice] 零指令纯日志投喂排障 | 2026-08-03 | fbcada82(本机)
用户只贴一段生产日志、不说一个字,systematic-debugging 驱动 AI 自主走完证据收集→三层根因(TradeQuery 诊断字段全丢弃/IsSuccess 是「API 调用成功」非「支付成功」/回调 500 触发重试且已付款单不入账),根因落 recharge.go:171-173 可验证,收尾「涉及生产资金代码,需要你拍板」。可验证(文件行号在案)。
状态:pending

### [apprentice] 多 agent 并发产长文档库 | 2026-08-06 | b0872007(本机)
11 agents(10 独立定位报告+1 汇总索引)统一结构、每 agent 直写 Outline 回传真实 URL,**5 分 45 秒 11/11 零失败**;验证=URL 回传+curl 探路由 200。与编队条目互证,此条的独立价值=「回传真实 URL 自验证」闭环。
状态:pending

### [apprentice] UI 像素级复刻验证法 | 2026-08-04/05 | d4e72e2c(本机)
逐元素 computed style 坐标/尺寸对照表(官方 vs 复刻,`24,22/104×20 ✓完全一致` 式逐项核对);两根因可复用:覆盖组件只复制 HTML 漏默认 `<style>` 的 @media 布局→塌陷;字号误用首页大字号。验证方式=对照表本身(同输入对比)。
状态:pending

### [apprentice] k8s 容器内 DNS 排障三步法 + exec 前先探可用工具 | 2026-08-17 | 94e8bf7d(本机)
第 0 步:报错栈是 node 不代表容器有 node(`exec: "node": executable file not found` 后先探 nslookup/getent/nc 再 exec);① 查容器 resolv.conf 的 search 列表定集群真实域;② 同名多后缀对比查询一次性证伪。验证=三种查询对照表。
状态:pending

### [apprentice] 「教我怎么做,不要替我操作」:生产集群人机分工边界 | 2026-08-18 | ef20cf99(本机)
同会话两现原话:「你别主动给我改。我自己来改」「遇到域名解析问题…怎么排查(不要替我操作)」——生产环境里 AI 只排查讲解、用户亲手执行。与全局「只读纪律」及 spark「只读约束前置声明」同构,可立课或升 CLAUDE 规则。
状态:pending

### [apprentice] 任务描述收敛法 | 2026-08-26 | 9e446262(本机)
「怎么描述专业点、收敛点」四要点:「做个 demo」→最小可运行示例+验收命令=停机条件;「子目录」→直接给目录名;动词不明→明确 append 到 CLAUDE.md;两事混一句→拆任务。核心一句**「每条诉求都补上『做到什么算完』」**;同日 1a161a0b 用收敛后描述实跑通 Quartz demo,验证在案。与 describe-the-goal/先复述再执行同族,合并与否由用户定。
状态:pending

### [apprentice] 外部工具配额耗尽降级链(收编:0804-05 队新维度提案) | 2026-08-05 | 4e92d911 + c03ea2ba(本机)
WebSearch 周配额耗尽 → WebFetch 被网络策略挡 → webReader MCP 429 → 最后退到本机确定性路径(直接抓原文);AI 每次主动换通道并同步「查到/没查到」。两例同日同根因,形态是工具降级预案(单课),不建馆。
状态:pending

### [asked] 类型系统与形式化验证讲义 | 2026-08-04 | 19315383(本机)
完整自洽讲义:静态/动态×强/弱、soundness、safety/liveness、模型检测 vs 定理证明(工具对照)、Curry–Howard 同构、保证强度谱系图。**正是已决区 asked 建馆条「待回读补录」的类型系统源头**;用户令「写进 outline,你可以丰富一下」后会话止于等 API token——讲义沉在对话里,恢复即可入库。
状态:pending

### [asked] deepseek-harness 设计哲学七支柱 | 2026-08-18 | 78f956bc(本机)
第一性假设「读者与贡献者是跨 session 无记忆的 AI agent」推出全仓设计;七支柱(一切皆插件/单一事实源其余皆投影/信任边界由序列化介质枚举/capability seam 按演化速率划界/响亮失败/判断落成机器可校验工件/测试即证据)+五个最反常规决策。**讲义已完整落盘该仓 analyze/KEY_POINTS.md + DESIGN_PHILOSOPHY.md——建议建指向条目,不搬正文**。
状态:pending

### [asked] 「门的门」:绿≠sound,漂移全部发生在层间缝隙 | 2026-08-18 | 163afc75(本机)
「CI 每次对真实仓库执行全部 gate——绿只证明『接受当前仓库』,不证明『拒绝坏仓库』」;发现 2 个孤儿 gate(含供应链门)+治理代码本身豁免覆盖率门;核心观察「每个门只守自己那一小片,门与门之间无人守望」——散文↔磁盘、gate存在↔gate执行、注释↔行为三种层间缝隙。**对 atlas 自身 build 门禁体系是直接镜子**。
状态:pending

### [asked] Maxwell→Kafka 分区不均:producer_partition_by 默认全挤一区 | 2026-07-29 | 93c2dae1(本机)
CMAK 实测:3 分区中 partition 1 独占 410 万 offset、0/2 为零;verdict=改 primary_key(均匀+同主键有序);顺序语义从同库有序变同主键有序,下游须幂等 upsert。**产出 ~/docs/maxwell-architecture.html(24KB,存在),source 现成**。
状态:pending

### [asked] Kafka 使用架构五节讲义 | 2026-07-29 | 5bd0d732(本机)
单问「kafka 使用架构逻辑」→ 组件/协调层(ZK/KRaft/Rebalance)/关键语义(acks/ISR/交付语义)自成体系。**产出 ~/docs/kafka-architecture.html(19KB,存在),source 现成**。
状态:pending

### [asked] Maxwell 重启循环根因在下游 Kafka 不在自身 | 2026-07-29 | 3a45dd34(本机)
ERROR「Topic 'maxwell-robinlogs' name does not exist. Failed to update metadata」→ 判读:supervisor 反复拉起的重启循环,三种根因按概率排序+老版本提醒;同日下午 CMAK 显示 topic 恢复 46k msg/s(间接闭环,修正未在本会话回验)。
状态:pending

### [asked] 「学道才能做好 AI 开发吗。为什么」 | 2026-07-30 | fccac3ef(本机)
道拆两层:技术之道(第一性原理,必然需要)与哲学之道(非必要但与概率性 LLM 系统深度共鸣)——「生而不有,为而不恃,长而不宰」即 Agent 设计纲领(越主宰越像被 micromanage 的员工),「反者道之动」对应 overfit 评测/过度护栏/过度堆工具三例;划界:哲学给方向感替代不了工程能力。
状态:pending

### [asked] Serverless GPU 生意账 | 2026-08-27 | 55c6c0ea(本机)
存算分离推理全景(Modal/RunPod/Baseten/Replicate 两类),scale-to-zero 月沉没 ~100 元、H3 单条 ~7 毛,金句**「GPU 不是资产是期权」**;出路四条+止损线「4 周+200 元没首单→关掉」;内含纠偏(GMI 免费名单实际不含 H3)。artifacts 已落 ~/docs/model-storage-compute-split.html。
状态:pending

### [asked] k8s 入门速查讲义 | 2026-08-07 | 86bf1d57 + 0217db00 + c11736ad(本机)
一天连环问:kubectl 三场景命令组+14 资源缩写术语+层级结构+「服务和脚本怎么区分」,AI 分场景表格长答自洽成体系。背景=c002eaf1 报告定位短板(「强语言弱运维」能力画像),属 k8s 补短板学习线一部分。
状态:pending

### [asked] k8s 配置怎么查:deploy→引用→cm/secret 反查讲义 | 2026-08-17 | 94e8bf7d(本机)
「配置怎么查询。cm 么」→ deploy 本身不存配置只引用(envFrom/volumes),路径=deploy→找 cm/secret 名→查内容;附 cm/secret/envFrom 的 jq 提取命令集。
状态:pending

### [asked] Outline 信息架构方法论 | 2026-08-06 | 666c3f48(本机)
collection vs 文档层级判据(独立知识域/权限边界→collection;同域细分→父文档)、深度 1-4 层上限、单层>7 拆/平铺>15 分组、命名约定、决策树;已写进 outline skill 文档(artifact 存在)。
状态:pending

### [asked] Surge 规则匹配语义:顺序优先于精确度 | 2026-08-05 | c03ea2ba(本机)
从上到下命中即停、不按精确度;/32 跳板规则必须排在 10.0.0.0/8 DIRECT 之前;验证法=Dashboard 看该请求 Policy 列。注意:ssh proxy 行最终语法未确认,会话止于「查官方手册」,**无走通记录,入库前须补验**。
状态:pending

### [asked] TKE 访问四场景 + kubectl 上手 | 2026-08-03 | bcbd5d97(本机)
控制台/kubectl+kubeconfig/集群内应用/TCR 四场景分流;网络接入是卡点最多一步;CAM→RBAC 映射错会 forbidden;当日实走通 tccli configure→DescribeClusterKubeconfig→kubectl 查 ns/pod(验证在案)。
状态:pending

### [asked·查重待定] 移动端一键登录原理 | 2026-08-03 | 1a4670dc(本机)
蜂窝网关识别 SIM 取号、两段式、三网聚合 SDK、客户端只拿 token 明文仅服务端兑换、成功率 80~95% 必须留短信回退。**asked 已有「一键登录」条(08-27 从小天源对话恢复)——本机此条是否同源重复,入库前查重**。
状态:pending

### [asked·待复核] Midscene.js 是什么/怎么用 | 2026-08-03 | e60c5e28(本机)
字节开源 LLM 驱动 UI 自动化:自然语言(aiAction/aiAssert/aiQuery)代替选择器,含 bridge mode/Android/Chrome 扩展形态。⚠️ 联网核对被 429 周限挡住,答基于知识库——**入库前须复核版本与现状**。
状态:pending

### [asked] 小件三则 · 本机可合并入速查类 | 2026-08-18 等 | fae29b5b 等
①macOS 命令行启动 Docker Desktop:`open -a Docker` + `until docker info; do sleep 2; done` 轮询就绪(fae29b5b,08-18);②警示图标三态语义:alert-circle/triangle/info 梯度(306bcfd9,08-06,价值一般);③看到 {花括号} 系统提示词=未渲染模板占位符(4e92d911,08-05,弱)。
状态:pending

### [pick] 自动化开发平台三层栈 | 2026-08-05/06 | b0872007(本机)
verdict:multica(①协作/平台/远程)+ Claude Code/Deep Agents(②规划大脑)+ Langfuse(③可观测);备选 oh-my-claudecode/Orca/三省六部Edict/OMA/Plandex/MetaGPT;10+1 份统一 12 节定位报告已入 Outline「技术设计」。**②层是否接受 Claude 绑定是唯一真分叉,未拍板(留给公司决策)——pick 条目需注明此分叉**。
状态:pending

### [pick] 文档知识库选 Outline(自托管) | 2026-07-29/30 | 5895b3c2(本机)
真人三条件「最火+AI 接入+好看」→ AI 对比 Outline/Dify/RAGFlow/Docusaurus/VitePress/BookStack/Obsidian/AFFiNE,verdict=Outline(Obsidian pass:无现成 MCP/API;AFFiNE pass:自托管微服务地狱);用户随后真去 docker 部署(363279f3 行为验证)。**与小天 53f490e3 的「Outline 9 坑实录」互为表里:一条记「为什么选」,一条记「部署的坑」,建议 related 互链;结局(08-25 弃用迁飞书)两条都该写进 verdict 时间线**。
状态:pending

### [pick] 「让 AI 写」前提下的图表库:ECharts | 2026-08-18 | 31db8d0e(本机)
问桑基图用什么画,用户限定「最佳用什么。让 ai 写」,verdict=ECharts——声明式 JSON 配置(option 对象)AI 生成准确率远高于命令式代码,自包含 HTML 落 docs/ 即开、可闭环验证。**适用域:「AI 代写」前提——可作 pick 内标签维度**。
状态:pending

### [pick] 股票 wiki 底座:VitePress(弃 Outline) | 2026-08-19 | c963d226(本机)
思源/Obsidian(编辑器形态不匹配「AI 写、人看」)→ 初定 Next.js+shadcn → 勘察发现 Mac mini 已有 Caddy Docker 栈 → 终判「VitePress 是唯一零新增常驻服务的选项」。附带勘察课:`which docker` 找不到只是 PATH 问题,com.docker 进程在监听 80——**查进程/端口勿信 PATH**。注意演变:08-26 又做 Quartz 5 demo(1a161a0b),是否换轨未定,入库如实标注。
状态:pending

### [维度观察] API 额度与登录态墙 | 2026-08-03 起 | 3 例(本机)
账号时段限(403 Please run /login 会话报废)/工具周限(webReader 429 reset 08-14)/登录态失效,撞墙后行为分叉:换知识库答/弃会话/换时段。**建议先收编进「环境与装机」维度观察,满 5 例再议是否门户视图**。
状态:pending

### [维度观察] Outline=统一知识归宿(定性反转证据) | 2026-08-04→07 | 4 会话(本机)
本机证据显示 Outline 在 08-06/07 是**活跃知识归宿而非沉没**:两 collection 实际落地(「技术设计」11 份选型报告、「商业洞察」抖音长文剪藏,一字未删+来源标注,幂等 curl 脚本可重跑)+ 专用 skill + IA 方法论。**与小天沉没清单条(结局:08-25 弃用迁飞书)合起来才是全貌——定夺沉没清单时参考,不改原条目**。
状态:pending

### [维度观察] holdcloud 生产集群运维(k8s) | 2026-08-17/18 | 2 会话(本机)
DNS 域、ConfigMap/Secret、跨 ns 服务发现连续排障。**收编**:排障方法→apprentice、fud3 翻车→mistakes、cm 查询讲义→asked(均已在上面单列);无独立门禁不建馆,门户可挂「运维」标签观察复发。
状态:pending

### [批注] 既有条目 +N 例汇总(本机新证据,不动原条目,并入与否用户定) | 2026-08-27 dig(本机)
- **并行 agent 编队作战 +8 例**:robin-cli 28-subagent SDD 编队(41f4fc3f,07-28:brief 拆分/每任务 review gate/whole-branch merge gate/被 kill subagent 半成品接力/小任务合批);longxia 2 句话驱动 19-agent 三层审计(0bf6bb65,07-27,产出 C1-C14 编号问题清单);workbuddy 契约先行三路并行(5086a366,07-27→30,接口契约解耦+目录硬边界,MVP 真跑通);holdon G1-G4+集成缝隙(22c19544,08-03:11 实施 agent 跑完后 Makefile 漏加 reconciler 由主线兜底);subagent 当验证关卡(ec4cff00,08-05:build 验证/ff merge/chrome 重跑);11 agents 并发写库(见上条);deepseek-harness 维度切分法(78f956bc,08-18:两轮各 10-11 片,每片带必读清单+穷举指令,单会话 2-6 分钟/轮 16 分钟);bili 9 路调研十分钟齐发+用户中途手砍(08-13/08-27,a14f4448 再派 5-scout);三级编队调研+Plan→实现接力(6d38e98f,08-14/18)
- **调查/审计驱动工作流 +6 例**:零指令纯日志排障(fbcada82)+zaiwu 文案语义漂移(311d68d6,「在线」实为「已用」)均 08-03;磁盘清理四档分级(305c70cd,08-04:3 subagent 并行扫 60G+ 四档清单+高危警示,「你被操作,我来执行」→后更正「你别操作」);mymy 五维审计(c002eaf1)+kubectl 只读盘点(c11736ad)+两轮 workflow(b0872007)均 08-06/07;longxia 全量审计改变选型成本计算(审计发现全是 RN 平台限制而非代码 bug);「先勘察既有资产再动手」再现(08-19/27:c963d226/a14f4448/55c6c0ea)
- **环境与装机 +4 例**:gvm -B 二进制装旧 Go 自救(a21c295f,08-03,与 go1.23×2021 x/net 链接断裂 22c19544 同根两解:WHAT 绕过 vs 降 Go 版);pnpm「cannot find binary path」实为系统未装 pnpm+报错误导(e054800d,08-06);Mac mini(10.0.0.100)已有完整 Caddy Docker 栈被勘察确认(c963d226);multica 全迁+密钥单独保存「配置 key 数据不进 git,但是找得到」(2801380a,08-06/07)
- **Outline 沉没清单 +4 例**:类型系统讲义想写未遂(19315383,08-04,「想写入未遂」新形态);WAL 讲义来源坐实(84c7c408,08-05);docker pull 被 keychain 挡死(363279f3,07-30,拉公开镜像也机械读 keychain);弃 Outline 选 VitePress 时「排版是硬伤」(c963d226,08-19)
- **SQLite 迁移+WAL +1 例(最完整现场)**:三件套双端验着迁本机→Mac mini(84c7c408,08-05:WAL 0 字节→lsof/ps→本地 quick_check→三件套同传 285MB 40s→远程逐字节对比+quick_check→打耗时)
- **Z 漂移「光做没产出」 +1 强例**:报告 verdict 原文「停开新项目。你已经有 35+ 个了」+35+ 独立 git 仓库非 monorepo 实况(c002eaf1,08-07)
- **tacit 插件 +1 例**:插件试用流水线在本机启用侧走通(155bb185/c3ff4cb1,08-06,tacit+blackbox+mattpocock-skills 装删)
- **pick 起源对话 +1 例(更早源头)**:ASR 选型与 2026 价格表(d772f3c0,08-18)——比 fce485e7(08-24)早 6 天,分场景 verdict+每小时价格表带来源链接
- **CLI 安装败于环境版本 +1 例**:go1.23.4×2021 版 x/net 链接断裂(22c19544,08-03,新版编译器×老依赖符号漂移)

## 已决

- [维度] asked(08-27)→ promoted:建馆 atlas/asked(五馆齐);首批 4 篇恢复入库:两种雾/数据库全景/WAL/一键登录;其余 4-5 例(类型系统/审美/gherkin/双向链接/AI 深度幻觉)待回读源对话后补录

- [pick] Sourcetree 选型调研(07-28)→ dismissed:重复——pick/git-gui-clients 已 9 条目含 sourcetree(trial),调研成果已被完整覆盖(2026-08-27 查重)
- [pick] prd-tools 调研(08-26)→ dismissed:重复——pick/prd-tools 已 7 条目(chatprd/claude/feishu/kiro/notion-ai/productboard/spec-kit)(2026-08-27 查重)
- [pick] 数据库横评全景(08-06)→ dismissed:重复——pick/primary-database 已 8 条目,PG/SQLite 双 adopt,三梯队结论已入库;**全景综述原文仍是 asked 沉没件**(见沉没清单)(2026-08-27 查重)
