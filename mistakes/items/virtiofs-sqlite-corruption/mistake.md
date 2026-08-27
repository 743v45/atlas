# 「只读无害」:virtiofs 直读 SQLite 两次损库

> **TL;DR**:错不在挂载姿势,在「只读访问无害」这个未验证假设——virtiofs 与 SQLite mmap 不兼容,损库与读写意图无关。

- **状态**:fixed(已修正)
- **日期**:2026-08-24
- **出处**:小天机会话 76ec3aae,容器经 virtiofs bind mount 访问宿主机 SQLite

## 经过

macOS Docker Desktop 容器通过 bind mount(virtiofs)访问宿主机上的 SQLite 文件,当时的判断是「只读访问,不会动文件,无害」。同日两次 `SQLITE_CORRUPT`——库文件损坏。每次都不可逆,只能回滚。

## 根因

我以为是「挂载参数没配对」,其实是「只读无害」这个假设本身不成立:macOS Docker 的 virtiofs 文件系统共享机制与 SQLite 的 mmap 语义不兼容——损库与否取决于文件系统层,不取决于我的访问意图是读还是写。用「我打算只读」替代「这条通道对 SQLite 安全」的验证,是把意图当成了判据。

## 修正

数据库文件整体退出 virtiofs 共享面:改用 named volume 托管,宿主机不再直挂。配套四层防线(产物在小天机):compose 文件头红线注记(禁止 virtiofs 直读 SQLite)、备份四层化(RPO 15 分钟)、verify-deployed 部署后自检、sqlite-rescue 抢救工具。
