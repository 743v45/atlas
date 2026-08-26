# fireredasr-ui

> **TL;DR**：FireRedASR 的第三方一键 WebUI+OpenAI 兼容 API 封装：本机部署的原型，但上游 2025-02 起停更 18 个月、不支持 v2——已被本地深度改造（队列/缓存/看门狗）接管，新项目勿直接采用上游原版。

- **结论**：hold 观望（上游停更；本机实例因深度改造继续服役）
- **核实日期**：2026-08-27

## 基本信息

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 上游最后推送 2025-02-24（截至今 18 个月无更新） | [1] |
| 许可证 | Apache-2.0 | [1] |
| 仓库 | https://github.com/jianchang512/fireredasr-ui（⭐88，gh 2026-08-27） | [1] |
| 维护活跃度 | **停更**：仅包 FireRedASR v1，v2（2026-02）无适配迹象（观察 2026-08-27） | [1] [2] |

## 为什么是本机现役（历史与价值）

1. **它是 2026-08-24 本机部署的载体**：Python 3.10 + venv + FireRedASR-AED-L（4.35GB 权重，ModelScope 国内镜像 + aria2 多线程下载，SHA256 校验通过），Flask 服务（127.0.0.1:5078），实测纯中文近零错、SRT 输出正常、内存约 880MB（Mac 无 CUDA，CPU 路径 [3]）。
2. **两个实用设计**：内置 30 秒自动切片（绕过 v1-AED 单条 60 秒上限）；OpenAI 兼容 `/v1/audio/transcriptions` 端点（`response_format=srt/json/text`）。

## 为什么 hold（对新项目）

1. **上游停更 18 个月**（gh 2026-08-27）[1]：bug 不修、模型不跟进。
2. **只包 v1**：FireRedASR2S（2026-02，词级时间戳/code-switching/all-in-one）无适配 [2]——上游原版拿不到 v2 能力。
3. **本机实例已被深度改造接管**：本地已重构为「常驻 dispatcher（0.0.0.0:5079）+ 按需启停 worker（stdin/stdout JSON-RPC）+ SQLite 队列与 sha256 缓存（TTL 1 天可配）+ 空闲 180s 卸载 + 状态面板 + caddy 反代（asr.work.taevas.host）」，21 个单元测试通过（2026-08-24 实施记录；设计文档 `~/Local/fireredasr-ui/docs/superpowers/specs/2026-08-14-fireredasr-queue-dispatcher-design.md`，commit 82df4e3）——与上游原版已是两个东西。
4. **部署坑实测沉淀**（2026-08-24）：Mac Docker 容器无法访问 Metal，ASR 须原生 pip 勿套 Docker；ModelScope 单连接限速约 195KB/s，aria2 16 连接可达约 12.6MB/s（4.35GB 模型 SHA256 校验通过后入库）。

## 对比

同类「壳」中：FunASR 官方自带服务与 WebUI（活跃，见 [funasr](../funasr/report.md)）是新项目的正解；本项目特例在于「壳包的是中文最准的模型」。逐维度见 `../comparison.md`。

## 风险与注意

- **升级路径**：迁往 FireRedASR2S 官方 CLI（v2 自带 VAD/标点/时间戳）+ 自研或 FunASR 服务化，是下一迭代的自然方向——**待验证**（v2 在 Mac 的实测）。
- 上游若复活或出现 v2 适配的第三方壳，重新评估。

## 来源

1. fireredasr-ui 上游仓库 — https://github.com/jianchang512/fireredasr-ui（访问 2026-08-27）
2. FireRedASR2S 官方仓库（v2 能力，上游未适配）— https://github.com/FireRedTeam/FireRedASR2S（访问 2026-08-27）
3. Open-LLM-VTuber 文档（Mac CPU 路径）— https://open-llm-vtuber.github.io/en/docs/user-guide/backend/asr/（访问 2026-08-27）

## 变更记录

| 日期 | verdict | 说明 |
|---|---|---|
| 2026-08-27 | hold | 首次记录：上游停更 18 个月；本机深度改造实例除外 |
