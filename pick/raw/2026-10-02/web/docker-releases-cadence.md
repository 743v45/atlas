# gh api moby/moby releases（近 15 条，发布节奏留档）

- 来源：`gh api repos/moby/moby/releases?per_page=15`
- 访问日期：2026-10-02

## 原始数据（docker-v* 系，client/api tag 为 Moby 多组件仓库惯例）

| tag | published_at (UTC) |
|---|---|
| docker-v29.9.0-rc.1 | 2026-10-01 |
| docker-v29.8.2 | 2026-09-30 |
| docker-v29.8.1 | 2026-09-15 |
| docker-v29.8.0 | 2026-09-03 |
| docker-v29.7.2 | 2026-08-06 |
| docker-v29.7.1 | 2026-07-31 |
| docker-v29.7.0 | 2026-07-30 |
| v25.0.18 | 2026-09-30 |
| api/v1.56.0 / client/v0.6.0 | 2026-09-03 |
| api/v1.56.1 / client/v0.6.1 | 2026-10-01 |

## 解读

- 当前版本线 **29.x**（2026 下半年），功能版约**月度**节奏（v29.7.0 7/30 → v29.8.0 9/3 → v29.9.0-rc 10/1），补丁版随时出
- v25 分支（2023 年的版本线）2026-09-30 仍在出补丁（v25.0.18）——旧版本线有维护期
- 仓库同发 client / api 组件 tag（Moby 拆分的 CLI 与 API 模块），非 Engine 本体版本
