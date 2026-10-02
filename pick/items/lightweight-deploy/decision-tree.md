# 轻量部署方案 · 选型设计树

> 根问题的决策路径。叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

个人/小团队的几个到十几个小服务，部署到一台自有 Linux VPS 或托管平台，选什么部署方案——轻量化（资源占用 + 运维心智）为轴？（源自 2026-10-02 会话「不用 docker 部署用什么部署，有没有轻量化点的」）

## 分叉与决策

### D1 自有 VPS 还是托管平台？（拥有 vs 租心智）

- **不想碰任何服务器/基础设施** → 托管三路线，按抽象层级分（转 D2'）。
- **自有 VPS（数据/成本/控制权在手）** → 转 D2。
- 托管叶子与分叉见 D2'。

### D2 容器隔离/镜像可复现是刚需吗？（VPS 侧第一分叉）

- **不需要，进程级部署够用** → systemd 是轻量默认解：发行版自带零安装、daemon RSS 0、Restart=always 自愈 + journalctl，配 Caddy 反代自动 HTTPS 即完整闭环；代价是仅 Linux、无隔离无镜像。
  - 叶：[systemd](systemd/) adopt
  - 若是 Node 生态、要 cluster mode/零停机 reload/npm 装完即用 → pm2；接受一层常驻 daemon（30–100MB、有泄漏史）与 systemd 功能重叠。
  - 叶：[pm2](pm2/) trial
- **要容器（环境隔离/镜像可复现/交付物标准化）** → 转 D3。

### D3 容器生命周期谁来管？（直管 vs 体验层）

- **自己直管容器** → 基线是 Docker（行业默认、compose 生态、可复现性；adopt 限定 Linux 服务器侧——桌面端 VM 2GB+ 是另一回事）；新装 Linux 机且无存量 Docker 生态选 Podman（daemonless 空闲 0、quadlet 把容器声明为 systemd unit，与 D2 的 systemd 路线在此合流；新装机场景可按 adopt 用）。
  - 叶：[Docker](docker/) adopt
  - 叶：[Podman](podman/) trial
  - 整机环境隔离/多发行版/快照回滚（部署单元=完整环境而非应用）→ LXC/Incus——适用域在本类别根问题轴外，故 hold；反转条件见其报告。
  - 叶：[LXC/Incus](lxc/) hold
- **要体验层（PaaS 手感/声明式，Docker 被藏起来而非绕开）** → 转 D4。

### D4 体验层三派（交互形态分叉）

- **CLI 极简派（git push 即部署、buildpack 免写 Dockerfile）** → Dokku；官方 1GB 硬门槛 + Bus Factor≈1（35 倍 commit 差）是两个未消化前不升 adopt 的闸门。
  - 叶：[Dokku](dokku/) trial
- **Web 面板派** → Coolify（最热 ⭐62.5k、300+ 一键服务、多机编排；2GB 资源底线 + 面板 root 级攻击面须守暴露面纪律）或 CapRover（老牌 360 一键应用、2026 维护回升；bus factor=1）。
  - 叶：[Coolify](coolify/) trial
  - 叶：[CapRover](caprover/) trial
- **声明式配置派（deploy.yml + 一条命令零停机，配置进 repo 可审计）** → Kamal；Docker 是硬前提（不用管、没绕开）。
  - 叶：[Kamal](kamal/) trial

### D2' 托管三路线（抽象层级分叉）

- **新写 API/全栈 JS 小服务、可按平台形态设计应用** → CF Workers：轻量托管轴的极点（isolate 零运维、免费层 10 万请求/日可真用、KV/D1/R2 状态内置）——前提是接受「按 isolate 重写」，已有 Node 服务不能原样迁移，锁定全场最深。
  - 叶：[Cloudflare Workers](cloudflare-workers/) trial
- **要「真机器手感」（VM 可 SSH、按秒计费、全球分布）** → Fly.io：Firecracker 微 VM ~$2.23/月起；免费额度已死（2024-10）、2024 Q4 连环故障、2026-07 公司转向 AI agent——非关键路径试用。
  - 叶：[Fly.io](flyio/) trial
- **纯 PaaS 沙箱、git push 零心智** → Render（免费起步默认解：免费层+托管 PG；15 分钟休眠/免费 PG 30 天过期/带宽 5GB 三重限制）或 Railway（体验标杆：PR 预览环境、模板市场；$5/月含 $5 额度但「超 $5 按全额收」悬崖）。
  - 叶：[Render](render/) trial
  - 叶：[Railway](railway/) trial

## 落选节点（不指向条目的死分支——「为什么没选 X」的记忆）

- **supervisord**：同赛道进程管理器，被 systemd 正面覆盖——Empellio 2026-03 基准 daemon RSS ~31MB vs systemd 0，无差异化功能胜点，不立目。
- **Kubernetes/k3s/Docker Swarm（独立编排）**：个人小服务场景的反向轻量化——多机编排系统解决「很多机器很多团队」的问题，单机引入即纯增心智；CapRover 内含 Swarm 但那只是其实现细节。
- **Firecracker（直接自建）**：microVM 技术本身是多租户基建，个人借道 Fly.io 使用即可（D2' 第一叶），无自建必要。
- **Easypanel / Dokploy / Coolify 系后起之秀**：与 Coolify 同赛道（Web 面板微 PaaS），Coolify 已是该形态事实代表（⭐62.5k），无独立立目的差异化证据——观察名单，若格局变化再评估。
- **LXD**：LXC 条目内按亚种规则正文小节记载（Canonical 接管后社区主线是 Incus，2026-06 起 release 停滞于 lxd-6.9），不独立立目。
- **Docker Desktop / OrbStack 等桌面容器**：口径排除——本横评部署目标锚定 Linux VPS/托管平台，桌面体验不参与裁决（comparison.md 口径第 1 条）。

## 决策矩阵一致性

加权排序（comparison.md 注入表）：systemd 112 > podman 107 > workers 105 > docker = pm2 100 > kamal 96 > render 95 > caprover = railway 91 > lxc = dokku 90 > flyio 87 > coolify 85。两条 adopt 落位一致（systemd 第一=轻量默认解；docker 第四但 adopt 限定 Linux 服务器侧基线域）；workers 高分 trial 是「重写前提+锁定」不在矩阵内的两层分工；lxc/dokku/flyio/coolify 靠后是根问题适配度排序，非否定其自身适用域（decision.json note）。
