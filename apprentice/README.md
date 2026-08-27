# apprentice — AI 学徒笔记库

向 AI 学艺的笔记：一课一目录，记「怎么把意图交给 AI」。主语永远是学徒——这库记的不是 AI 多聪明，是学徒怎么一点点学会走路。

课从真实对话里长出来（禁凭空创作），必带验证方法与翻车记录；沉淀出的模板 / skill / 规则反向链接回课，**图纸与公路永不对岔**。

**记录规则见 [RULES.md](RULES.md)，写任何一课前先读它。**

## 结构

```
apprentice/
├── README.md            # 本文件
├── CLAUDE.md            # 会话必守规则(AI 进入目录自动加载)
├── RULES.md             # 记录规则(核心)
├── DESIGN-TREE.md       # 架构决策树(变更当日加节点)
├── index.html           # 索引页(生成物,禁止手改)
├── scripts/
│   ├── build-index.py   # 聚合 meta + 渲染全部 HTML(含校验门禁 + 膨胀预警)
│   └── ORIGIN.md        # 引擎血缘:共享层、同步纪律、抽象触发条件
├── template/            # 新课模板(meta.json + lesson.md)
└── items/               # items/<类别>/<课>/{meta.json, lesson.md, lesson.html}
```

发布:push 到 atlas 的 main 由根 CI 统一构建部署(子目录 `.github` 在 monorepo 中不生效,已删;纯标准库零依赖);生成物入库,克隆即看。

## 快速上手

新建一课：

```bash
mkdir -p items/<类别>/<课>
cp template/meta.json template/lesson.md items/<类别>/<课>/
# … 从真实对话沉淀写作，遵守 RULES.md 第 3 节 …
python3 scripts/build-index.py   # 校验 + 渲染全部页面
```

日常查看：浏览器打开 `index.html`，按症状搜索、点状态章过滤，进入渲染后的课页（带面包屑与上下篇导航）。

## 与姊妹库的关系

- **pick** 管「选什么」，**apprentice** 管「怎么做」，**asked** 管「是什么/为什么」——五馆边界口诀见根 [COMPARISON.md](../COMPARISON.md)。
- 同一套骨架哲学：唯一事实来源在 meta + md，HTML 全生成，门禁不过不进索引。
- 引擎血缘与同步纪律：`scripts/ORIGIN.md`。

## 唯一事实来源

- 课的元信息只存于 `items/<类别>/<课>/meta.json`
- 所有 HTML 完全由脚本生成——改 meta 或 md 后重跑 build，不要手改
- 门禁校验：必填字段、status 枚举、日期格式、「## 验证」「## 翻车记录」小节、artifacts 路径存在性。不过门禁的课进不了索引
