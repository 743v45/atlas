{
  "query": "uni-app 微信小程序 skyline 渲染引擎 支持吗 dcloud 官方",
  "follow_up_questions": null,
  "answer": "Yes—according to DCloud’s official Q&A, uni‑app can use the Skyline rendering engine for a WeChat Mini Program by configuring the page in `pages.json` with `\"style\":{ \"renderer\":\"skyline\" }` and adding `\"lazyCodeLoading\":\"requiredComponents\"` in `manifest.json`.",
  "images": [],
  "results": [
    {
      "url": "https://ask.dcloud.net.cn/question/151186",
      "title": "微信小程序平台会有支持 Skyline 渲染引擎的计划吗？ - DCloud问答",
      "content": "### 相关问题\n\n uni-app中v-for循环渲染带有slot的vue自定义组件渲染slot中数据内容无效\n 【报Bug】微信Skyline+glass-easel ,3.0+基础库，组件样式隔离问题。附临时解决方案\n 官方有考虑 vue3 下支持 vant-weapp吗？ uniapp的vue2会解析微信小程序原生语言，但是vue3的编译引擎不会解析微信小程序原生语言\n APP 不能渲染SVG图片\n 【已解决】微信小程序订阅消息为什么只能订阅一个？\n 如何在微信小程序引入网络css样式\n\n优势智云 黑马程序员 程序员客栈 个推 锐亚教育 即速应用 DCloud新闻 InfoQ 蓝莺IM HeapDump性能社区 diygw可视化 艾普阳科技 申请友链\n\nDCloud 即数字天堂(北京)网络技术有限公司是W3C成员及HTML5中国产业联盟发起单位\n\n京ICP备12046007号-4 | 京公网安备：11010802035340号 | 国家信息安全等级保护三级，证书编号：11010813802-20001 [...] Brand  |  Brand\n\n注册 登录\n\ns@163.com \n\ns\\\\\\@163.com\n\n 发布：2022-08-12 18:06\n 更新：2023-03-13 13:07\n 阅读：3637\n\n# 微信小程序平台会有支持 Skyline 渲染引擎的计划吗？\n\n分类：uni-app\n\n现在打包到微信小程序 page.json 里开启 Skyline 相关的配置会被编译掉\n\n2022-08-12 18:06 负责人:无 分享\n\n没有找到相关结果\n\n已邀请:\n\n## 2 个回复\n\n最佳回复\n\n黑客与画家 \n\n黑客与画家\n\n我这边在pages.json配置可以：\n\n{  \n \"path\": \"路由\",  \n \"style\": {  \n \"renderer\": \"skyline\"  \n }  \n }\n\n另外manifest.json需要配置：\n\n\"lazyCodeLoading\": \"requiredComponents\"\n\n2023-03-13 13:07  分享\n\n132liyh \n\n132liyh\n\nmanifest.json\n\n2022-08-28 23:19  分享 [...] 为什么被折叠?  0 个回复被折叠\n\n该问题目前已经被锁定, 无法添加新回复\n\n付费技术咨询\n\n### 公告\n\n更多>\n\n 5.26版本：uni-app x, 运行到自定义基座, 提示【编译器版本号5.24和自定义基座版本号5.26不一致】的说明\n 关于 uni-push 小米厂商推送“个人订阅”迁移至“公信消息”的适配通知\n uni-app x 蒸汽模式3个App平台全发布，渲染速度超过原生、且支持js/ts开发，AI友好；uni-agent上线，uni系最佳AI\n 【公告】uniCloud阿里云服务空间云函数计费规则调整通知\n DCloud云打包计费规则调整公告\n\n### 相关问题",
      "score": 0.91760606,
      "raw_content": null,
      "id": "a6ae6e-00"
    },
    {
      "url": "https://uniapp.dcloud.io/ecosystem",
      "title": "uni-app官网",
      "content": "`uni-app`的App端虽然和小程序是相同的架构，逻辑层也运行在独立jscore而不是浏览器里，但一方面可通过web-view组件加载HTML，引入web相关库； 另一方面可通过renderjs实现在渲染层执行js，此时完整echart、threejs等web库均可使用。 （但为了全端使用，仍然建议减少对dom库的依赖，在uni-app的插件市场可寻找全端可以的库来替代）\n\n App端支持各种调用原生能力的方式\n\n1. 支持 原生混合开发\n2. 支持 比小程序能力更多的plus JSAPI\n3. 支持 Native.js 直接调用原生api\n4. 支持 原生插件扩展\n5. 支持 云打包原生插件。\n\n App端支持双渲染引擎 `uni-app`逻辑层在独立jscore，而渲染层可选webview渲染和weex引擎渲染。\n\n1. 使用webview渲染则整个架构与小程序相同，此时页面后缀为vue文件。\n2. 使用weex引擎（经过改造）渲染，则整个架构与快应用相同，此时页面后缀为nvue文件。使用webview渲染时，可以指定由系统webview渲染还是由x5引擎渲染。\n\n开发产品 [...] 兼容 weex 插件生态 uni-app内置了`weex`，`weex`的原生插件或ui库均可使用。注意`weex`的生态不如`uni-app`丰富，一般情况建议使用`uni-app`的插件市场。\n 兼容 普通 web 库 `uni-app`的H5端支持所有浏览器API。但众所周知，由于小程序的js不运行在浏览器里，所以小程序里不支持 HTML 和 DOM 的 API。 [...] 开发产品\n\nHBuilderXuni-appuni-app xuniClouduniMPsdk5+Runtimewap2appMUIuni-iduni-cdnuni-payuni-pushuni一键登录uni实人认证smsuni-starteruni-adminuni-upgrade-centeruni-imuni-aiuni-cmsuniCloud-mapuni-search\n\n运营产品\n\nuni-aduni统计uni发行uni安全专题\n\n开发者服务\n\n问答社区开发者后台\n\nuni-app文档uniCloud文档原生开发者支持文档HBuilder文档\n\n插件市场OAuth用户开放平台\n\n关于我们：  DCloud官网  案例  需求墙  许可协议  加入我们  赞助我们\n\n联系我们：  商务合作：bd@dcloud.io  广告合作：uniad@dcloud.io\n\nDCloud.io 数字天堂（北京）网络技术有限公司是\n\nHTML5中国产业联盟 发起单位\n\n国家信息安全等级保护三级，证书编号：11010813802-20001\n\nuni-agent",
      "score": 0.6737291,
      "raw_content": null,
      "id": "e3d95d-01"
    },
    {
      "url": "https://en.uniapp.dcloud.io/matter.html",
      "title": "uni-app",
      "content": "微信（可以使用virtualHost配置）/QQ/百度/抖音这四家小程序，自定义组件在渲染时会比App/H5端多一级节点，在写样式时需要注意： [...] ###The possibility that the MiniApp is normal but the App is abnormal The rendering engine of Vue pages on the App side defaults to the system webview (not the mobile phone's own browser, but the rom's webview). On older mobile phones, such as Android4.4, 5.0 or iOS8, some new css syntax is not supported of. Note that this does not mean that flex cannot be used, Android4.4 also supports flex, just don't use too new css. You can find an Android 4.4 mobile phone or use a pc emulator to actually [...] From HBuilderX 2.6, renderjs has been added on the App side, which is a js running in the view layer. Vue pages can operate browser objects through renderjs, and then allow browser-based libraries to run directly on the App side of uni-app , such as echart, threejs, see: renderjs",
      "score": 0.51413256,
      "raw_content": null,
      "id": "888024-02"
    },
    {
      "url": "https://hk.finance.yahoo.com/news/%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F%E5%8E%BB%E5%B9%B4%E8%B7%A8%E5%A2%83%E8%88%87%E5%A2%83%E5%A4%96%E7%94%A8%E6%88%B6%E4%BD%BF%E7%94%A8%E6%AC%A1%E6%95%B8%E7%AA%81%E7%A0%B450%E5%84%84%E6%AC%A1-095901359.html",
      "title": "微信小程序去年跨境與境外用戶使用次數突破50億次",
      "content": "跳至導覽  跳過主要內容  跳至右欄 [...] 條款  及 私隱政策\n\n私隱資訊主頁\n\n## 推薦新聞 [...] infocast\n\n# 微信小程序去年跨境與境外用戶使用次數突破50億次\n\ninfocast",
      "score": 0.07248569,
      "raw_content": null,
      "id": "b2b3cd-03"
    },
    {
      "url": "https://hk.finance.yahoo.com/news/%E5%BE%AE%E4%BF%A1%E6%8E%A8ai%E5%B0%8F%E7%A8%8B%E5%BA%8F%E6%88%90%E9%95%B7%E8%A8%88%E5%8A%83-%E7%82%BA%E6%9C%9F-%E5%B9%B4%E8%87%B3%E4%BB%8A%E5%B9%B4%E5%BA%95-055306995.html",
      "title": "微信推AI小程序成長計劃 為期一年至今年底",
      "content": "Title: 微信推AI小程序成長計劃 為期一年至今年底\n# 微信推AI小程序成長計劃 為期一年至今年底. 微信小程序正式推出「AI應用及線上工具小程序成長計劃」，提供雲開發資源、AI算力、數據分析、商業變現及流量激勵等全方位支持，成長計劃的激勵期為2026年全年，即至12月31日。(ta/da)~阿思達克財經新聞網址: www.aastocks.com. ## 推薦新聞.",
      "score": 0.03356739,
      "raw_content": null,
      "id": "47e0ce-04"
    },
    {
      "url": "https://hk.finance.yahoo.com/news/uber-x-%E5%BE%AE%E4%BF%A1-uber%E5%B0%87%E6%8E%A8%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F-%E9%A6%96%E9%9A%8E%E6%AE%B5%E8%A6%86%E8%93%8B%E9%A6%99%E6%B8%AF%E5%8F%8A%E6%97%A5%E6%9C%AC-110000250.html",
      "title": "Uber X 微信｜Uber將推微信小程序 首階段覆蓋香港及日本  未來數月擴展至歐美 方便內地遊客全球出行",
      "content": "跳至導覽  跳過主要內容  跳至右欄 [...] 8. 28Hse.com\n    9. AM730\n    10. Infocast\n    11. 鉅亨網\n    12. 詠竹坊\n    13. Money Club\n    14. investing.com HK [...] 2. 1. 最新新聞\n   2. Yahoo財經\n   3. Yahoo Money Talk\n   4. Tech\n3. 1. 外幣報價\n   2. 外幣兌換攻略\n   3. 日圓兌港元\n   4. 英鎊兌港元\n   5. 澳元兌港元\n   6. 美元兌港元\n   7. 港元兌人民幣\n   8. 港元兌台幣\n   9. 加元兌港元\n   10. 歐元兌港元\n   11. 貨幣轉換器\n4. 1. 港股首頁\n   2. 恒指\n   3. 恒生科技指數\n   4. 最活躍股票排行\n   5. 最大升幅股票排行\n   6. 最大跌幅股票排行\n5. 1. 美股首頁\n   2. 美股日誌\n   3. 道指\n   4. 標普500\n   5. 納指\n6. 1. 金價\n   2. 金價新聞\n   3. 銀價\n   4. 銅價\n7. 油價\n   1. 紐約期油價格\n   2. 布蘭特原油價格\n   3. 油價新聞\n   4. 天然氣價格\n8. 行情\n   1. 行情總覽\n   2. 國際指數\n   3. 期貨\n   4. 加密貨幣\n   5. 基金\n   6. 篩選工具\n9. 財經日曆",
      "score": 0.03315172,
      "raw_content": null,
      "id": "8103d1-05"
    },
    {
      "url": "https://hk.finance.yahoo.com/news/%E5%BE%AE%E4%BF%A1%E6%8E%A8-%E5%B0%8F%E7%A8%8B%E5%BA%8F-%E9%A8%B0%E8%A8%8A%E5%A2%9E%E9%95%B7%E6%B7%BB%E5%8B%95%E5%8A%9B-225634278--finance.html",
      "title": "微信推「小程序」 騰訊增長添動力",
      "content": "Title: 微信推「小程序」 騰訊增長添動力\n# 微信推「小程序」 騰訊增長添動力. 【經濟日報專訊】騰訊（00700）旗下坐擁逾8億用戶的微信將再添增長引擎，微信事業群總裁張小龍日前首度大談「小程序」，料將於明年1月9日上綫，分析指小程序最快2018年產生顯著收入。微信今年1月首次提及小程序，當時稱其為微信應用號，至11月，騰訊在公布季度業績時承認已在測試。大和證券報告指出，小程序令用戶能更容易發掘信息及更輕易使用各種服務，彷彿令微信成為一個所有手機都能匹配的手機系統。該行相信，小程序的出現將會令市場對騰訊的估值作出調整，透過付費搜尋、展示廣告、雲服務及支付等獲利，預料最快於2018年產生顯著收入貢獻。擁4特質 免安裝省儲存容量所謂小程序，張小龍指其具備毋須安裝、觸手可及、用完即走及毋須刪除4個特質，意味用戶可透過掃描二維碼獲得互動，令手機的儲存容量壓力大大減輕，加上應用程式毋須安裝，令用戶在使用服務後省卻刪除的過程。他指小程序看來是程序，但以完全不同於過去應用程式的形狀出現，是更靈活的應用。張小龍舉例稱：「當你看到一盞燈，它的開關應用程式自動出現了；又或當你走到一個公園門口，公園門票的應用程式亦會自動浮現，你可以通過眼鏡或者其他方法控制這一個程式，去啟動它，運行它。」大和證券報告形容，小程序令用戶能停留在微信之內，使他們在微信中也能體驗如獨立應用程式的感受。今年新春 不再推搶紅包營銷截至9月底，微信月活躍用戶達到8.5億戶，集團需持續增加用戶黏性來保持程式的使用次數，微信亦已由過去的單純溝通工具，發展成社交平台及支付的工具。至於兩年前由微信發起的農曆新年搶紅包活動，張小龍稱下月的新年將不再推動紅包營銷，希望用戶花更多時間陪伴家人。另外，騰訊日前與四維圖新（深：002405）及新加坡政府投資公司（GIC）共同收購開放位置平台公司HERE 10%股份，原股東奧迪（AUDI）、寶馬（BMW）及戴姆勒（Daimler）相關減持，料明年上半年完成交易。騰訊副總裁馬喆表示，合作將促進集團在自動駕駛、人工智能等未來科技的探索。.",
      "score": 0.030585974,
      "raw_content": null,
      "id": "69bc39-06"
    },
    {
      "url": "https://hk.finance.yahoo.com/news/uber%E6%8E%A8%E5%87%BA%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F-%E7%8E%87%E5%85%88%E5%9C%A8%E6%B8%AF%E4%BD%BF%E7%94%A8%E6%96%B9%E4%BE%BF%E4%B8%AD%E5%9C%8B%E9%81%8A%E5%AE%A2%E5%85%A8%E7%90%83%E5%87%BA%E8%A1%8C-030005318.html",
      "title": "Uber推出微信小程序 率先在港使用方便中國遊客全球出行",
      "content": "Title: Uber推出微信小程序 率先在港使用方便中國遊客全球出行\n# Uber推出微信小程序 率先在港使用方便中國遊客全球出行. <匯港通訊> Uber 正式推出官方微信小程序,方便中國內地遊客和香港市民在香港及全球多個旅遊熱點預約行程並支付車費。小程序於7月率先在香港和日本推出,並將於未來數月陸續擴展到美國、法國、澳洲等9個國家和地區。在香港使用的微信小程序將支援微信支付(人民幣錢包)及 WeChat Pay HK(WeChat 港幣錢包),讓中國內地遊客及香港市民暢享便捷無縫的出行體驗。. 用戶可在微信搜尋小程序,並以熟悉的中文介面和操作流程來使用,無需下載額外應用程式、無需綁定國際銀行卡,在微信內即可直接預約 Uber 行程。. Uber 網約共乘服務全球業務總管 Pradeep Parameswaran 表示:「Uber 與微信的合作,讓中國內地用戶外出旅遊的每一步都更加便捷。為了方便乘客,我們致力於他們最常使用的應用程式提供服務。對於中國內地旅客而言,微信無疑是首選。我們全新的微信小程序將確保他們從搜尋到支付,都能享受無縫的出行體驗。」. 微信小程序的推出標誌著 Uber 全球擴展策略的一個里程碑,突顯了與本地相關平台合作的決心。微信小程序有11億月活躍用戶,讓用戶無需下載獨立應用程式,即可在微信內購物、支付和使用其他服務。. 去年,逾1.3億中國內地旅客出境,預計2025年這個數字將繼續上升。是次合作通過微信小程序簡單易用的介面,連接 Uber 服務與用戶的日常使用習慣:語言自動適配中文介面,目的地輸入支援中文檢索,行程可即時同步微信好友,徹底消除跨境出行的資訊壁壘。. 微信支付國際業務總裁李培庫表示:「Uber 微信小程序為用戶帶來了便利。我們一直努力創新,讓中國內地遊客境外出行更方便無憂,我們致力於讓用戶在世界任何角落都能享受『境內外一致』的便捷數碼體驗。與 Uber 的合作也讓微信的跨境數字生活圈更加完善。」. 微信小程序團隊表示:「歡迎 Uber 加入微信小程序生態,讓用戶在微信內即可一鍵完成打車與便捷支付,極大提升跨境出行體驗。小程序也將攜手更多生態夥伴,推動境外生態的普惠與升級,為全球用戶提供創新、便捷的數碼化服務。」 (BC).",
      "score": 0.01999476,
      "raw_content": null,
      "id": "999555-07"
    }
  ],
  "response_time": 2.12,
  "request_id": "6412fff1-ccf3-40ee-809c-869302917c23"
}
