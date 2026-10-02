# WebSearch 汇总 — Incus Web UI 分发方式 与 Zabbly 打包渠道

- 采集方式：WebSearch（"Incus web UI 2026 incus-ui included by default package Zabbly OR IncusOS" 等多轮）
- 访问日期：2026-10-02

## Web UI 现状（关键结论）

- **主发行渠道（Zabbly apt / 发行版仓库）中 UI 是可选包，非默认捆绑**：
  - Zabbly：`apt install incus-ui-canonical`——官方描述"a package containing a rebranded version of the LXD web interface for use with Incus"；UI 源码仓库 github.com/zabbly/incus-ui-canonical（canonical/lxd-ui 的 fork）。
  - 装好后需 Incus 监听网络（`core.https_address` 或 `incus admin init`）；`incus webui` 命令打印 UI URL。
  - Arch Linux：包名 `incus-ui`（lxd-ui 打补丁适配 Incus）。
  - Debian 官方仓库**不含** UI，需加 Zabbly 仓库（discuss.linuxcontainers.org/t/25103，Debian 13 讨论）。
- **IncusOS 出厂带 UI**：IncusOS 文档（linuxcontainers.org/incus-os/docs/main/getting-started/access）"The Incus UI is also available for web access"，需把建镜像时的客户端证书导入为用户证书；IncusOS 公告（discuss.linuxcontainers.org/t/announcing-incusos/25139）称可"entirely from the web UI"完成安装配置运维。
- UI 需客户端证书认证（非裸 HTTP 暴露）——个人 VPS 场景安全性可接受但初次配置有一步证书操作。
- 安全公告：2026-04 公告提及 Incus UI web server 漏洞在 **6.23.0** 修复。

## Zabbly 打包渠道

- 仓库 github.com/zabbly/incus（Incus package repository），构建目标：Ubuntu 22.04/24.04/26.04 LTS、Debian 12/13。
- 通道：stable 与 lts-7.0 两条 apt 源（IncusOS 也从 Zabbly 拉 stable/lts-7.0 包）。
- Zabbly 同时是 Incus 项目的商业支持方与基础设施赞助方（linuxcontainers.org/incus 主页表述）。

## 原始链接

1. https://github.com/zabbly/incus — 包仓库 README（构建目标、incus-ui-canonical 描述）
2. https://discuss.linuxcontainers.org/t/debian-13-incus-web-ui-best-install-option/25103 — Debian 13 装 UI 须走 Zabbly
3. https://linuxcontainers.org/incus-os/docs/main/getting-started/access — IncusOS 内置 UI 文档
4. https://discuss.linuxcontainers.org/t/announcing-incusos/25139 — IncusOS 公告
5. https://github.com/zabbly/incus-ui-canonical — UI 源码（lxd-ui fork）
