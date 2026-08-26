# yawyd — 馆群 monorepo

一个仓、一个站、一条流水线。认知的定案住在馆里,门户与错题集聚合在根——**内容不搬家,原地链接**(单一事实源)。

## 馆

- **pick/** — 选什么:选型对比决策库(域 → 类别 → 条目,有据报告 + 决策矩阵)
- **apprentice/** — 怎么问:AI 学徒笔记库(结论馆,收录即定案)

各馆自带 RULES.md / 门禁 / CLAUDE.md,规则互不合并。第三个馆(如 spark 奇想录)出生即入本仓。

## 门户与错题集

根 `index.html` 由 `python3 scripts/build-atlas.py` 生成(需先跑两馆各自的 build):

- 馆导航 + 动态统计
- **错题集**——跨馆负知识聚合:翻车(apprentice 各课「翻车记录」)/ 落选(pick 的 hold)/ 腐烂警示(两馆超 180 天未验证或已过期)

## 部署

push 到 main → GitHub Pages 单站部署(`.github/workflows/pages.yml`:两馆 build + pick 防漂移断言 + atlas 聚合,纯标准库零依赖)。

## 迁移留档

2026-08-27 由 pick、apprentice 两个独立仓就地合并(路径未动,子目录 `.git.archived-mono/` 留存原仓历史;原 GitHub 仓库 743v45/pick、743v45/apprentice 仍在)。引擎血缘见 `apprentice/scripts/ORIGIN.md`——shared/ 抽取后,check-drift 退役。
