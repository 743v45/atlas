# atlas — 五馆横评(概念固定)

一张表固定五馆的边界,新条目不知道去哪时先查这里。走路体系:**asked 是师父讲的地形,apprentice 是师父教的走法,pick 是你选定的路线,mistakes 是你摔过的跤,spark 是你想去还没去的地方。**

| 维度 | pick | apprentice | mistakes | spark | asked |
|---|---|---|---|---|---|
| 一句话 | 选什么 | 怎么做 | 怎么摔的 | 想去哪 | 是什么、为什么 |
| 定义域 | 对比后的选型结论 | 「把意图交给 AI」的协作方法 | 真实翻车的完整档案 | 没走通的念头 | 一切值得留存的问答 |
| 本质 | 决策(拍板) | 方法论(长在手上) | 反例(伤疤) | 意向(占座) | 知识(进脑子) |
| 时态 | 完成时·会过期 | 完成时·会过期 | 过去时·不过期 | 将来时·不死 | 完成时·可更新 |
| 收录门槛 | 有据(来源+时间戳) | 走通+验证过(收录即定案) | 经过/根因/修正三段俱全 | 一句话即可(低摩擦是功能) | 自洽+出处可溯 |
| 门禁(代码) | verdict 枚举/来源非空/star 一致 | 验证段+翻车记录必填/artifacts 存在 | 三小节必填/related 存在 | 仅毕业去向必须真实 | source 路径存在/TL;DR 必在 |
| 复用动作 | 决策前查 | 下次照做 | 下次防着 | 想到先查(防重复提案) | 忘了翻查 |
| 失效方式 | 数据过期→待复核 | 模型换代→outdated | 不失效(复发→recurring) | 不失效(毕业/尸化) | 知识陈旧→更新正文 |
| 状态机 | adopt/trial/assess/hold | settled/outdated | fixed/recurring | idea/snoozed/graduated/dropped | 无(图书馆式) |
| 条目文件 | report.md | lesson.md | mistake.md | spark.md | answer.md |

## 边界口诀

- 问「**怎么做**」→ apprentice;问「**是什么/为什么**」→ asked。
- 带对比与 verdict → pick;只有结论没有对比 → 不是 pick。
- 摔了有根因 → mistakes;只是没走通 → spark。
- 同一场对话可拆多馆:方法进 apprentice,原理进 asked,翻车进 mistakes(首例:08-05 SQLite 场,一谈三收)。
- **有门禁的才是馆**;跨馆已有内容的复用是视图,进门户聚合(atlas 错题集层),不建内容馆。

## 与馆外体系的关系

- **taevas-plugins**:课/方法毕业成 skill 的发布形态(apprentice 的 artifacts 去向之一)。
- **conversations/**:三馆(apprentice/mistakes/asked)source 的底座——建条当日归档,可溯落地。
- **dig/**:历史会话翻阅,产出按本表分流。

---
*概念即定,改动需过 atlas/DESIGN-TREE 记节点。2026-08-27 立。*
