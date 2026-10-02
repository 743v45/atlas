# Cloudflare Workers 定价页原始留档

- 来源 URL: https://developers.cloudflare.com/workers/platform/pricing/
- 访问日期: 2026-10-02（WebFetch/web-reader 抓取）
- 页面 last-updated 元数据: 2026-08-28（publishedTime）
- 说明: 页面为 Astro 站点，web-reader 抓取时表格内具体单价数字被转换丢弃（下文「Example pricing」只有标题无数字行）；单价已用 WebFetch 对同页补抓核实（数字见 workers-developers.cloudflare.com-2.md），完整官方 markdown 版另存于本目录 workers-pricing-full.md（curl 直取 /index.md，Last updated Oct 2, 2026，含全部表格）。

---

## 正文（原样摘录）

By default, users have access to the Workers Free plan. The Workers Free plan includes limited usage of Workers, Pages Functions, Workers KV and Hyperdrive. Read more about the Free plan limits.

The Workers Paid plan includes Workers, Pages Functions, Workers KV, Hyperdrive, and Durable Objects usage for a minimum charge of $5 USD per month for an account. The plan includes increased initial usage allotments, with clear charges for usage that exceeds the base plan. There are no additional charges for data transfer (egress) or throughput (bandwidth).

All included usage is on a monthly basis.

## Workers

Users on the Workers Paid plan have access to the Standard usage model. Workers Enterprise accounts are billed based on the usage model specified in their contract. To switch to the Standard usage model, contact your Account Manager.

- 脚注要点：Inbound requests 计费（Worker 发起的 subrequest 不计费）；WebSocket 连接建立计 1 request，消息不计；**静态资源请求免费且不限量**；启用 Workers Caching 时缓存命中仍按同价计 request（CPU 时间只在 cache miss/bypass 时计）。

### Example pricing（页面有 5 个例子：15M req/7ms CPU、80% 静态资源、Cron 每小时 3 分钟 CPU、100M req、缓存 80% 命中率——表格数字未抓到）

### How to switch usage models

Standard usage model 为 Paid 默认；legacy 模型（Workers Unbound / Workers Bundled）建议迁移到 Standard，改 usage model 只影响计费无技术影响。

## Workers Logs / Logpush

- Workers Logs：Free 和 Paid 都含。
- Trace Events Logpush：仅 Paid；按过滤/采样后到达目的地的请求日志计费。

## Workers KV

Free 和 Paid 都含；Free 层有限额，所有限额每日 00:00 UTC 重置，超限该类操作报错。

## Hyperdrive

Free 和 Paid 都含；Free 层有限额（每日重置）。Database query 定义 = 经 Hyperdrive 的任意语句（SELECT/INSERT/UPDATE/DELETE/DDL）。

## Queues

按队列操作数计费：每 64KB 数据写/读/删算一次操作；消息按条不按批（默认批 10 条 = 10 次写+10 读+10 删）；无 egress 费。多数消息投递 = 3 操作（写+读+删），月账单公式：`((消息数 * 3) - 1,000,000) / 1,000,000 * $0.40`（即含 100 万操作免费额度，超出部分 $0.40/百万操作）。

## Workflows

官方公告的计费开始日前，step 与 storage 用量不计费。

## D1

Free 和 Paid 都可用。按 rows read / rows written / storage 计：rows read 按扫描行数（全表扫描 5000 行 = 5000）；rows written 按 INSERT/UPDATE/DELETE 贡献行数；索引会额外多写一行（索引行）；存储按月每 GB、账户所有库合计；**无 egress 费**；读副本不额外收费（同价按 rows_read/rows_written）；Free 限额每日重置，Paid 月度额度按订阅日重置。

## Durable Objects

### Compute billing

按 wall-clock duration 计费（DO 活跃运行或 idle 但不可 hibernate 时）；idle 可 hibernate 的 DO 不计 duration。计费维度超额部分向上取整到计费单位。RPC session：每次 RPC 方法调用 = 1 request；返回 stub 上的后续调用属同一 session 不重复计。WebSocket：建连计 1 request；计费口径上入站 WS 消息按 20:1 折算 request（100 条消息 = 5 requests）；`setWebSocketAutoResponse()` 的自动应答不计。Duration 按 128 MB 内存配额计（无论实际用量），同 isolate 多 DO 实例共享内存仍按每实例 128 MB 计。建议用 WebSocket Hibernation API 避免连接期间持续计 duration。

### Storage billing

Storage API 仅 DO 内可用。两种后端：
- **SQLite-backed（推荐）**：Free 层只能创建/访问 SQLite-backed DO；rows read/written 限额与费率对齐 D1；kv 方法（get/put/delete/list）按底层隐藏 SQLite 表的行读写计费；每次 setAlarm() 计 1 行写；删除计行写；数据删除前持续计存储。
- **Key-value backed**：仅 Paid；request unit = 4KB 读写（9KB 写 = 3 units）；list 按检查数据量计读 unit；setAlarm = 1 写 unit；删除不计费。

## Vectorize

仅 Paid。公式 `((queried + stored vectors) * dimensions * ($0.01/1M)) + (stored * dimensions * ($0.05/100M))`；例：10,000 条 768 维向量 + 每日 1,000 次查询 ≈ $0.31/月（不含月度免费额度部分）。

## R2

按存储总量 + 两类操作计费：Class A（改状态，较贵）/ Class B（读状态）。**egress 带宽零费用**。

## Containers

容器每活跃 10ms 计费（费率表未抓到），含于 $5/月 Workers Paid 的月度额度内；按用量付——请求到达或手动启动才开始计费，容器休眠后停止计费（可自动超时休眠）。Containers 出口流量单独定价（费率表未抓到）。

## Service bindings

Worker→Worker 经 Service Binding 调用不收额外 request 费：计 1 request（初始调用）+ 两者 CPU 时间合计——鼓励拆多个 Worker 不加钱。

## Fine Print

Workers Paid 与其他 Cloudflare plan（Free/Pro/Business）相互独立；只有命中 Worker 的请求计入限额与账单；Workers 在 Cloudflare cache 之前运行，缓存同样产生请求成本。

---

## 抓取要点速记（本次分析的中间结论）

1. Paid = $5/月起步（minimum charge），含各产品月度免费额度（具体额度数字在丢失的表格里，需补抓核实）。
2. 无 egress 费是全产品线反复强调的点（Workers/KV/D1/R2/Queues 均注明）。
3. 静态资源请求免费不限量 → 小型全栈站（静态为主 + 少量动态）在 Paid 下也极便宜。
4. Free 层限额每日重置（00:00 UTC），超限报错（不是照常服务再扣费）。
5. 页面明确有 Containers 产品（2026-08 仍标注计费细节），需另查 GA/beta 状态。
