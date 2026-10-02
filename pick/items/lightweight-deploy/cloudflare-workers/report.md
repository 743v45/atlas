# Cloudflare Workers

> **TL;DR**：托管轻量化轴的极点：V8 isolate 边缘运行时把运维压到零、免费层（10 万请求/日 + 10ms CPU，2026-10 查）即可起步，状态存储平台内置（KV/D1/Durable Objects/R2/Queues）——但 isolate 不是进程，应用必须按 Workers 形态写（请求驱动、无长驻后台、绑定最深），已有 Node 服务不能原样迁移，另有 Containers 补容器类负载；适用域为新写 API/全栈 JS 小服务与全球低延迟场景，非通用部署方案。

- **结论**：trial（试用域：新写的 API/边缘逻辑/全栈 JS 小项目可上生产；「把现有 Node 服务部署上去」的场景不适用，应选本类别其他条目）
- **核实日期**：2026-10-02（官方 pricing/limits/runtime/compat/containers/frameworks 六页当日核实 + gh workerd 仓库）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 产品形态 | 托管边缘运行时（V8 isolate），请求驱动；运行时 [workerd](https://github.com/cloudflare/workerd) 开源（⭐8,801、Apache-2.0、push 2026-10-02，gh 2026-10-02 采集），平台本身闭源 | [3][7] |
| 定价（2026-10-02 查） | Free：100,000 请求/日（00:00 UTC 重置）、10ms CPU/次调用；Paid $5/月起（Standard 模型）：含 1000 万请求/月 + 3000 万 CPU-ms/月，超出 $0.30/百万请求、$0.02/百万 CPU-ms；**无 egress 费**；静态资源请求免费不限量 | [1] |
| 资源上限（2026-10-02 查） | 内存 128MB/isolate；CPU 免费层 10ms、付费默认 30s 可调至 5min（Cron/Queue 消费者上限 15min）；Worker 体积 64MiB；启动 1s；子请求免费层 50/次、付费 10,000/次；单账号 Worker 数免费 100、付费 500 | [1][2] |
| Node 兼容 | compat date ≥2026-08-04 时 `nodejs_compat` 默认开启；fs/http/stream/crypto/process 等原生支持，dns/tls/console 部分支持，child_process/worker_threads/cluster/vm 等仅非功能 stub | [4] |
| 框架支持 | Next.js（OpenNext adapter）、React Router（前 Remix）、Astro、SvelteKit、Nuxt、Vue、Hono、TanStack Start 等均有官方部署指南（官方页 2026-07-03 更新） | [6] |
| 触发场景 | 轻量部署类别横评：托管平台独立路线（边缘 isolate，区别于容器/进程路线） | — |

## 为什么选（适用域：新写 API/全栈 JS 小服务）

1. **运维压到零**：无服务器、无进程、无系统更新，部署即 `wrangler deploy`，代码自动跑在 Cloudflare 全球数百地数据中心上，请求就近路由 [3]。类别轴上的「运维心智」这一项，本方案是全类别最小值。
2. **冷启动近零**：isolate 不是 VM/容器——官方口径 isolate 启动比容器/VM 里的 Node 进程快约 100 倍、内存占用低一个量级，VM 模型的冷启动问题在此模型下不存在 [3]。对个人小服务「最怕没人访问还掉链子」的体验是实质改善。
3. **免费起步、成本极低**：免费层 10 万请求/日足够个人 API；付费 $5/月含千万级请求与 3000 万 CPU-ms；官方称平均 Worker 每请求仅 ~2.2ms CPU（官方口径，2026-09 文档），即 $5 档 CPU 额度可覆盖约每分钟数千次请求的纯 API 负载；静态资源请求免费不限量，静态为主的小全栈站几乎不产生费用 [1][2]。
4. **状态存储平台内置**：KV / D1（SQLite）/ Durable Objects / R2 / Queues 原生于平台且共享同一计费框架，小型全栈应用**不需要自挂数据库**；SQLite-backed Durable Objects 已进免费层（KV-backed DO 仅 Paid）[1]。
5. **全栈框架可落地**：Next.js / React Router(前 Remix) / Astro / SvelteKit / Nuxt / Hono 等主流框架有官方部署指南与自动配置，不是只能写裸 fetch handler [6]。

## 边界：为什么不能当通用部署方案（与类别其他条目的分界）

1. **isolate 不是进程**：无常驻后台进程、无文件系统持久化、全局状态随 isolate 逐出随时丢失（官方明确建议不依赖全局可变状态）、编程模型是请求驱动的 `fetch()` handler——「把现有 Node 服务原样部署上去」多数不行，应用要按 Workers 形态写（Hono 等）或做适配 [3]。
2. **CPU 时间是硬上限**：免费层 10ms/次、付费默认 30s（可调至 5min），超限返回 1102 错误；转码、爬虫、批处理等长 CPU 任务不合适。等待网络 I/O 不计 CPU 时间，故 API 类负载影响有限，但计算密集型天然不匹配 [2]。
3. **Node 生态兼容有边界**：`nodejs_compat` 覆盖面已很宽（2026-08 起 compat date 默认开启），但 dns/tls 仅部分支持，child_process、worker_threads、cluster、vm、http2 等为非功能 stub——依赖这些的原生 Node 服务直接跑不了，只能改写或走 Containers [4]。
4. **平台绑定最深**：存储（KV/DO/R2）、编排（Cron/Queues）、部署（wrangler）全是平台专有 API；自托管 workerd 只能得到运行时本身，平台存储与全球编排能力带不走（故本条目矩阵「自托管」写「否」）[1][3][7]。
5. **容器类负载有了但仍受平台形态约束**：Containers（官方文档 2026-09-30 版列为 Workers Paid 可用产品、已纳入计费表）可跑任意语言/镜像/完整文件系统，但由 Worker 代码（Durable Object 类）控制生命周期、按活跃 10ms 计费、Paid 专属——是 Workers 形态的延伸而非独立部署通道 [1][5]。

## 对比（类别内路线差异，逐维度见 `../comparison.md`）

| 维度 | **Workers** | Fly.io 类托管容器 | Dokku 类 VPS 微 PaaS | systemd/Docker 自管 VPS |
|---|---|---|---|---|
| 能跑什么 | 按 Workers 形态写的 JS/TS（Containers 补任意镜像，Paid） | 任意 Docker 镜像 | 任意应用（buildpack） | 任意 |
| 运维门槛 | 零 | 低 | 中 | 高 |
| 常驻模型 | 无（请求驱动 isolate） | 可常驻/按需启停 | 常驻进程 | 常驻进程 |
| 冷启动 | ~0（isolate）[3] | 秒级（机器唤醒） | 无（已常驻） | 无（已常驻） |
| 平台绑定 | 最深（存储/编排全专有） | 中 | 低 | 无 |
| 起步成本 | 免费层 → $5/月（2026-10 查）[1] | 按量计费起价 | 自持 VPS | 自持 VPS |

关键判断：**这是「开发平台」与「部署方案」的分界**。本类别其余条目都接受「现有服务原样部署」这一前提，Workers 是唯一要求应用按其形态重写的路线——选它不是选部署方式，是选运行平台。

## 风险与注意

- **平台依赖风险**：个人服务挂在单一商业平台的政策与定价变化上；免费层限额每日重置、超限直接报错（请求返回 1027）而非降级服务 [1][2]。
- **计费口径变动**：Workers Logs 将于 2026-12-01 起改用 Cloudflare Observability 计费（官方 pricing 页预告，2026-10-02 查）——平台各周边产品的计费口径仍在演进，依赖前核对当日 pricing 页 [1]。
- **性能数据口径**：本报告引用的「平均 ~2.2ms CPU/请求」「isolate 快 100 倍」均为 Cloudflare 官方口径（2026-09 文档），无独立第三方基准；CPU 密集场景建议先实测再定 [2][3]。
- **待验证**：Containers 于 2025-06 Developer Week 宣布 GA 的公告细节（本次核实 WebSearch 配额耗尽未取到原文；Containers 的可用性与计费已由官方文档 2026-09-30 版直接核实，GA 公告仅作背景待补）[5]。
- **workerd ≠ 平台**：运行时可自跑（Apache-2.0），但矩阵「自托管」仍写「否」——KV/DO/R2/Queues 等平台能力无自托管等价物，「自托管 Workers 平台」不是一个可选项 [7]。

## 来源

1. Workers Pricing（官方文档，含 Free/Standard 计费表、KV/D1/DO/R2/Queues/Containers 分节） — https://developers.cloudflare.com/workers/platform/pricing/（访问 2026-10-02，官方 md 版 Last updated 2026-10-02；原始留档 raw/2026-10-02/web/workers-pricing-full.md）
2. Workers Limits（官方文档，计划限额与平台限制表） — https://developers.cloudflare.com/workers/platform/limits/（访问 2026-10-02，Last updated 2026-09-05；留档 raw/2026-10-02/web/workers-limits-full.md）
3. How Workers works（官方文档，isolate 模型与冷启动论述） — https://developers.cloudflare.com/workers/reference/how-workers-works/（访问 2026-10-02，Last updated 2026-09-18；留档 raw/2026-10-02/web/workers-how-works.md）
4. Node.js compatibility（官方文档，原生/部分/stub 支持清单） — https://developers.cloudflare.com/workers/runtime-apis/nodejs/（访问 2026-10-02，Last updated 2026-08-12；留档 raw/2026-10-02/web/workers-nodejs-compat.md）
5. Containers（官方文档） — https://developers.cloudflare.com/containers/（访问 2026-10-02，Last updated 2026-09-30；留档 raw/2026-10-02/web/workers-containers.md）
6. Workers Framework Guides（官方文档，全栈框架部署指南索引） — https://developers.cloudflare.com/workers/framework-guides/（访问 2026-10-02，Last updated 2026-07-03；留档 raw/2026-10-02/web/workers-frameworks.md）
7. cloudflare/workerd — https://github.com/cloudflare/workerd（gh 2026-10-02 采集：⭐8,801、push 2026-10-02、Apache-2.0；留档 raw/2026-10-02/web/workerd-gh.json）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（六页官方文档当日核实；定价以 2026-10-02 查询口径为准） |
