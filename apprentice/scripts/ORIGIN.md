# 引擎血缘

- **出身**:骨架复制自 pick(init `617c31a`,2026-08-27)。理念与方法复制,代码按 apprentice 的 schema 重写;**Markdown 渲染器(`render_inline` / `render_markdown`)与 `BASE_CSS` 原样共享**——这两处是真正的引擎层,其余是各自 schema 的必然分叉。
- **共享层同步纪律**:任一边修改渲染器或 BASE_CSS,当天同步另一边,两边各留一条 commit 说明改了什么。
- **对账**:`bash scripts/check-drift.sh`——精确 diff 共享的渲染器函数。输出「✅ 同步」即安心;有 diff 则逐处确认是「故意的分叉」还是「忘了同步」,当天处理。
- **抽象触发条件(写死)**:第三个同类馆出现,或引擎第三次跨馆改同一段逻辑时,把 build 拆成 schema 驱动的共享引擎。在此之前,不为未发生的漂移预付抽象的税。

## 对账记录

- **2026-08-27 首跑**:抓到 pick 渲染器列表前缀真 bug(ul/ol 的 `re.sub` 用了 raw string 双反斜杠,`- ` / `1. ` 前缀剥不掉),当日修复并双向同步——机制开门红。
- **2026-08-27 备注**:pick 工作树存在另一会话进行中的重构(`render_category_sections`),build 暂崩于 `render_index` NameError;渲染器块不受影响,对账照常。待该重构完成后,重跑 `pick` 的 build 确认。
