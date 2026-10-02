# Coolify 安全事件调研（WebSearch 汇总，2026-10-02）

- 来源：WebSearch 多轮查询（2026-10-02 采集；注：搜索工具配额当日耗尽，后续补查需 2026-10-30 之后）
- 用途：风险条目——面板攻击面 / 暴露实例历史
- 结论速览：**未找到「2025-03 大规模实例被删+勒索」实际事件的确认报道**；有据可查的是两波漏洞披露 + 政府警告 + 零星用户被黑个案。

## 1. 2025-01 波次：CVE-2025-22605 / CVE-2025-22606

- CVE-2025-22605：OS 命令注入（CWE-77），认证用户可在 Coolify 容器执行任意代码，波及 4.0.0-beta.18 → beta.253，CVSS 7.8，beta.253 修复（CISA SB25-026，2025-01 第 3 周公告确认）
  - NVD: https://nvd.nist.gov/vuln/detail/CVE-2025-22605
  - GHSA-9wqm-fg79-4748: https://github.com/coollabsio/coolify/security/advisories/GHSA-9wqm-fg79-4748
- CVE-2025-22606：同期另一 RCE
- 背景（搜索摘要转述）：2025 年初 Horizon3.ai 攻研团队发布 Coolify 命令注入研究，指出大量实例直接暴露公网（部分无认证/默认配置），维护者转向**对暴露实例强制自动推送更新**以缓解
- UAE Cyber Security Council「Alert 88」（2025-01-29 PDF）：https://assets.adgm.com/download/assets/20250129+-+Critical+Vulnerabilities+in+Coolify+-+Alert+88.pdf ——政府级警告，明示勒索软件部署风险

## 2. 2026-01 波次：11 个 critical 漏洞披露

- The Hacker News（2026-01）：https://thehackernews.com/2026/01/coolify-discloses-11-critical-flaws.html ——「Coolify Discloses 11 Critical Flaws Enabling Full Server Compromise on Self-Hosted Instances」
- 关键 CVE（Censys 咨询）：CVE-2025-64419（提权命令注入）、CVE-2025-64420（root SSH key 暴露）、CVE-2025-64424
- Censys 威胁情报：**~52,000–52,890 个 Coolify 实例直接暴露公网**（德国 ~15,000 居首，美国、法国、巴西次之）
  - SC Media: https://www.scworld.com/brief/nearly-a-dozen-coolify-flaws-put-servers-at-risk
  - Heise: https://www.heise.de/en/news/Seven-critical-security-vulnerabilities-with-the-highest-rating-threaten-Coolify-11134651.html
  - Censys: https://censys.com/advisory/cve-2025-64424-cve-2025-64420-cve-2025-64419
- 比利时 CCB 警告页（2026-01-07 更新）：https://ccb.belgium.be/advisories/warning-critical-coolify-vulnerabilities-patch-immediately

## 3. 「实例被删/勒索」事件核实结果

- 多轮定向搜索（ransom / wiped / deleted instances 2025）**均未找到确认的攻击者批量删除实例并勒索的实际事件**
- 相关但有别的素材：
  - 用户个案：Reddit r/selfhosted「Server is getting hacked after installing coolify on VPS instance」（https://www.reddit.com/r/selfhosted/comments/1mnaf69/ ）——个案被黑（挖矿类）
  - GitHub discussion #3687「Here's how I broke Coolify – while updating through the web」——用户连点更新按钮致 env 丢失（自身升级事故，非攻击）
  - GitHub issue #6316「Volumes get deleted when stopping a service」——「Delete Unused Volumes」设置导致卷误删（产品行为风险）
- 判定：任务方提示的「2025-03 公开报道实例被删/勒索风波」**无法证实为实际事件**，如实按「漏洞披露+政府勒索风险警告+零星个案」记载；已发布官方修复均在披露后快速跟进

## 4. 对选型的含义（供报告风险节引用）

1. 面板 = root 级攻击面（管理着服务器 SSH key），暴露公网 = 高危（52k 实例暴露是实测数据）
2. 官方自己也建议 PrivateIP/VPN 访问面板（安装文档原文）
3. 2025-2026 两年内两波 critical 漏洞批披露，升级纪律必须严格（官方有自动更新通道，2025 年初曾对暴露实例强制推送）
