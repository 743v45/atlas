
  https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.htm
l
  developers.weixin.qq.com (6,263 chars)


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

                                     # 网络                                     

在小程序/小游戏中使用网络相关的 API 时，需要注意下列问题，请开发者提前了解。    

# 1. 服务器域名配置                                                             

每个微信小程序需要事先设置通讯域名，小程序只可以跟指定的域名进行网络通信。包括普
通 HTTPS                                                                        
请求（wx.request）、上传文件（wx.uploadFile）、下载文件（wx.downloadFile) 和    
WebSocket 通信（wx.connectSocket）。                                            

从基础库 2.4.0 开始，网络接口允许与局域网 IP 通信，但要注意 不允许与本机 IP     
通信。                                                                          

从 2.7.0 开始，提供了 UDP 通信（wx.createUDPSocket)。                           

从 2.18.0 开始，提供了 TCP                                                      
连接（wx.createTCPSocket)，只允许与同个局域网内的非本机 IP                      
以及配置过的服务器域名通信。                                                    

如使用微信云托管作为后端服务，则可无需配置通讯域名（在小程序内通过 callContainer
和 connectContainer 通过微信私有协议向云托管服务发起 HTTPS 调用和 WebSocket     
通信）。                                                                        

# 配置流程                                                                      

服务器域名请在 「小程序后台-开发-开发设置-服务器域名」                          
中进行配置，配置时需要注意：                                                    

 • 域名只支持 https (wx.request、wx.uploadFile、wx.downloadFile) 和 wss         
   (wx.connectSocket) 协议；                                                    
 • 域名不能使用 IP 地址（小程序的局域网 IP 除外）或 localhost；                 
 • 对于 https 域名，可以配置端口，如 https://myserver.com:8080，但是配置后只能向
   https://myserver.com:8080 发起请求。如果向                                   
   https://myserver.com、https://myserver.com:9091 等 URL                       
   请求则会失败。如果不配置端口。如 https://myserver.com，那么请求的 URL        
   中也不能包含端口，甚至是默认的 443 端口也不可以。如果向                      
   https://myserver.com:443 请求则会失败。                                      
 • 对于 wss 域名，无需配置端口，默认允许请求该域名下所有端口。                  
 • 域名必须经过 ICP 备案；                                                      
 • 出于安全考虑，api.weixin.qq.com 不能被配置为服务器域名，相关 API             
   也不能在小程序内调用。 开发者应将 AppSecret                                  
   保存到后台服务器中，通过服务器使用 `getA                                     


──────────────────────── 1 extracted, 0 failed | 0.02s ─────────────────────────
