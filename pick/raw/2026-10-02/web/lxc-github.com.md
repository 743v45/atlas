# gh api 一手数据 — LXC / Incus / LXD 三仓库对比

- 来源：GitHub API via `gh api`（api.github.com）
- 访问日期：2026-10-02
- 采集命令：`gh api repos/lxc/incus`、`gh api repos/lxc/incus/releases/latest`、`gh api repos/lxc/lxc`（+releases/latest）、`gh api repos/canonical/lxd`（+releases/latest）

## lxc/incus（本条目主对象）

```json
{"created_at":"2023-07-22T12:43:13Z","description":"Powerful system container and virtual machine manager","full_name":"lxc/incus","license":"Apache-2.0","open_issues":36,"pushed_at":"2026-10-02T09:22:30Z","stars":6310}
```

latest release：

```json
{"name":"Incus 7.5.1","published_at":"2026-09-25T01:18:04Z","tag_name":"v7.5.1"}
```

- stars 6,310（2026-10-02 gh 采集）；push 2026-10-02（当日仍在推）；open issues 36（偏低，活跃但积压少）
- 许可证 Apache-2.0；创建于 2023-07-22（LXD 社区分叉时间点吻合）
- 最新 release：v7.5.1，发布 2026-09-25（一周前，feature 线节奏月度级）

## lxc/lxc（底层 LXC 工具，上游）

```json
{"description":"LXC - Linux Containers","full_name":"lxc/lxc","license":"NOASSERTION","pushed_at":"2026-10-02T08:32:42Z","stars":5266}
```

```json
{"published_at":"2026-04-30T01:30:36Z","tag_name":"v7.0.0"}
```

- stars 5,266；push 2026-10-02；GitHub 未识别 SPDX（上游为 LGPL-2.1-or-later，仓库 LICENSE 为自定义拼接文本）
- 最新 release：v7.0.0（2026-04-30）——LXC 上游已到 7.0 大版本线
- 定位：C 语言底层容器工具（lxc-start/lxc-stop 等），Incus/LXD 均以其 liblxc 为运行时底座之一

## canonical/lxd（Canonical 接管后的 LXD）

```json
{"archived":false,"description":"Powerful system container and virtual machine manager","full_name":"canonical/lxd","license":"AGPL-3.0","pushed_at":"2026-10-02T14:58:30Z","stars":4833}
```

```json
{"published_at":"2026-06-23T08:38:37Z","tag_name":"lxd-6.9"}
```

- stars 4,833；push 2026-10-02（仓库未死、仍在推）；许可证 AGPL-3.0（对比 Incus Apache-2.0）
- GitHub latest release：lxd-6.9，2026-06-23——距采集日 3 个多月无新 tag（对照 Incus 同期已发 7.5.1，2026-09-25）
- 未 archived，仍在维护，但社区主线已明确移至 Incus（linuxcontainers.org 的 LXD 页挂迁移声明）
