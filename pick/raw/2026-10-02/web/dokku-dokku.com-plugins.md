# dokku.com 插件生态页（官方/社区插件清单与统计）

- 来源 URL: https://dokku.com/docs/community/plugins/
- 访问日期: 2026-10-02

## 原始提取

## 官方插件（29 个，由 dokku 维护者提供）

按名称列出：

1. Clickhouse
2. Copy Files to Image
3. CouchDB
4. Cron Restart
5. Elasticsearch
6. Grafana/Graphite/Statsd
7. HTTP Auth
8. Let's Encrypt
9. Maintenance mode
10. MariaDB
11. Meilisearch
12. Memcached
13. Mongo
14. MySQL
15. Nats
16. Omnisci
17. Postgres
18. Pushpin
19. RabbitMQ
20. Redirect
21. Redis
22. Registry
23. RethinkDB
24. Scheduler Kubernetes
25. Scheduler Nomad
26. Solr
27. SSH Hostkeys
28. Typesense

（共 28 个；除 Cron Restart 要求 0.30.0+、Registry 要求 0.12.0+ 外，其余均兼容 0.4.0+）

## 社区插件分类与数量

| 分类 | 数量 |
|---|---|
| 数据库 - 关系型 | 7 |
| 数据库 - NewSQL | 1 |
| 数据库 - 缓存 | 3 |
| 数据库 - 队列 | 4 |
| 数据库 - 其他 | 6 |
| 实现 Dokku 新功能 | 28 |
| 其他插件 | 4 |
| 已弃用（功能已并入核心） | 55 |
| 无人维护 | 19 |

## 统计汇总

- **官方插件：28 个**
- **活跃社区插件：53 个**
- **已弃用：55 个**
- **无人维护：19 个**
- **页面总计约 155 个插件**

页面还包含插件安装/创建的文档链接，以及 Docker 官方 nginx-vhosts 插件的结构示例（plugin.toml、commands、install、post-deploy）。

## 关键判断素材

- 数据服务全家桶在官方插件内：Postgres / MariaDB / MySQL / Redis / Mongo / Memcached / RabbitMQ / Elasticsearch / Solr / ClickHouse
- Let's Encrypt 证书为官方插件
- Scheduler Kubernetes / Scheduler Nomad 插件说明 dokku 的调度器可插拔
