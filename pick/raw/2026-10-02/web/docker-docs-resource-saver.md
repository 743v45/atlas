# Docker Desktop Resource Saver 官方文档留档

- 来源：https://docs.docker.com/desktop/use-desktop/resource-saver/ （Docker 官方文档）
- 访问日期：2026-10-02

## 原文关键数字（照录）

1. **默认启用**；触发条件：无容器运行且空闲达到一定时长，"The default time is set to 5 minutes"
2. **节省量**："reduces Docker Desktop's CPU and memory utilization on the host by 2 GBs or more"——即停止 Linux VM 后释放约 2 GB+ 内存（CPU 无具体百分比）
3. 触发后 "automatically stopping the Docker Desktop Linux VM"
4. **Windows + WSL 例外**：只暂停 `docker-desktop` 发行版内的 Docker Engine，不停止 VM——CPU 降低但内存不减少；要降内存需 WSL 的 `autoMemoryReclaim`
5. 退出该模式需重启 VM，"about 3 to 10 seconds"（Mac/Linux 快，Windows Hyper-V 慢）
6. 可在 Settings → Resources 禁用；官方建议保持启用（手动 Pause 节省效果差得多）

## 解读

- 该页面反向证实：默认配置下 Docker Desktop 的 Linux VM 常驻内存约 **2 GB+**（否则无从"节省 2 GB+"）——与社区「2-8 GB」经验区间一致
- VM 是桌面端开销的根源：空闲也要么常驻 2GB+，要么接受唤醒延迟 3-10 秒
