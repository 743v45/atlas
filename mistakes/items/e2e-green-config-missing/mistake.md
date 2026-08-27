# E2E 绿灯掩盖入口缺失:测试路径绕过配置

> **TL;DR**:错在验收链没覆盖用户真实启动路径——测试替产品持有配置,绿灯就是假绿灯。

- **状态**:fixed(已修正)
- **日期**:2026-07-27
- **出处**:workbuddy desktop(Electron + electron-vite),脚手架完成、E2E 全绿后用户首跑翻车

## 经过

desktop 脚手架完成,Playwright E2E 全绿。用户亲自跑 `pnpm dev`(electron-vite dev)当场报错:`Error: No entry point found for electron app, please add a "main" entry…`——renderer 的 dev server 正常起来了,Electron 主进程入口找不到,`package.json` 没有 `main` 字段。

## 根因

我以为是脚手架遗漏,其实是测试架构性盲区:E2E 配置里直接指定了 main 入口路径,绕过了 `package.json` 的 `main` 字段——测试替产品回答了「入口在哪」,于是配置缺失被测试路径永久遮蔽。测试过 ≠ 能跑:测试走的路和用户走的路不是同一条时,绿灯只证明前者。

## 修正

补 `"main": "out/main/main.js"`,dev 与 E2E 共用同一份入口配置。可复用判据:验收必须含「用户真实启动路径」;审查测试架构时专查一点——有没有配置是测试自己持有而产品没有的,凡有,该项验收作废。
