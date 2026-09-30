
  https://developers.weixin.qq.com/doc/oplatform/openApi/miniprogram-management/
domain-management/api_modifyserverdomaindirectly.html
  developers.weixin.qq.com (4,850 chars)

开放平台                                                                        

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

在开放平台下暂无结果，查看其它业务相关内容 >                                    

 • 第三方平台 API                                                               

[开放平台](javascript:;)                                                        

EN                                                                              

取消                                                                            

 • [第三方平台 API](javascript:;)                                               

                           # 快速配置小程序服务器域名                           

▌ 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考 
▌ 接口调用指南。                                                              

 • 该接口用于配置小程序服务器域名，不再需要先将域名配置到第三方平台，可通过该接 
   口直接进行配置到授权小程序。但是，配置成功后，需要发布上线后才会真正生效通过 
   该接口配置的域名。另外，开发者可通过接口获取发布后生效服务器域名列表看生效情 
   况                                                                           
 • 使用之前请详细查看代开发的小程序域名配置说明                                 
 • 使用过程中如遇到问题，可在开放平台服务商专区发帖交流。                       

# 1. 调用方式                                                                   

# HTTPS 调用                                                                    

# 云调用                                                                        

 • 本接口不支持云调用。                                                         

# 第三方调用                                                                    

 • 该接口所属的权限集 id 为：18                                                 
 • 服务商获得其中之一权限集授权后，可通过使用 authorizer_access_token           
   代商家进行调用，具体可查看 第三方调用 说明文档。                             

# 2. 请求参数                                                                   

# 查询参数 Query String Parameters                                              

                                                                          
 参数名        类型    必填  说明                                         
 ──────────────────────────────────────────────────────────────────────── 
 access_token  string  是    接口调用凭证，可使用 authorizer_access_token 
                                                                          

# 请求体 Request Payload                                                        

                                                                                
 参数名           类型    必填  说明                                            
 ────────────────────────────────────────────────────────────────────────────── 
 action           string  是    操作类型                                        
 requestdomain    array   是    request 合法域名；当 action 是 get 时不需要此字 
 wsrequestdomain  array   是    socket 合法域名；当 action 是 get               
                                时不需要此字段                                  
 uploaddomain     array   是    uploadFile 合法域名；当 action 是 get           
                                时不需要此字段                                  
 downloaddomain   array   是    downloadFile 合法域名；当 action 是 get         
                                时不需要此字段                                  
 udpdomain        array   是    udp 合法域名；当 action 是 get 时不需要此字段   
 tcpdomain        array   是    tcp 合法域名；当 action 是 get 时不需要此字段   
                                                                                

# 3. 返回参数                                                                   

# 返回体 Response Payload                                                       

                           
 参数名   类型    说明     
 ───────────────────────── 
 errcode  number  错误码   
 errmsg   string  错误信息 
                           

# 4. 注意事项                                                                   

 • 由于该接口是直接为小程序账号配置服务器域名，所以相关的规则限制对齐普通小程序 
   ，详情可查看小程序网络使用说明                                               
 • 由于当前有两种方式可以为第三方代开发小程序配置域名，在调用该接口之前，请先查 
   看详细的业务逻辑说明，以免出现误操作。详情可查看代开发的小程序域名配置说明   
 • 使用该接口为一个小程序配一次即可，下次审核代码不用重复set配置之前已配置过的域


──────────────────────── 1 extracted, 0 failed | 0.01s ─────────────────────────
