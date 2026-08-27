我先快速核实一下「方便 AI 接入」这块的最新情况（MCP/API 支持对你这种 agent 场景最关键），再给你精准选型。
"最火 + 方便 AI 接入 + 页面好看" 这三条同时满足，**Outline 是最匹配的答案**，其余看你具体场景。
## 首推：Outline
- 最火：GitHub 数万 stars，最成熟的开源团队知识库（Notion 替代品）。[官网](https://getoutline.com) · [仓库](https://github.com/outline/outline)
- 方便 AI 接入：完整 REST API + webhooks，文档/集合/用户/搜索全套 CRUD；社区已有 MCP server（`mcp-outline` 等），agent 可直接检索/读写文档；自托管也能挂 OpenAI 兼容端点做内置摘要/问答。
- 页面好看：React + Node.js，现代极简，编辑器体验接近 Notion。
自托管：Docker Compose，依赖 Postgres + Redis + S3 兼容存储（MinIO）。中等难度。
## 按你的真实场景备选
**如果你要的是「上传文档 → AI 问答」(RAG 引擎，而不是写文档的平台)**
- [**Dify**](https://github.com/langgenius/dify)：100K+ stars，内置知识库/RAG，**原生支持 MCP server**，把工作流/知识库直接暴露成 agent 工具 —— AI 接入最顺。
- [**RAGFlow**](https://github.com/infiniflow/ragflow)、[**FastGPT**](https://github.com/labring/FastGPT)、[**AnythingLLM**](https://github.com/Mintplex-Labs/anything-llm)：都是文档问答型，AI 是核心，但偏"问答引擎"，文档管理/颜值不如 Outline。
**如果你要的是「给开源项目做 docs.xxx.com」(静态文档站)**
- [**Docusaurus**](https://github.com/facebook/docusaurus)（Meta，最火）/ [**VitePress**](https://vitepress.dev)（最快，Vue）/ [**Nextra**](https://nextra.site)（Next.js）：页面都好看，但"AI 接入"要自己加一层（给静态站套 MCP / Algolia DocSearch）。
**简单一句话判断**
| 你要的 | 选 |
|---|---|
| 像 Notion 那样写文档，agent 能接入检索 | **Outline** ⭐ |
| 上传文档让 AI 问答，Dify 式 RAG | **Dify** / RAGFlow |
| 项目文档站，颜值高 | Docusaurus / VitePress |
| homelab 最省心、自己接 AI | [BookStack](https://github.com/BookStackApp/BookStack)（REST API 稳定，自托管最简单） |
—— 你的场景是哪个？（团队知识库 / AI 问答 / 项目文档站）告诉我我给你具体的接入方案（MCP 配置 / API 调用样例）。搜索刚好遇到限流，上面的 MCP 状态是我据已有知识给的，要的话我限流恢复后（约 1 小时后）再帮你核对一遍各项目的官方 MCP 最新进展。
"做一篇文档"和"选一个文档平台"其实是两件事——工具取决于这一篇以后**怎么用**。结合你上轮强调的「AI 接入 + 颜值」和你已有的东西（你在用 Hugo 写博客），我直接帮你判断：
## 给你三个落点，按"这一篇的归宿"分
**1. 就这一篇，现在要、好看就行** → 别搭平台，零门槛
直接写 Markdown，或一个自包含 HTML（你还偏好 HTML 关系图）。Pandoc / Marp / 一个 `markdown.css` 渲染即可，几分钟出活，不需要 Postgres/Redis 那一套。**为了一篇知识点去自托管 Outline 是杀鸡用牛刀。**
**2. 想长期攒成"AI 能查的技术知识库"** → **Outline** ⭐
这就是它的主场：自托管一次，以后每个知识点都是一篇，agent 通过 MCP/API 直接搜你的库。你现在问的"选型"就是第一篇。**如果你打算持续沉淀而不是写一次就完，选这个。**
**3. 想发布成公开技术文章** → **Hugo**（你已经在用，直接 `/hugo`）
发到你的博客，颜值靠主题，AI 接入靠后面套一层 MCP / Algolia。
## 我的建议
- **只要这一篇**：走方案 1，我直接帮你生成一个排版干净的自包含 HTML / Markdown，存到 `~/` 下你指定的地方。
- **打算以后越攒越多、还想让 agent 查**：上 Outline，这一篇当开篇。我可以帮你把 Docker Compose 起起来 + 写第一篇。
- **就是要发出去给人看**：走 Hugo，我直接 `/hugo` 把"开源文档服务选型"发成一篇。
—— 你这一篇是**自己存/给 agent 查**，还是**发出去**？
定了我就直接动手把内容做出来，不再停在选型上。
明白了，你的需求其实已经定了：你要的是一个**长期积累、可管理、好看、能被 AI 查的知识库**，而且你已经自觉地把它和 Hugo 分了工——
- **Hugo =「思考」**：对外发布的观点、长文、博客（经过整理、给人读）
- **文档库 =「知识」**：半结构化、持续攒、给自己和 agent 查的（选型、how-to、参考、备忘）
这个分工是对的。那答案就是 **Outline**，不用再纠结：
## 为什么是 Outline（而不是别的）
- **Obsidian**：本地笔记王者，但不是 web 服务、多端/远程要付费 Sync 或 Git，"方便 AI 接入"弱（没有现成 MCP/API 给 agent 查）——你重视 AI 接入，pass。
- **AFFiNE**：颜值更高，但自托管是微服务地狱、AI 能力基本绑云账号——pass。
- **BookStack**：自托管最简单，但颜值偏传统 wiki，不如 Outline 现代。
- **Outline**：Notion-like 颜值 + 完整 REST API + MCP + 自托管一次受益长期。**个人用也完全合适**，不一定要团队。
## 落地两步
**① 本机 Docker 起 Outline**（本地账号即可，单人够用；要公网多端再加 OIDC）。依赖 Postgres + Redis + MinIO(S3)，一套 compose 起来。
**② 把 Hugo 里的「知识型」内容迁过来**：Outline 支持 markdown 导入，也能走 API 批量建文档。Hugo 的 md 有 front matter，迁移脚本里把 `title/date/tags` 映射成 Outline 的文档标题 + 集合即可，正文原样进。
—— 我可以直接动手帮你做这两步。先确认两点：
1. **部署在哪**：本机 Docker 先试用 / 你有服务器要长期对外（多端 + agent 远程查）？
2. **Hugo 内容在哪**：仓库路径？以及你心里哪类算「文档」要迁（比如 `content/notes/`、或打了特定 tag 的）——给我路径我扫一遍分类。
定了我就：写 `docker-compose.yml` + 启动脚本起 Outline，再写个迁移脚本把 Hugo 知识型 md 批量导进去（按 CLAUDE.md 要求落到 `scripts/`，带计时和可重跑）。要开始就告诉我这两点。
谷歌没说错，但 **Dify 和 Outline 根本不是同一类东西**——它推荐 Dify 是因为它只盯着你说的「方便 AI 接入」这一条，从「AI 应用平台」角度出发，Dify 是最火的。可你的核心诉求前几句已经说清楚了：**管理很多文档 + 好看 + 自己写和组织**。这条路上 Dify 反而是弱项。
## 两者本质区别
| | **Outline** | **Dify** |
|---|---|---|
| 本质 | 文档库 / 知识库（Notion 类） | AI 应用开发平台（LLMOps） |
| 你在哪**写/组织**文档 | ✅ 主场，Notion-like 编辑器 | ❌ 不在这写文档，文档是「喂进去的语料」 |
| 颜值（文档阅读/编辑体验） | ⭐⭐⭐⭐⭐ | ⭐⭐⭐（是工作台/控制台风格，不是文档阅读体验） |
| AI 接入 | API + MCP（agent 能**读你的库**） | 原生主场：RAG 问答 / 搭 agent / 工作流，MCP 一等公民 |
| 适合的句子 | 「我有个漂亮地方管我的文档，AI 能查」 | 「我要让 AI 基于我的文档**问答/干活**」 |
**关键一句**：你不会在 Dify 里「写一篇知识文档」——Dify 是把你外面丢进来的文档切片做 RAG。你要的「以后有很多文档、有个地方管理、好看」= 要一个**写和组织文档的地方**，那是 Outline，不是 Dify。
## 但有一种情况谷歌是对的
如果你其实最想要的是「**和我的知识库对话 / 让 agent 用我的知识干活 / 搭工作流**」，那 Dify 比 Outline 强，谷歌没错。
## 我的建议：分工，两个都要
最佳架构不是二选一——
- **Outline 当「库」**：你日常写、组织、好看地管理文档。
- **Dify 当「引擎」**：把 Outline 的文档同步进 Dify 知识库，做 RAG 问答 / agent / 工作流。
这样「管理好看」和「AI 应用」各取所长，不冲突。
—— 先定你核心偏哪个，我直接动手搭：
这句回答把方向彻底锁定到 **Outline** 了——
> "ai 写读内容，但是展示要好看。我要看的。"
拆开看：
- **「ai 写读内容」** → AI 是生产者/操作者，人不是来"写"的。Outline 有完整 REST API + MCP，**agent 可以直接往库里写文档、检索文档**，完全满足。Dify 也行。
- **「展示要好看，我要看的」** → 你要的是**漂亮的文档阅读页给人看**。这一条 Dify **给不了你**——Dify 给你的是聊天框 / 应用控制台，不是"打开一篇文档看"的体验。Outline 的阅读页是 Notion-like，就是给人看的，漂亮。
**所以 = Outline。** Dify 的展示层在你这场景下不合格，谷歌那条路不适合"我要看文档"。而且你的「ai 写」可以更进一步：接 Outline API 写个 agent，**让 AI 自动把知识点生成成文档塞进库**，你只管打开 Outline 漂亮地看——这正是你要的闭环。
先探一下你机器环境，好给你可执行方案（只读探测）：
## 探测结果
- ✅ **Docker 29.6.2 + Compose v5.3.1 都已装好**
- ⚠️ **Docker daemon 没在跑** —— macOS 上需要先开起来。你在输入框敲 `! open -a Docker` 起 Docker Desktop（或点图标），起来后我才能 `docker compose up`。
- 端口 3000/3100 空着，可用。
## 方案定档：本机 Docker 起 Outline
先本机（最快试用），以后要 agent 远程查/多端访问再加服务器或反代。
我现在并行核对 Outline 自托管**唯一要注意的坑——认证**（它历史上只支持 Google/Slack/OIDC，没有简单本地密码登录，得确认新版有没有改善，这决定 compose 要不要额外挂一个 OIDC）。核完直接给你能 `docker compose up` 的完整文件 + 一个让 AI 经 API 写文档的脚本。
网络挡了 raw 域名，换条路抓官方文档（web_reader）：
**🌐 Z.ai Built-in Tool: webReader**
**Input:**
```json
{"return_format":"markdown","url":"https://github.com/outline/outline"}
```
*Executing on server...*
**🌐 Z.ai Built-in Tool: webReader**
**Input:**
```json
{"return_format":"markdown","url":"https://docs.getoutline.com/s/hosting/doc/hosting-outline-N3lf0weTdr"}
```
*Executing on server...*
**Output:**
**webReader_result_summary:** [{"text": "MCP error -429: {\"error\":{\"code\":\"1310\",\"message\":\"Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-08-14 15:27:30\"}}", "type": "text"}]
**Output:**
**webReader_result_summary:** [{"text": "MCP error -429: {\"error\":{\"code\":\"1310\",\"message\":\"Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-08-14 15:27:30\"}}", "type": "text"}]
联网工具暂时全挂了（WebSearch、WebFetch、web_reader 都限流，最晚到 8/14 才恢复），所以下面基于我的知识给你，等 Docker 起来我们直接按实际跑通迭代——Outline 启动会自己校验配置并报缺什么，比文档还准。
先定**唯一影响 compose 结构的决策点**：Outline 自托管**不自带本地密码登录**，必须挂一个第三方登录。这一步配好就永久不用管：
Google 登录，定了。动手。
思路：联网限流只影响 web 工具，**git 通道不受影响**，所以我直接 clone Outline 官方 repo 拿最权威的 `.env.sample` 和 `docker-compose.yml`，照它写配置——比凭记忆准。同时探 Docker daemon。
先建任务跟踪，并行拉参考配置：
clone 成功，拿到官方 `docker-compose.yml` 了。但 **Docker daemon 还没起**（`server ` 后面空）——你先 `! open -a Docker` 开一下 Docker Desktop，起来我才能 `up`。
读官方 compose + 找 env 模板：
关键发现：官方根 `docker-compose.yml` 只是**开发用**（只有 redis + postgres，没有 outline/minio 容器），不能直接拿来自托管。但有 `.env.sample`（13KB，1.9.1 全量配置清单）——这是金矿。读它来写准确的自托管配置：
好消息：1.9.1 默认 `FILE_STORAGE=local`（本地磁盘存附件），**不用 MinIO**，compose 简化到 3 个容器。认证确认要 Google（`GOOGLE_CLIENT_ID/SECRET`），无本地密码登录。最后确认下 Google 回调路径，就写配置：
grep 没命中（1.9.1 把 auth 改进了 plugin 系统）。再定位一次准确路径——redirect URI 填错登录会直接失败，值得确认：
路径基本锁定——email 的 callback 是 `/auth/email.callback`（`SigninEmail.tsx:149`），所以 Google 几乎确定是 `/auth/google.callback`。grep 做最终确认，同时**基于 1.9.1 的 `.env.sample` 把全套配置写好**：
**callback 已从源码坐实**：`google.ts:51` → `callbackURL: ${env.URL}/auth/${config.id}.callback`，且 `config.id = google`。所以 redirect URI 就是 **`http://localhost:3000/auth/google.callback`**——我写进 `.env`/README 的值准确无误。
全套配置已落到 `~/code/outline/`，给脚本加可执行权限：
全部就位 ✅。目录结构：
- [docker-compose.yml](file:///Users/taevas/code/outline/docker-compose.yml) — 3 容器：outline + postgres + redis，本地存储（不用 MinIO）
- [.env](file:///Users/taevas/code/outline/.env) — 配置（secrets 占位，Google 待填）
- [scripts/bootstrap.sh](file:///Users/taevas/code/outline/scripts/bootstrap.sh) — 一键：检查前置 → 生成密钥 → up → 健康检查（幂等可重跑）
- [README.md](file:///Users/taevas/code/outline/README.md) — 操作说明
## 现在轮到你 3 步
**① 开 Docker**（daemon 还没起）
输入框敲：`! open -a Docker`，等十几秒让它起来。
**② 配 Google OAuth Client**
1. 打开 https://console.cloud.google.com/apis/credentials
2. 先配 **OAuth consent screen**：External → App name 填 `Outline`、support/developer email 填你的 → 测试用户加自己邮箱
3. **Credentials → Create Credentials → OAuth client ID → Web application**
4. **Authorized redirect URIs** 填（已源码确认准确）：
   ```
   http://localhost:3000/auth/google.callback
   ```
5. 创建后拷 **Client ID** 和 **Client Secret**
**③ 填 creds + 起**
把拿到的 ID/Secret 填进 [.env](file:///Users/taevas/code/outline/.env) 的 `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET`——用编辑器打开替换占位符，或输入框一行（替换括号）：
```
! perl -pi -e 's/__GOOGLE_CLIENT_ID__/ID贴这里/; s/__GOOGLE_CLIENT_SECRET__/SECRET贴这里/' ~/code/outline/.env
```
---
**开好 Docker + 填好 creds 就回我一声**，我来跑 `./scripts/bootstrap.sh` 并盯着日志调通（拉镜像/起容器/健康检查，有 env 报错我当场改）。Google 配置哪步卡了也直接问。
旁注：`~/code/outline/.ref` 是我 clone 的官方源码参考（只为拿准确配置），用不到可以删；`.gitignore` 已忽略它和 `.env`。
