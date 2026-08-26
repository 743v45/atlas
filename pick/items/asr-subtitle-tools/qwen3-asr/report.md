# Qwen3-ASR

> **TL;DR**：2026-01 新秀：1.7B 即达普通话平均 CER 3.76%，覆盖 30 语言+22 中文方言，transformers 原生/vLLM 部署还带 ForcedAligner 时间戳模型；Mac 本地路径未经验证，适合先试用再定。

- **结论**：trial 试用
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 0.6B/1.7B + ForcedAligner-0.6B（2026-01-29 发布）；2026-06-26 transformers 原生支持（含 `torch.compile`） | [1] |
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/QwenLM/Qwen3-ASR（⭐3,422，gh 2026-08-27） | [1] |
| 维护活跃度 | 活跃（最近推送 2026-06-26；半年内三波功能更新：发版 → vLLM/流式 → transformers 原生） | [1] |

## 为什么选（值得试用的理由）

1. **小参数量打出高准确率**：1.7B 版普通话平均 CER 3.76%（AISHELL-1 1.48%），官方称「开源 ASR 中 SOTA、可与最强商业 API 竞争」；第三方统一口径下仅次于 FireRedASR2（2.89/3.05%）与 Doubao-ASR（3.69%）[1] [2]。
2. **语言/方言覆盖最广的一档**：30 语言 + 22 中文方言（含粤语两种口音、吴语、闽南语），中英混杂、多口音素材的兜底能力强 [1]。
3. **字幕刚需的时间戳有专门模型**：Qwen3-ForcedAligner-0.6B 做非自回归强制对齐，11 语言内任意单元时间戳，单次对齐最长 5 分钟语音，官方称时间戳精度超 E2E 对齐模型 [1]。
4. **推理栈现代且全**：vLLM 批量/异步服务、流式与离线统一、长音频直转、Docker、Gradio demo；2026-06 起不依赖自定义代码（transformers 原生 + torch.compile）[1]。
5. **0.6B 档吞吐惊人**：官方口径 128 并发下 2000 倍吞吐——批量字幕回填任务的成本友好选项 [1]。

## 对比

与 FireRedASR2 同代（2026 上半年）：统一口径普通话准确率略逊（3.76% vs 2.89%），方言互有胜负（11.85% vs 11.55%），但语言覆盖广得多、transformers 生态接入更顺 [2]。与 SenseVoice 比：更准但更重（1.7B LLM 架构 vs 234M 非自回归）。逐维度见 `../comparison.md`。

## 风险与注意

- **Mac 本地未验证**：官方推荐路径是 vLLM（Linux/GPU 向）；transformers 原生路径理论上可 CPU/MPS 跑 1.7B，但本机（16GB Apple Silicon）无实测记录——**待验证**后再定 verdict。
- 准确率主张主要来自自家技术报告 [3] 与 FireRedASR2 的对比口径 [2]，独立第三方横评尚少（2026-08 观察期）。
- 发布仅半年余，生产案例与社区问答密度不及 FunASR/Whisper 系。

## 来源

1. Qwen3-ASR 官方仓库（模型表/吞吐/ForcedAligner/部署路径）— https://github.com/QwenLM/Qwen3-ASR（访问 2026-08-27）
2. FireRedASR2S 评测表（Qwen3-ASR-1.7B 统一口径数据）— https://github.com/FireRedTeam/FireRedASR2S（访问 2026-08-27）
3. Qwen3-ASR 技术报告 — https://arxiv.org/abs/2601.21337（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | trial | 首次记录：多语言/新栈路线的有力候选 |
