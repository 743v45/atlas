# pm2 官方文档：startup（开机自启）留档

- 来源 URL: https://pm2.keymetrics.io/docs/usage/startup/
- 访问日期: 2026-10-02（WebFetch 提取）

## 核心事实（含原文关键句）

- `pm2 startup`：「PM2 can generate startup scripts and configure them in order to keep your process list intact across expected or unexpected machine restarts.」自动检测 init 系统，输出一条需 sudo 执行的命令
- `pm2 save`：「save the app list so it will respawn after reboot」
- `pm2 resurrect`：手动恢复 save 过的进程列表
- 支持的 init 系统：systemd（Ubuntu≥16/CentOS≥7/Arch/Debian≥7）、upstart（Ubuntu≤14）、launchd（macOS）、openrc（Gentoo）、rcd（FreeBSD）、systemv（CentOS 6/Amazon Linux）；Windows 需第三方 pm2-installer
- 注意：Node 升级后需 `pm2 unstartup` 再重新 `pm2 startup`（脚本指向新 Node 二进制）；`pm2 unstartup` 移除自启
