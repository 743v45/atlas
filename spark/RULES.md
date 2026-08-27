# spark — 记录规则

奇想录:没走通的念头。四馆收结论(pick / apprentice / mistakes / asked),这里收「想去但还没走的 Z」。

## 1. 什么算一条念头

- 点子、假设、困惑、半成品脑洞——共同点只有一个:**还没成为结论,但值得占个座**。
- 从真实对话或真实处境里冒出来;一句话也够。**低摩擦是核心功能**:无必填小节,md 可以只有一行。
- 单层 `items/<念头>/`;条目 >9 且类型分化明显时再谈分类(与 apprentice 结构判据同源)。

## 2. meta 字段(刻意轻)

| 字段 | 必填 | 说明 |
|---|---|---|
| name | ✓ | 一句话说清这个念头想干什么 |
| date | ✓ | 冒出日期 YYYY-MM-DD |
| status | ✓ | `idea`(灵感)/ `snoozed`(搁置)/ `graduated`(毕业)/ `dropped`(放弃) |
| tags | | 随意标签 |
| graduated_to | | 毕业去向(相对本馆根的路径,可跨馆 `../`)**——status=graduated 时必填且必须存在** |

## 3. 生命周期(毕业制)

- 冒出 → `idea`;挂着不动的改 `snoozed`。
- 走通了 → `graduated` + 填 `graduated_to`(去向:apprentice 课 / mistakes 错题 / pick 报告 / taevas-plugins 插件),md 里记一行毕业说明。**毕业必须留去向**——门禁强制。
- 放弃 → `dropped`,md 里写一行死因。尸体留着:防的是三个月后又想到同一个点子,从头再兴奋一遍。
- 念头不死、不过期,无时效字段。

## 4. 引擎

渲染器在 `atlas/shared/render.py`(全馆共用),本馆 build 无本地副本。HTML 由 `python3 scripts/build-index.py` 生成,禁止手改;门禁只有三条硬规则:必填字段、status 枚举、毕业必须有真实去向——其余一切从宽。
