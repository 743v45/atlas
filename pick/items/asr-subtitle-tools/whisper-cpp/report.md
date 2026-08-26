# whisper.cpp

> **TL;DR**：C/C++ Whisper 运行时、Apple Silicon 速度冠军（Metal/CoreML，2026 年 Mac 横评 large-v3 约 10x 实时）：追求 Mac 本地批量转写速度的壳，中文准确率仍受 Whisper 模型上限拖累。

- **结论**：trial 试用（英文/多语言素材 + Mac 本地速度优先场景）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 持续发版（仓库最近推送 2026-08-25，日更节奏） | [1] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/ggerganov/whisper.cpp（⭐53,196，gh 2026-08-27） | [1] |
| 维护活跃度 | 极活跃（ggerganov/llama.cpp 同作者的姊妹项目；Core ML/Metal/Vulkan/OpenCL 后端齐备） | [1] |

## 为什么值得试用

1. **Apple Silicon 上最快的 Whisper 路线**：Metal + Core ML GPU 内核，2026 年 Mac 开源 STT 对比称其对几乎所有模型尺寸最快——tiny~medium 近实时，large-v3 约 10 倍实时（Speakhapi 2026）[2]。
2. **零依赖单二进制**：C/C++ 自包含，无 Python/torch 环境，量化（GGML/GGUF 系）模型随取随用；服务器（whisper-server/whisper-cli）与 examples 齐全 [1]。
3. **社区事实上的「壳标准」」**：与 SenseVoice-GGUF（llama.cpp 风格运行时）同构的部署形态，Mac 上做批处理脚本的默认底座 [1] [3]。

## 为什么不是 adopt

- **中文准确率继承 Whisper 上限**（普通话平均 CER 9.86%，见 [whisper](../whisper/report.md)）：它是「壳」不是「模型」，换不到更好的中文结果 [2]。
- MLX 路线在 8bit 量化下可比 whisper.cpp 再快 30-40%（未量化 large 则略慢）——速度桂冠并非绝对，见横评速度表 [2]。

## 对比

与 faster-whisper：Mac 上全面占优（后者 macOS 仅 CPU 且慢约 3 倍）[2]。与 Buzz：whisper.cpp 是无 GUI 的引擎层，Buzz 这类 GUI 常以其为底座。逐维度见 `../comparison.md`。

## 风险与注意

- 时间戳为段级，词级对齐/说话人分离需另配（WhisperX 补位，见 [whisperx](../whisperx/report.md)）。
- 中文错字率敏感的场景，速度优势不构成采用理由（准确率优先）。

## 来源

1. whisper.cpp 官方仓库 — https://github.com/ggerganov/whisper.cpp（访问 2026-08-27）
2. Open Source Speech to Text on Mac: 2026 Comparison（Speakhapi，2026）— https://speakhapi.com/blog/open-source-speech-to-text-mac（访问 2026-08-27）
3. SenseVoice 官方仓库（GGUF 单文件运行时，同构形态）— https://github.com/FunAudioLLM/SenseVoice（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录：Mac 速度冠军运行时，受限于 Whisper 模型中文上限 |
