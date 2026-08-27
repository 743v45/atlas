# 三层开源栈（multica + 规划大脑 + Langfuse）

> **TL;DR**：自动化开发平台的推荐解是三层开源栈而非单一工具：① multica 自托管（协作/平台/远程）+ ② Claude Code 或 Deep Agents（规划大脑——是否接受 Claude 绑定的分叉未拍板，留给组织决策）+ ③ Langfuse 自托管（trace/eval/datasets 复利）；三层各自独立可用、全部可自托管。

- **结论**：adopt（组合方案；② 层选手未拍板，不影响栈结构成立）
- **核实日期**：2026-08-27（gh 一手数据 + 官网当日核实；选型过程出自 2026-08-05/06 会话）

## 基本信息

| 层 | 工具 | 解决什么 | 活跃度（gh 2026-08-27 采集） |
|---|---|---|---|
| ① 协作/平台/远程 | multica（自托管） | 团队 workspace、issue 流派发、Autopilot 定时、远程 daemon、web/desktop/手机看板 | ⭐47,969、push 2026-08-27 [2] |
| ② 规划大脑 | Claude Code **或** Deep Agents（作 custom runtime） | 需求拆解、sub-agents、验证、memory | Claude Code ⭐143,157、push 2026-08-26 [6]；Deep Agents ⭐28,584、push 2026-08-27 [7] |
| ③ 可观测/评估 | Langfuse（自托管） | trace 团队共享、eval、datasets 回归 | ⭐33,802、push 2026-08-27 [4] |

三层均为开源可自托管（multica [1][2]、Langfuse [3][4]、Deep Agents MIT [7]；Claude Code 为 Anthropic 商业产品、CLI 本体免费使用 [5][6]）。

## 为什么是「组栈」而不是「选一个」

- **单一工具覆盖不了三层需求**：起点是对 multica 的不满——它的「规划」只有两层（把 issue 派给 agent + Autopilot 定时触发），需求怎么拆、子任务怎么排依赖、做完怎么验证、失败怎么重规划，**全部压在单个 agent 的 prompt 里，平台不管** [8]。用户 100 篇 multica Issue 调研中的 #815、#1943、#1767、#2120 都戳中这一痛点 [8]。
- **关键洞察：multica 是两层，不是要被整体抛弃的工具**——弱的是它的规划大脑层，强的是远程控制基础设施层（server(Go) + daemon(远程机器) + web/desktop/手机三端架构）[8]。所以正解是「用规划大脑升级 multica 的 agent，不浪费已有投入」，而不是换平台 [8]。
- **③ 层选 Langfuse 而非 LangSmith，是为了数据不出内网**：trace 让团队看见 agent 干了什么；**eval + datasets 让「改进」可度量、可回归**——改进 agent 后自动跑历史数据回归，越用越准 [8]。
- **复利飞轮**：agent 干活 → Langfuse 留 trace → 团队标注 → 沉淀 dataset + skill → 下次改 agent 自动跑回归。三层各自复利、互相反哺（③→② eval 回归、③→① 质量门、②→① skill 沉淀）[8]。
- **渐进共建**：阶段 1 自托管 multica 团队先用 → 阶段 2 接规划大脑 runtime 升级 → 阶段 3 接 Langfuse 转起飞轮。每层独立可用，不必一次到位 [8]。

## ② 层分叉：Claude Code vs Deep Agents（未拍板）

同层对标（harness 侧）：Claude Agent SDK ↔ Deep Agents [8]。

| 维度 | Claude Code / Agent SDK | Deep Agents |
|---|---|---|
| 模型 | 绑 Claude | model-agnostic（含本地 Ollama/vLLM） |
| harness 成熟度 | 业界最成熟之一（工具链最全） | 成熟但更年轻 |
| 接 multica | **原生支持，零适配** | 需写 dcode↔multica 协议 wrapper |
| 规划能力 | Plan mode / Agent Teams / Workflow / subagents | 自带 planner + LangGraph durable execution |

- 唯一的真分叉：**是否接受 Claude 绑定**。接受 → Claude Code 更快更稳（multica 原生支持，省掉 wrapper 风险）；要 model-agnostic / 多模型 / 本地模型 → Deep Agents [8]。
- **如实记录：该分叉在选型会话内未拍板**，停在「这个答案直接定栈」的提问上，留给组织决策 [8]。本条目 verdict 落在栈结构（三层各自成立），不预支 ② 层结论。
- 规划层演进佐证：LangChain 官方在 LangGraph 之上推出 Deep Agents 高层封装（plan + subagents + filesystem），多 agent 官方推荐 tool-based supervisor——规划大脑已成为独立产品化层 [8]。

## 对比（会话内调研的备选，2026-08-05 gh 采集快照 [8]）

| 备选 | 定位 | 为何不是主推 |
|---|---|---|
| oh-my-claudecode ⭐38,352 | Claude Code 插件，`/autopilot` plan→build→qa 闭环 | 个人单机最快路径；平台/远程/团队层缺 |
| Orca ⭐37,967 | 可视化管一群并行 agent | 并行 fan-out 强，协作平台与观测闭环缺 |
| 三省六部 Edict ⭐16,329 | 审核闭环 + 实时看板 + 可干预 | 全链路自含，但生态与调研深度不及三层栈 |
| Open Multi-Agent ⭐6,722 | TS 框架，goal 自动拆 task DAG，可 replay | 要写代码，平台层全自建 |
| Plandex / MetaGPT | 计划驱动 coding / 多角色 SOP | 定位报告已写，均不覆盖三层 |

（star 为 2026-08-05 会话内 gh 采集快照，非当日值 [8]。）备选工具各有 12 节定位报告，与三层栈总览同库存档——原存团队知识库「技术设计」collection，2026-08-23 数据迁飞书 [8]。

## 风险与注意

- **② 层未拍板**（上文）：栈结构不受影响，但阶段 2 动工前必须先答「是否接受 Claude 绑定」。
- **最大技术不确定性**：若走 Deep Agents，dcode 接 multica runtime 需协议 wrapper（multica 已支持 claude/codex 等 14 种 runtime，wrapper 是可验证的小工程，但未实测）[8]。
- 11 份定位报告的原始 URL 已随知识库迁移失效，以飞书库为准（迁移记录见 lark-cli 会话 0e78d1c6）。

## 来源

1. Multica 官网 — https://multica.ai（访问 2026-08-27）
2. multica-ai/multica — https://github.com/multica-ai/multica（gh 2026-08-27 采集：⭐47,969、push 2026-08-27；原始响应留档 raw/2026-08-27/gh/multica-ai_multica.json）
3. Langfuse 官网 — https://langfuse.com（访问 2026-08-27）
4. langfuse/langfuse — https://github.com/langfuse/langfuse（gh 2026-08-27 采集：⭐33,802、push 2026-08-27；留档 raw/2026-08-27/gh/langfuse_langfuse.json）
5. Claude Code 产品页 — https://www.claude.com/product/claude-code（访问 2026-08-27）
6. anthropics/claude-code — https://github.com/anthropics/claude-code（gh 2026-08-27 采集：⭐143,157、push 2026-08-26；留档 raw/2026-08-27/gh/anthropics_claude-code.json）
7. langchain-ai/deepagents — https://github.com/langchain-ai/deepagents（gh 2026-08-27 采集：⭐28,584、push 2026-08-27、MIT；留档 raw/2026-08-27/gh/langchain-ai_deepagents.json）
8. Claude 会话 b0872007（2026-08-05/06）——选型全程原始记录（multica 100 篇调研、四维度对比、三层栈成形、Claude Code vs Deep Agents 对标、11 份定位报告写入）；提取文本留档 raw/2026-08-27/sessions/automation-platform-3layer-{user,assistant}.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（源会话 2026-08-05/06；dig INBOX 定稿入库） |
