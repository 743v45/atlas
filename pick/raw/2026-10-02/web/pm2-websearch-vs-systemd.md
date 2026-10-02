# pm2 vs systemd 社区共识 WebSearch 检索留档

- 来源: WebSearch（检索词 `pm2 vs systemd node.js production 2025 2026 which to use tradeoffs`）
- 访问日期: 2026-10-02

## 主要来源

1. **PM2 vs systemd for Node.js Services: 2026 Production Guide** (https://khimananda.com/blog/pm2-vs-systemd-for-node-js-services)
   - 「For most production environments, systemd is the better choice…due to native kernel integration」
   - PM2 跑一个独立 daemon，**~30–50MB RAM 开销**；systemd 经 cgroups 直接管服务，「essentially no extra footprint」
   - systemd 免费获得 boot ordering、依赖管理（`After=`/`Requires=`）、沙箱加固（`ProtectSystem=`/`PrivateTmp=`）
2. **Node.js Process Management: PM2 vs systemd vs Docker** (https://www.resumelens.org/blog/nodejs/nodejs-pm2-vs-systemd-process-mgmt)
   - 对比 restart policies、log rotation、**zero-downtime reloads**、cluster mode——pm2 传统强项
3. **Process Manager Comparison 2026: PM2, Systemd, Supervisor** (https://dev.to/empellio/process-manager-comparison-2026-pm2-systemd-supervisor-oxmgr-and-more-4e0p)
   - 同硬件 benchmark 对比；称 PM2 为「the industry standard for Node.js」但如实记录对新替代品的取舍
4. 反方观点：**Stop Using PM2 in Production** (https://dflow.sh/blog/stop-using-pm2-in-production-why-your-nodejs-app-deserves-better)、**Think Twice Before Using PM2** (https://nodevibe.substack.com/p/think-twice-before-using-pm2-a-critical-look-at-the-popular-tool)
   - 「PM2 was designed as a dev tool」；systemd cgroups 资源限制比 `--max-memory-restart` 更可靠

## 权衡总结表（检索结果原文）

| 因素 | PM2 | systemd |
|---|---|---|
| 零停机 reload / cluster mode | ✅ 内置 (`pm2 reload`, cluster) | ❌ 手动（socket activation / 应用层自己做） |
| 内存开销 | ❌ ~30–50MB daemon | ✅ 无（内核管理） |
| 资源限制 (cgroups) | 基础 (`--max-memory-restart`) | ✅ 硬 cgroup 强制 (`MemoryMax=`, `CPUQuota=`) |
| 开机自启 / 依赖 | 配置式，boot 时脆弱 | ✅ 原生 ordering、`Restart=always`、`WatchdogSec` |
| 学习曲线 / DX | ✅ 熟悉的 CLI (`pm2 logs`, `pm2 monit`) | 陡；unit file 语法 |
| 日志管理 | 内置 `pm2 logs` | journald（需熟悉） |
| 单机多应用 | ✅ 逐应用管理方便 | 每应用一个 unit file |

## 实践结论（检索结果引述）

- 「Push to prod fast, one box, need clustering」→ PM2 合适
- 「Long-lived, hardened, ops-team-managed services」→ systemd（多核用应用内原生 cluster module）
- 容器化/K8s → 两者都不用
