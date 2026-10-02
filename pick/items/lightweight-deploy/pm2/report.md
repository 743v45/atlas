# PM2

> **TL;DR**：Node 生态上手最快的进程管理器：npm 装完即用，cluster mode 与零停机 reload 内置，pm2 startup+save 覆盖六种 init 系统开机自启——代价是多一层常驻 God daemon（基线约 30–100MB、有泄漏史 open issue）且与 VPS 上已有的 systemd 功能重叠；快速上线的 Node 单机多应用适用，长期加固运维场景 systemd 更轻。

- **结论**：trial（适用域：**快速上线的 Node 单机多应用**；差异价值集中在 cluster mode、零停机 reload 与统一 CLI——若这些不需要，systemd 是更轻的默认）
- **核实日期**：2026-10-02（gh 一手数据 + npm registry + 官方文档当日核实）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v7.0.4（2026-08-24 发布）；v7.0.0 大版本 2026-05-02，要求 Node ≥ 18，新增 Bun 运行时支持 | [2][3] |
| 许可证 | AGPL-3.0（npm `license` 字段与仓库 LICENSE 文件一致；gh API 因文件名报 NOASSERTION） | [1][3] |
| 仓库 | https://github.com/Unitech/pm2 | — |
| 维护活跃度 | ⭐43,297、push 2026-09-04、open issues 1,105（gh 2026-10-02 采集）；月下载 14,020,856（2026-09，npm） | [1][3] |
| 商业化 | PM2 Runtime 免费开源；PM2 Plus 监控 SaaS $79/月起、无免费档（© 2014-2026 PM2） | [10] |

## 为什么 trial（三条立得住的强项）

1. **上手最快、心智最少**：`npm install -g pm2 && pm2 start app.js` 即完成接管，`pm2 logs`/`pm2 monit`/`pm2 status` 一套 CLI 覆盖日常运维——个人小团队「推上去就跑」的路径里没有比它更短的 [4][12]。对比 systemd 需要为每个应用写 unit file 并学习其语法 [9]。
2. **cluster mode 与零停机 reload 是内置的**：`pm2 start app.js -i max` 自动按全部 CPU 扩展网络型 Node 应用，「without any code modifications」；`pm2 reload` 实现「0-second-downtime reload」，失败超时自动回退普通重启 [4]。这在 systemd 路线里要靠 socket activation 或应用层自研，是 pm2 相对 systemd 最实的差异点 [9]。
3. **开机自启与恢复全 init 覆盖**：`pm2 startup` 自动检测 init 系统（systemd/upstart/launchd/openrc/rcd/systemv 六种）生成自启脚本，`pm2 save` 固化进程列表、重启后 `resurrect` 恢复 [5]。v7 线维护健康：2025-03 至 2026-08 间 15 个 release，v7.0.0 主动做了供应链收敛（内部化 pm2-axon 等 5 个依赖）并修复 3 处命令注入与原型污染漏洞 [2]。

## 为什么不是 adopt（轻量化轴上的三层代价）

1. **多一层常驻 God daemon**：pm2 以独立 Node daemon 管理应用，自身基线内存多来源口径为 ~30–100MB RSS——Stack Overflow 口径 ~27MB（应用全停时）[8]、2026 生产指南口径 ~30–50MB [9]、Reddit Hostinger VPS 实测 ~95MB [11]。systemd 经 cgroups 直接管进程，「essentially no extra footprint」[9]。对小内存 VPS（512MB–1GB）这是 5–20% 的固定税。
2. **daemon 泄漏史且处置不积极**：issue #6113（v6.0.14，2026-05-16 建）报告 daemon 22 天涨至 ~5.7GB RSS（websocket 高频、17 进程场景），**至今 open、仅 1 条评论** [6]；issue #5145（v5.1.0，2021-08 建，daemon 230MB 占 512MB 机器一半）**open 近 5 年未关** [7]。长生命周期 daemon 的内存卫生是 pm2 的结构性风险，`max_memory_restart` 只管应用进程、管不了 daemon 自身 [8]。
3. **与 systemd 功能重叠、社区共识偏向后者**：2026 年社区对比的共识是「多数生产环境 systemd 更优」——原生 boot ordering、`Restart=always`、cgroups 硬资源限制（`MemoryMax=`/`CPUQuota=`）与沙箱加固全是内核级白给能力 [9]；反方评论甚至认为「PM2 was designed as a dev tool」[9]。自有 Linux VPS 上 systemd 必然已存在，选 pm2 意味着维护两套进程管理体系的心智重叠。

## 对比（vs systemd，本类别核心对手）

| 维度 | PM2 | systemd |
|---|---|---|
| daemon 额外开销 | ~30–100MB 常驻 + 泄漏史 [6][8][9][11] | 无（cgroups 内核直管）[9] |
| cluster mode / 零停机 reload | ✅ 内置（`-i max` + `pm2 reload`）[4] | ❌ 手动（socket activation / 应用层）[9] |
| 资源限制 | 基础（`--max-memory-restart`，仅应用进程）[8] | ✅ 硬限制（`MemoryMax=`/`CPUQuota=`）[9] |
| 开机自启 | `pm2 startup`+`save`，覆盖六种 init [5] | 原生 unit + 依赖排序 [9] |
| 日志 | `pm2 logs` 内置直读 [4] | journald（需另行熟悉）[9] |
| 上手路径 | npm 全局装、CLI 即用 [4] | 每应用写 unit file [9] |
| 生态绑定 | Node 为主（v7 兼 Bun），可跑任意进程 [2] | 语言无关 |

同类横评维度并排见 `../comparison.md`（如已建）。定位口径（社区共识 [9]）：快速上线、单机、需要 clustering → PM2 合适；长生命周期、加固、运维团队管理 → systemd；容器化 → 两者都不用。

## 风险与注意

- **小内存 VPS 慎用**：daemon 基线 30–100MB 对 512MB 机器占比过高，且 #5145/#6113 两个泄漏 issue 长期 open [6][7][8]——低内存机器上 pm2 定期 `pm2 save && pm2 kill && pm2 resurrect` 刷 daemon 是已知实践（#6113 报告者的临时处置）[6]。
- **AGPL-3.0 传染性**：个人自用无感；若把 pm2 嵌入对外发行的商业软件需评估 AGPL 义务（商业化本身是 Runtime 免费 + 监控 SaaS 收费的双轨，基础部署不涉及付费）[3][10]。
- **Windows 支持弱**：官方 startup 不覆盖 Windows，需第三方 pm2-installer [5]。
- **issue 响应偏慢**：open issues 1,105 [1]，两个标志性内存 issue 长期无人关闭 [6][7]——指望社区快速修 daemon 层问题不现实。
- **无状态前提**：cluster mode 要求应用无状态（session/websocket 外置到 Redis 等），有状态应用上 cluster 前先改造 [4]。
- **daemon 自身内存无上限约束**：待验证——pm2 是否提供限制 God daemon 自身内存的机制（现有检索未见）。

## 来源

1. Unitech/pm2 仓库 — https://github.com/Unitech/pm2（gh 2026-10-02 采集：⭐43,297、push 2026-09-04、open issues 1,105、created 2013-05-21；原始响应留档 raw/2026-10-02/gh/pm2.json）
2. PM2 releases 与 v7.0.0 release notes — https://github.com/Unitech/pm2/releases（gh 2026-10-02 采集：v7.0.4 2026-08-24、v7.0.0 2026-05-02；Node≥18、Bun 支持、CVE 修复与供应链收敛；留档 raw/2026-10-02/gh/pm2-releases.json）
3. npm registry — https://registry.npmjs.org/pm2（2026-10-02 采集：version 7.0.4、license AGPL-3.0、engines node>=18、月下载 14,020,856（2026-09）；留档 raw/2026-10-02/web/pm2-npmjs-registry.md）
4. PM2 官方文档：Cluster Mode — https://pm2.keymetrics.io/docs/usage/cluster-mode/（访问 2026-10-02；留档 raw/2026-10-02/web/pm2-keymetrics-io-cluster-mode.md）
5. PM2 官方文档：Startup Script — https://pm2.keymetrics.io/docs/usage/startup/（访问 2026-10-02；留档 raw/2026-10-02/web/pm2-keymetrics-io-startup.md）
6. GitHub issue #6113 "PM2 God Daemon Memory Leak (6.0.14)" — https://github.com/Unitech/pm2/issues/6113（2026-05-16 建，open；gh 2026-10-02 采集，留档 raw/2026-10-02/gh/pm2-issue-6113.json）
7. GitHub issue #5145 "God Daemon taking up huge amounts of memory" — https://github.com/Unitech/pm2/issues/5145（2021-08-06 建，open；gh 2026-10-02 采集，留档 raw/2026-10-02/gh/pm2-issue-5145.json）
8. Stack Overflow "Should PM2 God daemon always be running" — https://stackoverflow.com/questions/34520775/should-pm2-god-daemon-always-be-running（2026-10-02 检索：daemon 常驻 ~27MB 口径；留档 raw/2026-10-02/web/pm2-websearch-memory.md）
9. PM2 vs systemd for Node.js Services: 2026 Production Guide — https://khimananda.com/blog/pm2-vs-systemd-for-node-js-services（2026-10-02 检索：daemon ~30–50MB 口径与 systemd 对比共识；另含 dflow.sh「Stop Using PM2 in Production」观点；留档 raw/2026-10-02/web/pm2-websearch-vs-systemd.md）
10. PM2 Pricing — https://pm2.keymetrics.io/pricing（访问 2026-10-02：PM2 Plus $79/月起、无免费档、Runtime 免费开源；留档 raw/2026-10-02/web/pm2-websearch-pricing.md）
11. Reddit r/node "PM2 daemon keeps dying on Hostinger premium" — https://www.reddit.com/r/node/comments/1ocoqxd/（2026-10-02 检索：daemon ~95MB 实测口径；留档 raw/2026-10-02/web/pm2-websearch-memory.md）
12. Process Manager Comparison 2026: PM2, Systemd, Supervisor — https://dev.to/empellio/process-manager-comparison-2026-pm2-systemd-supervisor-oxmgr-and-more-4e0p（2026-10-02 检索：「the industry standard for Node.js」定位；留档 raw/2026-10-02/web/pm2-websearch-vs-systemd.md）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-10-02 | trial | 首次记录（gh/npm/官方文档/社区对比当日全量核实） |
