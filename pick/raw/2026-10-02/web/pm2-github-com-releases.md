# pm2 releases 与 v7.0.0 release notes 留档（同步写入 raw/2026-10-02/gh/pm2-releases.json）

- 来源 URL: https://api.github.com/repos/Unitech/pm2/releases（经 `gh api`）与 https://github.com/Unitech/pm2/releases/tag/v7.0.0
- 访问日期: 2026-10-02

## release 时间线（近 15 个）

| tag | 发布日期 |
|---|---|
| v7.0.4 | 2026-08-24 |
| v7.0.3 | 2026-06-29 |
| v7.0.2 | 2026-06-29 |
| v7.0.1 | 2026-05-02 |
| v7.0.0 | 2026-05-02 |
| v6.0.14 | 2025-11-26 |
| v6.0.13 | 2025-09-22 |
| v6.0.12 | 2025-09-22 |
| v6.0.11 | 2025-09-11 |
| v6.0.10 | 2025-09-02 |
| v6.0.9 | 2025-09-01 |
| v6.0.8 | 2025-06-05 |
| v6.0.7 | 2025-06-05 |
| v6.0.6 | 2025-05-13 |
| v6.0.5 | 2025-03-15 |

## v7.0.0 release notes 摘录（原文要点）

- Breaking: Require Node.js >= 18.0.0 (dropped Node.js 16 support)
- Core Refactor: Internalize pm2-axon, pm2-axon-rpc, pm2-io-bpm, pm2-io-agent, fclone as local modules (reduced supply chain surface)
- Add Bun runtime support (ProcessContainerBun.js, ProcessContainerForkBun.js)
- Replace `needle` with native `fetch`；replace enquirer/promptly/mkdirp/source-map-support/sprintf-js 等为内置实现
- Security: CVE-2025-5891 ReDoS fix；CVE-2026-27699 proxy-agent/basic-ftp 升级；3 处 command injection 修复（exec()→execFile()）；prototype pollution 修复（Configuration.set/unset）
- Bug Fixes: TreeKill 重写（消除竞态）；Windows home path 修复
- Dependencies: 新增 OpenTelemetry tracing 直接依赖；pidusage 3.0.2→4.0.1；ws ^8.18.0
- Testing: Docker 并行测试 runner（Node.js + Bun）；Windows test suite；CI matrix Node 18/20/latest
