# 字幕/语音识别工具 · 选型设计树

> 叶子格式 `- 叶：[名](slug/) verdict`，build 校验与 meta 一致（RULES.md 第 8 节）。

## 根问题

有没有好用的识别视频音频字幕的工具，免费或本地可部署？（2026-08-12~18 会话；约束逐步收敛：准确率优先、16GB Apple Silicon Mac、启停方便、素材中英混杂主要中文）

## 分叉与决策

### D1 云 API 还是本地？

- 豆包 Seed-ASR：中文错误率比传统低 10-40%、热词/方言、1.8 元/小时——但字节从不开源权重，本地部署不存在。
- 决策：免费+本地是硬约束 → 云 API 列为付费备选。
- 叶：[豆包 Seed-ASR](seed-asr/) trial

### D2 中文准确率谁最高？

- CER 榜（官方口径分列，见 comparison）：FireRedASR2S 普通话 2.89% SOTA > Qwen3-ASR 3.76% > Fun-ASR-Nano 4.55%（幻觉重）> SenseVoice 7.81% > Whisper-large-v3 ~11% > large-v3-turbo 21.71%（中文别用）。
- 叶：[FireRedASR](fireredasr/) adopt（用户实际部署 AED-L）· [FunASR](funasr/) adopt · [SenseVoice](sensevoice/) adopt · [Qwen3-ASR](qwen3-asr/) trial

### D3 16GB 内存约束？

- FireRedASR-LLM（8.3B，含 Qwen2-7B）官方推荐 32GB+——16GB 能跑但紧张，出局；AED-L 落地（CPU 10.6s/13.5s、内存 880MB）。
- 落选节点：[faster-whisper](faster-whisper/) hold（维护放缓 9 个月 + Mac 仅 CPU 慢 3x）

### D4 中英混杂短板？

- AED 是纯声学模型：英文专有名词弱（实测 "FireRedASR"→"FIRE RATE ASR"，纯中文 0 错）。
- 升级路径：FireRedASR2S v2（2026-02）原生 code-switching + 词级时间戳——恰好补板（Mac 实测待验证）。

### D5 Whisper 生态怎么定位？

- 英文/多语言基线仍强（whisper.cpp ⭐53k Mac 最快），但中文场景 CER 双位数。
- 落选节点：[Whisper](whisper/) hold（中文场景）· 叶：[whisper.cpp](whisper-cpp/) trial · [WhisperX](whisperx/) trial · [Buzz](buzz/) trial（Mac GUI）

### D6 交付形态？

- 用户把 fireredasr-ui（第三方 WebUI，停更 18 个月）深度改造成 dispatcher 队列服务（5079/OpenAI 兼容 API/180s 空闲卸载/caddy 反代）——「停更但被深度改造」是 hold 的特例注记。
- 叶：[fireredasr-ui](fireredasr-ui/) hold

### 部署坑（实测沉淀）

Mac Docker 无 Metal GPU→原生 pip；modelscope 限速 195KB/s→aria2 16 连接 12.6MB/s；AED 单条上限 60s（WebUI 30s 切片）。

## 决策矩阵一致性

加权排序：funasr 103 > sensevoice 101 > fireredasr 94——「最好用」与「最准」的排序差异即矩阵与 verdict 分工。
