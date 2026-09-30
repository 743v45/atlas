# 小程序框架 releases / npm / LICENSE 快照（2026-10-01 采集）

采集通道：gh api + registry.npmjs.org + api.npmjs.org（下载量窗口 2026-09-22 ~ 2026-09-28）

## GitHub latest release

| repo | latest tag | published |
|---|---|---|
| NervJS/taro | v4.3.0 | 2026-09-29T08:08:21Z |
| didi/mpx | v2.11.1 | 2026-07-22T13:29:03Z |
| eleme/morjs | v1.0.113 | 2024-05-21T09:30:10Z |
| Tencent/kbone | （releases/latest 返回 404：无 release） | — |
| dcloudio/uni-app | （releases/latest 返回 404：经 npm/HBuilderX 分发，无 GitHub release） | — |

注：uni-app npm 版本号形如 `2.0.2-5020620260917001`（2026-09-18 发布），内嵌 HBuilderX 版本段（5020620260917 ≈ HBuilderX 4.0206202609170），与 HBuilderX 发布节奏绑定。

## npm 版本与周下载

| 包 | latest | published | 周下载（2026-09-22~09-28） |
|---|---|---|---|
| @tarojs/taro | 4.3.0 | 2026-09-29 | 32,352 |
| @dcloudio/uni-app | 2.0.2-5020620260917001 | 2026-09-18 | 35,887 |
| @mpxjs/core | 2.11.1 | 2026-07-22 | 2,114 |
| @morjs/core | 1.0.114-beta.21（beta；最新稳定 1.0.113 = 2024-05-21） | 2025-08-15 | 13 |

## LICENSE 解码（license API 报 NOASSERTION 的三家）

- NervJS/taro：LICENSE 文件为标准 MIT 文本（Copyright (c) 2018 O2Team）→ **MIT**。解码留档：本目录 `taro-LICENSE-decoded.txt`
- Tencent/kbone：LICENSE 文件为腾讯自定义文本「Kbone is licensed under the BSD 3-Clause License, except for the third-party components listed below」→ **BSD-3-Clause**（依赖列表 MIT）。解码留档：本目录 `kbone-LICENSE-decoded.txt`
- Tencent/wepy（落选节点）：仓库**存在 LICENSE 文件**（任务预判「无 LICENSE 文件」不成立），为腾讯自定义文本：binary 与 source 均按 MIT 许可 + 第三方组件独立条款（Copyright (C) 2017 THL A29 Limited）→ **自定义 MIT 类**（gh license API 报 NOASSERTION 系文本非标准导致）。解码留档：本目录 `wepy-LICENSE-decoded.txt`

## didi/mpx 的 Skyline 相关 issue/PR 检索（gh search 2026-10-01）

total_count = 7，关键项：
- issue #1312（2023-11-02，closed）有考虑支持 skyline 引擎进行渲染吗
- issue #1393（2024-01-25，closed）Skyline 模式下 worklet 写在 composition api setup 中不触发
- issue #1454（2024-04-24，closed）Skyline是否支持 → 维护者 hiyuki 2024-04-25 回复：选项式 API 支持（按微信文档正常编写），组合式 API 因微信编译规则暂无法用 worklet（留档 `mpx-issue-1454-comments.json`）
- issue #1488（2024-05-27，closed）[Feature Request] 支持 Skyline app-bar
- PR #2540（2026-07-01，open）mpx skyline skill

留档：`mpx-skyline-issues-search.json`、`mpx-issue-1454.json`、`mpx-issue-1454-comments.json`
