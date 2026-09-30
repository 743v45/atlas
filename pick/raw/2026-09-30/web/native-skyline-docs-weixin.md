
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/mig
ration/compatibility.html
  developers.weixin.qq.com (3,733 chars)

小程序                                                                          

 • 小程序                                                                       
 • 小游戏                                                                       
 • 公众号                                                                       
 • 服务号                                                                       
 • 开放平台                                                                     
 • 企业微信                                                                     
 • 微信支付                                                                     
 • 视频号                                                                       
 • 微信小店                                                                     
 • 智能对话                                                                     
 • 腾讯小微                                                                     
 • 教育平台                                                                     

在小程序下暂无结果，查看其它业务相关内容 >                                      

 •  • 行业能力                                                                  
    • 商业能力                                                                  
    • 多端能力                                                                  
    • 服务市场                                                                  
    • 城市服务                                                                  
    • 付费能力                                                                  
    • 拓展能力                                                                  
 •  • 云开发                                                                    
    • 云托管                                                                    
 • AI 能力                                                                      

[开发](javascript:;)                                                            

取消                                                                            

 • [指南](javascript:;)                                                         

                                     # 兼容                                     

Skyline 目前各端的支持情况见下表                                                

                                          
 平台        支持版本              备注   
 ──────────────────────────────────────── 
 安卓        8.0.33+               支持   
 iOS         8.0.34+               支持   
 开发者工具  Stable 1.06.2307260+  支持   
 Windows     未支持                规划中 
 Mac         未支持                规划中 
 企业微信    未支持                开发中 
                                          

可以看出，小程序若不是只跑在最新版本的微信移动端，则需要关注兼容 WebView        
的情况，这里我们整理了一些兼容方法及常见的兼容问题                              

# 兼容方法                                                                      

# 样式兼容                                                                      

Skyline 与 WebView                                                              
的主要差异在于样式支持度，因此大部分兼容工作主要集中在样式适配，这里可以利用开发
者工具的 WXML 调试工具，通过定位到有问题的节点，分析对应的样式兼容性。          

对于具体样式兼容的策略上，由于 Skyline 中部分样式的默认值与 web                 
不同，因使用默认值而省略的样式需要显示指定，如 flex-direction:                  
row，但此处更推荐开启默认 Block 布局和默认 ContentBox 盒模型，默认值处理与 web  
更接近，其他更多信息，详见 Skyline WXSS 样式支持与差异                          

# 根据不同 renderer 兼容                                                        

有时，单纯用 WXML 和 WXSS 无法做好兼容时，可以通过 JS 判断是否 Skyline          
以使用不同的 WXML 或 WXSS 实现。我们在页面或组件实例增加了 renderer 成员，取值为
webview 或 skyline，参考以下代码                                                

                                                                                
 <view class="position {{renderer}}"><view< class ="position {{renderer}}" = "  
 ">view> view> view>                                                            
                                                                                

                                                                                
 Page({data:{renderer: 'webview'}, onLoad(){this. setData({renderer:            
 this.,})},})                                                                   
                                                                                

# 常见的兼容问题                                                                

 • Skyline 一定需要应用到整个小程序吗？                                         
   不需要，Skyline 支持按页面粒度或分包粒度开启，可渐进式迁移。                 
 • 开启 Skyline 后布局错乱                                                      
   一般是默认 flex 布局及 box-sizing 默认为 border-box 导致，推荐开发者开启默认 
   Block 布局、默认 ContentBox 盒模型。                                         
 • 切换 Skyline后，为什么顶部原生导航栏消失？                                   
   不支持原生导航栏，需自行实现，或使用 weui 组件库。推荐页面配置加上           
   "navigationStyle": "custom" 以保持与 WebView 兼容                            
 • 切换 Skyline 后，为什么 position: absolute 相对坐标不准确？                  
   在 Skyline 模式下，所有节点默认是 relative，可能导致 absolute                
   相对坐标不准。建议开发者修改节点 position 或者修改相对坐标。                 
 • 因不支持 inline 布局导致，需改成 flex 布局实现，或者使用 text                
   组件包裹多段文本，而不是用 view 组件包裹，也可以使用 span 组件包裹 te        


──────────────────────── 1 extracted, 0 failed | 0.02s ─────────────────────────
