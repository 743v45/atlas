# FireRedASR

> **TL;DR**：小红书开源的中文 ASR 准确率冠军：v2（FireRedASR2S，2026-02）普通话平均 CER 2.89% 且原生支持中英混杂与词级时间戳，v1-AED 已在本机 16GB Mac 部署实测（纯中文近零错）；无官方 WebUI、自配门槛偏高。

- **结论**：adopt 推荐
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | v2（FireRedASR2S）：AED+VAD+LID+Punc 2026-02-12 发布，LLM 权重 2026-02-25，技术报告 2026-03-12；v1：AED-L 2025-01-24、LLM-L 2025-02-17 | [1] [2] |
| 许可证 | Apache-2.0（v1/v2 均是） | [1] [2] |
| 仓库 | https://github.com/FireRedTeam/FireRedASR2S（v2，⭐653）；https://github.com/FireRedTeam/FireRedASR（v1，1,971 star，gh 2026-08-27） | [1] [2] |
| 维护活跃度 | v2 仓库最近推送 2026-06-02（约 3 个月前）；v1 仓库 2026-02-25 后停更——重心已迁往 v2（gh 2026-08-27 采集） | [1] [2] |

## 为什么选

1. **中文准确率开源第一**。v2 官方评测（24 个公开测试集）：普通话平均 CER，FireRedASR2-LLM 2.89%、AED 3.05%，优于 Doubao-ASR（3.69%）、Qwen3-ASR-1.7B（3.76%）、Fun-ASR（4.16%）、Fun-ASR-Nano-2512（4.55%）；AISHELL-1 上 AED 低至 0.57% [1]。v1 官方口径同样霸榜：LLM 8.3B 平均 3.05%、AED 1.1B 3.18%，对比 Whisper-Large-v3 9.86%、Paraformer-Large 4.56%、SenseVoice-L 4.47% [2]。
2. **v2 原生支持中英混杂（code-switching）与词级时间戳**——正是字幕场景两大刚需，也补上了 v1-AED 的最大短板（见「风险」第 1 条）。FireRedASR2-AED 支持词级时间戳与置信度，CLI 输出带 `sentences`/`words` 时间轴的 JSON，可直接拼 SRT [1]。
3. **All-in-One 系统省去拼装**：v2 把 ASR、FireRedVAD（F1 97.57%，超 Silero/TEN/FunASR-VAD）、FireRedLID（100+ 语言）、FireRedPunc（中英标点 F1 78.90% vs FunASR-Punc 62.77%）打包成一个 `fireredasr2s-cli`，长音频由内置 VAD 切段 [1]。
4. **本机已实测可跑**：v1-AED-L（1.1B，4.35GB 权重）部署于 16GB Apple Silicon Mac，CPU 推理 13.5 秒测试音频 10.6 秒完成，内存约 880MB；纯中文段零错误，SRT 输出格式正确（2026-08-24 本地实测；Mac 无 CUDA 只能 CPU 路径，MPS 算子不全 [4]）。
5. **方言覆盖广**：v2 支持普通话 + 20 余种方言口音（粤/川/沪/吴/闽南等），方言 19 测试集平均 CER 11.55%（LLM），仍优于对比组 [1]。

## 对比

与 FunASR/SenseVoice 的取舍是「准确率上限 vs 生态易用」：FireRedASR2 准确率第一但无官方 WebUI、无 Docker 一键服务，Python 3.10 + 手动下模型起步；FunASR 反之（详见 [funasr](../funasr/report.md) 与横评）。与 Qwen3-ASR 相比准确率略胜、方言略胜，但 Qwen3 语言覆盖（30 语）更广。逐维度对比见 `../comparison.md`。

## 风险与注意

- **v1-AED 中英混杂弱**：本机实测英文专名误差明显（"FireRedASR"→"FIRE RATE ASR"；测试音为合成语音，放大了误差，2026-08-24 实测记录）。v1-AED 单条音频上限约 60 秒（超时幻觉），长音频须切片 [4]。**v2 已原生支持 code-switching，理论上缓解，但 v2 在 Mac 的实测尚缺——待验证。**
- **v1 仓库实质停更**（最后推送 2026-02-25），新能力都在 v2 仓库；现存第三方壳（如 fireredasr-ui）均只包 v1 [1] [3]。
- **LLM 版吃内存**：v1-LLM 需挂 Qwen2-7B-Instruct [2]，官方推荐 32GB+ 统一内存才从容，16GB Mac 能跑但紧张（2026-08-24 调研结论）；v2-LLM 体量相近（服务器向，vLLM/TensorRT-LLM 加速均面向 NVIDIA GPU [1]）。**Mac 上建议 AED 路线。**
- star 体量小（v2 ⭐653，gh 2026-08-27），社区生态薄于 FunASR/Whisper 系，遇坑多靠自查。

## 来源

1. FireRedASR2S 官方仓库（评测表/模块说明/Quick Start）— https://github.com/FireRedTeam/FireRedASR2S（访问 2026-08-27）
2. FireRedASR v1 官方仓库（v1 评测表/LLM 依赖 Qwen2-7B）— https://github.com/FireRedTeam/FireRedASR（访问 2026-08-27）
3. 中文语音识别该用谁？6 个开源模型 + 2 个配套工具（腾讯云开发者社区，CoovallyAIHub，2026-03-20）— https://cloud.tencent.com/developer/article/2642961（访问 2026-08-27）
4. Open-LLM-VTuber 文档：FireRedASR 在 Mac 只能 CPU 跑 — https://open-llm-vtuber.github.io/en/docs/user-guide/backend/asr/（访问 2026-08-27，2026-08-24 本地实测依据）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录：v1-AED 为本机现役部署（2026-08-24 实测），v2 为升级目标 |
