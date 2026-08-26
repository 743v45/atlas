# mistakes — 错题集

一次真实翻车 = 一条错题(`items/<错题>/{meta.json, mistake.md}`):经过 / 根因 / 修正三段完整叙事。

## 必守规则

- **写任何错题前先读 [RULES.md](RULES.md)**。
- **单一事实源**:apprentice 课的翻车小节只留摘要 + 链接,根因与修正只住本馆。
- **根因落在判断上**:「我以为是 X,其实是 Y」合格;「太着急」不合格。
- **同根因再犯** → status 改 `recurring`,经过里追加复发记录——修正失效是新信息。
- 所有 HTML 均为生成物,改完 meta 或 md 跑 `python3 scripts/build-index.py`(门禁:必填 / 枚举 / related 存在性 / 三小节齐全)。
