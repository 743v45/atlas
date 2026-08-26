# 引擎血缘

- **出身**:骨架复制自 pick(init `617c31a`,2026-08-27)。理念与方法复制,代码按 apprentice 的 schema 重写;渲染器与 BASE_CSS 起初两馆各存一份,靠本目录的 check-drift 对账。
- **2026-08-27 第三馆触发抽取**:mistakes 馆成立,命中当初写死的抽象触发条件——渲染器与 BASE_CSS 上提至 `atlas/shared/render.py`,三馆与门户统一 import。**对账退役**:分叉的物理根源已消失,check-drift 改为反向断言(任何 build 内不得再出现本地渲染器副本,防止有人复制回去)。
- **共享层同步纪律(不变)**:改 `shared/render.py` 当天跑三馆 build + pick 的 `check.py`,全绿才算同步完成。
- **新馆接入**:从任一馆复制骨架 → 删本地渲染器 → 接 shared import → 自带 RULES 与门禁。
