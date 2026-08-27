# apprentice — AI 学徒笔记库

一课一目录,记「怎么把意图交给 AI」(`items/<类别>/<课>/{meta.json, lesson.md}`)。主语是学徒,不是 AI——这库记的不是 AI 多聪明,是学徒怎么学会走路。

## 必守规则

- **写任何一课前先读 [RULES.md](RULES.md)**——目录命名、meta 字段、写作规范、结构判据都在里面。
- **课必须从真实对话里长出来**:meta.source 必填,禁止凭空创作方法论。想出来的课看起来一样整齐,但没有走过。
- **收录即定案**:课是结论馆不是草稿箱——走出结论、验证通过才建课;唯一后续变迁是过期(outdated)。
- **时效是硬规则**:verified + model 必标——无时效标注的课视为无效,模型换代后技巧会过期。超 180 天索引标「待重验」。
- **所有 HTML 均为生成物,禁止手改**:改完 meta 或 md 后跑 `python3 scripts/build-index.py`(含校验门禁:验证段/翻车记录必填、artifacts 路径存在性——不过门禁不进索引)。
- **图纸与公路对账**:课的 artifacts 指向沉淀出的模板 / skill / 规则文件,文件头注来源课;改路当天更新图纸(RULES 第 4 节)。
- **引擎单源**:渲染器与 BASE_CSS 住 `atlas/shared/render.py`,本馆 build 统一 import,本地不得有副本——对账跑根级 `python3 scripts/check-all.py`(含单源反向断言);纪律与触发条件见 `scripts/ORIGIN.md`。
