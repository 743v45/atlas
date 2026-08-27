# Apache ECharts

> **TL;DR**：「让 AI 写」前提下的图表库首选：声明式 option 对象让 AI 生成准确率远高于命令式代码，自包含单文件 HTML 落 docs/ 浏览器即开、写→看→改可闭环验证，桑基等复杂布局由引擎自动计算——适用域明确为 AI 代写，人工手写场景不限于此。

- **结论**：adopt（适用域：**AI 代写图表**——本条目的全部裁决都以「图是 AI 写出来的」为前提）
- **核实日期**：2026-08-27（gh 一手数据 + 官网当日核实；选型出自 2026-08-18 会话）

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本线 | Apache 顶级项目，官网当前 v6 代 | [1][2] |
| 许可证 | Apache-2.0 | [2] |
| 维护活跃度 | ⭐67,160、push 2026-08-04（gh 2026-08-27 采集） | [2] |
| 触发场景 | 桑基图问句（「桑基图用什么画图…最佳用什么。让 ai 写」） | [4] |

## 为什么选（AI 代写域内的四条论断）

1. **声明式配置**：整个图就是一个 `option` 对象，数据是 `data`/`links` 数组——AI 生成 JSON 配置的准确率远高于命令式代码，改数据不用动逻辑 [4]。官方范式即为 option 配置式 [3]。
2. **自包含 HTML**：CDN 两行 + 配置，落 `docs/*.html` 浏览器即开，符合「关系图默认 HTML」的既有工作流 [4]。
3. **闭环验证**：AI 写完可以用浏览器直接打开截图检查（布局、标签碰撞、比例），写→看→改在一个流程里——这是给 AI 写代码最重要的性质 [4]。
4. **容错好**：节点排序、带子布局、标签避让都是引擎自动算的，AI 不用写布局数学 [4]。

桑基图最小用法（会话原样 [4]）：

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

## 对比（AI 生成友好度，会话内对比 [4]）

| 工具 | AI 写起来 | 问题 |
|---|---|---|
| **ECharts** | ✅ 一个 option 对象 | 无 |
| Plotly（Python） | ✅ 几行声明式 | 输出 HTML 略重，交互样式不如 ECharts 精致 |
| mermaid `sankey-beta` | ✅ 三列 CSV | 定制太弱，节点一多就没法看（>~15 节点换 ECharts） |
| d3-sankey | ⚠️ 命令式 + 手动布局 | AI 写错率高，只做极致定制才值得 |
| RAWGraphs / Flourish | 无代码（人拖数据） | 一次性汇报可，不是 AI 代写通道 |
| Tableau / Power BI | BI 内置桑基 | 原生桑基都别扭，Power BI 需自定义视觉对象 |

## 风险与注意

- **数据结构要求**：桑基图要求数据为有向无环流、节点进出总量最好守恒——数据脏时 ECharts 会画出自环或比例失衡的带子，画之前先清洗校验 [4]。
- **CDN 依赖网络**：自包含 HTML 引 CDN 脚本，离线场景需把 `echarts.min.js` 内嵌进单文件。
- 适用域声明：本结论限定「AI 代写」前提；人工手写、深度定制（自绘布局数学）场景不受此裁决约束 [4]。

## 来源

1. Apache ECharts 官网 — https://echarts.apache.org（访问 2026-08-27）
2. apache/echarts — https://github.com/apache/echarts（gh 2026-08-27 采集：⭐67,160、push 2026-08-04、Apache-2.0；原始响应留档 raw/2026-08-27/gh/apache_echarts.json）
3. ECharts 官方入门（option 配置式用法） — https://echarts.apache.org/handbook/zh/get-started（访问 2026-08-27）
4. Claude 会话 31db8d0e（2026-08-18）——桑基图选型与 AI 代写友好度对比；提取文本留档 raw/2026-08-27/sessions/echarts-{user,assistant}.md

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（源会话 2026-08-18；dig INBOX 定稿入库） |
