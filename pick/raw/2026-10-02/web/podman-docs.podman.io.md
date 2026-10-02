# Podman 官方文档：quadlet-basic-usage(7) — WebFetch

- 来源 URL: https://docs.podman.io/en/latest/markdown/podman-quadlet-basic-usage.7.html
- 访问日期: 2026-10-02

## 原文要点

- **机制**：Quadlet 把声明式 unit 文件翻译成 systemd services，从而可用 `systemctl` 管理。
- 生成 unit 正常启动（如 `systemctl --user start hello.service`）；**不能被 enable**（生成型 unit），开机自启要在源文件里写 `[Install] WantedBy=multi-user.target`。
- **本页出现的扩展名**：`.container`、`.volume`（其余 .network/.pod/.kube/.image/.build/.artifact 见 podman-systemd.unit(5)）。
- **目录**：rootless → `~/.config/containers/systemd/`；rootful → `/etc/containers/systemd/`。
- **关键指令示例**：`Image=`、`Exec=`、`PublishPort=8080:80`、`Volume=mydata.volume:/data`（按名引用 `.volume` 文件即挂载托管卷）；`[Volume]` 节 `VolumeName=`、`Label=`。
- **依赖**：本页未显式讲；卷示例展示隐式接线——容器 `Volume=` 引用名 → 启动 `mydata-volume.service` 时创建卷。
- **排错**：systemd 找不到 `foo.service` 通常是语法错误；用 `systemd-analyze --user --generators=true verify foo.service` 验证。
- 全程 rootless 可行（`systemctl --user` + `journalctl --user`）；本页未提 linger。
- 日志：`journalctl (-u | --user -u) <service>.service`。
