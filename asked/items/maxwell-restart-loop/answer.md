# Maxwell 重启循环:根因在下游 Kafka,不在 Maxwell 自身

> **TL;DR**:Maxwell 进程反复被拉起又挂掉,supervisor 循环重启——看启动日志会发现 MySQL 侧完全正常(`Binlog connected` 成功),真正挂的是**下游要写入的 Kafka**:Producer 请求 topic 元数据 60 秒拿不到,`TimeoutException` 超时退出,TaskManager 停掉全部 task。三种根因按概率排序:broker 挂/网络不通 > topic 不存在且关了自动建 > bootstrap.servers 配错。

*(恢复自 2026-07-29 生产排障问答,原答骨架忠实,IP/topic 名已脱敏泛化。)*

## 一、日志怎么读

用户贴出的日志里,启动段一切正常:

```
Maxwell v1.38.0 is booting ... starting at Position[BinlogPosition[...]]
Restoring schema id 2 / id 1 ... played 1 deltas
Setting initial binlog pos ...
Maxwell http server started on port 8080
BinaryLogClient - Connected to <mysql-host>:3306 ...
Binlog connected.
```

——MySQL 复制连接、schema 恢复、位点初始化全部成功。数分钟后的这两行才是根因:

```
ERROR MaxwellKafkaProducer - Topic '<topic>' name does not exist.
    Exception: Failed to update metadata after 60000 ms.
ERROR TaskManager - cause:
org.apache.kafka.common.errors.TimeoutException: Failed to update metadata after 60000 ms.
```

因果链:Maxwell 的 Kafka Producer 向 broker 请求 topic 的元数据 → **60 秒拿不到 → 超时退出 → TaskManager 把 5 个 task 全停掉 → 进程挂**。随后又重新 boot(从同一个 binlog 位点),说明被守护进程/supervisor **反复拉起**,但每次都因同样的 Kafka 超时再挂——典型重启循环。

**判读要点:别被「Maxwell 挂了」带偏。挂的不是 Maxwell 自己,是它依赖的 Kafka。**

## 二、三种可能根因(按概率排序)

1. **Kafka broker 挂了 / 网络不通**——`Failed to update metadata` 最常见就是 producer 连不上任何 broker。先 ping/telnet `kafka.bootstrap.servers` 的端口。
2. **topic 不存在,且 broker 关了自动建 topic**——`auto.create.topics.enable=false` 时,写一个不存在的 topic 会一直等不到 metadata。手动 `kafka-topics --create` 建一下即可。
3. **bootstrap.servers 配错**——Maxwell 配置里 Kafka 地址写错,或指向了已下线的 broker。

## 三、两点额外提醒

- 该环境 **Kafka 版本是 0.9.0.1**(日志开头 `AppInfoParser - Kafka version : 0.9.0.1`),非常老,metadata 行为和新版差异较大,排障时别拿新版文档硬套。
- MySQL 这边完全正常:`Binlog connected`、row count 指标都在跑——问题只在 Kafka 这一头。

**排查第一步**:去 Kafka 侧确认 broker 进程和目标 topic 是否存在。broker 恢复 / topic 建好后,Maxwell 重启循环会自己消失(间接闭环:同日 Kafka 恢复后 CMAK 实测吞吐回到约 46k msg/s)。

## 出处

- 源对话归档:../../../conversations/2026-07-29-maxwell-kafka-pipeline.md(2026-07-29)
- 原始会话:~/.claude/projects/-Users-taevas/3a45dd34-0840-40ff-9e57-30296b7c68d9.jsonl
- 关联条目:[maxwell-kafka-single-partition](../maxwell-kafka-single-partition/)(同链路的分区倾斜)、[kafka-architecture-logic](../kafka-architecture-logic/)
