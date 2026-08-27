---
date: 2026-08-27
topic: Serverless GPU 生意账
related:
  - ../asked/items/serverless-gpu-business/
原始会话: ~/.claude/projects/-Users-taevas/55c6c0ea-44cc-426f-94de-70e73e8a61b0.jsonl
---

# 2026-08-27 · Serverless GPU 生意账

从闲聊 MiniMax 免费活动(GMI minimax-week)一路聊成一门生意账:用户设想「模型放一个地方、机器放一个地方、计算就是调度」,AI 点破这就是 Serverless GPU / 存算分离推理(Modal、RunPod Serverless、Baseten、Replicate、Fal.ai 整个行业),并给三个工程修正(权重是冷启动时拉不是每请求拉、KV cache 有状态所以要会话亲和调度、统一调度平台即 Replicate 产品形态),落盘 ~/docs/model-storage-compute-split.html。

对上 H3(MiniMax H3,33B 全模态、视频直出、量化生态猛)后算账:自部署 serverless 4090 单条 780P+超分视频成本约 0.66 元,官方 API 同规格约 9 元——贩子生意的全部秘密是自部署把成本压到七毛以下。关键纠偏:AI 主动核查发现 GMI 免费名单是 M3/M2.7/Speech/Music,**不含 H3 视频**,免费活动对视频生意白嫖不到。风险四条比账单更容易杀死生意(AIGC 内容标识合规、endpoint 防刷须挡 one-api/new-api 网关、外币支付门槛有国内替代、scale-to-zero 冷启动延迟)。用户问「卖不掉咋整」,AI 给出本条最核心的判断:**GPU 不是资产是期权**——scale-to-zero 下卖不掉月沉没约 100 元(权重网络盘+网关小鸡)随时归零;出路四条按推荐排序(第一个客户是自己/卖成品不卖 API/to B 电商商家/免费换启动),止损线「4 周+200 元没首单→关掉」。行动第 0 步:花 20 块实测生成时长,那是整个账的地基。

讲义恢复为 asked/items/serverless-gpu-business。
