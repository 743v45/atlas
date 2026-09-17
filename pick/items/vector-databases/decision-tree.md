# 向量数据库 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

RAG 的嵌入向量存在哪、怎么查？（2026-09-17 会话；用户画像：个人/学习起步优先低运维，规模动机优先检索能力）

## 分叉与决策

### D1 能不能不出 Postgres？

- 已有 PG 时新增一个向量库 = 新增一套运维面 + 数据同步——先问「PG 够不够」再谈专用库。
- 叶：[pgvector](pgvector/) adopt（起步默认答案：ACID/权限/备份白拿，千万级向量内不换库；与本仓 data-storage 域「以 PostgreSQL 为锚」哲学同源）

### D2 PG 不够用了，专用库选哪档规模？

- 亿级以内单机/轻集群 → 轻量专用库；十亿级/吞吐极限 → 分布式重炮。规模判断先于品牌偏好。
- 叶：[Qdrant](qdrant/) trial（亿级以内第一升级：Rust 内核、payload 过滤与量化强项、云/自托管同核）
- 叶：[Milvus](milvus/) trial（十亿级战场：LF AI 毕业项目 + Zilliz 背书；etcd/对象存储全家桶，个人项目过重）
- 叶：[Weaviate](weaviate/) trial（混合检索/库内模块优先时与 Qdrant 对位比选；BSD-3 许可最干净，社区声量小一档）

### D3 本地原型要不要独立服务？

- 原型期连 Docker 都不想起 → 进程内嵌入式；代价是生产要迁移。
- 叶：[Chroma](chroma/) trial（pip 即用零配置，notebook/教学事实标准；定位转向「Search infrastructure for AI」，生产换库）

### D4 存量搜索栈要不要顺手用？

- 已有 ES/OpenSearch 的团队做 RAG 是顺路（索引/权限/监控复用）；绿地项目为 RAG 拉起 JVM 集群不划算。
- 叶：[Elasticsearch](elasticsearch/) assess（BM25+向量最成熟；三轨 license 合规心智负担；存量栈用户可升 trial）

### D5 免运维托管值不值锁定代价？

- 闭源托管换来零运维，付出数据出域、成本黑箱、API 锁定三价；开源核心+托管云（Qdrant Cloud/Zilliz）提供「可搬走」的中间态。
- 叶：[Pinecone](pinecone/) assess（serverless 代名词；「只有它能扛规模」的窗口期已关闭，个人/学习场景性价比低）

## 落选节点（不立条目的死分支）

- **Vespa（Yahoo）**：规模与功能天花板最高之一，但学习曲线极陡、为「超大站内搜索 + RAG 混合」设计——RAG 单动机不值得其复杂度；真到那个规模直接进 Milvus/Vespa 双选评估。
- **OpenSearch（AWS 分叉）**：与 Elasticsearch 同为 Lucene 系，定位重叠——存量 ES 用户归 ES、要 Apache-2.0 干净许可的存量用户归 OpenSearch，单独立目无增量信息。
- **Redis（向量能力）**：向量是缓存主业的附属能力，混合检索/索引类型弱于专用库；已在用 Redis 的团队可作轻量补充，不作为 RAG 底座候选。
- **LanceDB**：嵌入式新秀（数据湖/多模态取向），被多份对比文提名但社区体量与 RAG 生态位尚小——观察名单，不占大牌坑位。
- **Supabase Vector / 托管 pgvector**：pgvector 的托管形态，不是独立选型——选了 pgvector 自然覆盖。

## 观察名单（下次复核触发器）

- LanceDB：RAG 场景生产案例沉淀 → 重估是否立目
- Flowise 事件镜像检查：Chroma 商业化转型若持续挤压开源单机版 → trial 降 hold
- ES：若 AGPL 轨道生态成熟（托管商支持）→ assess 复估
