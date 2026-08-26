# FunASR

> **TL;DR**：达摩院语音工具链事实标准（⭐20,035、日更）：一个 AutoModel 串起 VAD/ASR/标点/说话人并直出 SRT，自带 Docker 服务与 OpenAI 兼容端点，中文靠 SenseVoice/Paraformer 模型撑起第一梯队——「要开箱即用的字幕服务」的默认起点。

- **结论**：adopt 推荐
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v1.3.29（2026-07：恢复 SenseVoice VAD 分段时间戳）；最近推送 2026-08-26（日更节奏） | [1] |
| 许可证 | MIT | [1] |
| 仓库 | https://github.com/modelscope/FunASR（⭐20,035，gh 2026-08-27） | [1] |
| 维护活跃度 | 极活跃：2026 年连续发版（1.3.27 语言元数据、1.3.29 字幕分段时间戳），官方站 funasr.com 持续输出部署指南（观察 2026-08-27） | [1] [2] |

## 为什么选

1. **「模型 + 工具链」分工里的工具链层事实标准**：统一的 `AutoModel` 接口把 VAD、ASR、标点恢复、说话人分离（FSMN-VAD + CAM++）串成流水线，Paraformer、SenseVoice、Fun-ASR-Nano 都经它调用 [3]。做字幕要的「分段 + 时间戳 + 标点」是一条现成管线，不用自己拼。
2. **部署形态最全**：pip 三行起步、官方 Docker 服务、多语言客户端（Python/C++/HTML/Java/C#）、OpenAI 兼容端点（`verbose_json.language` 上报检出语言，2026-06 起）[1] [2]。
3. **字幕场景在 2026 年被持续修**：v1.3.29 让 `sentence_timestamp=True` 在缺 token 时间戳时也返回每个 VAD 区间——字幕/剪辑客户端不再拿到空时间轴 [1]。
4. **中文准确率靠内置模型守住第一梯队**（工具链本身不产模型）：Paraformer-Large 普通话平均 CER 4.56%、SenseVoice-L 4.47%（FireRedASR v1 官方对比口径，2025-01）[4]；虽逊于 FireRedASR2（2.89%），但比 Whisper-Large-v3（9.86%）强一倍以上。
5. **生态体量最大**：⭐20,035、贡献者众多（gh 2026-08-27），ModelScope 国内部署链路成熟，中文文档/社区问答密度远超同类 [1]。

## 对比

FireRedASR2 准确率更高但无官方 WebUI/服务化封装；FunASR 是「易用 + 够准」的平衡点，也是给 FireRedASR/Qwen3 模型做服务化包装时最顺手的底座。模型层选型（SenseVoice vs Paraformer vs Fun-ASR-Nano）见 [sensevoice](../sensevoice/report.md) 与横评 `../comparison.md`。

## 风险与注意

- **工具链 ≠ 模型**：中文上限由所选模型决定，FunASR 自家最强开源模型（Fun-ASR-Nano-2512，800M）普通话平均 CER 4.55%，落后 FireRedASR2 一个身位（统一口径对比，2026-02）[5]。
- 说话人分离是「组合流水线」（FSMN-VAD + CAM++ + 标点模型拼装），非 SenseVoice 模型本体输出；部分能力需源码安装（`pip install git+...`，2026-05 公告）[2]。
- Apple Silicon 上 Docker 路线退化纯 CPU（容器内无 Metal），官方预编译镜像多为 x86；Mac 建议原生 pip 路线（2026-08-24 本地部署经验）。

## 来源

1. FunASR 官方仓库（Release/功能公告）— https://github.com/modelscope/FunASR（访问 2026-08-27）
2. SenseVoice 官方仓库（FunASR 组合流水线/发布说明转载）— https://github.com/FunAudioLLM/SenseVoice（访问 2026-08-27）
3. FunASR 官网 — https://www.funasr.com/（访问 2026-08-27）
4. FireRedASR v1 评测表（Paraformer-Large 4.56%、SenseVoice-L 4.47%、Whisper-Large-v3 9.86%）— https://github.com/FireRedTeam/FireRedASR（访问 2026-08-27）
5. FireRedASR2S 评测表（Fun-ASR-Nano-2512 4.55%）— https://github.com/FireRedTeam/FireRedASR2S（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录：工具链层默认选择（历史会话 2026-08-24「最好用」结论一致） |
