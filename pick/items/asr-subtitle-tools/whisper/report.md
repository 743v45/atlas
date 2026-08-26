# OpenAI Whisper

> **TL;DR**：多语言基线但中文明显掉队：官方口径 large-v3 普通话平均 CER 9.86%（约为 FireRedASR2 的 3.4 倍）、turbo 更差，字幕主力中文场景不建议新采用；价值在英文/小语种覆盖与庞大生态。

- **结论**：hold 观望（中文字幕场景不推荐新采用；英文/多语言场景仍是合理基线）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | large-v3 / large-v3-turbo（2023-11 系列，此后未出新一代模型）；仓库最近推送 2026-07-28 | [1] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/openai/whisper（⭐107,968，gh 2026-08-27——ASR 生态第一体量） | [1] |
| 维护活跃度 | 仓库仍收 PR/issue，但模型本体两年余未迭代（观察 2026-08-27） | [1] |

## 为什么不选（中文场景）

1. **中文准确率差一个量级**：第三方统一口径（FireRedASR v1 官方对比表，2025-01）large-v3 普通话平均 CER 9.86%——aishell1 5.14%、ws_meeting 高达 18.87%；同期 FireRedASR-LLM 3.05%、Paraformer-Large 4.56% [2]。历史调研亦引用 turbo 中文 CER 21.71% 的横评数据（腾讯云 2026-03 汇总口径）[3]。
2. **自回归架构慢**：large 档逐 token 生成，同参数量下显著慢于非自回归的 SenseVoice（15x 差距，官方口径）[4]；Mac 上须靠 whisper.cpp/MLX 等运行时加速（见 [whisper-cpp](../whisper-cpp/report.md)）。
3. **中文专属问题**：历史会话与社区反馈中的同音字/术语错误集中（历史调研 2026-08-24）；无热词机制，专有名词纠错只能靠后处理。

## 仍然值得知道的（为什么它还是「基线」）

- **99+ 语言覆盖无可替代**：小语种素材只有 Whisper 系能兜住 [1]。
- **生态是所有运行时/GUI 的公共底座**：whisper.cpp、faster-whisper、WhisperX、Buzz 全部兼容其模型格式——「模型」与「壳」可独立替换（见横评 `../comparison.md` 层次分解）。

## 对比

中文场景被 FireRedASR2/SenseVoice/Qwen3-ASR 全面压制；英文/多语言场景仍是默认起点，配 whisper.cpp（Mac 速度）或 WhisperX（时间轴精度）使用。逐维度见 `../comparison.md`。

## 风险与注意

- OpenAI 模型迭代已停滞（模型本体两年余无新代），改进主要发生在社区运行时层 [1]。
- hold 限定于「中文为主的字幕场景」；若素材以英文为主，本条目应重新评估（此时它是 trial）。

## 来源

1. OpenAI Whisper 官方仓库 — https://github.com/openai/whisper（访问 2026-08-27）
2. FireRedASR v1 官方评测表（Whisper-Large-v3 平均 9.86%、ws_meeting 18.87%）— https://github.com/FireRedTeam/FireRedASR（访问 2026-08-27）
3. 腾讯云开发者社区横评（CoovallyAIHub，2026-03-20）— https://cloud.tencent.com/developer/article/2642961（访问 2026-08-27）
4. SenseVoiceSmall HF 官方模型卡（15x 速度口径）— https://huggingface.co/FunAudioLLM/SenseVoiceSmall（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录：中文场景准确率掉队（历史会话 2026-08-24 同结论） |
