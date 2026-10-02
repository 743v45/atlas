# CapRover gh 一手数据汇总

- 来源：`gh api`（api.github.com）
- 采集日期：2026-10-02
- 用途：caprover 条目（lightweight-deploy 类别）

## repo 基础（caprover/caprover）

```json
{"archived":false,"created_at":"2017-10-25T05:00:43Z","description":"Scalable PaaS (automated Docker+nginx) - aka Heroku on Steroids","homepage":"https://CapRover.com","license":"NOASSERTION","open_issues":178,"pushed_at":"2026-09-30T01:22:03Z","stars":15177,"forks":1004}
```

- license 细节：LICENSE 正文为 Apache-2.0（Copyright 2017-2024 BigZee Ventures LLC）+ Appendix（冲突时 appendix 优先）：付费功能不可修改、不可再分发付费版、免费功能的修改须开源分发。→ GitHub 识别为 NOASSERTION/Other。

## releases（近 10 个）

| tag | 日期 |
|---|---|
| v1.15.4 | 2026-08-30 |
| v1.15.3 | 2026-08-20 |
| v1.15.2 | 2026-08-15 |
| v1.15.1 | 2026-08-08 |
| v1.15.0 | 2026-08-05 |
| v1.14.2 | 2026-05-14 |
| v1.14.1 | 2025-11-11（tag 名笔误 "v.14.1"） |
| v1.14.0 | 2025-06-08 |
| v1.13.3 | 2024-12-01 |
| v1.13.2 | 2024-11-09 |

节奏解读：2024 年 2 个、2025 年 2 个（间隔约 5-6 个月）→ 2026 年 8 月单月连发 5 版（v1.15.0-1.15.4），全年明显提速。

## commits 年度分布（search/commits）

| 年 | commits |
|---|---|
| 2023 | 83 |
| 2024 | 158 |
| 2025 | 92（低谷） |
| 2026 | 237（截至 10-02，已超 2025 全年 2.5 倍） |

主分支最新 commit：2026-09-23；pushed_at 2026-09-30。

## 贡献者集中度（contributors 前 15）

| login | contributions |
|---|---|
| **githubsaturn** | **1,837** |
| dshook | 25 |
| ngoyal16 | 20 |
| sidharthv96 | 16 |
| 其余 | ≤8 |

第 1 名是第 2 名的 73 倍。近期 30 个 commit 作者全部为 githubsaturn（2026-10-02 统计）。

## issue 响应抽样（2026-10-02）

- open issues 共 178。
- 2026-09 新开/活跃 issue 多为当天～次日关闭：#2499（2.5h）、#2497（4h）、#2496（7h）、#2495（3h）、#2491（约 1 天）。
- 社区功能建议可能长期无人接：#2408（7 月，0 评论）、#2410（7 月，提议把内置 Netdata 换 Beszel，0 评论）。
- CapRover PRO（付费商业版）存在：`search/issues q="CapRover PRO"` 命中 9 个，如 #2384（open）、#2395、#2392。

## one-click-apps 仓库（caprover/one-click-apps）

- stars 637、pushed_at 2026-09-29、描述 "Community Maintained One Click Apps"
- `public/v4/apps/` 下 **360 个** yml（2026-10-02 实测），样例：wordpress、minio、postgres、mysql、mongo、n8n、ghost、nextcloud、authentik、appsmith、airflow 等
