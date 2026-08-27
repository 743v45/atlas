# dig/INBOX — 候选收件箱

dig 翻阅产出中一切**等用户定夺**的候选:新维度候选(建馆/视图/收编)与馆级内容候选(课/错题/报告)。

**标记规则**(用户动手,只改「状态」行):

- `pending` → `promoted:<去向>`——转正,附一句它变成了什么(建了馆/入了哪馆哪条)
- `pending` → `dismissed:<理由>`——清理,附一句否决理由

promoted / dismissed 的条目移入「已决」区保留一行,**不删**——落选留理由,防的是以后重复提案再兴奋一遍(与 spark 的尸体规则、决策树的落选节点同构)。

AI 的边界(dig/RULES §3):spark 级可直接代录入苗圃;**凡进本收件箱的,定夺权全在用户**——收录即定案,门禁归人。

---

## 待审


### [维度] 环境与装机(setup) | 2026-07-28 起 | 跨两机 10+ 例
pyenv 版本、zsh 插件缺失、CLI 依赖报错、API login 403(07-28);远程机 Go 版本损坏(08-05);tsx not found + node_modules 缺失(08-06);multica 跨机迁移部署(08-06)。
**+本机 4 例**:gvm -B 二进制装旧 Go(08-03,与 go1.23×老 x/net 链接断裂同根两解);pnpm「cannot find binary path」实为系统未装+报错误导(08-06);Mac mini 既有 Caddy Docker 栈勘察确认(08-19);multica 全迁+密钥单独保存(08-06/07)。
**+并入(08-27 定夺)**:CLI 安装败于环境版本(2 例均环境变体,不立错题);**API 额度与登录态墙**(3 例:账号时段限 403/工具周限 429/登录态失效——外部依赖墙归入环境维度)。
证据持续累积(本地+远程)。若有独立生命周期+门禁(机器配置清单?还原脚本?)才配建馆,否则 spark 念头即可。
状态:pending

### [conversations] Outline 沉没内容清单 | 07-30 起 | ✅去向已明:迁往飞书
**08-23 已执行「outline 数据全部导入飞书,用 lark-cli」**(0e78d1c6)——弃用 Outline 时的数据迁移实际去向是飞书,非 taevasidian。
- 07-30:「Outline 自托管 9 坑实录」
- 08-05:「端到端是 AI 开发终极形态吗」;SQLite WAL 机制详解
- 08-06:**数据库横评全景,最大件**
- 08-04:Apple Liquid Glass 中译副本(源在 report 项目,损失小)
后续:在飞书侧核对上述件是否完整迁达。**08-27 已从源对话恢复 3 件入 asked**(数据库全景/WAL 详解/一键登录);端到端与九坑实录仍待恢复。
**+定性反转证据(本机,08-27 并入)**:本机 08-04→07 四会话显示 Outline 弃用前是**活跃知识归宿**——两 collection 实际落地(选型 11 报告+商业洞察剪藏,幂等 curl 写入流水线+IA 方法论+专用 skill)。沉没清单(丢什么)与活跃面(存什么)合起来才是全貌,定夺时两边都看。
状态:pending

### [mistakes·素材] Outline 自托管 9 坑实录的下落 | 2026-07-30 | 53f490e3 + 4ac44e68
3.7MB 部署全程会话产出文章「Outline 本机自托管踩坑实录:9 个坑才跑通 Google 登录」,发布到 Outline wiki「部署踩坑」collection——**而 Outline 已于 08-25 弃用**(memory:存量/迁移留档)。
后续:文章应已随 08-23「outline 数据全部导入飞书」落地飞书(见上条,非 taevasidian);在飞书侧核对是否完整迁达,若未达,源对话 53f490e3 是恢复底稿。9 个坑若完好,可拆成 mistakes 条目素材。**行动项:飞书核对。**
状态:pending


### [conversations] pick 起源对话待归档 | 2026-08-03 | 5af1327a + 7df267c2;+08-21
「技术选型,最佳的技术报告该是什么样」(2.6MB)是 pick 的直接前身;同日 report 项目规则(索引文件/单向链接关联代码地址)是 pick「有理有据」体系的思想源头。
**+08-21**:knowledge-base 类别起源(99faa8a0);**+08-24**:asr-subtitle-tools 起源「有没有好用的识别视频音频的字幕,免费的,或者本地能部署的」(fce485e7);**同日 apprentice 前身之问**:「教教我,这个项目怎么写。怎么设计出来,设计哲学。出一份教程,顺序教学」(3475e2c2→e8f845e1 调研一手材料)。**+本机(08-18)**:ASR 选型与 2026 价格表(d772f3c0)——比 fce485e7 早 6 天的更早源头,分场景 verdict+价格表带来源链接。
低优先:按 conversations 规则归档摘要,链接进 pick 的 README 或 DESIGN-TREE 作起源存证。
状态:pending

### [pick] 31 条 meta.sources 为不可解析文本引用 | 2026-08-27 | 审查发现
pick 门禁承诺「有据可溯」,但全库 78 条中 31 条的 meta.sources 存在既非 URL 亦非 raw/ 实路径的纯文本引用(如「Claude 历史会话(2026-08-25)——提取源」)——可溯性承诺未兑现,需重新溯源为 URL 或实路径(raw/ 留档)。**08-27 新入 3 条已示范正解:raw/2026-08-27/ 落 sessions 提取+gh 快照。行动项:31 条旧条逐条补源。**
状态:pending

### [asked] Surge 规则匹配语义:顺序优先于精确度 | 2026-08-05 | c03ea2ba(本机)
从上到下命中即停、不按精确度;/32 跳板规则必须排在 10.0.0.0/8 DIRECT 之前;验证法=Dashboard 看该请求 Policy 列。**挂起原因:ssh proxy 行最终语法未确认,会话止于「查官方手册」,无走通记录——补验后再入。**
状态:pending

### [asked·待复核] Midscene.js 是什么/怎么用 | 2026-08-03 | e60c5e28(本机)
字节开源 LLM 驱动 UI 自动化:自然语言(aiAction/aiAssert/aiQuery)代替选择器。⚠️ 联网核对被 429 周限挡住,答基于知识库——**复核版本与现状后再入。**
状态:pending

### [apprentice] 外部工具配额耗尽降级链 | 2026-08-05 | 4e92d911 + c03ea2ba(本机)
WebSearch 周限→WebFetch 被挡→webReader 429→本机确定性路径;AI 每次主动换通道并同步「查到/没查到」。**挂起原因:仅同日 2 例,攒跨日再立**(与「降级凑合为失败」互补:那是禁无序降级,这是有序降级预案)。
状态:pending

### [pick] 股票 wiki 底座:VitePress | 2026-08-19 | c963d226(本机)
勘察发现 Mac mini 已有 Caddy Docker 栈→「VitePress 是唯一零新增常驻服务的选项」;附带勘察课:**查进程/端口勿信 PATH**。**挂起原因:08-26 又做 Quartz 5 demo(1a161a0b),换轨未定,等收口再收。**
状态:pending

## 已决

- [维度] asked(08-27)→ promoted:建馆 atlas/asked(五馆齐);首批 4 篇恢复入库:两种雾/数据库全景/WAL/一键登录;类型系统已回读补录(08-27 见下);其余 3-4 例(审美/gherkin/双向链接/AI 深度幻觉)待回读源对话后补录

**08-27 全量清账(grilling 定夺,四馆并发执行):**

- [mistakes×11] → promoted:virtiofs 损库(items/virtiofs-sqlite-corruption)、光做没产出 Z 漂移(items/project-z-drift)、fudN 误当 DNS 域(items/cluster-suffix-dns)、whisper 逐词崩溃(items/whisper-word-timestamps)、urllib 自签截断(items/urllib-selfsigned-truncation)、纸面样板冒充生产经验(items/paper-production-experience)、E2E 绿灯掩盖配置缺失(items/e2e-green-config-missing)、凭据无验证闭环(items/cli-credential-verification)、subagent 长报告截断(items/subagent-report-truncation)、task gate 拦不住全局 lint(items/fragment-lint-collapse)、AI 凭印象断言语法对(items/syntax-assertion-surge)——错题集 1→12
- [apprentice×7·小天] → promoted:tacit 插件(automate/tacit-plugin)、SQLite 安全迁移+红线(verify/sqlite-safe-migration)、批量翻译流水线(automate/batch-translation-pipeline)、调查/审计驱动工作流(express/audit-first-workflow,含 holdon 支付链案例节)、并行 agent 编队作战(express/agent-fleet-parallelism,吸本机 8 例+11agents 写库验证闭环)、CLI for AI(automate/cli-for-ai,吸 lark-cli +1 例)、「降级凑合为失败」(express/no-degraded-fallback)
- [apprentice×5·本机] → promoted:CLI 鉴权幂等状态机(verify/auth-idempotent-state-machine)、零指令纯日志排障(express/log-only-debugging)、UI 像素级复刻验证(verify/pixel-perfect-replication)、k8s 容器内 DNS 排障三步法(verify/container-dns-triage)、「教我怎么做,不要替我操作」(express/teach-dont-operate)——课集 1→13
- [apprentice·并入] 任务描述收敛法 → promoted:并入 express/describe-the-goal 新小节「每条诉求补『做到什么算完』」(变体不单立,门禁规则)
- [asked×12] → promoted:类型系统与形式化验证(待补录源头落地,items/type-system-and-formal-verification)、deepseek-harness 七支柱(指向条目)、门的门绿≠sound、Maxwell 分区不均、Kafka 五节、Maxwell 重启循环、学道才能做好 AI 开发、Serverless GPU 生意账、k8s 入门速查、k8s 配置反查、TKE 四场景、文档库信息架构(标注载体已弃用判据通用)——问答馆 4→16
- [pick×3] → promoted:自动化平台三层栈(adopt,automation-platform 新类别)、文档知识库 Outline(hold,完整生命周期四幕报告,knowledge-base 重写)、ECharts(adopt 标「AI 代写」域,charting 新类别)——80 条;raw/2026-08-27/ 落 sessions 提取+gh 快照 5 repo
- [维度观察×3·本机] → dismissed:API 额度与登录态墙(并入环境维度观察,见上);Outline=统一知识归宿(定性反转证据已附沉没清单条,不单立);holdcloud 生产集群运维(已收编:方法→apprentice、错题→mistakes、讲义→asked,门户挂标签观察复发)
- [+N 例批注·本机] → dismissed:证据已随各课转正分发(编队+8→fleet 课;调查+6→audit-first 课;环境+4→本条;SQLite 最完整现场→sqlite 课;Z 漂移+1→project-z-drift;tacit+1→tacit 课;ASR 更早源头→pick 起源条;CLI 安装败+1→环境维度)
- [mistakes·小件] commander 报错输出两遍、kubectl -n 误传 → dismissed:太碎价值低,证据在源会话不丢(同一归档 2026-07-28-robin-cli-fleet-review.md)
- [mistakes] CLI 安装败于环境版本 → dismissed:并入环境维度观察(2 例均为环境问题变体,不占错题集)
- [asked] 移动端一键登录原理(本机 1a4670dc)→ dismissed:重复——asked 已有同名条(08-27 从小天源对话恢复入库)
- [asked·小件三则] macOS 命令行启动 Docker/警示图标三态/花括号未渲染模板 → dismissed:单薄不够格(一行命令/图标语义/弱观察)
- [apprentice] 多 agent 并发产长文档库 → dismissed:并入 agent-fleet-parallelism 验证闭环节(11 agents 5m45s+回传 URL 自验证),变体不单立
- [apprentice] lark-cli 自动写飞书 wiki → dismissed:并入 cli-for-ai 课作 +1 例(薄证据,2 句话单会话)

- [pick] Sourcetree 选型调研(07-28)→ dismissed:重复——pick/git-gui-clients 已 9 条目含 sourcetree(trial),调研成果已被完整覆盖(2026-08-27 查重)
- [pick] prd-tools 调研(08-26)→ dismissed:重复——pick/prd-tools 已 7 条目(chatprd/claude/feishu/kiro/notion-ai/productboard/spec-kit)(2026-08-27 查重)
- [pick] 数据库横评全景(08-06)→ dismissed:重复——pick/primary-database 已 8 条目,PG/SQLite 双 adopt,三梯队结论已入库;**全景综述原文仍是 asked 沉没件**(见沉没清单)(2026-08-27 查重)
