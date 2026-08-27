# Maxwell→Kafka 分区为什么全挤一个区?producer_partition_by 诊断记

> **TL;DR**:CMAK 控制台看到 3 分区的 topic 里 partition 1 独占约 410 万 offset、partition 0/2 恒为 0——Kafka 层完全健康,根因在 Maxwell 的分区键:默认 `producer_partition_by=database`,只同步一个库时 hash 恒定,每条消息都落同一个分区。verdict 是改 `primary_key`(均匀分散 + 同主键有序),下游必须幂等 upsert。本条还含一次 AI 记错参数名、被真实 `--help` 纠正的实录。

*(恢复自 2026-07-29 生产排查问答,原答骨架忠实,IP/topic 名已脱敏泛化。)*

## 一、证据:Kafka 这边完全健康

| 指标 | 值 | 说明 |
|------|-----|------|
| Partition 0 Latest Offset | **0** | 从未有消息写入(不是消费问题,是 produce 端没写) |
| Partition 1 Latest Offset | 4,100,036 | 全部消息都在这 |
| Partition 2 Latest Offset | **0** | 从未被写入 |
| Under Replicated | 0% | 复制健康 |
| Preferred Leader | 全 true | leader 分配正常 |
| Failed produce /sec | 0 | producer 写入没有失败 |

`Latest Offset = 0` 是关键:它表示该分区的 log-end-offset 是 0,即 **producer 从没成功写过一条消息进 partition 0/2**。这不是消费者没消费,是生产者根本没发过去——所以排查方向不在 Kafka 集群,在 Maxwell 的分区路由。

## 二、根因:Maxwell 的分区键

Maxwell 写 Kafka 时按 `producer_partition_by` 决定消息进哪个分区:

```
partition = hash(分区键) % 分区数
```

默认值是 **`database`**(按数据库名 hash)。只同步一个库时:

```
hash("单个库名") % 3  恒等于同一个数   ← 每条消息都算出同一个分区
```

→ 全部消息落同一分区,其余分区永远是 0。

**反向推理同样成立**:如果当前是 `primary_key` 或 `random`,410 万条消息早就均匀分散了。所以看到单分区倾斜,生效的必然是 `database` 或 `table`(两者单库/单表时 hash 都恒定)。

## 三、参数名纠错实录

AI 先按记忆写了 `kafka_partition_hash` 配置项;用户贴出真实的 `--help` 输出后,AI 公开认错更正:**正确参数名是 `--producer_partition_by`**,可选值为:

| 值 | 单库单表时的分布 | 会单分区倾斜吗 |
|----|-----------------|---------------|
| `database`(默认) | `hash(db) % N` 恒定 | **是 ← 本例** |
| `table` | `hash(table) % N` 恒定 | **是 ← 也可能** |
| `primary_key` | 按主键值均匀 | 否 |
| `transaction_id` | 按事务 id 均匀 | 否 |
| `random` | 随机均匀 | 否 |
| `column` | 看指定列的值 | 视列而定 |

教训:**凭记忆写配置项名要拿官方 help 核对,尤其老版本工具的参数名各版本差异大**(本例环境 Kafka 0.9.0.1 + Maxwell v1.38.0)。

## 四、解决:改 primary_key

```bash
# 命令行
--producer_partition_by=primary_key
# 或 config.properties 里(去掉 --)
producer_partition_by=primary_key
```

**`primary_key` 是最佳实践**:既把数据均匀分散到全部分区,又保证同一主键的多次变更落在同一分区内有序(下游按主键还原状态正确)。改完重启 Maxwell,观察控制台:闲置分区的 offset 开始增长,原分区增速降到约 1/N。

进阶玩法 `column` 模式(按业务字段 hash,让同一用户/订单的变更聚在同一分区):

```bash
--producer_partition_by=column
--producer_partition_columns=user_id
--producer_partition_by_fallback=primary_key   # 行没有该列时回退
```

## 五、改的时候必须知道的 4 件事

1. **不迁移已有数据**:倾斜分区里的旧消息不会动,新配置只影响之后的消息。
2. **顺序语义变化**:从「同库有序」变成「同主键有序」,跨主键不再全局有序——CDC 下游通常可接受。
3. **下游必须幂等 upsert**:Maxwell 是 at-least-once,重放会重复,按主键/position 去重。
4. **消费组才能真正并行**:之前只有 1 个分区有数据,消费组里多个消费者也没用;分区均匀后 N 消费者才各司其职——这是改它最大的收益。

## 出处

- 源对话归档:../../../conversations/2026-07-29-maxwell-kafka-pipeline.md(2026-07-29)
- 原始会话:~/.claude/projects/-Users-taevas/93c2dae1-f0c9-4cb3-bc15-bcfb71724127.jsonl
- 关联 artifact:~/docs/maxwell-architecture.html(Maxwell 全链路架构 7 section,含本坑的沉淀位)
- 关联条目:[kafka-architecture-logic](../kafka-architecture-logic/)(同日的 Kafka 全景)、[maxwell-restart-loop](../maxwell-restart-loop/)(同日下游故障)
