# raw — github.com（basecamp/kamal discussion #1823「I am recommending against Kamal right now」）

- 来源 URL: https://github.com/basecamp/kamal/discussions/1823
- 访问日期: 2026-10-02（WebFetch 提取）

## 提取要点（反对派一手材料）

- **日期/作者**：2026-04-10，用户 braun2morrow。
- **论点**：
  1. SSH 加密链路依赖 sshkit → net-ssh（纯 Ruby 加密实现，作者称 "do-your-own-crypto-in-ruby project"），主张应 shell out 到 OpenSSH。
  2. **硬绑 Docker**：不支持 Podman 等替代容器引擎（关联 issue #61）；部署通道等价于给部署者匿名 root 权限。
  3. 过度集成：装 Docker 是 curl 脚本管道进 root shell（"dangerous footgun"）；未检查 logging driver 就注入 `--log-opt max-size=10m`（#1709）；部署 git HEAD 而非工作区文件（坑了作者 1 小时+）。
  4. 文档缺口：缺完整 deploy.yml 示例；缩减服务器列表方法不明；git 行为未文档化。
  5. 运维怪问题：服务器 syslog DNS 报错、本地 Docker DNS 卡死（作者自认可能是 Docker bug，但归因于无替代引擎）。
  6. `proxy:run:http_port` 行为与名字不符（特权端口 + Docker 转发）。
- **附和**：n3ph（2026-04-14）补充 secrets 注入不可靠——子 shell 失败会静默产出空 secret；作者（04-20）回应 secret 管理可自己绕开。
- **维护者**：可见线程内无 Kamal 维护者回应。
- **作者结论**：Kamal 有前景但 "not ready for production use yet"（一家之言，注意样本偏差）。
