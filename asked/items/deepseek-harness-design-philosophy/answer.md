# deepseek-harness 的设计哲学:为无记忆的 AI agent 造工具

> **TL;DR**:对开源仓库 deepseek-harness(50+ 包的 agent 运行时)做十维度并行分析后,可以把它的全部设计收敛到一个第一性假设——**读者与贡献者是跨 session 无记忆的 AI agent**。由此推导出七根支柱:一切皆插件、单一事实源其余皆投影、信任边界由序列化介质枚举、seam 按演化速率划界、响亮失败、判断落成机器可校验工件、测试即证据。完整分析已落盘该仓库 analyze/ 目录,本条是 TL;DR + 骨架 + 指针。

*(本条为「指向条目」:正文只留骨架,完整论证见落盘文件,不搬运。)*

## 第一性假设

仓库围绕「读者与贡献者是跨 session 无记忆的 AI agent」设计——一切文档、门禁、工件的存在,都是给不记得上次做过什么的协作者(人或 AI)买保险。

## 七根支柱(骨架)

1. **一切皆插件**——内核收缩到 vendored Cordis 的组合语义 + 一条 durable session log;连 agent-loop 都是可替换插件,「plugins, not loop changes」写进根规则并强制架构图同步。
2. **单一事实源,其余皆投影**——session log 是唯一事实,模型历史/fixture/审计是投影;TS 类型树是另一棵事实源,wire codec/双 SDK/文档目录由它派生;反模式是「第二份需要同步的拷贝」。Model-visible ⟺ logged 有 runtime 断言。
3. **信任边界由序列化介质枚举**——config/queued/tool JSON/file/worker/process/wire 七类边界才校验,进程内靠 brand 类型防串线而非重验;校验点清单由介质决定,不靠风险直觉。
4. **capability seam 按演化速率划界**——三角色完备律(Request/Spec/resolve 显式默认化);vendoring 同样按「internals 是否承载正确性」划界。
5. **响亮失败**——required-on-read「过度拒绝优于静默残缺」;审批 fail-closed;版本钉 0 的零兼容窗口。
6. **判断落成工件**——决策→Agent Note(Alternatives 强制)、规则→27 个门、审查→skill、证据→最小证伪;不依赖人的记忆。
7. **测试即证据**——per-file 100% 覆盖被定位为*删代码机制*(未覆盖行是待删的死代码);postmortem 0001 之后「组装转录 > 单测」;verify the world, not the self-report。

**五个最反常规决策**:循环也是插件 / Model-visible⟺logged 有 runtime 断言 / per-file 100%=删代码机制 / CoT-leakage 分类学 / 有账本的 vendored fork。

**附赠发现**:一处真实文档漂移——AGENTS.md:100 与 vendor/README.md:34 仍写 vendored 包 `private: true`,但框架已公开发布为 `@deepseek-ai/cordis` 4.0.1。(该漂移的系统性追问见同馆 [gate-of-gates-green-not-sound](../gate-of-gates-green-not-sound/)。)

## 方法

10 个维度并行 agent 分析(核心架构 / capability seam / 类型边界 / 会话可观测性 / 测试 / 治理 / 防御模式 / vendoring / loop 与工具 / 前端 SDK / 文档文化),交叉综合成 1 个第一性假设 + 7 根支柱,非简单拼接。

## 指向:落盘文件(正文所在)

| 文件(位于 ~/code/openresources/deepseek-harness/) | 定位 |
|---|---|
| analyze/DESIGN_PHILOSOPHY.md | 完整版,~600 行,全部论断带 `file:line` 证据 |
| analyze/KEY_POINTS.md | 重点提炼纯文本版(~90 行,可粘贴引用) |
| analyze/index.html | 单页报告:重点 + 5 张内嵌 mermaid 关系图 |
| analyze/design-philosophy.html | 5 图全集(事实源→投影 / 七类信任边界 / seam 三角色 / 治理流水线) |
| analyze/INDEX.md | 主索引:阅读顺序与维度覆盖 |

## 出处

- 源对话归档:../../../conversations/2026-08-18-deepseek-harness-philosophy.md(2026-08-18)
- 原始会话:~/.claude/projects/-Users-taevas-code-openresources-deepseek-harness/78f956bc-bb7b-4aca-895a-671827784f26.jsonl
- 恢复说明:讲义当日已完整落盘被分析仓库的 analyze/ 目录(浏览器实测 5 SVG 全渲染、0 语法错误),本条按「指向条目」处理:TL;DR + 骨架 + 指向,不搬正文。
