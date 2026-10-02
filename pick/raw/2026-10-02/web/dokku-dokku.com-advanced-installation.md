# dokku.com 高级安装文档（低内存警告与 swap 建议）

- 来源 URL: https://dokku.com/docs/getting-started/advanced-installation/
- 访问日期: 2026-10-02

## 原始提取

## 1) 系统内存不足的警告（原文）

- "Having less than 1 GB of system memory available for Dokku and its containers may result in unexpected errors"
- 错误示例原文："! [remote rejected] master -> master (pre-receive hook declined)"
- 该错误与 NPM 依赖安装相关，文档链接指向 npm 的 GitHub issue #3867。

## 2) 官方对 swap 的建议

- 原文："it might suffice to augment the Linux swap file size to a maximum of twice the physical memory size."
- 即：将 Linux swap 文件增大到物理内存的两倍即可解决。
- 文档还提示："it may be necessary to call swapoff, mkswap and swapon explicitly"，例如 `sudo /sbin/swapoff /var/swap.img`。
- 示例步骤：在 `/var` 下创建 `swap.img`，设置权限 600，用 `dd` 写入 1000 个 1MB 块（即 1GB），再 `mkswap`、`swapon`，最后将挂载项追加到 `/etc/fstab` 实现开机自动挂载。

## 3) 低内存场景的其他建议

- 页面中针对低内存 VM 的建议仅限于上述 swap 调整方案，文档未给出其他内存优化措施。
- 提供了两个外部参考链接：DigitalOcean 的虚拟内存/swap 配置教程，以及 ServerFault 上关于扩容已有 swap 文件的问答。
