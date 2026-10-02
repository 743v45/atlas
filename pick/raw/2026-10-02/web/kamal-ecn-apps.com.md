# raw — ecn-apps.com（Kamal 2 vs Coolify 2026 对比，资源占用基准）

- 来源 URL: https://ecn-apps.com/pages/articles/kamal-vs-coolify-2026.html
- 访问日期: 2026-10-02（WebFetch 提取）

## 提取要点（资源占用数据点）

- **基准环境**：Kamal v2.2.0 + Coolify v4.0.0-beta.380+，Ubuntu 24.04 LTS；页面标注 2026，无精确发布日。
- **kamal-proxy 空闲内存**：基准表 "14.2 MB (kamal-proxy only)"；正文 "~15MB RAM"、"consumes only ~14 MB of RAM"（Go 单二进制）。
- **对照 Coolify**：空闲 "~850MB to 1.2GB RAM at idle"，基准表 "885.6 MB (7 core containers)"；结论称 Kamal 控制面 "62x leaner"。
- **CPU 空闲**：Kamal "0.1% – 0.3%" vs Coolify "1.8% – 4.2%"（后者构建尖峰 2 vCPU 上打满 100% 持续 1–4 分钟）。
- **磁盘**：Kamal "App images + base layers only"；Coolify 多 Nixpacks 缓存 + DB 卷 → Kamal 更省盘。
- **最小 VPS**：Kamal 在 "$4/mo (1GB RAM) VPS" 可用（留 "980MB for apps"）；8GB（$12/mo CPX31）舒适；Coolify 1GB 不可行（崩溃/重 swap），官方建议 8–16GB（控制面留 ~1GB）。
- 侧写：这些数字只覆盖控制面（proxy+Docker 常驻），应用容器另算（Rails 小应用 ~150–300MB/容器，见 kamal-proxy discussion #222 检索记录）。
