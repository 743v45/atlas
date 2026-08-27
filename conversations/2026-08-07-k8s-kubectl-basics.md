---
date: 2026-08-07
topic: kubectl 与 k8s 入门速查
related:
  - ../asked/items/k8s-kubectl-cheatsheet/
原始会话:
  - ~/.claude/projects/-Users-taevas/86bf1d57-f3a8-43d7-b18c-6e111d5ceaf3.jsonl(命令/术语/层级/CronJob)
  - ~/.claude/projects/-Users-taevas/0217db00-8872-4e76-b2ae-c8d0739773fc.jsonl(pods 维度之问)
  - ~/.claude/projects/-Users-taevas/c11736ad-cddc-4dbe-91f4-e40ec00a373b.jsonl(kubectl 查询脚本盘点)
---

# 2026-08-07 · kubectl 与 k8s 入门速查

主会话(86bf1d57)是密集的入门连环问:「kubectl 怎么查看服务列表」「kubectl 怎么用,有哪些主要功能」「术语解析 pods/svc/deploy/node,除了这些还有哪些」「怎么看它从哪里拉的镜像」「服务和脚本怎么区分」「还有定时脚本,kubectl 里怎么查」。AI 逐题给成体系的答案:三场景命令组(查看/增删改/调试日志/发布滚动/标签/集群节点/配置上下文/输出格式)、14 个资源缩写速记、资源层级结构、「服务 vs 脚本」的判据(restartPolicy: Always 的常驻服务 vs Never/OnFailure 的跑完即退任务,CronJob 管定时)、CronJob→Job→Pod→日志的排查链。用户给出一页缩写笔记(po/svc/deploy/rs/sts/ds/ns/cm)作确认。AI 按关系图规则落盘 ~/docs/k8s-resource-hierarchy.html,并按流程脚本化规则用 curl 驱动脚本把内容发布到自托管 Outline(collection「Kubernetes」+ 1 父文档 + 5 子文档,7 次 API 全 200,总耗时 1961ms,带判重不覆盖);后段补讲 ConfigMap 查看(describe 即明文,Secret 才要 base64 -d)与「改 cm 后 volume 挂载约 1 分钟自动更新、envFrom 注入须重启才生效」的坑。

两个卫星会话:0217db00 问「pods 是什么维度」,因缺上下文 AI 请用户给出处而非硬答;c11736ad 问「用 kubectl 查询脚本有哪些(禁止操作数据)」,AI 盘点自有项目结论——纯查询 kubectl 脚本几乎没有,大多是 CI 部署调用,唯一接近的 e2e-test.sh 同文件混有 kubectl delete 不能整文件套用(该部分属仓库调研,不入讲义)。

讲义恢复为 asked/items/k8s-kubectl-cheatsheet,主体取主会话。
