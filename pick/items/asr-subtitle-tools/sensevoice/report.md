# SenseVoice

> **TL;DR**：通义 234M 非自回归小模型：10 秒音频 70ms 出结果（官方口径比 Whisper-Large 快 15 倍），中粤英日韩五语+情感/事件检测，2026-06 起有 llama.cpp 单文件 GGUF 运行时（q8 仅 254MB）——轻量本地字幕/实时场景首选模型。

- **结论**：adopt 推荐
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | SenseVoiceSmall（2024-07 开源）；GGUF/llama.cpp 运行时 2026-06；仓库最近推送 2026-08-18 | [1] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/FunAudioLLM/SenseVoice（⭐9,150，gh 2026-08-27） | [1] |
| 维护活跃度 | 活跃：2026 年连续更新（5 月 diarization 组合、6 月 GGUF、7 月时间戳/语言元数据跟随 FunASR 发版）（观察 2026-08-27） | [1] |

## 为什么选

1. **推理速度断层领先**：非自回归端到端架构，10 秒音频仅需 70ms——官方口径比 Whisper-Large 快 15 倍、比 Whisper-Small 快 5 倍以上（HF 官方模型卡/论文口径，2024-07）[2]。字幕批量回填、近实时转写都够用。
2. **中文+粤语在内的五语覆盖**：普通话、粤语、英语、日语、韩语，官方基准称中文与粤语识别优于 Whisper（SenseVoice 仓库基准图，2024-07）[1]；历史会话横评口径下 AISHELL-1 CER 约 3.0%（腾讯云 2026-03 引 SenseVoice 仓库柱状图近似值）[3]。
3. **字幕场景的增值输出**：附带语音情感识别（官方称持平或超过当时最佳情感模型）与音频事件检测（bgm/掌声/笑声/咳嗽等）——做视频字幕时可顺带标记非语音段 [1]。
4. **2026-06 起有单文件运行时**：llama.cpp/GGUF 路线，whisper.cpp 式自包含二进制、内置 VAD、运行期无 Python，q8 量化模型仅约 254MB 且精度不变（官方口径）——Mac/边缘设备零依赖部署 [1]。
5. **准确率档位明确**：SenseVoice-L 1.6B 普通话平均 CER 4.47%（FireRedASR v1 官方对比表，2025-01）[4]——不如 FireRedASR2（2.89%）但显著优于 Whisper-Large-v3（9.86%）[4]；Small 版更轻更快，精度略低于 L 版。

## 对比

与 FireRedASR2 是「速度/轻量 vs 极致准确」的对子：素材以纯普通话为主且要最低错字率选 FireRedASR2；要五语覆盖、情感/事件标签、单文件部署或高吞吐选 SenseVoice。经 FunASR 调用可补齐标点/说话人/时间戳流水线（见 [funasr](../funasr/report.md)）。逐维度见 `../comparison.md`。

## 风险与注意

- **普通话准确率非第一**：比 FireRedASR2 落后约 1-1.6 个百分点（不同口径，[3] [4]）；错字率敏感的纯中文场景不是最优解。
- 说话人分离不是模型本体能力，须 FunASR 组合 FSMN-VAD + CAM++ 流水线（2026-05 公告，需源码安装）[1]。
- 研究口径（5 万小时/50+ 语言的大模型版 SenseVoice-Large）与**已发布 checkpoint**（Small，5 语）范围不同，选型时勿混淆 [1]。
- GGUF 运行时发布较新（2026-06），Mac 上长期稳定性待验证。

## 来源

1. SenseVoice 官方仓库（What's News/Benchmarks/能力边界注记）— https://github.com/FunAudioLLM/SenseVoice（访问 2026-08-27）
2. SenseVoiceSmall HF 官方模型卡（70ms/10s、15x/5x 速度口径）— https://huggingface.co/FunAudioLLM/SenseVoiceSmall（访问 2026-08-27）
3. 腾讯云开发者社区横评（CoovallyAIHub，2026-03-20；AISHELL-1 ≈3.0% 为其对仓库柱状图的近似读数）— https://cloud.tencent.com/developer/article/2642961（访问 2026-08-27）
4. FireRedASR v1 官方评测表（SenseVoice-L 4.47%、Whisper-Large-v3 9.86%）— https://github.com/FireRedTeam/FireRedASR（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录：轻量/多语/实时路线首选模型 |
