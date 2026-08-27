---
date: 2026-08-05
topic: SQLite 库文件跨机安全迁移实操(WAL 三件套)
related:
  - ../apprentice/items/verify/sqlite-safe-migration/
原始会话: ~/.claude/projects/-Users-taevas-code-mymy-bilibili-extensions/84c7c408-9f69-4e71-afd1-fc5fa64c111e.jsonl(本机,08-05);同日姊妹会话在小天机 e8b976d5(待同步补档)
---

# 2026-08-05 · SQLite 库文件跨机安全迁移实操

同一主题的知识侧归档见 [2026-08-05-sqlite-wal-and-migration.md](2026-08-05-sqlite-wal-and-migration.md)(WAL 机制详解,asked 馆);本篇记**实操现场**:怎么把一个在用的 SQLite 库安全搬到另一台机器。

**原始表述**:「(本地项目的)collector.db(可能还有其他文件)需要把这里的数据库复制到 ssh <内网主机> 的(目标项目)下面(你得看下对应地址)」——「可能还有其他文件」这句直觉是对的:ls 一看是三件套 `.db / .db-wal / .db-shm`。

**关键转折**:用户没有直接说「拷过去」,而是先问「这三个文件是干嘛的」「wal 是什么」。AI 先讲清 WAL 机制(写操作先进预写日志,checkpoint 才落主库——最近的写入可能还住在 -wal 里),再动手。这个顺序决定了后面所有安全动作:既然 -wal 里可能有未落库数据,「只拷 .db」就不成立。

**执行序列**(全程计时,每步有可观察输出):

1. 查 `-wal` 是否 0 字节——决定走哪条红线;
2. `lsof` / `ps` 确认无进程持有库文件(有写入者时拷到的是中间态);
3. 源库 `PRAGMA quick_check` 完整性校验通过;
4. 三件套同传(现场 285MB,40 秒),不是只拷 .db;
5. 对端逐字节对比 + 再跑一次 `quick_check` 复验;
6. 打印每步与总耗时。

**最终结论(沉淀)**:两条红线——**WAL 0 字节才可单独拷 .db;非空 -wal 绝不能丢**(丢=丢最近写入)。沉淀为 apprentice 课 [sqlite-safe-migration](../apprentice/items/verify/sqlite-safe-migration/)。
