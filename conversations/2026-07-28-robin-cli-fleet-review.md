---
date: 2026-07-28
topic: robin CLI 大舰队会话三连翻（凭据验证 / subagent 截断 / 全局 lint）
related:
  - ../mistakes/items/cli-credential-verification/
  - ../mistakes/items/subagent-report-truncation/
  - ../mistakes/items/fragment-lint-collapse/
原始会话: ~/.claude/projects/-Users-taevas-code-upyun-robin/41f4fc3f-f48f-4bc9-862e-bb1530fe11e8.jsonl + 同目录 subagents/agent-a14286de83d2709f3.jsonl
---

# 2026-07-28 · robin CLI 大舰队会话三连翻

会话原始需求（服务与网关细节脱敏，方法保留）：「根据 robin 服务接口，做一个 cli 工具, 带二次确认的。（禁止访问 config/production.js 和 config/production.json）」。28 个 agent 分片并行开发，当日三次翻车，三个独立教训。

## 翻车一：凭据采集无验证闭环

CLI `login` 只提示「从浏览器 DevTools 复制网关 cookie 值并粘贴」，随手粘 `123` 也直接「已保存网关 cookie」。用户当场揭穿——**原始表述（翻车证据）**：「你不验证一下吗。我随便填写的。账号密码。密码隐藏的方式输入吧。输入账号的时候，密码就得传入，隐藏的。并且要验证密码」。**修正**：login 采集（账号明文 + 密码隐藏输入 + cookie 粘贴）后立即打真实接口验证（GET /api/domains，双层鉴权：Basic + 网关 cookie，200 才保存、失败给出哪层失败并不保存）。

## 翻车二：subagent 长报告回传截断

final whole-branch review subagent（merge gate 审查，非单任务 gate）审查完成，coordinator 只收到报告的最后一句（`--force` 无效）。coordinator 反馈原话：「**你的审查完成了,但返回的内容只剩最后一句**……我需要全部 findings 才能决定修复范围。请把完整的结构化报告再发一遍」。**修正方向**：长报告落盘为文件、回传路径引用，不全靠 final text 当传输通道。

## 翻车三：分片达标，合并溃败

28 个 agent 各自通过 task 级 gate 交付，合并后用户一句定案——**原始表述（翻车证据）**：「lint 全是问题。修复」。**修正**：全局质量门禁（lint/build/test 全仓级）独立于分发单元单独跑，分片达标 ≠ 整体达标。

三翻分别沉淀为本馆错题：[cli-credential-verification](../mistakes/items/cli-credential-verification/) / [subagent-report-truncation](../mistakes/items/subagent-report-truncation/) / [fragment-lint-collapse](../mistakes/items/fragment-lint-collapse/)。
