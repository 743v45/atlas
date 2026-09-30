
  https://docs.taro.zone/docs/skyline
  docs.taro.zone (5,048 chars)

由凹凸实验室倾力打造的「Deco                                                    
设计稿一键生成多端代码」预览版正式上线啦，欢迎免费试用！                        

版本：4.x                                                                       

                                    Skyline                                     

Skyline 的具体内容详见：Skyline 介绍                                            

信息                                                                            

仅支持在微信小程序使用，worklet 部分从 4.0.8 开始支持                           

开启 Skyline​                                                                    

配置方法和微信小程序相同，开发前请仔细阅读 《微信小程序 Skyline - 起步》。      

示例：                                                                          

app.config.js                                                                   

                                                                                
 export default defineAppConfig({export  default  defineAppConfig({ pages: [    
 pages:  [ 'pages/index/index',  'pages/index/index',  ]  ]  lazyCodeLoading:   
 "requiredComponents",  lazyCodeLoading:  "requiredComponents",                 
 rendererOptions: { rendererOptions:  { skyline: { skyline:  {                  
 defaultDisplayBlock: true,  defaultDisplayBlock:  true,  defaultContentBox:    
 true  defaultContentBox:  true  }  }  }  } }) })                               
                                                                                

page/index/index.config.js                                                      

                                                                                
 export default definePageConfig({export  default  definePageConfig({           
 navigationBarTitleText: '首页',  navigationBarTitleText:  '首页',  renderer:   
 'skyline',  renderer:  'skyline',  componentFramework: 'glass-easel',          
 componentFramework:  'glass-easel',  navigationStyle: 'custom',                
 navigationStyle:  'custom', }) })                                              
                                                                                

使用 worklet​                                                                    

在 Taro 中使用 worklet 需要首先开启半编译，开启方法见：半编译模式使用方法。     

使用 worklet 动画能力时确保以下两项：详见 worklet 动画                          

 • 确保开发者工具右上角 > 详情 > 本地设置里的 将 JS 编译成 ES5 选项被勾选上     
   (代码包体积会少量增加)                                                       
 • worklet 动画相关接口仅在 Skyline 渲染模式下才能使用                          

示例：                                                                          

config/index.js                                                                 

                                                                                
 {{ mini: { mini:  { experimental: { experimental:  { compileMode: true         
 compileMode:  true  }  }  }  } } }                                             
                                                                                

pages/index/behavior.js                                                         

                                                                                
 const behavior = Behavior({const  behavior =  Behavior({ methods: { methods:   
 { onScrollUpdate(){ onScrollUpdate(){ "worklet";  "worklet";                   
 console.log('onScrollUpdateWorklet')  console. log('onScrollUpdateWorklet')    
 },  },  onGesture(evt) { onGesture(evt)  { 'worklet';  'worklet';  if          
 (evt.state === 2) { if  (evt. state  ===  2)  { this._offset.value +=          
 evt.deltaX;  this. _offset. value  +=  evt. deltaX;  }  }  }  }  }  } }) })    
 export default behavior export  default  behavior                              
                                                                                

pages/index/index.jsx                                                           

                                                                                
 import { View, ScrollView, PanGestureHandler } from "@tarojs/components";      
 import  { View,  ScrollView,  PanGestureHandler  }  from                       
 "@tarojs/components"; import Taro, { useLoad } from "@tarojs/taro"; import     
 Taro,  { useLoad }  from  "@tarojs/taro"; import behavior from "./behavior";   
 import  behavior  from  "./behavior";  Index.behaviors = [behavior]; Index.    
 behaviors  =  [behavior];  export default function Index() { export  default   
 function  Index()  { useLoad(() => { useLoad(()  =>  { const { page } =        
 Taro.getCurrentInstance();  const  { page }  =  Taro. getCurrentInstance();    
 if (page) { if  (page)  { const offset = Taro.worklet.shared(0);  const        
 offset =  Taro. workl                                                          
                                                                                


──────────────────────── 1 extracted, 0 failed | 0.01s ─────────────────────────
