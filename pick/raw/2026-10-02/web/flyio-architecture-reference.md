# Fly.io 官方架构文档抓取（docs.fly.io/reference/architecture，访问 2026-10-02）

- 来源：https://docs.fly.io/reference/architecture（WebFetch 全文提取；fly.io/docs/* 301 至 docs.fly.io）
- 访问日期：2026-10-02

## 确认的架构事实

- **Firecracker microVM**：原文「Application code runs in Firecracker microVMs. These are lightweight, secure virtual machines based on strong hardware virtualization.」——应用跑在硬件虚拟化的轻量安全 VM 里，非容器沙箱。
- **Anycast 就近路由**：「We broadcast and accept traffic from ranges of IP addresses (both IPv4 and IPv6) in all our datacenters」，代理层把连接转发到「the closest available microVM」——同一 IP 池全域广播，流量就近落地。
- **数据中心间 WireGuard 隧道回程**：跨 DC 回程走 WireGuard tunnel，「very little additional latency」。
- **多区域部署**：页面示例（Dallas 收流 → Chicago 的 microVM）隐含区域放置；`fly regions`/机器放置工具细节在别的文档节。
- 本页**未覆盖**：自动 HTTPS 签发细节（只提 TLS termination handler）；fly.toml（在别节）。

## 交叉印证

- 自动证书：定价页（本日抓取）「Every organization's first 10 single hostname certificates are free」——证书自动供给体系存在；fly.dev 域名证书全自动，自定义域名 `fly certs add` 走自动化签发。
