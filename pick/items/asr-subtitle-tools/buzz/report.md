# Buzz

> **TL;DR**：开箱即用的开源桌面 GUI（Mac/Win/Linux）：拖文件出 SRT/VTT，零命令行门槛；后端 Whisper 使中文准确率一般，适合懒人快处理与非中文素材。

- **结论**：trial 试用（GUI 懒人路线 / 非中文素材）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 持续发版（仓库最近推送 2026-08-23） | [1] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/chidiwilliams/buzz（⭐21,143，gh 2026-08-27）；官网 buzzcaptions.com（Mac App Store 亦有分发） | [1] |
| 维护活跃度 | 活跃（本月有推送） | [1] |

## 为什么值得试用

1. **零门槛**：Mac 上装 App、拖文件、出 SRT/VTT/TXT——历史调研中被列为「图形界面懒人」首选（2026-08-24 会话结论）[2 引述口径]。
2. **本地模型**：识别在本地跑，隐私可控，支持 whisper.cpp 引擎与任务队列批处理 [1]。
3. **开源 GUI 里体量最大**：⭐21,143（gh 2026-08-27），跨三平台，2026 年 Mac 开源 STT 对比收录 [2]。

## 为什么不是 adopt

- **中文准确率受 Whisper 后端拖累**（普通话平均 9.86%，见 [whisper](../whisper/report.md) 与 [3]）——历史调研同样给出「中文一般」的结论（2026-08-24）。
- GUI 形态不可编程：进不了流水线/队列/API（本项目场景需要 API 化，见 [fireredasr-ui](../fireredasr-ui/report.md) 的路线对比）。

## 对比

中文优先的 GUI 路线，本机实践最终走了「fireredasr-ui（WebUI）」而非 Buzz——准确率优先使然（2026-08-24 会话决策链）。逐维度见 `../comparison.md`。

## 风险与注意

- Mac App Store 版与 GitHub 版功能可能有滞后——**待验证**。
- 大模型档在无 GPU Mac 上速度一般（Speakhapi 2026 对 Whisper 系 Mac 表现的综合口径）[2]。

## 来源

1. Buzz 官方仓库 — https://github.com/chidiwilliams/buzz（访问 2026-08-27）
2. Open Source Speech to Text on Mac: 2026 Comparison（Speakhapi，2026）— https://speakhapi.com/blog/open-source-speech-to-text-mac（访问 2026-08-27）
3. FireRedASR v1 官方评测表（Whisper-Large-v3 中文 9.86%）— https://github.com/FireRedTeam/FireRedASR（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录：GUI 懒人路线代表 |
