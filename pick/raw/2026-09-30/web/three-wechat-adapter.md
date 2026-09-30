# tvly search: threejs-miniprogram 微信官方 three.js 适配库现状
- 采集: 2026-09-30, tvly search --json --max-results 8

{
  "query": "threejs-miniprogram 微信 官方 three.js 适配库 现状",
  "follow_up_questions": null,
  "answer": null,
  "images": [],
  "results": [
    {
      "url": "https://www.cnblogs.com/fws407296762/p/13952826.html",
      "title": "微信小程序中写threejs系列之 threejs-miniprogram - 松鼠闹IT - 博客园",
      "content": "1. `threejs` 会操作 `DOM`,但是小程序里面没有 `DOM`\n2. `threejs` 会绑定 `window` 对象，但是小程序里面没有 `window`\n\n网上对这一块有一些解决方案，有一个大佬自己开发了一个适配小程序的 threejs.miniprogram，基本上大部分的功能是都可以用的  \n 还有的人针对 小游戏 里面的 `weapp-adapter` 做了二次开发，主要是将浏览器中的 `DOM` 和 `window` 对象进行模拟  \n 这两个方案毕竟都是民间的，得不到稳定的维护，后来我发现微信官方出了一个 threejs-miniprogram，官方出品的，把 `threejs` 里面的大部分功能适配过来了，但是也有很多不足的地方，比如 `Controls` 这一块没有适配过来，可能小程序上需要实现的 3D 效果不需要很多的原因吧\n\n使用方式：\n\n`npm install --save threejs-miniprogram` [...] ```\nimport {createScopedThreejs} from 'threejs-miniprogram' Page({ onReady() { wx.createSelectorQuery() .select('#webgl') .node() .exec((res) => { const canvas = res.node // 创建一个与 canvas 绑定的 three.js const THREE = createScopedThreejs(canvas) // 传递并使用 THREE 变量 }) } }) \n```\n\n也要注意一点：`threejs-miniprogram` 适配的 Three.js 版本号为 0.108.0，如果需要修改只能自己动手了，还有就是里面的 `Controls` 估计也只能自己动手\n\nposted on 2020-11-10 11:15  松鼠闹IT  阅读(5609)  评论(2)    收藏)  举报\n\n刷新页面返回顶部\n\n  订阅\n 管理 [...] 松鼠闹IT\n\n# 微信小程序中写threejs系列之 threejs-miniprogram\n\n我们大家都知道要在浏览器中写 `WebGL` 会用到 `threejs` 这个库，这个库提供了很多好用的属性，实话说，如果没有计算机图形知识的人而言，刚开始接触这个库的时候，确实很多概念都很难理解，我刚开始就是这样。  \n 我大概学 `threejs` 花了三个阶段：  \n 第一个阶段：不求甚解，这个阶段完全就是看看实现的效果，看看里面的基本概念，但是啥都不了解  \n 第二个阶段：了解基本概念，这个阶段就是去弄懂里面大概的几个概念了，知道是怎么回事了，但是还是不知道怎么用  \n 第三个阶段：运用里面大部分的API，这个阶段，我基本上知道怎么用了，可以做一些简单的项目了  \n 后面还有灵活运用、基于threejs开发工具这几个阶段还没到。  \n 既然我已经知道怎么用 `threejs`，正好现在微信小程序开始支持 `WebGL` 了，那我就直接到小程序里面开发了。  \n 刚开始开发的时候我就碰到了几个问题：",
      "score": 0.8156003,
      "raw_content": null,
      "id": "315885-00"
    },
    {
      "url": "https://www.bookstack.cn/read/miniprogram-guide-20210305/b9cde0e559483258.md",
      "title": "工具类库 - threejs-miniprogram - 《微信小程序官方开发文档(全) - 20210305》 - 书栈网 · BookStack",
      "content": "```\n\n## 说明\n\n 本项目当前使用的 Three.js 版本号为 0.108.0，如要更新 threejs 版本可发 PR 修改或 fork 后自行修改。\n 该适配版本的 THREE 不在全局环境中，如使用 Three.js 的其他配套类库，需要自行传入 THREE 到类库中。\n 如在使用过程中发现有适配问题，可通过 issue 反馈或发 PR 修复。\n\n当前内容版权归 腾讯 或其关联方所有，如需对内容或内容相关联开源项目进行关注与资助，请访问 腾讯 .\n\n上一篇:\n\n下一篇:\n\n 书签\n 添加书签  移除书签 [...] 思维导图备注\n\n微信小程序官方开发文档(全) - 20210305 - 20210305\")\n\n首页  AI助手   白天  夜间   BookChat 小程序 小程序  阅读 \n\n 书签 我的书签\n 添加书签 添加书签  移除书签 移除书签\n\n# threejs-miniprogram\n\n来源:腾讯  浏览 4709  扫码  2021-03-05 22:10:36\n\n threejs-miniprogram\n  + 使用\n  + 说明\n\n# threejs-miniprogram\n\nThree.js 小程序 WebGL 的适配版本。\n\n## 使用\n\n可参考 example 目录下的示例项目或参照以下流程：\n\n1. 通过 npm 安装\n\n```\n\n1. npm install -- save threejs - miniprogram\n\n```\n\n安装完成之后在微信开发者工具中点击构建 npm。\n\n1. 导入小程序适配版本的 Three.js\n\n``` [...] ```\n\n1. import  {createScopedThreejs}  from  'threejs-miniprogram'\n2. Page({\n3. onReady()  {\n4. wx. createSelectorQuery()\n5. . select('#webgl')\n6. . node()\n7. . exec((res)  =>  {\n8. const  canvas =  res. node\n9. // 创建一个与 canvas 绑定的 three.js\n10. const  THREE =  createScopedThreejs(canvas)\n11. // 传递并使用 THREE 变量\n12. })\n13. }\n14. })\n\n```\n\n## 说明",
      "score": 0.78493005,
      "raw_content": null,
      "id": "c7ca10-01"
    },
    {
      "url": "https://github.com/wechat-miniprogram/threejs-miniprogram",
      "title": "GitHub - wechat-miniprogram/threejs-miniprogram: WeChat MiniProgram adapted version of Three.js · GitHub",
      "content": "## 说明\n\n 本项目当前使用的 Three.js 版本号为 0.108.0，如要更新 threejs 版本可发 PR 修改或 fork 后自行修改。\n 该适配版本的 THREE 不在全局环境中，如使用 Three.js 的其他配套类库，需要自行传入 THREE 到类库中。\n 如在使用过程中发现有适配问题，可通过 issue 反馈或发 PR 修复。\n\n## About\n\nWeChat MiniProgram adapted version of Three.js\n\n### Resources\n\nMIT license\n\nCustom properties\n\n### Stars\n\n799 stars\n\n### Watchers\n\n15 watching\n\n### Forks\n\n238 forks\n\nReport repository\n\n## Used by\n\nYou can’t perform that action at this time. [...] Three.js 小程序 WebGL 的适配版本。\n\n## 使用\n\n可参考 example 目录下的示例项目或参照以下流程：\n\n1. 通过 npm 安装\n\n   ```\n   npm install --save threejs-miniprogram \n   ```\n\n安装完成之后在微信开发者工具中点击构建 npm。\n\n1. 导入小程序适配版本的 Three.js\n\n```\nimport{createScopedThreejs} from'threejs-miniprogram' Page({onReady(){wx. createSelectorQuery(). select('#webgl'). node(). exec((res) =>{const canvas = res. node// 创建一个与 canvas 绑定的 three.js const THREE = createScopedThreejs(canvas)// 传递并使用 THREE 变量})}})\n```\n\n## 说明 [...] | Name | Name | Last commit message | Last commit date |\n ---  --- |\n| build | build |  |  |\n| example | example |  |  |\n| src | src |  |  |\n| .eslintrc.js | .eslintrc.js |  |  |\n| .gitignore | .gitignore |  |  |\n| .npmignore | .npmignore |  |  |\n| .npmrc | .npmrc |  |  |\n| LICENSE | LICENSE |  |  |\n| README.md | README.md |  |  |\n| package-lock.json | package-lock.json |  |  |\n| package.json | package.json |  |  |\n|  |\n\n## Repository files navigation\n\n# threejs-miniprogram",
      "score": 0.76152116,
      "raw_content": null,
      "id": "13cd3e-02"
    },
    {
      "url": "https://discourse.threejs.org/t/transplant-three-js-to-wechat-mini-program/10333",
      "title": "Transplant three.js to wechat mini program - Resources - three.js forum",
      "content": "# Transplant three.js to wechat mini program\n\nI have transplanted three.js to wechat min program (app in China) ,for now Primitive geometry, texture, orbitcontrol, gtlfLoader, objLoader are supported! See  for more detail. PR and issue are invited！\n\n不是很早以前就可以了吗\n\n### Related topics [...] ### Related topics\n\n| Topic |  | Replies | Views | Activity |\n ---  --- \n| Please Read This Before Posting a Question  Questions questions | 0 | 5569 | March 13, 2017 |\n| GPT for three.js  Discussion | 0 | 464 | February 4, 2024 |\n| Little personal page with bits of ThreeJS  Showcase | 2 | 708 | September 8, 2022 |\n| I am not able to use ay of controls in three js  Questions | 1 | 80 | January 19, 2025 |\n| Get Started with Three.js (in 5 mins)  Resources | 1 | 63 | April 14, 2026 | [...] Powered by Discourse, best viewed with JavaScript enabled",
      "score": 0.6755297,
      "raw_content": null,
      "id": "3abc3c-03"
    },
    {
      "url": "https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/en/extended/utils/api-typings.html",
      "title": "WeChat Mini Program definition file | 微信开放文档",
      "content": "WeChat Mini Program API of TypeScript Type definition file\n\n> For more detailed instructions and guidelines, please clickProject address。\n\n# # threejs-miniprogram\n\nThree.js Mini Programs WebGL An adaptation version of the.\n\n> For more detailed instructions and guidelines, please clickProject address。\n\n# # lottie-miniprogram\n\nlottie The animation library adapts the version of the Mini Program.\n\n> For more detailed instructions and guidelines, please clickProject address。\n\n# # sm-crypto [...] # # sm-crypto\n\nMini Programs js Kurt. National secret algorithm sm2、sm3 and sm4 The realization of.\n\n> Using this component requires a dependency on the Mini Program base library 2.2.1 The above versions also rely on the npm Build. Details can be found atOfficial npm file。\n\n> For more detailed instructions and guidelines, please clickProject address。\n\n# # miniprogram-i18n [...] miniprogram-i18n There are four main parts in the usage of. They are: build scripts and i18 configuration, i18n text definition, usage in WXML, and usage in JavaScript.\n\n> For more detailed instructions and guidelines, please clickProject address。\n\nThe translations are provided by WeChat Translation and are for reference only. In case of any inconsistency and discrepancy between the Chinese version and the English version, the Chinese version shall prevail.Incorrect translation. Tap to report.",
      "score": 0.44073462,
      "raw_content": null,
      "id": "d379a8-04"
    },
    {
      "url": "https://cloud.tencent.com/developer/article/2127614",
      "title": "【愚公系列】2022年09月 微信小程序-three.js加载3D模型-腾讯云开发者社区-腾讯云",
      "content": "bindtouchstart=\"touchStart\"\nbindtouchmove=\"touchMove\"\nbindtouchend=\"touchEnd\"\n></canvas>`\n`import { createScopedThreejs } from 'threejs-miniprogram'\nconst { renderModel } = require('../../../lib/test-cases/model')\nconst app = getApp()\nPage({\ndata: {},\nonLoad: function () {\nwx.createSelectorQuery()\n.select('#webgl')\n.node()\n.exec((res) => {\nconst canvas = res.node\nthis.canvas = canvas\nconst THREE = createScopedThreejs(canvas)\nthis.fadeToAction = renderModel(canvas, THREE)//3d model [...] ## 【愚公系列】2022年09月 微信小程序-three.js加载3D模型\n\n# 【愚公系列】2022年09月 微信小程序-three.js加载3D模型\n\n作者头像\n\n#### 文章目录\n\n## 前言\n\nThree.js 是一款运行在浏览器中的 3D 引擎，你可以用它创建各种三维场景，包括了摄影机、光影、材质等各种对象。\n\n一个典型的 Three.js 程序至少要包括渲染器（Renderer）、场景（Scene）、照相机（Camera），以及你在场景中创建的物体。\n\nThree.js相关文档：\n\n## 一、Three.js的使用\n\n安装第三方包：`npm i --save threejs-miniprogram`\n\n`npm i --save threejs-miniprogram`\n\n### 1.3D模型的绘制 [...] // 不能投射阴影。\n// skyColor : 0xffffff, groundColor : 0x444444,\nvar light = new THREE.HemisphereLight(0xffffff, 0x444444);\nlight.position.set(0, 20, 0);\nscene.add(light);\n// 平行光，常用平行光来模拟太阳光的效果\nlight = new THREE.DirectionalLight(0xffffff);\nlight.position.set(0, 20, 10);\nscene.add(light);\n/// 构造带网格的大地辅助\n// 网格Mesh\n// 平面几何体PlaneGeometry，PlaneBufferGeometry是PlaneGeometry中的BufferGeometry接口，使用 BufferGeometry 可以有效减少向 GPU 传输上述数据所需的开销。\n// MeshPhongMaterial，一种用于具有镜面高光表面的材质。",
      "score": 0.40443742,
      "raw_content": null,
      "id": "24fd2f-05"
    },
    {
      "url": "https://hk.investing.com/news/stock-market-news/article-1372145",
      "title": "微信推出官方龍蝦插件 騰訊雲率先適配",
      "content": "iShares MSCI World\n           iShares MSCI Emerging Markets\n           新华富时中国25指数\n\n       基金\n\n           世界基金\n           主要基金\n\n           施羅德亞洲高息股債基金 A Acc\n           東亞聯豐環球債券基金 A Acc\n           匯豐中國翔龍基金A\n           東亞聯豐港元債券基金 A Acc\n\n       債券\n\n           金融期货\n           世界政府债券\n           国债利差\n           期货汇率\n           債券指數\n           信用違約互換利率(CDS)\n\n           美国十年期债券\n           欧元债券\n           日本政府债券20年期\n           英国公债\n           美国三十年期\n\n       加密貨幣 [...] 黃金\n           WTI原油\n           白銀\n           天然氣\n           銅\n           美國大豆\n\n       指數\n\n           中国 - 指数\n           主要金融指数\n           财经指数\n           全球指數\n           期货指数\n           股指CFDs\n\n           香港恒生指數\n           道瓊斯指數\n           標普500指數\n           纳斯达克100\n           上證指數\n           日經225\n           ASX200指數\n\n       证券 [...] English (USA)\n   English (UK)\n   English (India)\n   English (Canada)\n   English (Australia)\n   English (South Africa)\n   English (Philippines)\n   English (Nigeria)\n   Deutsch\n   Español (España)\n   Español (México)\n   Français\n   Italiano\n   Nederlands\n   Polski\n   Português (Portugal)\n   Português (Brasil)\n   Русский\n   Türkçe\n   ‏العربية‏\n   Ελληνικά\n   Svenska\n   Suomi\n   עברית\n   日本語\n   한국어\n   简体中文\n   Bahasa Indonesia\n   Bahasa Melayu\n   ไทย\n   Tiếng Việt\n   हिंदी",
      "score": 0.19534872,
      "raw_content": null,
      "id": "9e15aa-06"
    },
    {
      "url": "https://cn.investing.com/news/stock-market-news/article-3273639",
      "title": "微信推出官方龙虾插件 腾讯云率先适配 提供者 智通财经",
      "content": "© 2007-2026 -Fusion Media Limited | 粤ICP备17131071号 | 保留所有权利。\n\n   条款及条件\n   隐私政策\n   风险警示 [...] 中国10年期国债\n           美国10年期T-Note\n           美国30年期T-Bond\n           英国公债\n           长期欧元债券\n           短期欧元债券\n\n       加密货币\n\n           所有加密货币\n           加密货币对\n           比特币\n           以太坊\n           bitcoin-cash\n           Dogecoin\n           OFFICIAL TRUMP\n           永续期货\n           货币转换器\n\n           比特币/美元\n           以太坊/美元\n           比特币现金/美元\n           莱特币/美元\n           狗狗币/美元\n           以太坊经典/美元\n           以太坊/比特币\n           XRP/美元\n           比特币期货 CME\n\n       交易所交易票据ETC [...] | 名称 | 最新价 | 涨跌幅 | 交易量 |  |\n ---  --- \n| 昆船智能 | 17.98 | +20.03% | 3,384.51万 |  |\n| Ceyear Technologies Co. | 83.88 | +20.00% | 3,264.18万 |  |\n| 霍莱沃 | 37.94 | +19.99% | 597.64万 |  |\n| Luoyang Bearing Co. | 35.54 | +19.99% | 2,580.58万 |  |\n| 海峡创新 | 10.81 | +19.98% | 1.62亿 |  |\n| Fujian Tendering | 13.30 | +12.33% | 2,587.30万 |  |\n| 超频三 | 9.56 | +11.81% | 1.04亿 |  |",
      "score": 0.16313887,
      "raw_content": null,
      "id": "51c7ec-07"
    }
  ],
  "response_time": 1.64,
  "request_id": "300de0ef-c0ff-4adf-a630-a17e44c58746"
}
