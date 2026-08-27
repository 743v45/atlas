---
date: 2026-08-05
topic: SQLite WAL 机制与 db 安全迁移
related:
  - ../asked/items/sqlite-wal/
原始会话: ~/.claude/projects/-Users-taevas/e8b976d5-xxxx.jsonl
---

# 2026-08-05 · SQLite WAL 机制与 db 安全迁移

一场对话两块产出:① db 文件安全迁移方法(探测 lsof/PRAGMA quick_check/WAL 0 字节 → 传输 → 大小对比+一致性校验),沉淀为 apprentice 课候选(dig/INBOX);② 「SQLite WAL:预写日志机制详解」自洽长文,当日推送 Outline「技术设计」collection(链接 outline-work.taevas.host:6540/doc/sqlite-wal-pfFYrbnHyl,后随平台弃用),报告结构:一句话定义+三件套定位 / 便签类比与工作流程 / 与 rollback journal 对比(读不阻塞写)/ checkpoint 与崩溃恢复 / 代价限制 / 实战红线两条。讲义骨架恢复为 asked/entries/sqlite-wal。
