# atlas — 馆群 monorepo

atlas = 地图集:馆是图上的区域,错题集是警示图层,根 `index.html` 是封面。一个仓、一个站、一条流水线——**内容不搬家,原地链接**(单一事实源)。

**[PHILOSOPHY.md](PHILOSOPHY.md) — 设计理念与术语表,新会话先读它。**

住在 `~/Code/yawyd/`(纯项目容器)之下,与其他项目平级。

## 馆

- **pick/** — 选什么:选型对比决策库(域 → 类别 → 条目,有据报告 + 决策矩阵)
- **apprentice/** — 怎么做:AI 学徒笔记库(方法,收录即定案)
- **mistakes/** — 怎么摔的:错题集(经过 / 根因 / 修正,单一事实源)
- **spark/** — 想去哪:奇想录(低摩擦苗圃,毕业制流向各馆)
- **asked/** — 是什么、为什么:问答馆(我问、AI 长答、值得留存;自洽+可溯)

**五馆横评与边界口诀见 [COMPARISON.md](COMPARISON.md)——概念固定,新条目不知去哪先查它。**

**conversations/** — 对话归档:apprentice / mistakes / asked 三馆 source 的底座(建条当日归档,source 变实路径)。
**DESIGN-TREE.md** — 总设计树(跨馆架构决策,变更当日加节点)。
**dig/** — 历史会话翻阅:方法规则 `dig/RULES.md`(任何 AI 读了即可执行)+ 时间线规则 `dig/TIMELINE.md` + 进度 `dig/progress.json`(唯一事实源)+ **`dig/INBOX.md` 候选收件箱**(维度与馆级候选待审,用户标记 promoted/dismissed)。

各馆自带 RULES.md / 门禁 / CLAUDE.md,规则互不合并。渲染引擎单源 `shared/render.py`(新馆复制骨架、删副本、接 shared)。时态分工:spark 将来时 / 对话现在时 / pick·apprentice·asked 完成时 / mistakes 过去时不过期。

## 门户封面与错题集

封面 `index.html` 由 `python3 scripts/build-atlas.py` 生成(需先跑五馆各自的 build),只回答「这是什么地方、去哪」:大标题 + 一句话 + 五馆卡片(各带一枚馆印)。

错题集只有一处:**mistakes 馆索引**(`mistakes/index.html`)。馆索引主表(搜索/状态过滤/排序)之外,页面底部附两区跨馆警示——直读邻馆 meta(源文件),内容不搬家,原地链接(见 [DESIGN-TREE.md](DESIGN-TREE.md) A11):

- **落选**:pick 的 hold 条目(默认折叠),按 push 倒序,无 stats 的沉底
- **腐烂警示**:pick / apprentice 超 180 天未验证/未采集的条目 + apprentice status=outdated,按腐烂天数倒序

两区是聚合警示区不是第六馆(有门禁的才是馆,见 PHILOSOPHY.md §5)——不过 mistakes 门禁,只聚合+链接。

## 默认排序

入口页一律**日期倒序**(口径与各馆字段选择见 [DESIGN-TREE.md](DESIGN-TREE.md) A10):索引表行序与详情页上下篇导航同源同一份 Python 列表,故排序在 build 层做,两处才自洽;同日/同值条目按目录名升序定次级键,输出可复现。

## 部署

本地一键:`python3 scripts/build-all.py`——五馆 build + atlas 聚合 + 全部断言,顺序与 CI 一致,任一步失败即停并打出失败现场;只做构建不刷新数据(star/push 采集另行先跑 `pick/scripts/refresh-stats.py`)。

push 到 main → GitHub Pages 单站部署:五馆 build + pick 防漂移断言 + 全站链接断言 + atlas 聚合,纯标准库零依赖。

## 迁移留档

2026-08-27 由 pick、apprentice 两个独立仓就地合并(先名 yawyd 后更名 halls,终名 atlas;文件级合并,原仓提交历史未继承)。原 GitHub 仓库 743v45/pick、743v45/apprentice 已删除;原仓完整历史另存两处——私有档案仓 [743v45/pick-archive](https://github.com/743v45/pick-archive)、[743v45/apprentice-archive](https://github.com/743v45/apprentice-archive),以及本机子目录 `.git.archived-mono/`(被 .gitignore 忽略,不随本仓分发)。引擎血缘见 `apprentice/scripts/ORIGIN.md`——shared/ 抽取后,check-drift 断言并入根级 `scripts/check-all.py`。
