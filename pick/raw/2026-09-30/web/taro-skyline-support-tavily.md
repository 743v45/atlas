{
  "query": "Taro skyline 渲染 支持 微信",
  "follow_up_questions": null,
  "answer": null,
  "images": [],
  "results": [
    {
      "url": "https://docs.taro.zone/docs/skyline",
      "title": "Skyline | Taro 文档",
      "content": "由凹凸实验室倾力打造的「Deco 设计稿一键生成多端代码」预览版正式上线啦，欢迎免费试用！\n\n版本：4.x\n\n# Skyline\n\nSkyline 的具体内容详见：Skyline 介绍\n\n信息\n\n仅支持在微信小程序使用，worklet 部分从 `4.0.8` 开始支持\n\n## 开启 Skyline​\n\n配置方法和微信小程序相同，开发前请仔细阅读 《微信小程序 Skyline - 起步》。\n\n示例：\n\napp.config.js\n\n```\nexport default defineAppConfig({export  default  defineAppConfig({ pages: [ pages:  [ 'pages/index/index',  'pages/index/index',  ]  ]  lazyCodeLoading: \"requiredComponents\",  lazyCodeLoading:  \"requiredComponents\",  rendererOptions: { rendererOptions:  { skyline: { skyline:  { defaultDisplayBlock: true,  defaultDisplayBlock:  true,  defaultContentBox: true  defaultContentBox:  true  }  }  }  } }) })\n```\n\npage/index/index.config.js [...] =  offset;  Taro.nextTick(() => { Taro. nextTick(()  =>  { page.applyAnimatedStyle(\".circle\", () => { page. applyAnimatedStyle(\".circle\",  ()  =>  { \"worklet\";  \"worklet\";  return { return  { transform: `translateX(${offset.value}px)`,  transform:  `translateX(${offset. value}px) `,  };  };  });  });  });  });  }  }  });  });   return ( return  ( <View className='index' compileMode>  < View  className = ' index '  compileMode>  {/ 手势 /}  {/ 手势 /}  <PanGestureHandler onGestureWorklet='onGesture'>  < PanGestureHandler  onGestureWorklet = ' onGesture '>  <View className='circle'>拖动我View> PanGestureHandler> {/ 非手势组件的 worklet 回调 /} <ScrollView style={{ height: \"300px\", border: '1px solid #ccc' }} type='custom' scroll-y onScrollUpdateWorklet='onScrollUpdate' > {Array(100) .fill(1) .map((item, [...] page/index/index.config.js\n\n```\nexport default definePageConfig({export  default  definePageConfig({ navigationBarTitleText: '首页',  navigationBarTitleText:  '首页',  renderer: 'skyline',  renderer:  'skyline',  componentFramework: 'glass-easel',  componentFramework:  'glass-easel',  navigationStyle: 'custom',  navigationStyle:  'custom', }) })\n```\n\n### 使用 worklet​\n\n在 Taro 中使用 worklet 需要首先开启半编译，开启方法见：半编译模式使用方法。\n\n使用 worklet 动画能力时确保以下两项：详见 worklet 动画\n\n 确保开发者工具右上角 > 详情 > 本地设置里的 将 JS 编译成 ES5 选项被勾选上 (代码包体积会少量增加)\n worklet 动画相关接口仅在 Skyline 渲染模式下才能使用\n\n示例：\n\nconfig/index.js\n\n```\n{{ mini: { mini:  { experimental: { experimental:  { compileMode: true  compileMode:  true  }  }  }  } } }\n```\n\npages/index/behavior.js",
      "score": 0.84948516,
      "raw_content": null,
      "id": "49750a-00"
    },
    {
      "url": "https://github.com/NervJS/taro/discussions/12238",
      "title": "微信小程序Skyline渲染引擎讨论#12238 - NervJS taro",
      "content": "粗略把文档过了一遍，除去Skyline 与Webview 渲染自身的差异不谈，Taro 需要兼容的地方：. 部分组件的属性; 事件回调支持worklet; 兼容手势组件.",
      "score": 0.80771893,
      "raw_content": null,
      "id": "3ce11b-01"
    },
    {
      "url": "https://github.com/nervjs/taro/issues/18708",
      "title": "微信小程序Skyline 模式下, Span 组件渲染成View #18708",
      "content": "Taro 版本. v4. 相关领域 ; 使用框架. React. 相关平台 ; 小程序基础库版本. 3.13.1. 问题描述 ; 复现链接. 无. 复现步骤 ; 环境信息. 无. 开源贡献.",
      "score": 0.79369855,
      "raw_content": null,
      "id": "e04478-02"
    },
    {
      "url": "https://github.com/NervJS/taro/discussions/19379",
      "title": "Taro 已支持Vite 8 + React 19 并支持微信小程序开发热更新",
      "content": "Taro 已支持Vite 8 + React 19 并支持微信小程序开发… 支持在app.tsx 中渲染任意内容全自动分包,不用再为2M大小",
      "score": 0.7900289,
      "raw_content": null,
      "id": "48b220-03"
    },
    {
      "url": "https://juejin.cn/post/7451878515375996965",
      "title": "Taro小程序开发性能优化实践我们团队在利用Taro进行秒送频道小程序的同时，一直在探索性能优化的最佳实践。随着需求的不 - 掘金",
      "content": "1.分包加载速度慢，导致首屏耗时偏长。\n\n2.接口请求时长过长。\n\n3.feeds渲染耗时偏长。\n\n需要根据存在的问题，针对性地采取对应处理方案。\n\n## 优化实践\n\n### 1.切换Skyline渲染引擎\n\n为了解决首屏耗时较长的问题，我们经过调研，决定采用Skyline引擎来进行优化。\n\nSkyline是微信官方提供的渲染引擎，目标是进一步优化小程序性能，提供更为接近原生的用户体验。其使用更精简高效的渲染管线，并带来诸多增强特性，让 Skyline拥有了更接近原生渲染的性能体验。\n\nSkyline 创建了一条渲染线程来负责渲染任务，并在 AppService 中划出一个独立的上下文，来运行之前 WebView 承担的 JS 逻辑、DOM 树创建等逻辑。\n\n﻿\n\n﻿﻿\n\n这种新的架构相比原有的 WebView 架构，有以下特点：\n\n•界面更不容易被逻辑阻塞，进一步减少卡顿\n\n•无需为每个页面新建一个 JS 引擎实例（WebView），减少了内存、时间开销\n\n•框架可以在页面之间共享更多的资源，进一步减少运行时内存、时间开销\n\n•框架的代码之间无需再通过 JSBridge 进行数据交换，减少了大量通信时间开销\n\n而与此同时，这个新的架构能很好地保持和原有架构的兼容性，可以很大程度上降低首屏的渲染耗时。\n\n﻿\n\n﻿﻿\n\n在实际Skyline适配的过程中，我们对遇到的问题进行了记录：\n\n﻿\n\n1.利用backgroundPosition，backgroundImage和height裁剪背景图片的时候，backgroundPosition不可以使用calc运算符：\n\n目的：裁剪图片从底部开始，向上，高度为gradientHeight的部分\n\n原写法：\n\n```\ncalc 100% getPx\n```\n\n适配写法：\n\n```\nstyle\n``` [...] 如果实在无法提高层级，可以考虑使用: root-portal组件\n\n7. 所有节点默认是 relative，可能导致absolute不准/margin-top无效：\n\n按实际情况调整UI。如果遇到节点下的第一个margin-top无效，可以在前面加一个占位的的view\n\n最终适配完成后的优化效果如下\n\n冷启动：\n\n﻿\n\n﻿﻿\n\n﻿\n\n热启动：\n\n﻿\n\n﻿﻿\n\n﻿\n\n### 2.资源位延迟加载\n\nfeeds楼层存在着渲染时长偏长的问题，最主要的问题集中在店带品楼层上：\n\n﻿\n\n﻿﻿\n\n该楼层带有商品列表，列表中的商品每一个都会渲染一个资源位，数目在15到20个不等，这样的楼层会下发13个左右，且每次都会在接口下发后一次性全部渲染，导致渲染的资源位数目暴增。\n\n本次优化对商品资源位的加载进行了优化，首屏只最多渲染6个：\n\n﻿\n\n﻿﻿\n\n其余商品在滑动触底是懒加载。\n\n```\nhandleScrolltolowerloadMoreImg.current falseloadMoreImg.current true[loadMoreImg]\n```\n\n以此方式来减少渲染工作量，提高渲染速度。底部的feeds商品资源位也采用相同的处理方式，首屏最多加载6个：\n\n﻿\n\n﻿﻿\n\n### 3.多团队沟通优化\n\n除了使用懒加载的方式，我们也积极与产品和UED团队沟通，针对店带品的使用场景沟通解决方案。最终确定可以将首屏下发的楼层数从13个调整为9个，进一步降低渲染压力，提升feeds部分的渲染速度。\n\n在实际优化实践中，往往与其他团队进行沟通，是最有效的优化方式，大家可以多借鉴一下。\n\n### 4.图片资源优化 [...] 在实际优化实践中，往往与其他团队进行沟通，是最有效的优化方式，大家可以多借鉴一下。\n\n### 4.图片资源优化\n\n图片资源尺寸过大，会导致图片下载缓慢，资源位白屏，用户体验差。以往网管在进行商品图片下发的时候，无论是店带品楼层的商品还是商品详情页展示的商品大图，采用的都是同一套尺寸较大的图片，这就导致在店带品楼层商品列表过多时，图片下载过程等待时间过长。经过与后端团队，产品和UED团队积极沟通，确定了一套3尺寸图片方案：\n\n﻿\n\n﻿﻿\n\n产品配置图片的时候，会配置大、中、小三种尺寸的图片，网关在下发时会根据资源位的类型区别下发，针对店带品楼层、feeds商品这种楼层，仅下发小尺寸图片，以减小接口请求数据量以及图片下发时间，极大地提高了图片夹杂速度。\n\n### 5.接口请求逻辑改造\n\n秒送频道页涉及到两个接口请求，分别是主接口和feeds数据接口，之前因为代码结构的原因，两个接口采用了串行请求的方式做请求。这次的优化经过方案评审，将串行改为并行，并将两个接口返回的结果进行隔离，分批渲染，从而降低了整体接口请求的时长。\n\n## 优化成果\n\n经过一系列优化，在接口请求总时长，feeds渲染提升非常明显，首屏加载速度有了很大提升：\n\n﻿\n\n﻿﻿\n\n根据掐秒表的结果，也能够最直观的感觉出整体开启速度的提升：\n\n﻿\n\n﻿﻿\n\n## 结语\n\nTaro小程序开发的性能优化实践，不仅涉及到前端代码优化，还涉及到了多个团队之间的沟通配合，好的代码习惯也不是一朝一夕就能养成的，优化也需要日积月累，不断持续地推进，希望这篇文章可以帮助到大家，助力大促期间的用户体验改进。\n\navatar\n\n京东零售技术  创作等级LV.5 \n\n技术运营 @京东\n\n242\n\n文章 209k\n\n阅读 1.4k\n\n粉丝",
      "score": 0.7598145,
      "raw_content": null,
      "id": "4f0a75-04"
    },
    {
      "url": "https://zhuanlan.zhihu.com/p/552939721",
      "title": "Taro小程序跨端开发入门实战",
      "content": "Taro 是一个开放式跨端跨框架解决方案,支持使用React/Vue/Nerv 等框架来开发微信/ 不支持同层渲染,原生组件上只能使用Cover 组件",
      "score": 0.75421005,
      "raw_content": null,
      "id": "4c7b49-05"
    },
    {
      "url": "https://blog.csdn.net/weixin_55897003/article/details/145595201",
      "title": "Taro集成towxml渲染markdown文档原创",
      "content": "TaroParse taro版本富文本解析组件支持Html及markdown可视化版本号:1.1.5特色 。 用于解决在微信小程序中Markdown、HTML不能直接渲染的问题。",
      "score": 0.75027883,
      "raw_content": null,
      "id": "e76632-06"
    },
    {
      "url": "https://blog.csdn.net/weixin_43951315/article/details/147087979",
      "title": "Skyline配置指南-微信小程序原创",
      "content": "Skyline与WebView渲染模式不兼容，部分旧版API可能不支持。 · Skyline渲染模式在2.29.2及以上基础库支持，线上最低基础版本库也必须大于该版本，不然就会",
      "score": 0.74229145,
      "raw_content": null,
      "id": "d6d115-07"
    }
  ],
  "response_time": 2.53,
  "request_id": "817bc561-9e2b-44ef-99a0-fa0283a94bd1"
}
