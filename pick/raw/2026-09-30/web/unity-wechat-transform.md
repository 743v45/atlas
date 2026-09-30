# tvly search: Unity 微信小游戏 转换 现状 2026
- 采集: 2026-09-30, tvly search --json --max-results 8

{
  "query": "Unity 微信小游戏 转换 现状 2026",
  "follow_up_questions": null,
  "answer": null,
  "images": [],
  "results": [
    {
      "url": "https://app.cinevva.com/zh-CN/guides/wechat-mini-game-engines",
      "title": "微信小游戏的游戏引擎选择 (2026) | Cinevva",
      "content": "Unity 没有原生的微信导出，但腾讯和 Unity 维护着一个官方工具，把 Unity WebGL 构建转换成小游戏包：微信小游戏转换 SDK，有时以 WeChat MiniGame Exporter 的形式发布。2025 年中的一次更新起，它支持一键导出，配套的 `minigame-adaptor` 声称用微信优化过的渲染路径，性能比纯 WebGL 快约 3 倍。\n\n如果你已经有一个 Unity 游戏，想不重写就搬上微信，这是这条路。但要现实地看待代价。Unity WebGL 构建很大，而 4MB 首包对一个当初不是围绕它设计的引擎来说极其残酷。你会在裁剪、代码拆分、把素材推进分包上花实打实的功夫。它是移植现有游戏的工具，不是优先做微信的工具。\n\n## 团结引擎：Unity 中国的原生答案 ​ [...] 如果你喜欢 Unity 的工作流，又想把微信当成真正的构建目标而不是 WebGL 转换，看看团结引擎（Unity 中国的本地化引擎）。它基于 Unity 2022 LTS，把微信小游戏当作和 iOS、Android 并列的原生平台，另外还支持 OpenHarmony、AliOS 等国内目标。近期版本加入了完整的实时全局光照系统（TuanjieGI），下载量已超过 50 万。\n\n对一个立足中国市场、又有 Unity 肌肉记忆的工作室，团结引擎是 Unity 家族里最面向未来的选项，因为微信不是通过 WebGL 后补上的,而是一等的导出目标。\n\n## Three.js 与裸 WebGL ​\n\n你可以通过微信的 `weapp-adapter`（它把库所期望的 DOM 和 canvas 对象打桩补上）在小游戏里跑 Three.js 或手写的 WebGL。这是最灵活、也最费劲的路线：渲染循环、素材管线、分包、每一个适配边角，都由你自己扛。它适合一个小的、定制的、对体积敏感的游戏（完整引擎属于杀鸡用牛刀），或者你的团队本来就活在 Three.js 里、想复用它的代码。 [...] ## LayaAir：强力替代 ​\n\nLayaAir（来自 Laya）是另一个早早适配微信、并把它当一等目标的引擎。你在构建面板里选微信小游戏就能发布。它支持 2D 和 3D，用 TypeScript，有一批更喜欢它工作流的忠实开发者。同时用过两者的人，往往把选择描述成口味问题，而不是能力问题。\n\n要权衡的一点：LayaAir 的引擎运行时不像 Cocos 那样烘焙进微信客户端，所以引擎本身要多占你的包体预算。对小的 2D 游戏通常没问题。对素材繁重、4MB 里每一 KB 都要抠的 3D 游戏，Cocos 的内置插件可能就是决定性因素。\n\n## 白鹭 Egret：老将，慎用 ​\n\nEgret（白鹭）是一个更老的 2D HTML5 引擎，很早支持微信小游戏，撑起了第一波里很多作品。它现在还能用，但势头已经转向 Cocos 和 Laya，社区活跃度变薄，2026 年在它上面开新项目，就是押注一个正在收缩的生态。如果你在维护现有的 Egret 游戏，没问题。如果从零开始，选 Cocos 或 Laya。\n\n## Unity：WebGL 转换路线 ​",
      "score": 0.8464638,
      "raw_content": null,
      "id": "037575-00"
    },
    {
      "url": "https://intl.cloud.tencent.com/zh/document/product/1219/78928",
      "title": "Unity WebGL 小游戏适配",
      "content": "文档腾讯云超级应用服务小游戏开发指南指南游戏引擎Unity WebGL 小游戏适配\n\n# Unity WebGL 小游戏适配\n\n下载\n\n聚焦模式\n\n字号\n\n最后更新时间： 2026-04-20 16:57:39\n\n## 概述\n\n欢迎使用 Unity WebGL 小游戏适配(转换)方案，本方案基于 WebAssembly 技术，旨在大幅降低 Unity 项目迁移至小游戏平台的成本。您无需更换引擎或重写核心逻辑，即可完成适配。由于 TCSAS 小游戏环境同样基于 WebAssembly 与 wx API 构建，该方案可直接复用微信官方适配路径，核心技术栈完全兼容。\n\n您可获取详细的 Unity WebGL 微信小游戏适配方案。\n\n## 方案特点\n\n保持原引擎工具链与技术栈。\n\n无需重写游戏核心逻辑，支持大部分第三方插件。\n\n由转换工具与小游戏运行环境保证适配兼容，保持较高还原度。\n\n小游戏平台能力以 C# SDK 方式提供给开发者，快速对接平台开放能力。\n\n## 技术原理 [...] ### ﻿ 工具转换 ﻿\n\n我们提供了 Unity 转换插件帮助开发者将项目自动导出为小游戏包，随后即可使用 TCSAS 开发者工具或 Android/iOS 真机进行预览。\n\n以下为转换流程：\n\n﻿\n\n﻿\n\n### ﻿ ﻿\n\n微信小游戏平台提供众多开放能力，但目前是以 JavaScript API 形式提供。为降低开发者对接平台能力的门槛，我们提供了平台能力 C# SDK，开发者可通过熟悉的 C# 接口完成平台能力调用，相关文档请参阅 WX\\_SDK。\n\n﻿\n\n﻿\n\n上一篇: Cocos/Laya/Egert 引擎适配下一篇: 运行环境\n\n## 帮助和支持\n\n您也可以 联系销售 或 提交工单 以寻求帮助。 [...] # tencent cloud\n\n 最新优惠;)\n 产品;)\n 解决方案;)\n 价格中心;)\n 合作伙伴网络;)\n 云市场;)\n 探索更多;)\n\nPrev;)Next;)\n\n 动态与公告\n  + 【2025年1月2日】关于腾讯云小程序平台更名为腾讯云超级应用服务的公告\n  + 控制台更新动态\n  + Android SDK 更新动态\n  + iOS SDK 更新动态\n  + Flutter 更新动态\n  + IDE 更新动态\n  + 基础库更新动态\n 产品简介\n  + 产品概述\n  + 产品优势\n  + 应用场景\n 购买指南\n  + 计费概述\n  + 按量计费（后付费）\n  + 续费指引\n  + 停服说明\n 快速入门\n 套餐管理\n  + 概述\n  + 控制台账号管理\n  + 存储配置\n  + 加速配置\n 平台功能\n  + 控制台登录\n  + 用户和权限体系\n  + 小程序管理\n  + 小游戏管理\n\n  + 平台管理\n  + 用户管理\n  + 团队管理\n 代码接入指引\n  + Demo 及 SDK 获取",
      "score": 0.7913865,
      "raw_content": null,
      "id": "c8bb94-01"
    },
    {
      "url": "https://www.bilibili.com/video/BV1XcWjeSEhE",
      "title": "如何将Unity游戏转换为微信小游戏/网页小游戏（WebGL打包流程分享和坑点总结）_哔哩哔哩_bilibili",
      "content": "林沐牧\n\n4.2万 44\n\nunity教程零基础全套2026最新合集（unity3D游戏教程+unity2D游戏教程）unity游戏开发教程，unity小游戏制作教程，unity做游戏教程\n\nunity教程\n\n29万 858\n\nJavaScript开发微信小游戏【已完结】\n\n野生程序君-Paul\n\n10万 167\n\nunity教程零基础全套2026最新合集（unity游戏开发教程+unity3D游戏教程+unity2D游戏教程）unity小游戏制作教程，unity做游戏教程\n\nunity教程零基础\n\n28.1万 911\n\n2026最新Cocos Creator 3.8.6游戏开发新手入门实战教程\n\n大发程序员\n\n77.8万 1356\n\n【Godot】支持微信/抖音小游戏导出啦\n\n无所不能的咲夜\n\n1.8万 1\n\n个人制作微信小游戏一年的总结分享\n\nD2ryy\n\n4.6万 19\n\n3453 1\n\n是神奇海螺ya\n\n1.2万 1\n\n9547 3\n\n2.3万 12\n\n3.3万 6\n\n赛事库 课堂 2021拜年纪 [...] 11:35\n\n【Unity微信小游戏开发】1.开发到上架流程\n\nJoker\\_游戏开发\n\n3.7万 2\n\n【全是干货】如何在Unity WEB平台做好虚拟展馆 同济大学案例分析 拒绝渣画质 小意思VR\n\n小意思VR\n\n13.8万 95\n\n大概是全网最详细微信小游戏上架流程\n\n是神奇海螺ya\n\n2.9万 48\n\n用Godot——给朋友制作的生日小游戏\n\n一根韭菜苔\n\n7.2万 15\n\n零基础、零编程，轻松学会微信小游戏制作【持续更新中——第20集】\n\n野生程序君-Paul\n\n35.6万 1259\n\n别再把团结引擎当Unity了！Unity6正确下载安装教程\n\n嗜睡的猫咪\n\n14.5万 143\n\n2026零基础开发抖音小游戏和开发微信小游戏教程-Cocos Creator 3.8.8教程\n\n三虫科技\n\n9.4万 156\n\n【unity/2d/超基础】教你做一款2d横版游戏\n\n秋梦汐\n\n37.8万 1310\n\nunity新手入门教程：Unity制作微信小游戏并发布-益智冒险的游戏制作\n\n林沐牧\n\n4.2万 44 [...] 番剧\n 直播\n 游戏中心\n 会员购\n 漫画\n 赛事\n\n2024-08-24 12:00:00\n\n暂无课程总结\n\n文字版： 1. 2. 3.\n\n发现《Reality》\n\n游戏开发\n\n小游戏\n\n教程\n\nUnity\n\n微信\n\n微信小游戏\n\nWebGL\n\n打工人小棋   发消息\n\n（不接广告哦，停更学习中）游戏研发攻城狮，游戏区Bug主，引擎只是载体，思路才是关键。\n\n关注 2.7万\n\nUnity百宝箱\n\n（27/28）\n\n148.4万播放\n\n简介\n\n订阅合集\n\nUnity基础\n\n技术精华\n\n背包系统\n\nUnity基础\n\n技术精华\n\n背包系统\n\nP0. 课程介绍\n\n02:43\n\nP1. 背包界面拼接\n\n17:31\n\nP2. 存储框架\n\n12:29\n\nP3. 界面逻辑\n\n13:25\n\nP4. 物品交互和物品详情\n\n15:01\n\nP5. 抽卡和删除物品\n\n17:13\n\n如何将Unity游戏转换为微信小游戏/网页小游戏（WebGL打包流程分享和坑点总结）\n\n17:03\n\n游戏中的【红点系统】是如何实现的？技术原理分析 | uinity案例分享\n\n11:35",
      "score": 0.72184175,
      "raw_content": null,
      "id": "6338d6-02"
    },
    {
      "url": "https://unity.com/cn/resources/gaming-report",
      "title": "2026 年 Unity 游戏开发报告：开发者见解和趋势 | Unity",
      "content": "Unity 引擎\n\n下载 Unity计划和定价\n\n探索 Unity 支持的超过 25 个平台\n\n通过 Unity 投放广告通过 Unity 实现变现\n\n使用案例\n\n移动游戏\n\n使用 Unity 打造移动端爆款游戏独立游戏\n\n小团队也能做出大游戏XR 游戏\n\n跨平台发布 XR 游戏多人游戏\n\n简化多人游戏开发\n\n使用案例\n\n3D协作\n\n实时构建和审查3D项目沉浸式培训\n\n在沉浸式环境中培训客户体验\n\n创建互动3D体验人机界面（HMI）\n\n开发交互式3D嵌入式系统\n\n行业\n\n制造业\n\n实现运营卓越零售\n\n将店内体验转化为在线体验汽车\n\n提升创新能力和车内体验\n\n查看所有行业\n\n技术库\n\n文档\n\n官方用户手册和API参考开发者工具\n\n发布版本和问题跟踪器路线图\n\n查看即将推出的功能术语表\n\n技术术语库\n\n洞察\n\n案例分析\n\n真实成功案例最佳实践指南\n\n专家提示和技巧演示\n\n演示、示例和构建模块\n\n所有资源\n\n新增功能\n\n博客\n\n更新、信息和技术提示新闻\n\n新闻、故事和新闻中心\n\n社区中心\n\n讨论\n\n讨论、解决问题和连接事件\n\n全球和本地活动\n\n社区故事\n\nMade with Unity [...] Made with Unity\n\n展示Unity创作者直播活动\n\n加入开发者、创作者和内部人员Unity奖项\n\n庆祝全球的Unity创作者\n\n适合每个级别\n\nUnity Learn\n\n免费掌握Unity技能专业培训\n\n通过Unity培训师提升您的团队\n\nUnity新手\n\n准备开始\n\n开始您的学习Unity基础路径\n\n你是Unity 新手？开始您的旅程使用指南\n\n可操作的技巧和最佳实践\n\n教育\n\n对于学生\n\n开启您的职业生涯对于教育者\n\n增强您的教学教育资助许可证\n\n将Unity的力量带入您的机构认证\n\n证明您的Unity精通\n\n支持选项\n\n获取帮助\n\n帮助您在Unity中取得成功成功计划\n\n通过专家支持更快实现目标常见问题解答\n\n常见问题解答联系我们\n\n与我们的团队联系\n\n下载 Unity开始使用",
      "score": 0.6188962,
      "raw_content": null,
      "id": "41cb18-03"
    },
    {
      "url": "https://blog.csdn.net/Czhenya/article/details/125049115",
      "title": "Unity 之 发布WebGL转微信小游戏过程详解_unity发布微信小游戏-CSDN博客",
      "content": "个\n\n红包个数最小为10个\n\n红包总金额 \n\n元\n\n红包金额最低5元\n\n余额支付 \n\n 当前余额 3.43 元 前往充值 >\n\n 需支付：10.00 元 \n\n取消 确定\n\nImage 191\n\n成就一亿技术人!\n\n 领取后你会自动成为博主和红包主的粉丝 规则\n\nImage 192\n\nhope_wisdom\n\n 发出的红包 \n\n打赏作者Image 193\n\nImage 194\n陈言必行\n\n你的鼓励将是我创作的最大动力\n\n¥1¥2¥4¥6¥10¥20\n\n扫码支付：¥1\n\nImage 195获取中\n\nImage 196Image 197扫码支付\n\n您的余额不足，请更换扫码支付或充值\n\n打赏作者\n\n实付 元\n\n使用余额支付\n\nImage 198点击重新获取\n\nImage 199Image 200Image 201扫码支付\n\n钱包余额 0\n\nImage 202\n\n抵扣说明：\n\n1.余额是钱包充值的虚拟货币，按照1:1的比例进行支付金额的抵扣。  \n 2.余额无法直接购买下载，可以购买VIP、付费专栏及课程。\n\nImage 203余额充值\n\nImage 204\n\n确定 取消Image 205 [...] Image 107公安备案号11010502030143\n   京ICP备19004658号\n   京网文〔2020〕1039-165号\n   经营性网站备案信息\n   北京互联网违法和不良信息举报中心\n   家长监护\n   网络110报警服务\n   中国互联网举报中心\n   Chrome商店下载\n   账号管理规范\n   版权与免责声明\n   版权申诉\n   出版物许可证\n   营业执照\n   ©1999-2026北京创新乐知网络技术有限公司\n\nImage 108Image 109\n\n陈言必行\n\n博客等级 Image 110\n\n码龄9年\n\nImage 111领域专家: 游戏开发技术领域\n\n845 原创5911 点赞 1万+收藏 1万+粉丝\n\n关注\n\n私信\n\nImage 112\n\n### 热门文章 [...] AI写代码 csharp\n\n   1\n   2\n   3\n   4\n   5\n\n设置小程序常亮 – 仅当前小程序生效\n\n```csharp\nWeChatWASM.WX.SetKeepScreenOn(new SetKeepScreenOnOption\n        {\n            keepScreenOn = true\n        });\n```\n\nAI写代码 csharp\n\n   1\n   2\n   3\n   4\n\n  \n\n## :  \nImage 54\n\n等待导出完成，导出后的目录：\n\nImage 55\n\n### 测试一段时间后，再 _发布_ _webgl_ 版，发现有些 _发布_ 设置已经被 _微信_ _小游戏_ 的工具修改过了；(在WXEditorWindow.cs里，有兴趣的童靴可以自己看下)同时，_微信_ _小游戏_ 的工具里的.jslib文件和对应的引用文件也会影响 _webgl_ 版的正常打包，所以写个编辑器批处理把 _微信_ _小游戏_ 工具的整个文件夹 _转_ 移到备份文件夹中。要打 _微信_ _小游戏_ 版再 _转_ 回来。",
      "score": 0.5412882,
      "raw_content": null,
      "id": "dceed0-04"
    },
    {
      "url": "https://developers.weixin.qq.com/minigame/dev/guide/game-engine/unity-webgl-transform/Design/Guide.html",
      "title": "Unity 游戏接入微信小游戏指南 | 微信开放文档",
      "content": "小游戏\n\n 小程序\n 小游戏\n 公众号\n 服务号\n 开放平台\n 企业微信\n 微信支付\n 视频号\n 微信小店\n 智能对话\n 腾讯小微\n 教育平台\n\n在游戏下暂无结果，查看其它业务相关内容 >\n\n + 云开发\n  + 云托管\n\n开发\n\n取消\n\n- 指南\n\n# # Unity 游戏接入微信小游戏指南\n\n​ 下图中介绍了新游戏接入微信小游戏平台的主要转换流程，下文将介绍每一个阶段的工作：\n\nUnity快适配调优指南\n\n 【阶段一】兼容性评估：初步确认技术方案是否符合游戏项目\n 【阶段二】项目转换：可体验的WebGL、小游戏项目\n 【阶段三】微信平台能力接入：接入更多平台能力\n 【阶段四】体验调优：达到可上线标准的小游戏体验\n 【阶段五】发布上线与现网监控：上线后的问题排查与分析\n\n## # 【阶段一】兼容性评估\n\n> 相关手册：兼容性评估 、推荐引擎版本、更多小游戏成功转换案例 、技术常见问题QA\n\n​ 新计划接入游戏的开发者应阅读本节相关手册内容，参考已转化的案例游戏并结合自身游戏情况评估转化的可行性。\n\n## # 【阶段二】项目转换 [...] ## # 【阶段二】项目转换\n\n​ 本节内容将指引开发者如何让自己的游戏工程在微信小游戏平台成功运行。\n\n### # 快速开始——转换工具导出微信小游戏\n\n> 相关下载： 微信 Unity 插件下载\n>\n> 相关手册：快速开始：转换工具导出微信小游戏\n\n​ 阅读 快速开始：转换工具导出微信小游戏 快速熟悉工具的使用并完成一次简单的转化工作！\n\n### # 资源按需加载\n\n> 相关手册：资源按需加载概述 、AA(Addressable) 进行资源按需加载 、 AB(AssetBundle)进行资源按需加载 、Instant Game 实践指南\n\n​ 区别于原生 APP 游戏很少考虑场景内的资源规划问题，开发时通常将资源在游戏启动时全加载到内存中，而小游戏需要做到“即点即玩”，影响游戏的呈现速度因素中如首资源包的下载往往占比较大，因此需要根据场景中的主次内容进行资源上的优化分包处理。有关分包策略可参阅 资源按需加载概述 选择符合当前游戏的方案，具体实施可阅读具体指引文档。\n\n### # 后端/网络通信适配\n\n> 相关手册：后端服务指引 、网络通信适配 [...] ### # 接入微信API\n\n> 相关手册：WX SDK 平台能力适配 、屏幕适配 、 输入法适配 、 排行榜与微信关系数据\n\n​ Unity 游戏接入微信小游戏平台将获得微信提供的 API 以及开放能力，开发者根据需要进行按需接入。微信 API 支持的能力包括登录、设备（存储、震动）、开放数据、广告等等。\n\n### # 启动留存数据上报统计\n\n> 相关手册：启动留存数据上报统计\n\n​ 在小游戏中玩家对启动时长与体验十分敏感（尤其从“广告”等买量场景进入的玩家），因此需要在必要的位置进行相关的数据上报，Unity Loader 插件为游戏提供了一些基础上报数据，但游戏内部关键帧位置仍需要开发者自行上报，可参阅相关手册完成上报配置。\n\n## # 【阶段四】体验调优\n\n​ 截止本阶段，开发者的 Unity 游戏将在微信小游戏平台成功启动运行，但为了能够达到更佳的游戏体验开发者应继续进行对游戏工程的调优工作，本节将介绍目前微信小游戏平台为开发者提供的调优能力完成上线前的最后优化工作。\n\n### # 首场景启动优化——首帧逻辑优化",
      "score": 0.49699774,
      "raw_content": null,
      "id": "cbb18e-05"
    },
    {
      "url": "https://github.com/NoahZuo/minigame-unity-webgl-transform",
      "title": "GitHub - NoahZuo/minigame-unity-webgl-transform: Wechat Mini Game Unity engine adapter documents. · GitHub",
      "content": "## Repository files navigation\n\n# 微信小游戏Unity/团结引擎适配方案\n\n欢迎使用 Unity WebGL 小游戏适配方案(又称Unity/团结引擎快适配)，本方案设计目的是降低 Unity 游戏转换到微信小游戏的开发成本。基于WebAssembly技术，无需更换Unity引擎与重写核心代码的情况下将原有游戏项目适配到微信小游戏。\n\n官方文档：\n\n### 方案特点\n\n 保持原引擎工具链与技术栈\n 无需重写游戏核心逻辑，支持大部分第三方插件\n 由转换工具与微信小游戏运行环境保证适配兼容，保持较高还原度\n 微信小游戏平台能力以C# SDK方式提供给开发者，快速对接平台开放能力\n\n### 转换案例\n\n| 我叫MT2(回合战斗) | 旅行串串(休闲) | 谜题大陆(SLG) | 热血神剑(MMO) |\n ---  --- |\n|\n\n查阅更多转换案例\n\n## 安装与使用\n\nPackageManager(git安装URL): \n\nUnityPackage：下载地址\n\n版本更新请查看更新日志，Unity/团结引擎详细安装请查阅SDK安装指引 [...] 请查阅推荐引擎版本，安装时选择WebGL组件\n 前往微信开发者工具下载安装Stable版开发者工具【注意：为保证稳定性，请勿使用小游戏版 Minigame Build】\n 查阅小游戏开发者文档-快速上手创建小游戏类目应用\n 登录MP微信公众平台，能力地图-生产提效包-快适配，开通使用\n 查阅快速开始：转换工具导出微信小游戏进行小游戏导出转换\n\n## About\n\nWechat Mini Game Unity engine adapter documents.\n\n### Resources\n\n### Stars\n\n8 stars\n\n### Watchers\n\n0 watching\n\n### Forks\n\n4 forks\n\nReport repository\n\nYou can’t perform that action at this time. [...] | package-lock.json | package-lock.json |  |  |\n| package.json | package.json |  |  |\n|  |",
      "score": 0.47343868,
      "raw_content": null,
      "id": "3452ca-06"
    },
    {
      "url": "https://developers.weixin.qq.com/minigame/dev/guide/game-engine/unity-webgl-transform.html",
      "title": "微信小游戏适配解决方案（支持 Unity/团结引擎 项目适配） | 微信开放文档",
      "content": "### # 方案特点\n\n 保持原引擎工具链与技术栈\n 无需重写游戏核心逻辑，支持大部分第三方插件\n 由转换工具与微信小游戏运行环境保证适配兼容，保持较高还原度\n 微信小游戏平台能力以C# SDK方式提供给开发者，快速对接平台开放能力\n\n### # 转换案例\n\n| 我叫MT2(回合战斗) | 旅行串串(休闲) | 谜题大陆(SLG) | 热血神剑(MMO) |\n ---  --- |\n|\n\n## # 安装与使用\n\n详细安装请查阅SDK安装指引\n\n#### # 正式版\n\n PackageManager(git安装URL)：\n UnityPackage：下载地址\n 更新日志：请查看更新日志\n\n#### # 预览版\n\n PackageManager(git安装URL)：\n UnityPackage：预览版仅支持采用git url安装\n 更新日志：请查看更新日志\n\n#### # 使用指引 [...] #### # 使用指引\n\n 请查阅推荐引擎版本，安装时选择WebGL组件\n 前往微信开发者工具下载安装Stable版开发者工具【注意：为保证稳定性，请勿使用小游戏版 Minigame Build】\n 查阅小游戏开发者文档-快速上手创建小游戏类目应用\n 登录MP微信公众平台，能力地图-生产提效包-快适配，开通使用\n 查阅快速开始：转换工具导出微信小游戏进行小游戏导出转换\n\nThe translations are provided by WeChat Translation and are for reference only. In case of any inconsistency and discrepancy between the Chinese version and the English version, the Chinese version shall prevail.Incorrect translation. Tap to report. [...] 小游戏\n\n 小程序\n 小游戏\n 公众号\n 服务号\n 开放平台\n 企业微信\n 微信支付\n 视频号\n 微信小店\n 智能对话\n 腾讯小微\n 教育平台\n\n在游戏下暂无结果，查看其它业务相关内容 >\n\n + 云开发\n  + 云托管\n\n开发\n\n中文\n\nEN\n\n取消\n\n- 指南\n\n# # 微信小游戏适配解决方案（支持 Unity/团结引擎 项目适配）\n\n本方案是微信小游戏平台提供的技术适配解决方案，支持将 Unity 及团结引擎项目适配到微信小游戏平台，旨在降低项目适配到微信小游戏的开发成本。通过 WebAssembly 技术，开发者无需更换引擎与重写核心代码，即可将原有项目快速适配到微信小游戏。\n\n### # 支持引擎\n\n本适配方案支持团结引擎及 Unity 引擎项目的适配转换。采用 WebAssembly 技术，具有非常宽泛的兼容性，转换插件理论上支持的引擎版本涵盖：Unity 2018~2022、团结引擎\n\n### # 方案特点",
      "score": 0.44275752,
      "raw_content": null,
      "id": "8bc2cc-07"
    }
  ],
  "response_time": 1.32,
  "request_id": "b8f8cf53-32e7-46c2-bdba-c04963e0b5dc"
}
