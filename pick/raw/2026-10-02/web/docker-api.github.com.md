# gh api moby/moby 原始响应留档

- 来源：`gh api repos/moby/moby` + `gh api repos/moby/moby/releases/latest`
- 访问日期：2026-10-02（Tapevas 时区当晚；UTC 响应时间戳见下）

## repos/moby/moby（节选字段）

```json
{
  "archived": false,
  "full_name": "moby/moby",
  "license": "Apache-2.0",
  "open_issues": 3913,
  "pushed_at": "2026-10-01T20:55:12Z",
  "stars": 72144
}
```

## repos/moby/moby/releases/latest

```json
{
  "name": "v29.8.2",
  "published_at": "2026-09-30T20:28:33Z",
  "tag_name": "docker-v29.8.2"
}
```

## repos/docker/compose（2026-10-02 同场补采）

```json
{
  "license": "Apache-2.0",
  "pushed_at": "2026-10-02T10:33:27Z",
  "stars": 38278
}
```

```json
{ "tag_name": "v5.5.1", "published_at": "2026-09-03T15:53:28Z" }
```

- compose 已到 v5 代（2026-09 发布 v5.5.1），⭐38,278，当日仍在推送

## 解读（采集时快照）

- stars：72,144（gh 2026-10-02 采集）
- pushed_at：2026-10-01（采集前一天仍在推送，活跃）
- 最新 release：v29.8.2，2026-09-30 发布——tag 前缀 `docker-v` 是 Moby 仓库惯例（上游含非 Engine 组件）
- license：Apache-2.0（SPDX）
- 注：moby/moby 是 Docker Engine（daemon）的上游开发仓库；发布到 download.docker.com 的 Docker Engine（社区版）与该仓库的 release 节奏对应
