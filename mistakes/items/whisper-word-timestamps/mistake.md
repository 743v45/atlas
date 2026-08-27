# 逐词时间戳必崩:turbo 仓库不带 cross-attentions

> **TL;DR**:错在「UI 提供了选项 = 组合一定可用」——模型仓库变体决定能力边界,且崩溃路径上没有降级。

- **状态**:fixed(已修正)
- **日期**:2026-08-06
- **出处**:voicetxt(浏览器端 whisper 转写),turbo 模型 + 逐词时间戳组合

## 经过

页面上选 `turbo · 800 MB · q4` 并开「逐词时间戳」,转写直接崩,worker 抛 `Model outputs must contain cross attentions to extract timestamps. This is most likely because the model was not exported with output_attentions=True.`——功能开关照常可选,用户组合勾选即触雷。

## 根因

我以为是偶发故障,其实是确定性不兼容:transformers.js 提取逐词时间戳要求 `_timestamped` 变体仓库(导出带 cross-attentions),无后缀的 turbo 仓库不带——逐词路径在这个仓库上必崩。两个锅:能力假设没对照模型变体验证;崩溃路径裸奔,没有降级出口,用户拿到的是白屏不是结果。

## 修正

两条:turbo 永久禁用逐词时间戳(能力矩阵写死);全模型逐词路径包 try/catch,异常自动降级逐句——崩溃变成能力降级,任何组合下用户总能拿到转写结果。可复用判据:凡是「按模型/按仓库/按变体」的能力开关,开启前先验证当前变体支持,且降级路径先于功能存在。
