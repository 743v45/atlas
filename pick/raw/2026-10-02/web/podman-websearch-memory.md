# Podman vs Docker 资源占用 — WebSearch 聚合

- 来源 URL: WebSearch 聚合页（查询词 "podman vs docker memory usage overhead benchmark daemonless idle"，经 z.ai web_search_prime）
- 访问日期: 2026-10-02
- ⚠️ 口径警示：以下数字全部来自 2026 年技术博客，方法论严谨度参差，只作量级参考

## 关键数字（聚合）

| 维度 | Podman | Docker | 来源 |
|---|---|---|---|
| 空闲内存（无容器运行） | **0 MB**（daemonless，无常驻进程） | dockerd 常驻 **140–180 MB** | Medium @jamilxt（2026）；daily.dev 同口径 |
| 总体内存（综合口径） | 比 Docker 低 **65–70%** | — | uptrace.dev 对比页 |
| 单容器内存（负载下） | 一致性低 **15–20%** | — | xurrent.com / tech-insider.org / middleware.io（多源同向） |
| 30 容器稳态 | 差距收窄（约 2.5×→口径不一） | — | shattered.io（ sustain load 下 Docker 29% vs Podman 41% overhead 的反例也存在于特定负载，**基准互相矛盾**） |
| 容器启动速度 | 快约 **20–33%**（0.8s vs 1.2s 单例） | — | daily.dev |
| rootless 冷启动代价 | 双方都要付约 **25–30%** 额外启动开销 | 同 | lucaberton.com（2026） |

## 结论（聚合判断）

- **空闲内存优势是架构性的、无争议的**：daemonless = 无容器运行时零基线成本；dockerd 常驻百 MB 级。
- **负载下差距有争议**：不同基准给出相反结果（shattered.io 自身警告），exact figures 只可作量级参考。
- 对「几个到十几个小服务」场景，决定性的是**空闲基线**而非满载峰值。

## 引用来源

1. Medium @jamilxt（2026）— https://medium.com/@jamilxt/docker-vs-podman-in-2026-the-benchmarks-contradict-each-other-here-is-how-to-decide-6eda538f8190
2. uptrace.dev podman-vs-docker — https://uptrace.dev/comparisons/podman-vs-docker
3. shattered.io overhead comparison 2026 — https://shattered.io/docker-vs-podman-overhead-comparison-2026
4. daily.dev docker-vs-podman — https://daily.dev/blog/docker-vs-podman-container-runtime-which-to-use
5. lucaberton.com podman-vs-docker 2026 — https://lucaberton.com/blog/podman-vs-docker-2026
