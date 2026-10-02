# dokku 官方 upgrading 文档（GitHub 仓库 docs/getting-started/upgrading/index.md）

- 来源 URL: https://github.com/dokku/dokku/blob/main/docs/getting-started/upgrading/index.md（即 https://dokku.com/docs/getting-started/upgrading/ ）
- 获取方式: gh api repos/dokku/dokku/contents/docs/getting-started/upgrading/index.md
- 访问日期: 2026-10-02
- 原始解码文件: gh/dokku-upgrading-doc.md（同目录）

## 关键原文

## 不跑 daemon

> "As Dokku does not run any daemons, the security risk introduced by our software is minimal."

（⇒ dokku 自身无常驻进程；VPS 上的常驻 = dockerd + nginx（默认 proxy）+ 各应用容器 + systemd 单元）

## Migration Guides（每代大版本都有迁移指南，共 25 份）

> "Before upgrading, check the migration guides to get comfortable with new features and prepare your deployment to be upgraded."

- Upgrading to 0.38 / 0.37 / 0.36 / 0.35 / 0.34 / 0.33 / 0.32 / 0.31 / 0.30 / 0.29 / 0.28 / 0.27 / 0.26 / 0.25 / 0.24 / 0.23 / 0.22 / 0.21 / 0.20（0.20–0.38 连续每代都有）
- 更早：0.10 / 0.9 / 0.8 / 0.7 / 0.6 / 0.5
- pre 0.3.0 官方建议直接新装："If your version of Dokku is pre 0.3.0 (check with `dokku version`), we recommend a fresh install on a new server."

## 升级流程注意事项

> "If you'll be updating docker or the herokuish package simultaneously, it's recommended that you stop all applications before upgrading and rebuild afterwards. This is not required if the upgrade only impacts the `dokku` package."

Why stop all apps:
- "`docker`: Containers may be randomly reset during the upgrade process, resulting in requests being sent to the wrong containers. Acknowledging and scheduling downtime thus becomes much more important."
- "`herokuish`: … base image. Herokuish changes do not cause issues unless the base OS changes, which may happen in minor or major releases."

升级命令（0.22.0+）：`dokku ps:stop --all`
