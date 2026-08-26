# atlas — 馆群 monorepo

atlas = 地图集:馆是图上的区域,错题集是警示图层,根 `index.html` 是封面。一个仓、一个站、一条流水线——**内容不搬家,原地链接**(单一事实源)。

**[PHILOSOPHY.md](PHILOSOPHY.md) — 设计理念与术语表,新会话先读它。**

住在 `~/Code/yawyd/`(纯项目容器)之下,与其他项目平级。

## 馆

- **pick/** — 选什么:选型对比决策库(域 → 类别 → 条目,有据报告 + 决策矩阵)
- **apprentice/** — 怎么问:AI 学徒笔记库(结论馆,收录即定案)
- **mistakes/** — 怎么摔的:错题集(经过 / 根因 / 修正,单一事实源)
- **spark/** — 想去哪:奇想录(低摩擦苗圃,毕业制流向三馆)

**conversations/** — 对话归档:三馆 source 的底座(建条当日归档,source 变实路径)。
**DESIGN-TREE.md** — 总设计树(跨馆架构决策,变更当日加节点)。

各馆自带 RULES.md / 门禁 / CLAUDE.md,规则互不合并。渲染引擎单源 `shared/render.py`(新馆复制骨架、删副本、接 shared)。时态分工:spark 将来时 / 对话现在时 / 三馆完成时。

## 门户与错题集视图

根 `index.html` 由 `python3 scripts/build-atlas.py` 生成(需先跑三馆各自的 build):

- 馆导航 + 动态统计
- **翻车**:mistakes 馆条目,根因一行直读
- **落选**:pick 的 hold 条目(默认折叠)
- **腐烂警示**:两馆超 180 天未验证/过期的条目

## 部署

push 到 main → GitHub Pages 单站部署:三馆 build + pick 防漂移断言 + atlas 聚合,纯标准库零依赖。

## 迁移留档

2026-08-27 由 pick、apprentice 两个独立仓就地合并(先名 yawyd 后更名 halls,终名 atlas;子目录 `.git.archived-mono/` 留存原仓历史;原 GitHub 仓库 743v45/pick、743v45/apprentice 仍在)。引擎血缘见 `apprentice/scripts/ORIGIN.md`——shared/ 抽取后,check-drift 退役。
