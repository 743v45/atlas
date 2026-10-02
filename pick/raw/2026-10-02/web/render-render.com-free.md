# Render 免费层文档（render.com/docs/free）

- 来源：https://render.com/docs/free
- 访问日期：2026-10-02（WebFetch，取回为页面正文摘要）
- 用途：render 条目定价/免费层现状核实

## 免费层内容（页面原文要点）

- 免费对象：Web services（Node.js/Python/Rails 等）、Render Postgres、Render Key Value（Redis 兼容）
- Static sites "free to deploy on Render"，计入月度带宽与 pipeline 分钟数
- Cron jobs **不**支持免费实例："Other service types don't support Free instances"

## Web services（免费）

- **Spin-down**：15 分钟无入站流量（HTTP 请求或 WebSocket 消息）后休眠
- **冷启动**：唤醒约 1 分钟（"takes about one minute"），期间展示 loading 页
- **实例小时**：每 workspace 每自然月 "750 Free instance hours"；休眠中的服务不消耗小时数；耗尽后免费服务被**暂停**至下月；小时数不结转
- **带宽**：免费 web service 计入月度 outbound 带宽与 pipeline 分钟数的包含额度（本文档未写 100GB 数字）；超额触发补充计费，无付款方式则暂停免费服务
- 回滚仅限最近 2 个之前的 deploy
- 文件系统临时性；免费层无持久磁盘；休眠期间 `/robots.txt` 请求自动返回 "disallow all"（不唤醒服务）
- 免费服务对外发起"异常大量流量"可能被 Render 暂停
- 不能多实例扩展；无 edge caching、无 one-off jobs、无 shell/SSH 访问；不能接收私网流量；保留端口 18012/18013/19099 不可用；SMTP 端口 25/465/587 被封

## 免费 Postgres

- 每 workspace 一个免费数据库，固定 1 GB 存储
- 创建后 **30 天过期**，有 14 天宽限期升级（否则 Render 删除数据库）
- 无备份、无托管连接池；维护/重启可能随时发生

## 免费 Key Value（Redis 兼容）

- 每 workspace 一个免费实例；"In-memory only"——重启全丢
- 即使升级到付费计划数据也丢（升级不迁移）
- 维护/重启随时可能

## 其他

- 升级 workspace 计划不会解除免费实例限制；需逐服务改 compute plan
- 用量在 Billing 页 "Monthly Included Usage" 查看接近上限有邮件提醒
