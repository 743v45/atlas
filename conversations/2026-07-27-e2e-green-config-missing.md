---
date: 2026-07-27
topic: E2E 绿灯掩盖 package.json main 缺失
related:
  - ../mistakes/items/e2e-green-config-missing/
原始会话: ~/.claude/projects/-Users-taevas-code-openresources-learn-workbuddy/5086a366-d180-4478-ada7-8f99ba24e42b.jsonl（07-27~30，报错在 07-27）
---

# 2026-07-27 · E2E 绿灯掩盖 package.json main 缺失

workbuddy desktop 脚手架完成、Playwright E2E 全绿之后，用户亲自跑 `pnpm dev`（electron-vite dev）当场翻车：

```
error during start dev server and electron app:
Error: No entry point found for electron app, please add a "main" entry…
```

**原始表述（翻车证据）**：renderer 的 dev server 起来了（Port 5173 in use, trying another one → 5174），Electron 主进程入口却找不到——`package.json` 没有 `main` 字段。

**关键转折**：排查发现 E2E 之所以绿，是因为测试配置里直接指定了 main 入口路径，绕过了 `package.json` 的 `main` 字段——测试路径绕过配置，等于替产品回答了「入口在哪」，测试过 ≠ 产品能跑。

**最终结论（沉淀）**：补 `"main": "out/main/main.js"`；判据沉淀：验收链必须覆盖「用户真实启动路径」，凡测试替产品持有的配置，绿灯都是假绿灯。沉淀为本馆错题 [e2e-green-config-missing](../mistakes/items/e2e-green-config-missing/)。
