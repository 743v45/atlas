---
date: 2026-08-07
topic: xiaopacai 纸面样板冒充生产经验
related:
  - ../mistakes/items/paper-production-experience/
原始会话: ~/.claude/projects/-Users-taevas-code-mymy/c002eaf1-5bcd-43f1-8d93-3af3bbe82fa0.jsonl（08-07 会话，审查内容为 08-04/05 报告）
---

# 2026-08-07 · xiaopacai 纸面样板冒充生产经验

**原始表述（需求原话）**：「当我想学全栈，全运维，我要学什么。subagent 审查项目，运维部署选型，我想学系统工程，系统级别的。分析一份报告. 放 /Users/taevas/code/myself/报告 子目录里」

**关键转折**：subagent 审查报告揭穿 xiaopacai——「看起来完整、实际从未跑过」：全套 K8s/Helm/Prometheus 配置齐全但从未执行；三套互相矛盾的 CD 管线并存（.gitlab-ci.yml 用 SSH+PM2，ci-cd.yml 用 Helm+ghcr.io，cd.yml 混用两者）；占位 URL 全是 `*.example.com`；未执行过的 typo 遍地（`wc -h << EOF` 应为 `cat`、`frozen-locklockfile`、`docker-compose.testkt.yml`）；PM2 与 k8s 两套运行时并存。报告结论「双峰分布极其明显」：标杆是 agentproxy（真实生产级），幻觉是 xiaopacai——「这是最危险的」。

**最终结论（沉淀）**：根因是「读过模板 = 会生产运维」的幻觉；修正走路线图阶段 3 专破——亲手跑通一次真部署，让「读过」变成「跑过一次」。沉淀为本馆错题 [paper-production-experience](../mistakes/items/paper-production-experience/)。
