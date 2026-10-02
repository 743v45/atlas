# 轻量部署方案 · 横评

> **TL;DR**：一台 Linux VPS 跑几个到十几个小服务，轻量默认解是 **systemd 裸进程**（adopt，无中间层）；要容器则 **Docker 基线 / Podman daemonless 替代**；微型 PaaS 与 Kamal 都是把 Docker **藏起来**而非绕开；托管路线把运维心智换成钱与绑定，其中 **Cloudflare Workers** 是轻量极点但要求按平台形态重写应用。系统容器（LXC/Incus）对本类别的根问题判 hold——它的部署单元是完整环境，不是应用。

## 口径（先读这个，否则对比失真）

1. **部署目标 = 自有 Linux VPS 或托管平台**；桌面端（macOS/Windows）体验不参与裁决——Docker 的「重」几乎全在桌面 VM（常驻 2 GB+），Linux 服务器侧 dockerd 空闲仅 ~60–180 MB（[docker](docker/) 报告）。口径不对齐会让裸进程类因「桌面端不存在」天然占优。
2. **轴 = 资源占用 + 运维心智**（轻量化），不是「哪个更强大」。K8s 等多机编排系统不在列（个人小服务场景的反向轻量化，见 [decision-tree.md](decision-tree.md) 落选节点）。
3. **数据时点 2026-10-02**：star/版本为 gh 当日采集，价格注查询日期，性能数据注明出处与环境；各行数据出处见该列条目 `report.md`（基本信息/风险节），横评不逐格重复标注。
4. **托管平台运维门槛口径**：零 = 纯 PaaS/请求驱动、无基础设施概念（Railway/Render/Workers）；低 = 有机器或平台概念但无需碰 OS（Fly.io）。

## 属性对比矩阵

| 维度 | systemd | pm2 | Docker | Podman | LXC/Incus | Kamal | Dokku | CapRover | Coolify | Fly.io | Railway | Render | CF Workers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **verdict** | **adopt** | trial | **adopt**¹ | trial | hold | trial | trial | trial | trial | trial | trial | trial | trial |
| 形态 | 进程管理器 | 进程管理器 | 容器引擎 | 容器引擎 | 系统容器 | 声明式工具 | 微型PaaS | 微型PaaS | 微型PaaS | 托管平台 | 托管平台 | 托管平台 | 边缘运行时 |
| 资源占用 | 极低 | 低 | Linux低/桌面VM高 | 低 | 中 | 极低 | 中（1GB门槛） | 低 | 高 | 按量微VM | 按量容器 | 托管实例 | isolate按请求 |
| 空闲常驻（实测口径） | ≈0（daemon RSS 0） | ~30–100 MB | ~60–100 MB | 0（daemonless） | ~16 MB/容器 | 14.2 MB（kamal-proxy） | dockerd+nginx+容器 | ~300–400 MB | ~885 MB（7容器） | — | — | — | — |
| 最低门槛 | 现成 Linux | Node.js | Linux | Linux | Linux | 1GB VPS | 1GB RAM（官方） | 1GB RAM（官方） | 2GB RAM（官方） | $2.23/月起 | $5/月 | $0 免费层 | $0 免费层 |
| 运维门槛 | 低 | 低 | 中 | 中 | 中 | 中 | 低-中 | 低 | 低 | 低 | 零 | 零 | 零 |
| 自托管 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 否 | 否 | 否 | 否 |
| 多应用 | 多应用 | 多应用 | 多应用 | 多应用 | 多应用 | 多机编排 | 多应用 | 多机编排 | 多机编排 | 多应用 | 多应用 | 多应用 | 多应用 |
| 成本 | 免费开源 | 免费开源 | 开源免费（Desktop收费） | 免费开源 | 免费开源 | 免费（自付VPS） | 免费（MIT+Pro） | 免费开源（+PRO） | 免费（Cloud $5起） | 按量~$2.2/月 | $5/月起 | 免费层+$7/月起 | 免费层+$5/月 |
| **Docker 依赖** | 无 | 无 | 本体 | 无 | 无 | **硬依赖** | 藏 | 藏 | 藏 | 平台托管 | 平台托管 | 平台托管 | 不适用（isolate） |
| 维护健康（2026-10） | 优（发行版级） | 优（v7，issue响应慢） | 优 | 优（CNCF） | 良（Incus社区主线） | 良（回应偏慢） | 弱（Bus Factor≈1） | 弱（回升中仍单人） | 中（火热但单人+安全响应） | 中（公司转向AI agent） | 良（Series B） | 良（$1.5B估值） | 优（Cloudflare） |
| 锁定度 | 无 | 无（Node绑定） | 行业标准反锁人 | 无 | 低 | 低（yaml自带） | 中 | 中 | 中（停用应用照跑） | 高 | 高 | 高 | 最高（重写） |

¹ docker 的 adopt 限定域：**Linux 服务器侧单机多应用**——「轻量轴的真实对手不是 Docker 本体而是桌面端体验」，见其报告双视角论证。

### 空闲常驻内存阶梯（本横评的核心证据线）

```
systemd ≈0 ── Podman 0 ──┬── Kamal 14.2 MB ── LXC ~16 MB/容器 ──┬── PM2 ~30–100 MB ── dockerd ~60–100 MB ──┬── CapRover ~300–400 MB ── Coolify ~885 MB
                          └（daemonless，无常驻）                  └（完整用户态，介于进程与 VM 之间）              └（+桌面端 Docker Desktop 另算：VM 常驻 2 GB+）
```

来源口径：systemd/PM2 为 Empellio 2026-03 基准（t3.small/Ubuntu 22.04，厂商非中立已注明）；dockerd 140–180 MB 为 2026 年多博客一致口径；kamal-proxy 14.2 MB 与 Coolify 885.6 MB 同出 ecn-apps 2026 三方基准（Kamal v2.2.0/Ubuntu 24.04）；CapRover 300–400 MB 为 MassiveGRID 2026-02 实测；LXC ~16 MB 为 Proxmox 社区实测。各条目报告已分别标注性质与出处。

## 三个关键洞察

1. **轻量轴的真正对手是「中间层」，不是功能**。从裸进程到面板 PaaS，空闲常驻跨了三个数量级（0 → 885 MB）。systemd 的 adopt 不是情怀：发行版自带、Restart 自愈与 journalctl 开箱即得，代价仅是「自己写 20 行 unit」——这笔一次性心智支出换来零中间层。
2. **微型 PaaS 和 Kamal 是「藏 Docker」，不是「绕 Docker」**。dokku/caprover/coolify 安装即 docker run，kamal SSH 上去装 Docker——凡要 PaaS 体验，Docker 一层省不掉，省掉的只是「亲手操作它」。真正绕开 Docker 的只有两条路：进程级（systemd/pm2）或另一形态（lxc 系统容器）。
3. **托管平台把运维心智换成钱与锁定**。零运维的代价梯度清晰：Railway/Render 按月订阅（$5/$7 起，注意 Railway「超 $5 按全额收」悬崖与 Render 免费层 15 分钟休眠）；Fly.io 给「真机器手感」但公司 2026-07 转向 AI agent、平台承诺「不关」；Workers 运维为零、免费层可真用，但应用必须按 isolate 形态写——已有 Node 服务不能原样迁移，是全部条目里锁定最深的。

## 分层决策导览

- **VPS 自托管、进程级够用** → [systemd](systemd/)（+ Caddy 反代自动 HTTPS）
- **Node 生态要快速上线/cluster mode** → [pm2](pm2/)（接受一层 daemon）
- **要容器隔离/镜像可复现** → 基线 [Docker](docker/)；新装机、无存量 Docker 生态 → [Podman](podman/)（quadlet 把容器声明为 systemd unit，两条路线在此合流）
- **要 PaaS 体验（藏 Docker）** → CLI 极简 [Dokku](dokku/) / Web 面板 [Coolify](coolify/)（最热，2GB 底线+守暴露面）/[CapRover](caprover/)（老牌一键应用）；要声明式+零停机 → [Kamal](kamal/)
- **整机环境隔离/多发行版** → [LXC/Incus](lxc/)（轴外适用域，hold）
- **不碰服务器** → 微 VM [Fly.io](flyio/) / 全托管 [Railway](railway/)·[Render](render/) / 新写小服务直上 [CF Workers](cloudflare-workers/)

<!--gen:decision-matrix-->

## verdict 一致性

横评结论与各条目 verdict 一致：adopt 两条（systemd=轻量默认解；docker=Linux 服务器侧基线）在决策导览中分别对应「进程级够用」与「要容器」两问的默认答案；hold 一条（lxc）的适用域已写明在类别轴外；其余 trial 的适用域见各条目 TL;DR。矩阵总分排序与 verdict 的关系（workers 高分 trial、dokku 低分 trial 等）见 decision.json 的必读注记——矩阵只覆盖所列六维，维度外风险（重写成本、Bus Factor、安全暴露面、适用域错配）以各条目 verdict 为准。

## 变更记录

| 日期 | 说明 |
|---|---|
| 2026-10-02 | 首次横评：13 条目、属性矩阵 + 决策矩阵 + 设计树（源自「不用 docker 部署用什么部署，有没有轻量化点的」会话） |
