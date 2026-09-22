# UI 风格搜索平台 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 7 节）。

## 根问题

找 UI 风格灵感与真实产品参考时，用什么平台检索？（2026-09-22 会话；用户画像：真实实现与风格风向双场景，口碑为一等核查维度）

## 分叉与决策

### D1 要「真实实现」还是「风格风向」？

- 本类别第一分叉：AI slop 时代，「真实产品截图」与「概念稿/生成图」的污染线决定平台资格（Dribbble/Pinterest 双双因此出局）[1][2]。
- 叶：[Mobbin](mobbin/) adopt（真实库付费天花板：500k+ 屏三端 + flow 组织 + Figma/MCP；Trustpilot 差评集中于免费墙而非产品力）
- 叶：[Refero](refero/) trial（section/tag/文本级搜索独门；Free 仅 3% 库存、Android 覆盖待验证）
- 叶：[Nicelydone](nicelydone/) trial（SaaS 垂直 199k+ 屏；独立口碑样本待沉淀）
- 叶：[Page Flows](pageflows/) trial（录屏流程形态独占，「怎么流」是截图补不了的；定价待核实）

### D2 风格风向找法：策展浏览还是结构化检索？

- 画廊系的分工：品味日更（Godly）、竞赛风向（Awwwards）、按风格关键词精确检索（SiteInspire）三者互斥不可替代。
- 叶：[Godly](godly/) adopt（品味策展天花板 + 免费无墙；口碑一致偏好）
- 叶：[Awwwards](awwwards/) trial（风向标地位保底；「compilation of bad practices」可用性争议 + 提交费压住 adopt）
- 叶：[SiteInspire](siteinspire/) assess（三轴筛选仍最强；更新节奏与声量待验证）
- 叶：[Land-book](land-book/) trial（落地页策展质第一梯队）
- 叶：[Lapa Ninja](lapa-ninja/) trial（落地页量大免费路线默认项；策展密度稀释）
- 叶：[SaaS Landing Page](saas-landing-page/) assess（tech stack/字体筛选独一份；样本与活跃度待验证）

### D3 灵感采集与检索：人策还是 AI 搜？

- moodboard 三价态：AI 语义检索（Cosmos）、设计师收藏夹（Savee）、研究链（Are.na），同价位带（$7-8/月）分工不同。
- 叶：[Cosmos](cosmos/) trial（色板/风格/以图搜图独一档；astroturfing 指控 → 好评打折采信）
- 叶：[Savee](savee/) trial（瀑布流体验最舒服的设计师收藏夹；免费 200 saves 闸）
- 叶：[Are.na](arena/) assess（research trails 研究型定位独特；UI 检索效率不足以下结论）

### D4 要不要「案例叙事」与「垂直轴」？

- 库型平台只给「屏」，案例过程与排版轴需要专门入口。
- 叶：[Behance](behance/) trial（免费完整 case study，社区型唯一保住参考价值者）
- 叶：[Typewolf](typewolf/) trial（排版轴速查标准器；与 Fonts In Use 组合覆盖）
- 叶：[站酷 ZCOOL](zcool/) assess（国内可访问性独一份；参考库形态不匹配）

### D5 反选记录（明确出局）

- 叶：[Pinterest](pinterest/) hold（AI slop 重灾区 + 官方治理失效，r/Pinterest 2025-26 密集口碑）
- 叶：[Dribbble](dribbble/) hold（概念稿化 + AI slop，「真实参考」资格取消，社区降级其为审美板）

## 落选节点（不立条目的死分支）

- **Httpster**：复古/朋克风格垂直画廊（3,116 站，2026-09 活跃）——风格面过窄，Godly/SiteInspire 可覆盖其大部分场景；做亚文化风格专项时再启用。
- **Dark Mode Design**：暗色站垂直策展（2026-09 活跃）——同上，垂直过窄不立目。
- **One Page Love**：单页站垂直第一——单页场景出现频率不足以立目，落地页需求由 Land-book/Lapa 承接。
- **Best Website Gallery（BWG）**：David Hellmann 个人策展（2008 至今）——与 Godly 定位重叠，策展人单一构成单点风险。
- **Scrnshts（scrnshts.club）/ appshot.gallery / appshots.design**：App Store 截图垂直（ASO 向）——与 UI 风格检索主场景错位，ASO 专项时再看。
- **UI Sources / Screenlane / Collect UI / UI Movement**：组件级画廊——被 Mobbin 系库型平台的结构化组件/流程视图覆盖，无独占场景。
- **pttrns**：前移动 UI pattern 库——已衰落，主流名单不再收录（cbinsights 直接以 Mobbin 为其替代品）；作为「本类别死亡率」样本留档。
- **Muzli**：聚合 feed + 新标签页（12 年仍在运营）——定位是「资讯聚合」非检索库，与「搜索」命题错位；存在感下降。
- **Gummble / Watobu / InspoAI / ScreensDesign / Refframe**（2026 新玩家）：全部只出现在自家对比软文与 SEO 盘点文（「7 Best Mobbin Alternatives」型），**无独立社区口碑，利益相关降权不收录**；沉淀出真实用户口碑后重审。
- **shadcn 主题库 / tweakcn / shadcnblocks**：组件主题生成与模板市场——「UI 风格的代码实现」是另一物种（工程侧），不属本类别检索命题。
- **UI 中国 / 优设 UISDC / DOOOOR**：国内同类——优设偏文章教程、UI 中国样本声量弱，站酷已代表国内可访问路线。
- **CSS Design Awards**：第二梯队竞赛画廊（提交 $25–60）——与 Awwwards 同模式无差异优势，Awwwards 已代表竞赛路线。

## 观察名单（下次复核触发器）

- Mobbin：「Did Mobbin get worse」社区讨论是否实质化 → 影响 adopt。
- Cosmos：astroturfing 指控是否实锤 → 实锤则 trial 降 assess。
- Refero：Android 覆盖一手核实 → 覆盖补全则与 Mobbin 升级为双 adopt 候选。
- Page Flows / Nicelydone：一手定价与免费层限制核实（本轮均标待验证）。
- Savee / Are.na：免费额度政策变动（200 saves 闸是否收紧）。
