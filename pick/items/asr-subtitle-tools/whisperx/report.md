# WhisperX

> **TL;DR**：基于 faster-whisper 的研究级框架：词级时间戳强制对齐 + 说话人分离一步到位，是「字幕轴精修/多人访谈」的独占能力；中文准确率继承 Whisper 上限，速度换精度。

- **结论**：trial 试用（词级时间轴 + 说话人分离的刚需场景）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 持续发版（仓库最近推送 2026-07-13） | [1] |
| 许可证 | BSD-2-Clause | [1] |
| 仓库 | https://github.com/m-bain/whisperX（⭐23,761，gh 2026-08-27） | [1] |
| 维护活跃度 | 活跃（年内有推送；学术出身，社区驱动） | [1] |

## 为什么值得试用

1. **phoneme 级强制对齐**：转写后用 wav2vec2 对齐产出**词级时间戳**——字幕断句/轴精修、剪辑对齐的刚需，原生 Whisper 只有段级不稳定时间戳（官方 README 主张，2026-07 快照）[1]。
2. **说话人分离一步到位**：集成 pyannote，多人访谈/会议素材直接出「谁在何时说了什么」[1]。
3. **批处理效率**：faster-whisper 底座（GPU 服务器向）+ 批量推理，长音频吞吐好（2026 年速度测试口径）[3]。

## 为什么不是 adopt

- **中文准确率继承 Whisper 上限**（普通话平均 9.86%，见 [whisper](../whisper/report.md)）——中文素材它只是「时间轴工具」，文字质量不如 FireRedASR2/SenseVoice。
- **对齐质量以源转写质量为上限**：转写错了，对齐也锁死在错的词上。
- 依赖链长（faster-whisper + pyannote + wav2vec2 模型），与 faster-whisper 的维护状态连带（见 [faster-whisper](../faster-whisper/report.md)）[2]。

## 对比

独占位是「Whisper 系模型 + 词级轴 + 说话人」三合一；FireRedASR2-AED 现已原生词级时间戳（中文更准，见 [fireredasr](../fireredasr/report.md)），Qwen3-ForcedAligner 提供另一种对齐路线——中文场景下这两者是更强替代。逐维度见 `../comparison.md`。

## 风险与注意

- pyannote 说话人模型需接受其许可条款（非商用条款随版本变化）——商用前核验，**待验证**。
- GPU 服务器路径成熟；Mac 本地（CPU faster-whisper 底座）速度受限（Speakhapi 2026）[2 引述口径]。

## 来源

1. WhisperX 官方仓库 — https://github.com/m-bain/whisperX（访问 2026-08-27）
2. faster-whisper 官方仓库（依赖关系）— https://github.com/SYSTRAN/faster-whisper（访问 2026-08-27）
3. Whisper.cpp vs faster-whisper 2026: STT Speed Test（PromptQuorum，2026）— https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录：词级时间轴+说话人分离独占位 |
