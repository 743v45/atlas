# tvly search: Babylon.js 微信小游戏 适配 wechat minigame
- 采集: 2026-09-30, tvly search --json --max-results 8

{
  "query": "Babylon.js 微信小游戏 适配 wechat minigame",
  "follow_up_questions": null,
  "answer": null,
  "images": [],
  "results": [
    {
      "url": "https://jsr.io/@happy-js/minigame-std",
      "title": "@happy-js/minigame-std - JSR",
      "content": "还不能！\n\n一些 DOM Element 相关的适配代码仍需要 Adapter，主要是游戏引擎需要使用。\n\n## 小游戏平台的支持情况\n\n 微信小游戏\n\n  100% 经过测试。\n 其他小游戏\n\n  由于小游戏平台的 API 全部使用 `wx` 全局 namespace 进行调用，其他小游戏平台为了兼容微信小游戏，通常也会设置 `wx` namespace，比如 `GameGlobal.wx = qq`，且 API 会大体保持一致，所以基本也是支持的。\n\n  如发现有差异，请提 issue。\n\n## 代码裁剪\n\n`__MINIGAME_STD_MINA__`\n\n代码打包时通过设置 `__MINIGAME_STD_MINA__` boolean 变量来控制需要裁剪掉 web 平台还是小游戏平台的专属代码，所有平台特有的代码都是 `side effect free` 的，可以放心裁剪。\n\n设置为 `true` 则裁减掉 web 平台的代码，适合发布小游戏时的构建。\n\n设置为 `false` 则裁减掉小游戏平台代码，适合在浏览器上开发阶段或者发布到 web 平台时的构建。 [...] ```\n  import from'minigame-std'// 可插拔日志，支持级别过滤、控制台输出、文件持久化 init level 'debug' plugins fileLog split maxSize 10 1024 1024 info 'App started' error 'Something went wrong' new Error 'test'// 拦截全局 console 方法 init plugins fileLog injectConsole true console info 'Redirected to logger pipeline'// → file 写入 + console 输出// 微信小游戏日志（仅小游戏平台生效） init plugins wxLog level 'warn'\n  ```\n\n更多功能请查看 API 文档。\n\n## 和 Adapter 是什么关系\n\nAdapter 也是为了适配 wx API 和 DOM/BOM API 的差异，相比 Adapter，minigame-std 具有一些显著的优势。 [...] ```\n  import from'minigame-std'// 统一的错误和 Promise rejection 处理\n  ```\n 网络状态监听\n\n  ```\n  import from'minigame-std'\n  ```\n HTTP 请求\n\n  ```\n  import from'minigame-std'// 支持可中断的请求，兼容平台特定参数 const = fetchT abortable true abort// 中断请求\n  ```\n WebSocket\n\n  ```\n  import from'minigame-std' const = connectSocket'wss://example.com'\n  ```\n 本地存储\n\n  ```\n  import from'minigame-std'// localStorage 兼容 API await setItem 'key' 'value' const = await getItem 'key'\n  ```\n WebAudio",
      "score": 0.76279575,
      "raw_content": null,
      "id": "cf6b07-00"
    },
    {
      "url": "https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines",
      "title": "微信小游戏的游戏引擎选择 (2026) | Cinevva",
      "content": "Unity 没有原生的微信导出，但腾讯和 Unity 维护着一个官方工具，把 Unity WebGL 构建转换成小游戏包：微信小游戏转换 SDK，有时以 WeChat MiniGame Exporter 的形式发布。2025 年中的一次更新起，它支持一键导出，配套的 `minigame-adaptor` 声称用微信优化过的渲染路径，性能比纯 WebGL 快约 3 倍。\n\n如果你已经有一个 Unity 游戏，想不重写就搬上微信，这是这条路。但要现实地看待代价。Unity WebGL 构建很大，而 4MB 首包对一个当初不是围绕它设计的引擎来说极其残酷。你会在裁剪、代码拆分、把素材推进分包上花实打实的功夫。它是移植现有游戏的工具，不是优先做微信的工具。\n\n## 团结引擎：Unity 中国的原生答案 ​ [...] ## 相关阅读 ​\n\n 如何在微信与抖音小游戏上发行 —— 版号、审核与分成\n 中国小游戏与 HTML5 平台对比 —— 微信、抖音、QQ、4399 等\n 为中国市场做网页游戏本地化 —— 字体、托管、支付与防火墙\n 2026 年最佳网页游戏引擎（对比） —— 完整阵容\n Three.js 与 Babylon.js 对比 —— 如果你走裸 WebGL 路线\n Cinevva Engine —— 我们基于 Three.js 的开源、网页优先引擎 [...] 如果你喜欢 Unity 的工作流，又想把微信当成真正的构建目标而不是 WebGL 转换，看看团结引擎（Unity 中国的本地化引擎）。它基于 Unity 2022 LTS，把微信小游戏当作和 iOS、Android 并列的原生平台，另外还支持 OpenHarmony、AliOS 等国内目标。近期版本加入了完整的实时全局光照系统（TuanjieGI），下载量已超过 50 万。\n\n对一个立足中国市场、又有 Unity 肌肉记忆的工作室，团结引擎是 Unity 家族里最面向未来的选项，因为微信不是通过 WebGL 后补上的,而是一等的导出目标。\n\n## Three.js 与裸 WebGL ​\n\n你可以通过微信的 `weapp-adapter`（它把库所期望的 DOM 和 canvas 对象打桩补上）在小游戏里跑 Three.js 或手写的 WebGL。这是最灵活、也最费劲的路线：渲染循环、素材管线、分包、每一个适配边角，都由你自己扛。它适合一个小的、定制的、对体积敏感的游戏（完整引擎属于杀鸡用牛刀），或者你的团队本来就活在 Three.js 里、想复用它的代码。",
      "score": 0.31242296,
      "raw_content": null,
      "id": "61ff73-01"
    },
    {
      "url": "https://www.babylonjs.com",
      "title": "Babylon.js: Powerful, Beautiful, Simple, Open - Web-Based 3D At Its Best",
      "content": "A realistic shark resting on a sandy ocean floor with soft environment-based shadows and blue underwater lighting\n\nA pyramid of stacked red cups surrounded by dominoes and colorful building blocks on a patterned rug\n\nA yellow weather buoy with solar panels and instruments bobbing on a choppy blue ocean under a clear sky\n\nBright sunlight streaming through Gothic arched windows of a stone cathedral, casting volumetric light rays\n\n## Welcome to Babylon.js 9.0 [...] [](\n\n BABYLON LITE\n BABYLON NATIVE\n FEATURE DEMOS\n TOOLS\n COMMUNITY\n PARTNERS\n TESTIMONIALS\n INDUSTRIES\n VIEWER\n LEARN\n SPECIFICATIONS\n\n BABYLON NATIVE RUNTIME\n BABYLON REACT NATIVE\n\n PLAYGROUND\n SANDBOX\n NODE MATERIAL EDITOR\n NODE GEOMETRY EDITOR\n SMART FILTER EDITOR\n NODE PARTICLE EDITOR\n NODE RENDER GRAPH EDITOR\n VIEWER CONFIGURATOR\n DOCUMENTATION\n EXPORTERS\n SPECTOR.JS\n\n FORUM\n COMMUNITY DEMOS\n\n GAMES\n ECOMMERCE\n CREATION AND AUTHORING\n DIGITAL TWIN AND IOT\n METAVERSE [...] 3D Room Planner\n\n  by Macy's\n\n   \n Minecraft Classic\n\n  Minecraft Classic\n\n  by Mojang\n\n   \n Temple Run 2\n\n  Temple Run 2\n\n  by Imangi Studios\n\n   \n Xbox Design Lab custom Xbox controller in pride colors\n\n  Xbox Design Lab\n\n  by Microsoft\n\n   \n MillerKnoll Chair Configurator\n\n  Chair Configurator\n\n  by MillerKnoll\n\n   \n Volkswagen ID. Buzz Configurator\n\n  Volkswagen ID. Buzz Configurator\n\n  by Wrapmate\n\n   \n Stanley cup in a customizer window allowing for custom graphics and colors",
      "score": 0.2693717,
      "raw_content": null,
      "id": "c09495-02"
    },
    {
      "url": "https://intl.cloud.tencent.com/zh/document/product/1219/78928",
      "title": "Unity WebGL 小游戏适配",
      "content": "### ﻿ 工具转换 ﻿\n\n我们提供了 Unity 转换插件帮助开发者将项目自动导出为小游戏包，随后即可使用 TCSAS 开发者工具或 Android/iOS 真机进行预览。\n\n以下为转换流程：\n\n﻿\n\n﻿\n\n### ﻿ ﻿\n\n微信小游戏平台提供众多开放能力，但目前是以 JavaScript API 形式提供。为降低开发者对接平台能力的门槛，我们提供了平台能力 C# SDK，开发者可通过熟悉的 C# 接口完成平台能力调用，相关文档请参阅 WX\\_SDK。\n\n﻿\n\n﻿\n\n上一篇: Cocos/Laya/Egert 引擎适配下一篇: 运行环境\n\n## 帮助和支持\n\n您也可以 联系销售 或 提交工单 以寻求帮助。 [...] + App 服务端接入指南\n  + GUID 生成规则\n 小程序开发指南\n  + 小程序介绍与开发环境\n\n  + 框架\n  + 组件\n  + API\n  + 服务端\n  + JS SDK\n  + 基础库\n  + IDE 使用指南\n 小游戏开发指南\n  + 指南\n  + API\n  + 服务端\n 实践教程\n  + 小程序登录实践教程\n  + 小程序订阅消息实践教程\n  + 支付相关实践教程\n  + 广告接入实践教程\n  + 小游戏订阅消息实践教程\n API 文档\n  + 更新历史\n  + 简介\n  + API 概览\n  + 调用方式\n  + 应用相关接口\n  + 小程序相关接口\n  + 小游戏相关接口\n  + 敏感API相关接口\n  + 管理-敏感API相关接口\n  + 平台管理相关接口\n  + 控制台公共部分相关接口\n  + 团队管理相关接口\n  + 全局域名管理相关接口\n  + 用户管理相关接口\n  + 角色管理相关接口\n  + 运营管理相关接口\n  + 数据结构\n  + 错误码\n 相关协议\n  + 数据处理和安全协议 [...] # tencent cloud\n\n 最新优惠;)\n 产品;)\n 解决方案;)\n 价格中心;)\n 合作伙伴网络;)\n 云市场;)\n 探索更多;)\n\nPrev;)Next;)\n\n 动态与公告\n  + 【2025年1月2日】关于腾讯云小程序平台更名为腾讯云超级应用服务的公告\n  + 控制台更新动态\n  + Android SDK 更新动态\n  + iOS SDK 更新动态\n  + Flutter 更新动态\n  + IDE 更新动态\n  + 基础库更新动态\n 产品简介\n  + 产品概述\n  + 产品优势\n  + 应用场景\n 购买指南\n  + 计费概述\n  + 按量计费（后付费）\n  + 续费指引\n  + 停服说明\n 快速入门\n 套餐管理\n  + 概述\n  + 控制台账号管理\n  + 存储配置\n  + 加速配置\n 平台功能\n  + 控制台登录\n  + 用户和权限体系\n  + 小程序管理\n  + 小游戏管理\n\n  + 平台管理\n  + 用户管理\n  + 团队管理\n 代码接入指引\n  + Demo 及 SDK 获取",
      "score": 0.20131063,
      "raw_content": null,
      "id": "dbae82-03"
    },
    {
      "url": "https://developers.weixin.qq.com/minigame/dev/guide/runtime/js-support.html",
      "title": "JavaScript 支持情况 | 微信开放文档",
      "content": "小游戏\n\n 小程序\n 小游戏\n 公众号\n 服务号\n 开放平台\n 企业微信\n 微信支付\n 视频号\n 微信小店\n 智能对话\n 腾讯小微\n 教育平台\n\n在游戏下暂无结果，查看其它业务相关内容 >\n\n + 云开发\n  + 云托管\n\n开发\n\nEN\n\n取消\n\n- 指南\n\n# # JavaScript 支持情况\n\n## # 运行限制\n\n基于安全考虑，小程序中不支持动态执行 JS 代码，即：\n\n 不支持使用 `eval` 执行 JS 代码\n 不支持使用 `new Function` 创建函数\n\n## # 标准 ECMAScript 支持\n\n小程序的 JS 执行环境 在不同平台上的执行环境存在差异，因此导致不同平台对 ECMAScript 标准的支持存在差异。\n\n小程序基础库为了尽量抹平这些差异，内置了一份 `core-js` Polyfill。`core-js` 可以将平台环境缺失的标准 API 补齐。\n\n需要注意的是，平台对 ECMAScript 语法的支持差异无法抹平，当你需要使用一些高级语法时，如 `async/await` 时，则需要借助 代码转换工具 来支持这些语法。 [...] 从而，当指定特定小程序基础库版本时（可以在 小程序管理页 【设置】-【基本设置】-【基础库最低版本设置】中设置），我们能够得到最低需要支持的执行环境。\n\n具体数据可以从 这个开源库 中获得。\n\n也可以查看支持度列表\n\nThe translations are provided by WeChat Translation and are for reference only. In case of any inconsistency and discrepancy between the Chinese version and the English version, the Chinese version shall prevail.Incorrect translation. Tap to report. [...] iOS 16 及以上不存在差异。\n\n```\nvar =[] setTimeout(() =>. push(6), 0). push(1) const = new Promise(resolve =>{. push(2) resolve()}). push(3). then(() =>. push(5)). push(4) setTimeout(() =>. push(7), 0) setTimeout(() =>{// 应该输出 [1,2,3,4,5,6,7]// 在 iOS15 小程序环境，这里会输出 [1,2,3,4,6,5,7]. log()}, 1000)\n```\n\n关于普通任务和微任务的区别可以查看这篇文章\n\n## # 如何判断当前环境需要哪些 Polyfill & 代码转换目标\n\n特定的小程序基础库版本有最低微信客户端版本要求，如基础库 v2.15.0 要求安卓最低版本 7.0.22，iOS 最低版本 7.0.20。\n\n而特定的客户端版本有最低操作系统版本要求，如 iOS 7.0.20 要求最低 iOS 10。",
      "score": 0.17042546,
      "raw_content": null,
      "id": "c21646-04"
    },
    {
      "url": "https://cn.investing.com/analysis/article-200485325",
      "title": "微信算是碰上硬茬了 | Investing.com",
      "content": "对此，微信小游戏团队负责人李卿解释，“假设小游戏和 APP 是纯粹的竞争关系，走不远，因为 APP 已经是一个成规模的市场。很早之前，我们就意识到小游戏是游戏行业的一个增量，或者说跟 APP 市场是相对平行的状态。”\n\n值得一提的是，不乏行业研究人士向虎嗅表示，本轮小游戏爆发的契机主要源于技术突破，尤其是 Unity 适配使手游开发，可无缝衔接小游戏。对此，紫辰乐游高菲（代表产品《贪吃蛇无尽大作战》）坦言，“三四年前超休闲火的时候，Unity 不支持在微信小游戏呈现，近两年微信平台能力（支持 Unity）突破后，产品供给开始急速攀升。”\n\n这一判断与微信团队的分享不谋而合，李卿认为 2023 年微信小游戏的重要突破就是 Unity 适配和 1G 包体基建的放开。\n\n“首先，微信能力发布，到开发者转化生产力进来，中间有个过程，比如代码包从 20-30M 放开，iOS 下高适配、高清、高性能模式，解决了基本的卡顿问题；其次，《羊了个羊》让用户有了‘微信里还有游戏’的心智，在微信上找游戏变成一个用户层的循环。”李卿说道。\n\n抖音微信到底在争什么？ [...] 如此陡峭的增速，得益于小游戏能转化平台游戏用户及（接触游戏不多的）潜在游戏用户，撑起足够大的用户盘。\n\n以微信公开课-小游戏专场数据为例：2024Q1 微信小游戏 DAU 同比上涨 20%，IAA 小游戏 MAU 达 5 亿，开发者人数累计超过 40 万人——即便小游戏赛道的数据攀升曲线惊人，但同期微信用户数超过 13 亿、小程序 MAU 也超过 11 亿，后续小游戏还有巨大的成长空间。\n\n这背后，很大原因在于 IAA 小游戏不受系统/平台制约，更适配跨平台布局的轻量化产品落地（门槛更低、风险更可控）——当前 APP 游戏动辄几个 G 的安装包，且普遍有首次登陆加载包；而小游戏即点即玩、不用下载，易上手、适配更多场景。\n\n其次，从整个产业角度来看，之前小游戏主要聚焦休闲品类，近两年开始向多元化迭代，胜在项目周期短、投入轻量化——以《就我眼神好》为例，目前其全平台用户已超 1.5 亿，制作团队一克科技 CEO 陆振棠分享，该项目 6 月立项、7 月上线、8 月盈利、12 月流水破千万，充分印证 IAA 小游戏制作周期短，回本快的特点。 [...] 某企业高管向虎嗅表示，字节跳动这家年轻巨头站在舞台中央太久，凭一己之力在 BAT 丛林趟出一套流量体系。“过去‘大力出奇迹’的打法在资讯、短视频赛道撼动过 BAT；此后，字节跳动娴熟利用流量倒灌使新业务快速起量，在“快速拓展业务、快速投入资源试错、快速调整”的策略下攻城略地——它的目的是将商业体中的人、团队无限颗粒化，而它则变成‘神’。”\n\n一块“肥肉”，两个“饿汉”\n\n之所以将小游戏称作“肥肉”，源于两方面：\n\n一是，移动端游戏仍处于潜力释放阶段，而小游戏是一个正在爆发的巨大增量内容场景。\n\n  \n  \n数据来源：游戏工委、《2023 年中国游戏产业报告》\n\n以移动 APP 与小游戏增速作为参照切面：游戏工委发布的《2023 年中国游戏产业报告》显示，2023 年国内游戏市场实际销售收入突破 3000 亿元大关。\n\n其中，移动游戏市场实际销售收入达到 2268.6 亿元，同比增长 17.51%；小程序游戏市场实际收入飙升 300% 达到 200 亿元。\n\n  \n  \n数据来源：游戏工委、《2023 年中国游戏产业报告》",
      "score": 0.16004303,
      "raw_content": null,
      "id": "1aa7be-05"
    },
    {
      "url": "https://cn.investing.com/news/stock-market-news/article-3137212",
      "title": "华源证券：小游戏向精品化转型 建议把握生态的成熟放量",
      "content": "Title: 华源证券：小游戏向精品化转型 建议把握生态的成熟放量 提供者 智通财经\n#### 热门搜索. ##### 请尝试其他搜索. *   智通港股早知道 | 住建部指房地产进入存量时代 MiniMax(00100) Code CLI正式开源. *   纳指100再平衡周一美股开盘前生效 SpaceX(SPCX.US)权重大幅升至2.82%. *   Vanguard Total Stock Mkt Idx Instl Sel. *   PIMCO Commodity Real Ret Strat C. *   Vanguard Total Bond Market Index Adm. *   SG FTSE MIB Gross TR 5x Daily Short Strategy RT 18. *   Vontobel 7X Long Fixed Lever on Natural Gas 8.06. *   BNP Call 500.59 EUR AEX 31Dec99. *   COMMERZBANK AG Put CAC FUT 05/17 31Dec99. # 华源证券：小游戏向精品化转型 建议把握生态的成熟放量. 智通财经APP获悉，华源证券发布研报称，小游戏从碎片消遣到中重度化及精品化的转型。据伽马数据，2024年中国小游戏市场总收入达398.36亿元，同比增长99.18%。据DataEye，预计2025年中国小游戏市场总收入将超过600亿元。小游戏逐步实现了从碎片化消遣到中重度化及精品化的成长。日益繁荣的内容生态是游戏市场难得的增量空间。当前时点，该行建议把握生态的成熟放量。. 《飞机大战》是早期的微信小游戏，此时手机开始普及，微信生态开始带动轻量级游戏的兴起。2022年，微信小游戏创意鼓励计划升级，商业化提效，大量优质小游戏出现，产品向精品化发展。2024年4月，点点互动旗下的SLG小游戏《无尽冬日》超越《寻道大千》，登顶微信小游戏畅销榜第一。据伽马数据，2024年中国小游戏市场总收入达398.36亿元，同比增长99.18%。据DataEye，预计2025年中国小游戏市场总收入将超过600亿元。. 1)平台端/用户端：微信+小程序的流量红利。微信小程序作为微信流量重要的载体，2024年10月用户规模同比增长3%已达9.49亿，月活用户规模同比增量达到2784万。QuestMobile数据显示，2022至2024年的10月数据来看，微信小游戏连续成为抢占用户时长占比最高的应用类型。2024年10月，微信小游戏月活用户规模达到5.55亿，同比增长5.9%。2)渠道/变现模式：更灵活、更优质。微信已经推出一系列激励政策，微信小游戏在不同阶段可享不同额外激励，到手的收益预估在50%至100%以上不等。3)研发端：更快的周期和周转。目前厂商针对分端原生制作与H5版本兼容制作均有成熟的技术能力支持开发。即使是原生制作的小游戏，研发周期与成本至少能降低至手游APP的50%。此外，Unity为微信小游戏做了特殊的支持与优化，微信推出Unity WebGL小游戏适配(转换)方案，以降低Unity游戏转换到微信小游戏的开发成本。. 1)中重度化趋势有望强化用户粘性和ARPU。小游戏未来可能形成轻度化玩法为入口、重度化内容做留存的融合趋势。所谓“轻度化玩法”，是为了降低用户尝试门槛，所谓“重度化内容”，是通过养成体系等深度设计提升用户粘性。2)混合变现趋势或将加强。腾讯广告数据显示，2023年混变小游戏产品数和广告消耗增速超100%，2024年同比增速继续保持100%，IAP小游戏买量消耗中60%是混变小游戏。混变小游戏是2023年、2024年买量趋势中增速最快的赛道。3)小游戏出海是新的游戏输出形式。小游戏出海以低成本、短周期开发的轻度游戏为核心，聚焦H5游戏、小程序游戏等形式，用户获取依赖于流量平台，出海模式细分为H5游戏出海、小程序游戏出海及双端发行。小游戏海外生态逐步扩大，YouTube、TikTok、Discord等海外社交头部平台纷纷加速布局小游戏赛道，并逐步开启内购变现功能。. ## 最新评论. 阿克曼“换仓”AI巨头：清仓Alphabet(GOOGL.US)、加仓Meta(META.US)，投资者该跟吗? 《富爸爸穷爸爸》作者再发“崩盘”警告：AI、战争、债务加剧了担忧. | 中际旭创 | 944.48 | +1.95% | 1,340.21万 |  |. | CXMT | 56.87 | +2.40% | 1.70亿 |  |. | 中国巨石 | 45.78 | +1.69% | 1.95亿 |  |. | 亨通光电 | 72.61 | +4.49% | 1.16亿 |  |. | 兆易创新 | 393.00 | +1.24% | 2,119.20万 |  |. | 宁德时代 | 299.20 | -0.91% | 2,469.63万 |  |. | 68.60 | +23.38% | 2,266.77万 |  |. | 诺禾致源 | 18.18 | +20.00% | 1,697.99万 |  |. | 宏昌科技 | 54.25 | +20.00% | 1,508.19万 |  |. | 透景生命 | 20.35 | +19.99% | 3,297.01万 |  |. | \"ShenGu Co.\" | 45.91 | -20.53% | 7,857.73万 |  |. | 利扬芯片 | 36.66 | -12.07% | 2,480.54万 |  |. | 康芝药业 | 5.65 | -9.89% | 4,519.85万 |  |. | 德利股份 | 77.29 | -10.00% | 434.40万 |  |. | 禾信仪器 | 117.77 | -9.57% | 139.41万 |  |. | 英飞拓 | 5.86 | -9.29% | 3,499.54万 |  |. | 鲁抗医药 | 7.80 | +2.90% | 1,812.88万 |  |. | 海光信息 | 241.74 | +0.15% | 1,120.71万 |  |. | Malayan Banking | 10.42 | +0.97% | 174.24万 |  |. | 极兔速递-W | 8.96 | -0.17% | 659.81万 |  |. | AirAsia X | 0.535 | +0.94% | 3,740.13万 |  |. AI实力助阵，我们的 **优选股票**一路领跑，轻松**超越标普500**. 实时行情 问问WarrenAI AI精选股 自选组合 提醒 财经要闻 工具. 风险批露: 交易股票、外汇、商品、期货、债券、基金等金融工具或加密货币属高风险行为，这些风险包括损失您的部分或全部投资金额，所以交易并非适合所有投资者。加密货币价格极易波动，可能受金融、监管或政治事件等外部因素的影响。保证金交易会放大金融风险。. 在决定交易任何金融工具或加密货币前，您应当充分了解与金融市场交易相关的风险和成本，并谨慎考虑您的投资目标、经验水平以及风险偏好，必要时应当寻求专业意见。. **Fusion Media**提醒您，本网站所含数据未必实时、准确。本网站的数据和价格未必由市场或交易所提供，而可能由做市商提供，所以价格可能并不准确且可能与实际市场价格行情存在差异。即该价格仅为指示性价格，反映行情走势，不宜为交易目的使用。对于您因交易行为或依赖本网站所含信息所导致的任何损失，**Fusion Media**及本网站所含数据的提供商不承担责任。. 未经**Fusion Media**及/或数据提供商书面许可，禁止使用、存储、复制、展现、修改、传播或分发本网站所含数据。提供本网站所含数据的供应商及交易所保留其所有知识产权。. 本网站的广告客户可能会根据您与广告或广告主的互动情况，向**Fusion Media**支付费用。. © 2007-2026 -Fusion Media Limited | 粤ICP备17131071号 | 保留所有权利。.",
      "score": 0.14585622,
      "raw_content": null,
      "id": "10c443-06"
    },
    {
      "url": "https://developers.weixin.qq.com/minigame/dev/guide",
      "title": "开发指南 | 微信开放文档",
      "content": "小游戏\n\n 小程序\n 小游戏\n 公众号\n 服务号\n 开放平台\n 企业微信\n 微信支付\n 视频号\n 微信小店\n 智能对话\n 腾讯小微\n 教育平台\n\n在游戏下暂无结果，查看其它业务相关内容 >\n\n + 云开发\n  + 云托管\n\n开发\n\n取消\n\n- 指南\n\n# # 开发指南\n\n## # 小游戏介绍\n\n微信小游戏是小程序其中的一个类目，是一种基于微信平台开发，不需要下载安装即可使用的全新游戏应用，体现了“用完即走”的理念，充分节省用户的手机空间。 小游戏无论是开发以及使用都相当轻便快捷，同时基于微信的社交属性，让小游戏具备较强的社交传播力，用户可以和朋友一起享受游戏的乐趣。 期待您的加入一起构建小游戏的生态。\n\n## # 小游戏开发指引\n\n 如果你刚接触小游戏的开发，你可以先查看学习新手教程了解一些基础知识。\n 如果你已经熟悉小游戏，可以查看学习进阶指南了解更多内容。\n 如果你开发的小游戏准备发布上线，或者确定将来是要发布上线的，建议提前查看小游戏接入指引，相关资料的审核需要一定的时间，建议让游戏开发和审核相关的流程同时进行。\n\n## # 小游戏能力地图 [...] ## # 小游戏能力地图\n\n下列可能是你在开发小游戏过程中较为常用的能力，完整的能力列表可以查阅左侧目录\n\n#### 用户信息\n\n用户登录态 用户信息获取 用户隐私保护\n\n展示头像昵称等个性化信息\n\n#### 好友关系\n\n关系链数据 开放数据域基础能力 排行榜\n\n展示微信好友关系和排行榜\n\n#### 转发分享\n\n转发 分享海报 分享到朋友圈\n\n转发分享游戏，提升游戏曝光\n\n#### 游戏基础能力\n\n交互 音频 视频\n\n游戏基础能力，与用户交互并响应反馈\n\n#### 连接服务端\n\n网络 服务端API 云托管 云开发\n\n连接服务端，记录用户游戏数据和游戏进度\n\n#### 商业化\n\n虚拟支付 广告变现\n\n#### 缓存\n\n文件系统 本地缓存\n\n#### PC适配\n\nPC接入指南 PC大屏适配指南\n\n#### 测试\n\n云测试\n\n#### 性能\n\n性能优化概述 启动性能优化 运行性能优化\n\n#### 运营\n\n游戏圈 游戏礼包 社交组件 订阅消息\n\n#### 安全\n\n#### 数据与监控\n\n小游戏数据助手 研发工具箱 线上异常问题排查 [...] The translations are provided by WeChat Translation and are for reference only. In case of any inconsistency and discrepancy between the Chinese version and the English version, the Chinese version shall prevail.Incorrect translation. Tap to report.",
      "score": 0.13710469,
      "raw_content": null,
      "id": "261cc1-07"
    }
  ],
  "response_time": 2.1,
  "request_id": "a5ae30c6-c7fe-4210-b54d-f5ae7335b963"
}
