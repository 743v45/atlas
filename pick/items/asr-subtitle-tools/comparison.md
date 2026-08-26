# 字幕/语音识别工具横评（ASR）

> 调研时间 2026-08-27，方法 tvly（Tavily）+ gh（GitHub CLI 一手数据）+ 本机实测记录（2026-08-24 部署会话）。
> 核心命题：**视频/音频转字幕（ASR）选什么**——免费、本地可部署、中文准确率优先。源头问题是「先选模型，再选壳」：模型决定准确率上限，壳（工具链/运行时/GUI/API）决定好不好用。

**场景注记**：本类目解决「没有现成字幕的音视频」的上游转写。用户已有的两条相邻链路不在此列——飞书妙记（云服务，会议纪要/逐字稿）与 subtitle-collector（B 站/YouTube **已有字幕**采集，不做 ASR）；ASR 是它们的上游补充而非替代。

## 场景速配（TL;DR 矩阵）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 中文为主 + 准确率优先（本机现役） | [FireRedASR](fireredasr/report.md) | 普通话平均 CER 2.89% 开源第一；v2 原生中英混杂+词级时间戳 |
| 要开箱即用的本地字幕服务 | [FunASR](funasr/report.md) | WebUI/Docker/SRT/说话人一条龙，⭐20k 日更 |
| 轻量/中粤英日韩/实时转写 | [SenseVoice](sensevoice/report.md) | 10s 音频 70ms；GGUF 单文件 254MB |
| 多语言 + 22 中文方言 | [Qwen3-ASR](qwen3-asr/report.md) | 30 语言，1.7B 即 3.76%，transformers 原生 |
| 英文/小语种 + Mac 本地最快 | [whisper.cpp](whisper-cpp/report.md) | Metal/CoreML，large-v3 约 10x 实时 |
| 字幕轴精修 + 说话人分离 | [WhisperX](whisperx/report.md) | 词级强制对齐 + pyannote 独占组合 |
| 零命令行 GUI 懒人 | [Buzz](buzz/report.md) | 装 App 拖文件出 SRT/VTT |
| 可接受云 API + 热词纠错 | [Seed-ASR](seed-asr/report.md) | 闭源顶配 3.69%，1.8 元/小时 |

## 一、先选模型，再选壳：四层分解

| 层 | 回答的问题 | 本类目条目 | 特征 |
|---|---|---|---|
| 模型层 | 识别准不准 | whisper、sensevoice、fireredasr、qwen3-asr、seed-asr | 决定准确率上限；中文/多语言分野在此层 |
| 工具链层 | 怎么拼成服务 | funasr | VAD/ASR/标点/说话人流水线 + Docker/OpenAI 端点 |
| 运行时层 | 在什么硬件上跑得快 | whisper-cpp、faster-whisper（观察：sherpa-onnx、MLX） | 同一模型换运行时，速度差 3-10 倍 |
| 壳层 | 人怎么用 | buzz、fireredasr-ui、whisperx | GUI/WebUI/框架；不改变模型上限 |

各层是组合关系而非竞争：典型组合如「SenseVoice 模型 + FunASR 接口 + sherpa-onnx 部署到端侧」（腾讯云 2026-03 横评的分层口径 [3]）。选型错误多发生在「拿壳的问题去换模型」（为 GUI 便利接受 Whisper 的中文 9.86%）或反之。

## 二、属性对比矩阵

| 维度 | FireRedASR | FunASR | SenseVoice | Qwen3-ASR | Whisper | whisper.cpp | faster-whisper | WhisperX | Buzz | fireredasr-ui | Seed-ASR |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 形态 | 模型+官方 CLI | 工具链+Docker 服务 | 模型（GGUF/ONNX） | 模型（transformers/vLLM） | 模型+PyTorch 库 | C/C++ 运行时 | Python（CT2） | Python 框架 | 桌面 GUI | WebUI（Flask） | 云 API |
| 中文 CER（普通话平均） | **2.89%**（v2-LLM）/ 3.05%（AED） | 4.47-4.56%（经其模型 SenseVoice-L/Paraformer） | ≈3.0%（AISHELL-1，L 版 4.47% 平均） | 3.76% | **9.86%（弱）** | 同 Whisper 上限 | 同 Whisper 上限 | 同 Whisper 上限 | 同 Whisper 上限 | 继承 v1-AED 3.18% | 3.69%（顶配） |
| 中英混杂 | **✅ v2 原生 code-switching** | ⚠️ 靠模型 | ✅ 五语混说 | ✅ 30 语言 | ✅ 99+ 语言 | 同 Whisper | 同 Whisper | 同 Whisper | 同 Whisper | ❌ v1-AED 弱（实测） | ✅ |
| 词级时间戳 | **✅ v2-AED 原生** | ✅（CTC/VAD 分段） | ✅（CTC 对齐） | ✅（ForcedAligner） | ⚠️ 段级不稳 | ⚠️ 段级 | ⚠️ 段级 | **✅ 强制对齐** | — | ✅（SRT 输出） | ✅ |
| 本地部署 | ✅ CPU 实测（Mac 16GB） | ✅ pip/Docker | ✅ **单文件 254MB** | ✅ 服务器向 / Mac 待验证 | ✅ | ✅ Metal/CoreML | ✅（Mac 仅 CPU） | ✅ | ✅ | ✅（本机现役） | ❌ 无权重 |
| 速度 | 中（CPU ~1.3x 实时实测） | 快（取决于模型） | **70ms/10s** | 快（0.6B 高吞吐） | 慢（large 自回归） | **Mac 最快 ~10x** | GPU 快 / Mac 慢 3x | 快+对齐开销 | 中 | 中 | 快 |
| 许可 | Apache-2.0 | MIT | MIT | Apache-2.0 | MIT | MIT | MIT | BSD-2-Clause | MIT | Apache-2.0 | 商业闭源 |
| star（gh 2026-08-27） | 653（v2）/ 1,971（v1） | 20,035 | 9,150 | 3,422 | 107,968 | 53,196 | 25,097 | 23,760 | 21,143 | 88 | —（闭源） |
| 最近推送（gh 2026-08-27） | 2026-06-02 | **2026-08-26** | 2026-08-18 | 2026-06-26 | 2026-07-28 | **2026-08-25** | 2025-11-19 ⚠️ | 2026-07-13 | 2026-08-23 | 2025-02-24 ⚠️ | 商业持续 |

（准确率口径见下节注；同列「同 Whisper 上限」= 壳不改变模型准确率。）

## 决策矩阵（加权）

<!--gen:decision-matrix-->

## 三、准确率数据表

### 统一口径 A：FireRedASR2S 官方 24 测试集对比（2026-02，同一方测试）

| 模型 | AISHELL-1 | AISHELL-2 | WenetSpeech net | WenetSpeech meeting | **普通话平均** | 方言平均（19 集） | 全 24 集 |
|---|---|---|---|---|---|---|---|
| FireRedASR2-LLM（开源） | 0.64 | 2.15 | 4.44 | 4.32 | **2.89** | **11.55** | **9.67** |
| FireRedASR2-AED（开源，1.1B 档） | **0.57** | 2.51 | 4.57 | 4.53 | 3.05 | 11.67 | 9.80 |
| Doubao-ASR（闭源云 API） | 1.52 | 2.77 | 5.73 | 4.74 | 3.69 | 15.39 | 12.98 |
| Qwen3-ASR-1.7B（开源） | 1.48 | 2.71 | 4.97 | 5.88 | 3.76 | 11.85 | 10.12 |
| Fun-ASR 7.7B（**未开源**） | 1.64 | 2.38 | 6.85 | 5.78 | 4.16 | 12.76 | 10.92 |
| Fun-ASR-Nano-2512（开源，800M） | — | — | — | — | 4.55 | 15.07 | — |

（来源：FireRedASR2S 官方仓库评测表 [1]；CER%，越低越好。）

### 统一口径 B：FireRedASR v1 官方对比（2025-01，含 Whisper/SenseVoice/Paraformer）

| 模型 | 参数量 | AISHELL-1 | 普通话平均（4 集） |
|---|---|---|---|
| FireRedASR-LLM | 8.3B | 0.76 | **3.05** |
| FireRedASR-AED | 1.1B | 0.55 | 3.18 |
| Seed-ASR（豆包，未开源） | 12B+ | 0.68 | 3.33 |
| SenseVoice-L | 1.6B | 2.09 | 4.47 |
| Paraformer-Large | 0.2B | 1.68 | 4.56 |
| Qwen-Audio | 8.4B | 1.30 | 6.19 |
| Whisper-Large-v3 | 1.6B | 5.14 | **9.86**（ws_meeting 单项 18.87） |

（来源：FireRedASR v1 官方仓库评测表 [2]。）

**口径警告**：A/B 两表不可直接混比（测试年度与集合同）；SenseVoice-Small 的 AISHELL-1 ≈3.0% 是腾讯云 2026-03 横评对官方柱状图的近似读数 [3]，非统一口径。历史会话引用过的 SenseVoice-Small 7.81% / Paraformer 10.18% / Whisper-large-v3 ~11% / turbo 21.71% 系 FunASR 官方自设基准（2026-08-24 查询），口径另异——与其在不同测试集上的排名结论（B 表）方向一致但数值不可混用。**引用任何 CER 数字必须带它的表**。

### 本机实测（第一手）

| 项 | 结果（2026-08-24，16GB Apple Silicon Mac，CPU 路径 [4]） |
|---|---|
| FireRedASR-AED-L v1 纯中文段 | 0 错（13.5s 合成测试音） |
| 英文专名 | "FireRedASR"→"FIRE RATE ASR"、"Python Claude Docker"→"KISSON CLOTHES"（合成音放大误差） |
| 资源 | 内存 ~880MB，单核满载，10.6s/13.5s 音频 |
| v1-AED 限制 | 单条音频上限 60s（超时幻觉）→ 壳层 30s 自动切片绕过 |

## 四、速度数据表（Mac/本地视角）

| 方案 | 速度 | 测试方与时间 |
|---|---|---|
| whisper.cpp（Metal/CoreML） | large-v3 **约 10x 实时**；tiny-medium 近实时 | Speakhapi 2026 Mac 对比 [5] |
| MLX-whisper | 8bit 量化比 whisper.cpp 再快 30-40%；未量化 large 略慢 | Speakhapi 2026 [5] |
| faster-whisper | Mac 仅 CPU，比 whisper.cpp **慢约 3 倍**（large-v3 ≈3x 实时） | Speakhapi 2026 [5] |
| SenseVoice-Small | 10s 音频 **70ms**（15x Whisper-Large） | 官方 HF 模型卡，2024-07 口径 [6] |
| FireRedASR-AED v1（CPU） | ≈1.3x 实时（10.6s/13.5s） | 本机实测 2026-08-24 |
| FireRedASR2-AED（GPU） | TensorRT-LLM **12.7x 加速**（单卡 H20，vs PyTorch） | FireRedASR2S 官方，2026-02 [1] |
| Qwen3-ASR-0.6B | 128 并发下 2000x 吞吐（服务器口径） | Qwen3-ASR 官方，2026-01 [7] |

**修正记录**：历史会话（2026-08-24）曾采信「MLX-Whisper 比 whisper.cpp 快约 3x」的说法；2026 年 Mac 对比口径修正为「whisper.cpp 通常最快，MLX 仅在 8bit 量化下反超 30-40%」[5]。

## 五、GitHub 活跃度速查

<!--gen:activity-table-->

（FireRedASR 条目 stats 绑定 v2 仓库（FireRedASR2S，⭐653）；其 v1 仓库 1,971 star 但 2026-02 起停更。Seed-ASR 为商业闭源无 stats。选型门槛：模型/工具链 ≥1k star 或厂商背书，壳层按活跃度从严。）

## 六、选型决策树

```
要给视频/音频生成字幕（中文优先）
│
├── 素材以中文为主？
│   ├── 中英混杂 / 术语多 → FireRedASR2（v2 原生 code-switching；
│   │                        本机现役 v1-AED 的升级目标，英文专名是 v1 实测痛点）
│   ├── 纯普通话 + 极致准确 → FireRedASR2-LLM（2.89%）或 AED（3.05%，更轻）
│   ├── 要开箱即用服务（WebUI/Docker/SRT/说话人） → FunASR（+ SenseVoice/Paraformer）
│   ├── 要粤语/日语/韩语 + 情感事件标签 → SenseVoice
│   └── 方言口音重 + 多语言兜底 → Qwen3-ASR（22 中文方言）
│
├── 能接受云端 API？
│   ├── 要顶配准确率 + 热词纠专有名词 → 豆包 Seed-ASR（1.8 元/小时）
│   └── 隐私敏感 / 要免费 → 回本地路线
│
├── 素材以英文/小语种为主？
│   ├── Mac 本地要最快 → whisper.cpp（Metal/CoreML）
│   ├── 要词级时间轴 + 说话人 → WhisperX
│   └── 零命令行 → Buzz（GUI）
│
└── 要单文件/边缘/嵌入式部署？
    └── SenseVoice GGUF（q8 约 254MB，llama.cpp 式二进制）

前置问题：你在选「模型」还是「壳」？壳不改变准确率上限——
先按素材语言把模型定死，再按使用形态（服务/CLI/GUI）选壳。
```

务实组合（本机现状 + 演进）：**中文主力走 FireRedASR（现役 v1-AED 经定制 dispatcher 服务化，升级路径 v2 官方 CLI）；批量/多语走 FunASR+SenseVoice；英文素材临时处理用 whisper.cpp；飞书妙记覆盖会议纪要云场景、subtitle-collector 覆盖已有字幕采集——三者与本地 ASR 分工不重叠。**

## 七、观察名单（不建独立报告，含理由）

| 项 | 状态（观测 2026-08-27） | 备注 |
|---|---|---|
| sherpa-onnx | ⭐14,411，push 2026-08-25 | 端侧运行时（12 语言绑定，树莓派/鸿蒙）；SenseVoice/Paraformer 的边缘部署路径 |
| MLX-Whisper | ml-explore/mlx-examples ⭐8,906，push 2026-04 | Mac 原生 MLX 路线；8bit 量化下速度反超 whisper.cpp 30-40% [5] |
| Whisper-WebUI（jhj0517） | ⭐2,862，push 2025-12-29 | Docker 自托管 WebUI；推送放缓约 8 个月，暂观察 |
| Fun-ASR-Nano-2512 | 开源 800M，普通话 4.55% [1] | 通义新一代轻量；幻觉问题（历史调研提及）待独立验证 |
| Moonshine | ⭐约 7.3k | 27M 最轻端侧，但中文 CER ~36% 基本不可用 [3] |
| 飞书妙记 | 云服务 | 用户在用（会议纪要/逐字稿）；非本地 ASR，不入本类目条目 |
| subtitle-collector | 用户自建 | B 站/YouTube 已有字幕采集；非 ASR，是本类目的下游分流 |
| Whisper Notes / docker-whisper | 商业 GUI / 社区镜像 | 小众壳；前者的 SenseVoice 内置卖点已被 GGUF 路线覆盖 |

## 数据时间说明

本页所有 star / push / license 为 gh 2026-08-27 采集快照；CER 数据分别标注口径（FireRedASR2S 官方 2026-02 / FireRedASR v1 官方 2025-01 / 腾讯云 2026-03 / 官方模型卡 2024-07）；Mac 速度为 Speakhapi 2026 对比；价格为火山引擎 2026-08-24 查询；本机实测为 2026-08-24 记录。复用前先核对时效（RULES.md 第 3 节）。

### 来源

1. FireRedASR2S 官方仓库评测表 — https://github.com/FireRedTeam/FireRedASR2S（访问 2026-08-27）
2. FireRedASR v1 官方仓库评测表 — https://github.com/FireRedTeam/FireRedASR（访问 2026-08-27）
3. 中文语音识别该用谁？6 个开源模型 + 2 个配套工具（腾讯云开发者社区，CoovallyAIHub，2026-03-20）— https://cloud.tencent.com/developer/article/2642961（访问 2026-08-27）
4. Open-LLM-VTuber 文档（Mac CPU 路径）+ 本机部署实测记录（2026-08-24） — https://open-llm-vtuber.github.io/en/docs/user-guide/backend/asr/
5. Open Source Speech to Text on Mac: 2026 Comparison（Speakhapi，2026）— https://speakhapi.com/blog/open-source-speech-to-text-mac（访问 2026-08-27）
6. SenseVoiceSmall HF 官方模型卡 — https://huggingface.co/FunAudioLLM/SenseVoiceSmall（访问 2026-08-27）
7. Qwen3-ASR 官方仓库 — https://github.com/QwenLM/Qwen3-ASR（访问 2026-08-27）
