# 「门的门」:CI 绿不等于 sound,漂移发生在层间缝隙

> **TL;DR**:给 deepseek-harness 做了一次「治理体系自身的治理」审查(防漂移工具自己会不会漂移)。结论:治理的「机制层」有效——调度器有测试、CI 结构被钉住、manifest 双向自校验;但**漂移发生在无人守望的层间缝隙**,实证揪出 2 个孤儿 gate、9 行过期版本表、全线失守的软预算。核心方法论:**CI 绿只证明「接受当前仓库」,不证明「拒绝坏仓库」**——绿灯含义是 consistent(与当前仓库一致),不是 sound(真的挡得住坏东西)。

*(恢复自 2026-08-18 审查任务书驱动的问答,原结论骨架忠实;面向自洽的重组与解释标「AI 重构」。被审仓库为开源项目 deepseek-harness,证据行号对应当日快照。)*

## 一、核心命题:绿 ≠ sound

仓库自己的政策文件里就写着这句自认(i18n/README.md:40):

> green gate means consistent, not sound

具体到实例:翻译配对 gate 校验「中英文档的 pairing hash 一致」——它绿了,只说明两边是同一对;**它不校验翻译质量本身**。推广到一切门禁:门在跑、门是绿的,证明的是「当前仓库被这套规则接受了」;它不证明「一个坏仓库会被拒绝」。gate 的两个面(存在 ≠ 被执行)之间,就是漂移的藏身处。

## 二、漂移发生在三种层间缝隙

1. **散文 ↔ 磁盘**:文档/注释宣称的状态与代码实际状态脱节。实证:commit 97eb14a007 已删掉全部 `private: true`,但 AGENTS.md:100 与 vendor/README.md:34 仍声明它;AGENTS.md:73 说 hygiene 是 4 项检查,实际跑 12 项。
2. **gate 存在 ↔ gate 执行**:脚本存在不等于被任何 CI 路径引用。实证(2 个孤儿 gate):供应链 gate **verify-vendored-links** 只被本地 `hygiene` 聚合调用,CI 全部 15 个 workflow 零引用;**verify-cordis-api 是完全孤儿**——无任何引用方。根因:无机制强制新 verify 脚本挂进 CI,而 knip(死代码扫描)把 package.json scripts 当 entry 抓不到这种孤儿。
3. **注释 ↔ 行为**:脚本注释宣称的规则未被脚本强制。实证:doc-budgets 的 manifest 注释宣称「≥5% headroom ratchet」,脚本只查存在性+上限,4 个文件 headroom 实际为 0–1.1%;vendor/README.md 的 manifest 表 9 行版本全部过期(如 cordis 4.0.0-rc.7 → 实际 4.0.1),因为 check-vendor-manifest.sh 只盯 `vendor/*/src/**`,版本号 release 逃过守卫,且该守卫仅本地 hook、不进 CI。

## 三、治理工具自身的测试覆盖

- 28 个 verify-* 入口:9 个有直接 spec、4 个仅库级 spec、**15 个零测试**(含 verify-doc-budgets、verify-type-equiv、verify-vendored-links 这些最核心的门)。
- 12 个 gen-* 生成器:8 个无 spec,由 verify-* catalog 再推导比对补偿。
- **覆盖率门的作用域是 `packages/*/*/src`(vitest.config.ts:166)——scripts/ 下的治理代码完全豁免于 100% 覆盖门**:门卫自己不在门内。
- manifest 自治理强度排序:type-equiv 最强(块↔条目 1:1 双向强制)> translation-pairing(双向排除强制但无 stale-exclusion 检查)> doc-budgets 最弱。

## 四、仓库自认的失效模式

- 100% 覆盖率催生 assertion-free 测试(为覆盖率而写的空断言测试);变异测试(mutation testing)对冲方案自 2026-06-11 提出后至今仍 proposed。
- gen-doc-graphs 的 Client-face 事件监听已知漏报(:790 TODO)。

## 五、防漂移的漂移:gate 清单自身的结构

gate 清单**集中式**于 run-gates.ts(docSyncLeafGates L590-635),且有图校验 spec 钉住——这是有效的一面(新增 gate 改一处、被测试保护)。盲区在入口端:没有任何机制强制「新写的 verify 脚本必须挂进 CI 路径」,孤儿 gate 的出现是结构性必然,不只是失误。

## 六、可迁移的审查清单

*(AI 重构:从本次审查提炼,原文散落各节。)*

1. 数一遍 gate:写出来的门有几个真的被 CI 引用?(孤儿 gate 清单)
2. 数一遍门的测试:治理脚本本身有几个有 spec?覆盖率门罩不罩治理代码?
3. 抽查三缝隙各一例:文档说 X 代码还是 X 吗?脚本注释说的规则脚本真的强制吗?manifest 里的数字和现实一致吗?
4. 问一句「绿证明什么」:每盏绿灯的精确语义是 consistent 还是 sound?

## 出处

- 源对话归档:../../../conversations/2026-08-18-deepseek-harness-self-governance.md(2026-08-18)
- 原始会话:~/.claude/projects/-Users-taevas-code-openresources-deepseek-harness/163afc75-d939-4984-ae98-aa89375ad52d.jsonl
- 关联:同仓库设计哲学全景见 [deepseek-harness-design-philosophy](../deepseek-harness-design-philosophy/);本条是它的「已知漏洞」收尾维度。
