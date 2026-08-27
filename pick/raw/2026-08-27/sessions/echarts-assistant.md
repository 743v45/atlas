桑基图的工具选型，按你的场景（自包含 HTML、落 `docs/`、可交互）给推荐：
## 推荐：ECharts（HTML 首选）
`type: 'sankey'`，CDN 引入即用，交互（hover 高亮流向、拖拽节点）开箱即得，自包含单文件 HTML 放 `docs/*.html` 直接打开：
```js
series: [{
  type: 'sankey',
  data: [{ name: '搜索' }, { name: '详情页' }, { name: '下单' }],
  links: [
    { source: '搜索', target: '详情页', value: 300 },
    { source: '详情页', target: '下单', value: 120 },
  ],
  emphasis: { focus: 'adjacency' }  // 悬停聚焦上下游
}]
```
## 其他选项按场景
| 场景 | 工具 | 说明 |
|------|------|------|
| Python 工作流 | **Plotly** `go.Sankey` | 几行代码出交互图，可导出 HTML；matplotlib 无内置桑基，不推荐硬画 |
| 已有 mermaid 习惯 | **mermaid `sankey-beta`** | v11+ 支持，数据就是 CSV 三列（source,target,value），但定制能力弱（颜色/布局控制少） |
| 不想写代码 | **RAWGraphs** / **Flourish** | 网页拖数据即出图，适合一次性汇报 |
| BI 环境 | Tableau / Power BI | 自带桑基，但两者原生桑基都别扭，Power BI 需自定义视觉对象 |
| 极致定制 | **d3-sankey** | ECharts 不够用时才上，代码量大 |
## 结论
- **让我直接画一张** → ECharts HTML（符合你的 HTML 关系图习惯，配色我可以按 dataviz 规范走分类色序 + 校验）
- **数据在 Python/pandas 里** → Plotly，`fig.write_html()` 出单文件
- **快速贴个 markdown** → mermaid `sankey-beta`，但超过 ~15 个节点或需要配色控制时换 ECharts
要注意的一点：桑基图对数据结构有要求（有向无环流，节点进出总量最好守恒），数据脏时 ECharts 会画出自环或比例失衡的带子——如果你的数据源头复杂，画之前我可以先帮你清洗校验。要画的话把数据给我即可。
**ECharts。** 「让 AI 写」这个前提下没有悬念：
1. **声明式配置**——整个图就是一个 `option` 对象，数据是 `data`/`links` 数组。AI 生成 JSON 配置的准确率远高于命令式代码，改数据不用动逻辑。
2. **自包含 HTML**——CDN 两行 + 配置，落 `docs/*.html` 浏览器即开，符合你的习惯。
3. **闭环验证**——AI 写完可以用浏览器直接打开截图检查（布局、标签碰撞、比例），写→看→改在一个流程里，这是给 AI 写代码最重要的性质。
4. **容错好**——节点排序、带子布局、标签避让都是引擎自动算的，AI 不用写布局数学（d3-sankey 就得手写，AI 容易翻车）。
对比一下 AI 生成友好度：
| 工具 | AI 写起来 | 问题 |
|------|----------|------|
| **ECharts** | ✅ 一个 option 对象 | 无 |
| Plotly (Python) | ✅ 几行声明式 | 输出 HTML 略重，交互样式不如 ECharts 精致 |
| mermaid sankey-beta | ✅ 三列 CSV | 定制太弱，节点一多就没法看 |
| d3-sankey | ⚠️ 命令式 + 手动布局 | AI 写错率高，只做极致定制才值得 |
**结论**：数据给我，我直接用 ECharts 出 `docs/*.html`，配色按 dataviz 规范（分类色固定顺序 + 调色板校验），写完截图验证再交。
