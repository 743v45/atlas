# Coolify star 增速时间序列（Wayback Machine 一手快照）

- 采集方式：web.archive.org CDX API 列出 github.com/coollabsio/coolify 快照，逐快照抓取 HTML 提取 `repo-stars-counter-star` title 值
- 采集日期：2026-10-02
- 快照 URL 模式：`http://web.archive.org/web/<ts>id_/https://github.com/coollabsio/coolify`
- 快照列表来源：`http://web.archive.org/cdx/search/cdx?url=github.com/coollabsio/coolify&from=20250101&to=20261002&filter=statuscode:200&collapse=timestamp:6`（共 21 个快照，2025-01 → 2026-09 每月覆盖）

## 数据点

| 快照时间（UTC） | stars | 备注 |
|---|---|---|
| 2025-01-18 | 36,408 | |
| 2025-04-02 | 39,509 | |
| 2025-07-01 | 42,969 | |
| 2025-10-07 | 45,973 | |
| 2026-01-05 | 49,193 | |
| 2026-04-17 | 53,616 | |
| 2026-07-13 | 59,272 | |
| 2026-09-04 | 61,371 | |
| 2026-10-02 | 62,500 | 当日 `gh api repos/coollabsio/coolify` 实测（raw/2026-10-02/gh/coollabsio_coolify.json） |

## 增速推算（观测值差分，非官方数据）

- 2025 自然年（2025-01 → 2026-01 快照）：+12,785 星/年，月均 ~+1,065
- 2026 前 9 个月（2026-01 → 2026-10）：+13,307 星/9 个月，月均 ~+1,479——**较 2025 年提速约 39%，仍在加速**
- 月度快照序列单调递增，无断档迹象

## 采集备注

- repo stars 计数器取自 GitHub 页面 HTML `<span id="repo-stars-counter-star" title="…">`，为 GitHub 官方页面显示值
- 首次抓取未带 `--compressed` 时返回 gzip 原始体导致 grep 落空，已修正重抓；2025-07-01 快照两种方式结果一致（42,969），交叉验证通过
- 2026-10-02 当日 gh API：⭐62,500、pushed 2026-10-02T15:21:45Z、forks 5,580、open issues 737、Apache-2.0、created 2021-01-25
