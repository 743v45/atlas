# faster-whisper

> **TL;DR**：CTranslate2 加速的 Whisper Python 实现：GPU 服务器上快且省内存，但 macOS 只能 CPU 且比 whisper.cpp 慢约 3 倍，仓库已 9 个月无提交（gh 2026-08-27）——新项目不建议入。

- **结论**：hold 观望（维护放缓 + Mac 场景被 whisper.cpp 压制）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 仓库最近推送 2025-11-19（截至今 9 个月余无提交） | [1] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/SYSTRAN/faster-whisper（⭐25,097，gh 2026-08-27） | [1] |
| 维护活跃度 | **放缓**：2025-11 后无推送；issue 积压情况待复核（观察 2026-08-27） | [1] |

## 为什么不选

1. **macOS 上无加速且更慢**：CTranslate2 在 macOS 无 GPU 后端，仅 CPU 运行；2026 年 Mac 对比称 large-v3 约 3 倍实时——比 whisper.cpp 慢约 3 倍（Speakhapi 2026）[2]。2026 年 STT 速度测试同口径印证（PromptQuorum 2026）[3]。
2. **维护节奏掉队**：9 个月余无提交（gh 2026-08-27 采集）[1]；下游壳（WhisperX、各类 WebUI）对其版本锁定容易踩坑——本项目本机部署记录中即出现过 `VadOptions` 参数变更导致的兼容报错（2026-08-24 本地部署经验）。
3. **中文准确率继承 Whisper 上限**（普通话平均 9.86%，见 [whisper](../whisper/report.md)）。

## 何时仍会用到

- Linux + NVIDIA GPU 服务器上做 Python 流水线：CTranslate2 的 int8 量化 + 显存占用低仍是省卡选择（WhisperX 亦以其为底座）[1] [3]。
- 存量项目依赖未迁移前维持现状。

## 对比

Mac 本地：whisper.cpp 全面占优（速度、依赖、活跃度）[2]。服务器 GPU：仍是 WhisperX 的默认底座，见 [whisperx](../whisperx/report.md)。逐维度见 `../comparison.md`。

## 风险与注意

- 若维护长期停滞，考虑迁移到 whisper.cpp 或 MLX 路线；WhisperX 对其的依赖是连带风险。
- 「待验证」：SYSTRAN 是否以其他形式接手维护（观察期内复核）。

## 来源

1. faster-whisper 官方仓库 — https://github.com/SYSTRAN/faster-whisper（访问 2026-08-27）
2. Open Source Speech to Text on Mac: 2026 Comparison（Speakhapi，2026）— https://speakhapi.com/blog/open-source-speech-to-text-mac（访问 2026-08-27）
3. Whisper.cpp vs faster-whisper 2026: STT Speed Test（PromptQuorum，2026）— https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录：Mac 劣势 + 维护放缓 |
