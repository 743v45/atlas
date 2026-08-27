---
date: 2026-07-29
topic: Maxwell/Kafka 链路三连问
related:
  - ../asked/items/maxwell-kafka-single-partition/
  - ../asked/items/kafka-architecture-logic/
  - ../asked/items/maxwell-restart-loop/
原始会话:
  - ~/.claude/projects/-Users-taevas/93c2dae1-f0c9-4cb3-bc15-bcfb71724127.jsonl(原理与分区倾斜)
  - ~/.claude/projects/-Users-taevas/5bd0d732-5cc4-469c-9698-4c078aed0c36.jsonl(Kafka 架构)
  - ~/.claude/projects/-Users-taevas/3a45dd34-0840-40ff-9e57-30296b7c68d9.jsonl(重启循环)
---

# 2026-07-29 · Maxwell/Kafka 链路三连问

同日三场会话,围绕生产上一条 MySQL→Maxwell→Kafka 的 CDC 链路连环追问(以下 IP/topic 名已脱敏泛化,数据保留)。

**① 原理与架构**(93c2dae1):用户问「maxwell 原理,链路」「过程丢了怎么恢复」「怎么重置」「用 kafka 支持多副本吗、怎么配置」,最后要求「画个架构图讲解完整通信机制,做成 html」。AI 讲透伪装 Slave 复用 MySQL 复制协议、强依赖 ROW binlog、schema 库解码、positions 断点续传,落盘 ~/docs/maxwell-architecture.html(7 section:全景/逐跳/握手时序/位点闭环/Kafka 通信/HA/协议速查)。

**② 分区倾斜诊断**(同会话后段):用户贴出 CMAK 控制台截图信息,3 分区里 partition 1 独占约 410 万 offset,partition 0/2 恒为 0。AI 判定 Kafka 层完全健康(ISR 满、preferred leader 100%、failed produce 0),根因在 Maxwell 分区键:单库同步时按 database hash 恒定落同一分区。关键转折:AI 先按记忆写了 kafka_partition_hash 配置项,用户贴出真实 --help 后 AI 公开认错更正——正确参数名是 **producer_partition_by**,可选 database|table|primary_key|transaction_id|column|random。verdict 改 primary_key(均匀分布 + 同主键有序),下游须幂等 upsert;旧数据不迁移,只影响新消息;改后消费组才能真正 3 消费者并行。

**③ Kafka 架构**(5bd0d732):用户问「kafka 使用架构逻辑」,AI 按逻辑层/物理层/客户端/协调层/语义参数五组讲组件(Topic/Partition/Offset、Broker/Replica/ISR/Controller、Producer/Consumer Group、ZK vs KRaft/Rebalance、acks/交付语义),落盘 ~/docs/kafka-architecture.html(9 张 mermaid 图)。

**④ 重启循环**(3a45dd34):用户贴 Maxwell 日志(boot → Binlog connected 正常,数分钟后挂,supervisor 反复拉起)。AI 定位挂的不是 Maxwell 是下游 Kafka:ERROR「Topic 'maxwell-xxxlogs' name does not exist / Failed to update metadata after 60000 ms」→ Producer 拿不到 topic 元数据超时退出。三种根因按概率排序:broker 挂/网络不通 > topic 不存在且关了自动建 > bootstrap.servers 配错;另提醒该环境 Kafka 0.9.0.1 版本很老、metadata 行为与新版差异大,MySQL 侧完全正常。间接闭环:同日 CMAK 恢复后实测约 46k msg/s。

三问分别沉淀为 asked/items/maxwell-kafka-single-partition、kafka-architecture-logic、maxwell-restart-loop。
