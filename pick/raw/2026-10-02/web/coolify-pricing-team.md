# Coolify Cloud 定价 + 维护团队集中度（2026-10-02 采集）

## 一、定价（Wayback 快照 2026-09-20 的 coolify.io/pricing）

- 快照 URL：http://web.archive.org/web/20260920125737id_/https://coolify.io/pricing
- 访问日期：2026-10-02（curl 抓取存 /tmp/coolify_pricing.html 后文本化）

### Self-hosted（自托管）
- **Free Forever**：Deploy Coolify on your infrastructure without any restrictions on features
- Full access to all features / No limitation or restrictions
- Community support (19+ members)
- Automated or Self-managed updates
- Includes all upcoming features
- 导航栏「Community (20k+)」——社区规模 20k+（Discord）

### Coolify Cloud（官方托管面板）
- **$5/month 基础价（connect 2 servers）+ $3/month 每加一台服务器**
- 年付 save 20%
- 模式：Just connect your servers, Coolify runs on our managed infrastructure
- 你自己的服务器（Hetzner/DO/AWS/树莓派/旧笔记本均可）跑应用，面板由官方托管
- Founder-tested updates / Managed updates / Managed email alerts
- Teams Unlimited / Team Members Unlimited / Connected Servers Unlimited

### FAQ 要点
- Cloud 基于 open-source version；取消订阅后应用不受影响（面板停，应用照跑——与 README「If you stop using Coolify, your running resources continue to work」一致）

## 二、维护团队集中度（gh api contributors，2026-10-02）

`gh api repos/coollabsio/coolify/contributors?per_page=100&anon=true` → 前 100 名：

| 贡献者 | 提交数 |
|---|---|
| **andrasbacsai（创始人 Andras Bacsai）** | **12,909** |
| peaklabs-dev | 1,853 |
| ShadowArcanist | 226 |
| github-actions[bot] | 145 |
| adiologydev | 83 |

- 创始人提交数 = 第二名的 **~7 倍**，占前 100 名总提交的绝对大头
- → 「单维护者/小团队依赖」风险成立：核心代码主要由创始人一人维护
- raw 数据同日存于 raw/2026-10-02/gh/coollabsio_coolify.json（repo 元信息）与 coollabsio_coolify_releases.json（release 序列）
