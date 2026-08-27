# Kafka 使用架构逻辑:组件、协调层与关键语义

> **TL;DR**:一句话串起 Kafka——**Producer 往 Topic 的某 Partition 写,该 Partition 的 Leader(在某 Broker)落盘并复制给 ISR 里的 Follower;Consumer 以 Group 形式 pull、各自记录 Offset;集群状态由 ZooKeeper/KRaft + Controller 维护,消费组由 Group Coordinator 协调**。按逻辑层/物理层/客户端/协调层/语义参数五组记组件,比背零散名词快。

*(恢复自 2026-07-29 问答「kafka 使用架构逻辑」,原答骨架忠实。)*

## 一、逻辑层(数据怎么组织)

| 概念 | 含义 |
|---|---|
| **Topic** | 消息主题/分类,逻辑命名空间。生产消费都面向它 |
| **Partition** | 分区,topic 的水平切分。是**并行与扩展的单位**;单分区内消息有序,跨分区不保证 |
| **Offset** | 分区内消息的单调递增序号,消费进度的唯一标识 |
| **Record / Message** | 一条消息,由 `key + value + timestamp + headers` 组成 |
| **Key** | 消息键;有 key 则按哈希路由到固定分区(保序关键) |
| **Log Segment** | 分区日志的分段文件(`.log` + `.index` + `.timeindex`),按大小/时间滚动 |

## 二、物理层(数据存在哪)

| 概念 | 含义 |
|---|---|
| **Broker** | Kafka 服务器节点;多个 Broker 组成集群,无中心、对等 |
| **Cluster** | Broker 集群,由元数据层统一协调 |
| **Replica** | 分区副本:每个分区 = 1 Leader + N Follower |
| **Leader** | 副本的「主」,处理该分区的**所有读写** |
| **Follower** | 副本的「从」,被动从 Leader **拉取(pull)**同步数据 |
| **ISR** | In-Sync Replicas,与 Leader 保持同步的副本集合;`acks=all` 时等 ISR 全确认 |
| **Controller** | 集群中某个 Broker 兼任,负责 Leader 选举、分区/副本状态管理 |

## 三、客户端层(谁生产消费)

| 概念 | 含义 |
|---|---|
| **Producer** | 生产者,发布消息到 topic;按 key 哈希/轮询选分区,靠 `acks` 控制持久化 |
| **Consumer** | 消费者,主动 pull 消息,按 offset 顺序消费 |
| **Consumer Group** | 消费者组。**同组内一分区只被一个消费者消费**(队列模型);不同组各自全量消费(发布订阅) |

## 四、协调层(集群怎么管自己)

| 概念 | 含义 |
|---|---|
| **ZooKeeper / KRaft** | 元数据存储 + Controller 选举。KRaft 把元数据 raft 化,正逐步淘汰 ZK |
| **Group Coordinator** | (Broker 内)管消费者组成员、触发 **Rebalance**、记录消费 offset |
| **Rebalance** | 消费者/分区变化时重新分配分区,期间消费暂停 |
| **__consumer_offsets** | 内部 topic,持久化各消费者组的消费位点 |

## 五、关键语义/参数(决定行为)

| 概念 | 含义 |
|---|---|
| **acks** | 持久化强度:`0` 不等 / `1` Leader 落盘 / `all` 等 ISR 全确认 |
| **min.insync.replicas** | ISR 最少副本数(建议 ≥2),配合 `acks=all` 防丢 |
| **unclean.leader.election** | 是否允许非 ISR 副本当 Leader(关=一致性,开=可用性) |
| **retention** | 消息保留策略,按 `hours`/`bytes`/`compact`(只留每个 key 最新值) |
| **交付语义** | at-most-once / at-least-once(默认)/ exactly-once(幂等+事务 EOS) |

## 出处

- 源对话归档:../../../conversations/2026-07-29-maxwell-kafka-pipeline.md(2026-07-29)
- 原始会话:~/.claude/projects/-Users-taevas/5bd0d732-5cc4-469c-9698-4c078aed0c36.jsonl
- 关联 artifact:~/docs/kafka-architecture.html(9 张 mermaid 关系图:核心架构/核心组件等,卡片式布局 + 组件表)
- 关联条目:[maxwell-kafka-single-partition](../maxwell-kafka-single-partition/)(同日分区倾斜诊断)、[maxwell-restart-loop](../maxwell-restart-loop/)
