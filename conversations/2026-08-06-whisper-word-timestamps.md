---
date: 2026-08-06
topic: whisper turbo 逐词时间戳必崩
related:
  - ../mistakes/items/whisper-word-timestamps/
原始会话: ~/.claude/projects/-Users-taevas-code-mymy-voicetxt/2801380a-d620-4d08-a05e-7a0c9ae24189.jsonl（08-06/07）
---

# 2026-08-06 · whisper turbo 逐词时间戳必崩

voicetxt（浏览器端 whisper 转写）页面选 `turbo · 800 MB · q4` 模型并开「逐词时间戳」，转写直接崩，worker 抛错：

```
Error: Model outputs must contain cross attentions to extract timestamps.
This is most likely because the model was not exported with `output_attentions=True`.
    at _extract_token_timestamps (transcribe.worker.js)
```

**原始表述（翻车证据）**：功能开关照常可选（逐词时间戳 + turbo），用户组合勾选即触雷——UI 允许的选项组合，模型仓库未必支持。

**关键转折**：定位到模型仓库层面——transformers.js 提取逐词时间戳要求 `_timestamped` 变体仓库（导出时带 cross-attentions）；无后缀的 turbo 仓库不带 cross-attentions，逐词路径必然崩溃。不是偶发故障，是确定性不兼容。

**最终结论（沉淀）**：修法两条：turbo 永久禁用逐词时间戳；所有模型逐词路径包 try/catch，异常自动降级逐句——崩溃变成能力降级，用户总能拿到结果。沉淀为本馆错题 [whisper-word-timestamps](../mistakes/items/whisper-word-timestamps/)。
