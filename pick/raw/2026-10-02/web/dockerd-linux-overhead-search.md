# dockerd Linux 侧内存开销（社区数据聚合）

- 来源：WebSearch（Z.ai web_search_prime 聚合），查询词「dockerd daemon memory overhead idle Linux VPS MB baseline resource usage」
- 访问日期：2026-10-02
- 性质声明：以下均为社区经验/论坛数据，非官方 benchmark——报告中引用时注明出处与性质

## 数据点

1. **Docker Forums**（https://forums.docker.com/t/docker-daemon-using-300mb-400mb-ram/136695）：用户报告小 VPS 上 dockerd 占 300-400 MB RAM 并求优化——即 daemon 本体（不含容器）可达数百 MB
2. **Taubyte 博客**（https://taubyte.com/blog/posts/docker-performance-fresser）：基础 Docker 设置约 100-200 MB RAM + 容器管理的 CPU 与镜像分层的磁盘 I/O 开销
3. **Torizon 基准**（https://www.torizon.io/blog/containers-in-linux-and-performance-impact）：部署栈的内存开销约 23 MB，启动时间影响极小——容器本身近零开销
4. **Stackademic 自托管估算**（https://blog.stackademic.com/how-much-cpu-and-ram-do-you-really-need-for-self-hosting-a-sizing-guide-for-normal-people-68722365358f）：带 Docker 的自托管栈空闲约 300-500 MB；daemon 本身轻，每个容器叠加自身占用
5. 病态案例：Unraid 论坛 / SO 有 dockerd 内存无限增长（泄漏/状态累积）的报告——空闲 >400-500 MB 通常视为异常
6. 搜索聚合共识：**空闲 dockerd 约 60-100 MB；基础全套约 100-500 MB**（取决于配置、容器数、镜像缓存）

## 解读

- Linux 侧 daemon 开销数量级：**约 100 MB 级**，对比桌面端 VM 的 2 GB+ 是量级差异
- 真正的磁盘/内存大头在镜像缓存与容器自身，不在 daemon
