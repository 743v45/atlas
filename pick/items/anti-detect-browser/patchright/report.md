# Patchright

> **TL;DR**：Playwright 的 drop-in 反检测替换：改一行 import 即修补 CDP 泄漏，已有 Playwright 工作流的最低成本反检测升级。

- **结论**：adopt（推荐）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| star | ⭐4,190（gh 采集 2026-08-27） | [1] |
| 最后 push | 2026-08-19 | [1] |
| 许可证 | Apache-2.0 | [1] |
| 语言/形态 | Node（`patchright`）+ Python（`patchright-python`）双版本驱动库 | [1] |

## 为什么选

- **原理**：修补 Playwright 启动时的 CDP 泄漏——`Runtime.enable`、`Target.setAutoAttach` 调用序列会被反机器人系统在协议层识别；同时补掉 HeadlessChrome 标记。补丁在浏览器进程启动前生效，区别于 playwright-extra 那类运行时 JS 注入 [2]。
- **官方数据**：约 **67% headless 检测降幅** [2]（官方口径，待独立复核）。
- **AI 接入**：与 Playwright API 完全同构，Agent 代码改一个 import 即生效；支持 `channel=chrome` 调用真实 Chrome [1][2]。
- **加分项**：能操作 Closed Shadow Roots（普通 Playwright 做不到）[1]。

## 对比

与引擎派 Camoufox 的核心差异：Patchright 在 Chromium 上修痕迹（补丁派），迁移成本低；Camoufox 改 Firefox 引擎，指纹一致性理论更强。逐维度对比见 `../comparison.md`。

## 风险与注意

- 补丁派天花板：只修补已知检测信号，新型检测需等上游更新。
- 需跟随上游 Playwright 版本节奏（fork 维护成本）。

## 来源

1. Patchright — https://github.com/Kaliiiiiiiiii-Vinyzu/patchright（访问 2026-08-27，gh 一手数据）
2. Anti-Detect Browser Benchmark 2026: 7 Tools, 651 Verdicts — ianlpaterson.com（2026 评测，tvly 调研 2026-08-27）
3. The 6 best Patchright alternatives in 2026 — roundproxies.com（2026）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | adopt | 首次记录（源自 taevasidian 调研报告提取） |
