# 自动化开发平台 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

AI 自动化软件开发（规划 → 执行 → 验证 → 记忆），用什么平台或工具组合？（2026-08-05/06 会话首问；2026-08-27 入库）

## 分叉与决策

### D1 痛点定位：multica「规划太简单」缺的是什么？

- 剖析：multica 的规划只有两层——issue 派发（或 Squad leader 路由）+ Autopilot 定时触发；需求拆解、子任务依赖、验证、重规划全压在单 agent prompt 里，平台不管。
- 决策：要补的不是 UI/平台层，而是**规划大脑本身**——锚定整个选型。

### D2 自建还是找现成？

- 决策：**找现成好用的**（用户在用 Claude Code，要拿来就能开发用），不是设计自研系统——调研 + 推荐任务。
- 落选节点：纯 LangGraph 自建（规划最可控，但门槛高、看板/手机端全要自己搭）。

### D3 单一工具还是组合栈？

- 关键洞察：multica 是两层——远程控制基础设施（强：server + daemon + 三端看板）+ 规划大脑（弱）。两层互补，不是二选一。
- 决策：**三层开源栈**——① multica 自托管（协作/平台/远程）+ ② 规划大脑 + ③ Langfuse 自托管（trace/eval/datasets 复利飞轮）。
- 落选节点：裸用 multica（规划外包单 prompt，即 D1 痛点）；单一工具路线（oh-my-claudecode / Orca / Edict / OMA 各覆盖一层，均不三层全含——12 节定位报告已备，作参照不为主推）。
- 叶：[三层开源栈](three-layer-stack/) adopt

### D4 ② 层选手：Claude Code 还是 Deep Agents？

- 同层对标：Claude Agent SDK ↔ Deep Agents（都是 harness）。唯一真分叉 = **是否接受 Claude 绑定**：接受 → Claude Code（multica 原生支持零适配、harness 最成熟）；要 model-agnostic → Deep Agents（需写 dcode↔multica wrapper）。
- **未拍板**：会话停在提问，留给组织决策。栈结构不依赖此答案，阶段 2 动工前必须先答。

## 叶子

- 叶：[三层开源栈（multica + 规划大脑 + Langfuse）](three-layer-stack/) adopt
