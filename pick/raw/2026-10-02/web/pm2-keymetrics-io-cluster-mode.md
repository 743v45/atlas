# pm2 官方文档：cluster mode 留档

- 来源 URL: https://pm2.keymetrics.io/docs/usage/cluster-mode/
- 访问日期: 2026-10-02（WebFetch 提取）

## 核心事实（含原文关键句）

- 启用方式：`pm2 start app.js -i max`。「`max` means that PM2 will auto detect the number of available CPUs and run as many processes as possible」
- 配置文件方式：`{ instances: "max", exec_mode: "cluster" }`（js/yaml/json 均可）；「setting the `instances` option on a Node.js app automatically enables the cluster mode」
- `-i` 取值：`0`/`max`=全部 CPU；`-1`=CPU 数减 1；具体数字
- 零停机：「As opposed to `restart`, which kills and restarts the process, `reload` achieves a **0-second-downtime** reload.」reload 失败超时回退经典 restart
- 本质：「allows networked Node.js applications (http(s)/tcp/udp server) to be scaled across all CPUs available, without any code modifications.」基于 Node 原生 cluster 模块，子进程共享端口
- 前提要求：应用须无状态（session/websocket 不能存进程内，用 Redis 等外置）；优雅关闭需捕获 SIGINT
