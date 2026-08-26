# dig — 历史会话翻阅规则(方法)

> 给任何 AI 的操作手册:翻阅历史会话,为 atlas 馆群补充内容、探索新维度。本文件只管**怎么翻**;翻的节奏与进度见同目录 [TIMELINE.md](TIMELINE.md),进度状态以 `progress.json` 为唯一事实源。

## 0. 前置阅读

- `atlas/PHILOSOPHY.md`(末尾术语表必读:Z、两种雾、修枝、收录即定案……)
- 分流目标的馆规:`apprentice/RULES.md`、`mistakes/RULES.md`、`spark/RULES.md`(各馆的 meta 字段与门禁)

## 1. 数据源与抽取方法

- 数据:`~/.claude/projects/<项目目录>/<uuid>.jsonl`,每行一个 JSON;`type=="user"` 的行是用户消息,`message.content` 是字符串或数组(数组取 `type=="text"` 项;跳过 tool_result)。
- 抽用户消息(定主题用):

```bash
jq -r 'select(.type=="user") | .message.content | if type=="string" then . else ([.[]? | select(.type=="text") | .text] | join("\n")) end' FILE | head -60
```

- **抽样纪律**:大文件只看前 60 条用户消息;跨会话归纳活动模式,不陷进单会话细节。
- 排除:当前活跃会话(正在写的那个 jsonl);已归档进 `atlas/conversations/` 的对话标注「已有归宿」即可,不重挖。

## 2. 识别五类发现

| 类型 | 判据 | 建议去向 |
|---|---|---|
| 翻车 | 有原始表述 + 可落到判断上的根因 + 可复用的修正 | mistakes |
| 走通的方法 | 有结论、**须可验证**(复述关/同输入对比/格式锚标任一) | apprentice |
| 选型结论 | 有对比、有依据、有 verdict | pick |
| 没走通的念头 | 困惑、假设、半成品脑洞 | spark |
| 新维度 | 反复出现的活动模式(见 §4 判据) | 建馆候选 or 门户视图候选 |

已有归宿的主题(标注即可):选型对比、向 AI 学艺、atlas 馆群建设本身。

## 3. 分流规则(硬边界)

- **spark 级:AI 可直接录入**——它是草稿箱,低摩擦是功能。录入后跑 `spark/scripts/build-index.py`。
- **馆级(课 / 错题 / 选型)与新维度候选:一律写入 `dig/INBOX.md` 待审区,状态 pending**——定夺权全在用户(promoted 转正 / dismissed 清理,标记动作见 INBOX 头部规则)。收录即定案,门禁归人,不由 AI 代定。
- **每条发现必须带来源**:会话文件名前 8 位 + 日期 + 项目目录名。翻车的原始表述**保留原文**(它是证据,不是转述)。
- 用户标记 promoted 后:AI 执行入库(写 meta+md、跑对应馆 build,门禁必须过),`git commit + push`(注明 `[dig]`),INBOX 条目移入已决区,更新 `progress.json`。

## 4. 新维度判据

- **建馆候选**:有自己的实体与生命周期、**该有自己的门禁**(mistakes 有三小节门禁,spark 有毕业制门禁——有门禁的才是馆)。
- **门户视图候选**:只是各馆已有内容的跨库复用(翻车汇总、落选、过期)——进 atlas 门户聚合,内容不搬家。
- **收编进现有馆**:形态是已有馆的变体(操作剧本 → apprentice 的 automate 类)。
- 分不清时问一句:它有自己的门禁要守吗?

## 5. 汇报格式(最终回复 = 纯数据)

```
## 发现
[类型] 标题 | 来源(文件前8位+日期+目录) | 一句话 | 建议去向
## 新维度
维度名 | 证据(会话数+模式描述) | 建馆 / 视图 / 收编
## 当日一句话
```
