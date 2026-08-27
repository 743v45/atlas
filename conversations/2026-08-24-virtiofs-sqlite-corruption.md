---
date: 2026-08-24
topic: virtiofs 宿主机直读 SQLite 两次损库
related:
  - ../mistakes/items/virtiofs-sqlite-corruption/
原始会话: 小天机 ~/.claude/projects/ 会话 76ec3aae（源对话在小天机,待同步补档）
---

# 2026-08-24 · virtiofs 宿主机直读 SQLite 两次损库

macOS Docker Desktop 容器经 bind mount（virtiofs）直接读写宿主机上的 SQLite 文件，同日两次报 `SQLITE_CORRUPT`——库文件损坏，不可逆。

**原始表述（翻车证据）**：当时的假设是「容器挂宿主机路径读 SQLite，只读访问无害」；两次损库证明该假设错误——根因是 macOS Docker 的 virtiofs 文件系统共享机制与 SQLite 的 mmap 写入语义不兼容，即便访问路径名义上只读，损库照样发生。

**关键转折**：从「修库」转向「换通道」——不再信任 virtiofs 上任何形式的 SQLite 直读，数据库文件移出共享面。

**最终结论（沉淀）**：修正已全部产物化（在小天机）：改用 named volume 托管数据库；compose 文件头写红线注记（禁止 virtiofs 直读 SQLite）；备份四层化（RPO 15 分钟）；verify-deployed 自检步骤；sqlite-rescue 抢救工具。沉淀为本馆错题 [virtiofs-sqlite-corruption](../mistakes/items/virtiofs-sqlite-corruption/)。
