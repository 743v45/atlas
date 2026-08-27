# asked — 问答馆

「我问、AI 长答、值得留存的一切」(`items/<条目>/{meta.json, answer.md}`)。

## 必守规则

- **写任何条目前先读 [RULES.md](RULES.md)**。
- **自洽是硬标准**:没读过原对话的人能独立看懂。
- **source 必须是已归档的真实路径**——先归档到 atlas/conversations/,再建条目(门禁校验存在性)。
- 恢复自历史对话的内容忠于原答案骨架,重构补全标注「AI 重构」——存档馆不许无痕改史。
- 分界:怎么做 → apprentice;选型 → pick;翻车 → mistakes;念头 → spark。
- HTML 为生成物,改完 meta 或 md 跑 `python3 scripts/build-index.py`。
