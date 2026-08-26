---
date: 2026-08-27
topic: 拿走路学 AI:从雾中行走到 atlas 馆群
related:
  - ../apprentice/items/express/describe-the-goal/
  - ../mistakes/items/vague-goal/
---

# 2026-08-27 · 拿走路学 AI:从雾中行走到 atlas 馆群

一场约三小时的对话,起点是一个认知问题,终点是一座馆群。摘要版(按 conversations/README 规则:保留原始表述、关键转折、最终结论)。

## 起点:走路与雾(需求的原始表述)

> 「我们打算从 a 点走到 z 点,但是中间都是迷雾,我们中间会经历哪些阶段(我以为的:计划,选择,推翻)我在拿走路来了解 ai。」

由此展开:勘察(计划之前被漏掉的阶段)、验证(选择与推翻之间被漏掉的阶段)、推翻不是阶段而是闭合循环的那条边。衍生概念:两种雾(路不清 vs Z 不清)、走过的路会重新起雾(上下文有限)。

## 修枝

> 「算法里面有个词叫修枝。有些数据其实可以不用遍历。我不希望用这些方式。」

结论:修枝质量取决于先验,先验来自全遍历;先走满再修枝;每一刀要挣来。

## FDE 字幕提取(第一次翻车与修正)

原始表述(翻车证据,已入 mistakes/vague-goal):

> 「比如我有一堆的 FDE 视频的字幕。我是希望从数据里面提取我想要的。但是理论上,我应该先让ai 修枝对不对。只不过我该怎么描述,你教教我」

修正:Z 三要素(产出形态/判据带正反例/保真度)+ 先复述再执行——沉淀为 apprentice 首课 describe-the-goal。

## 关键转折(用户的历次定调)

1. 「重复的部分,没必要换路,转成自动化,或者固定好描述,防止漂移呢」→ 固化光谱(路标→规则→公路→隧道),强制优于记忆。
2. 「我想做一个系列。ai 教教我的系列」→ apprentice 诞生;命名之争(ask/teach/apprentice)用户选 apprentice。
3. 「我想要的全是定案的。得出结论的」→ 收录即定案,结论馆不是草稿箱。
4. 「可我是为了复用啊」(反驳「别为翻车建馆」)→ 复用要的是路由不是搬家;视图维度 vs 内容维度。
5. 「我觉得你得直接迁移」→ monorepo;「yawyd 不是项目啊。是存项目的目录」→ atlas 落位 yawyd 之下;「总项目叫 atlas 如何?」→ 定名。
6. 「错题集落选折叠吧…错题集 · 翻车挺好的。但是为什么不是单独的项目呢」→ mistakes 馆 + 门户折叠。

## 过程事件

- pick git init(它是 yawyd 里唯一没进版本控制的项目);check-drift 首跑抓到 pick 渲染器列表前缀真 bug(raw string 双反斜杠),当日修复。
- monorepo 迁移:就地(路径零变化)→ 更名链 pick+apprentice → yawyd → halls → atlas;旧 `.git` 归档 `.git.archived-mono`。
- 第三馆(mistakes)触发 ORIGIN 写死的抽象条款:渲染器上提 `shared/render.py`,check-drift 转反向断言。
- GitHub Pages:configure-pages 的 enablement 被 GITHUB_TOKEN 拒(Resource not accessible by integration),以 gh api 手动建站解。

## 最终结论(沉淀成了什么)

- 三馆 + 门户:https://743v45.github.io/atlas/
- apprentice/express/describe-the-goal(首课,Z 三要素)
- mistakes/vague-goal(首条错题)
- PHILOSOPHY.md(理念与术语表)、atlas/DESIGN-TREE.md(总架构决策)
- 派出六个挖掘小队检索 309MB 历史会话找可抽离维度(进行中)
