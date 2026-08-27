---
date: 2026-07-28
topic: robin CLI 鉴权幂等状态机的口述与演进
related:
  - ../apprentice/items/verify/auth-idempotent-state-machine/
  - ../mistakes/items/cli-credential-verification/
原始会话: ~/.claude/projects/-Users-taevas-code-upyun-robin/41f4fc3f-f48f-4bc9-862e-bb1530fe11e8.jsonl(本机,07-28 13:57~17:25 UTC;同会话的 SDD 并队视角另见 [2026-07-28-robin-cli-fleet-review.md](2026-07-28-robin-cli-fleet-review.md))
---

# 2026-07-28 · robin CLI 鉴权幂等状态机

会话主线是「根据服务接口做一个 CLI 工具,带二次确认」(内部 DNS 服务,双层鉴权:网关 cookie + 账号密码;以下内部服务名/cookie 名均已脱敏)。本篇只记**鉴权机制怎么从一堆口语长成一个状态机**。

**原始表述(设计口述,课核心)**——16:34,用户一段口语把整个机制说完:

> 「<网关>cookie 先认证的吧。认证完,就可以记录进配置,每次 auth 看看配置里的可不可用,可用就没必要再配置,除非 force 更新,如果账号已经登录,也没必要再登录,除非 logout,每一步确认鉴权通过」

这段话展开就是完整状态机:状态(已认证/未认证)、迁移(auth / force / logout)、幂等(可用不重配、已登录不重登)、且每一步带确认——不是散落在各命令里的 if,是一条全局规则。

**关键转折(按时间序,每条都是一句用户话催生的修正)**:

- 15:27 翻车:AI 对随手粘的假 cookie 直接「已保存」。用户:「你不验证一下吗。我随便填写的。账号密码。密码隐藏的方式输入吧。输入账号的时候,密码就得传入,隐藏的。并且要验证密码」——错题档案见 [mistakes/cli-credential-verification](../mistakes/items/cli-credential-verification/);
- 15:46 「状态码可以展示一下.(其他的接口报错,状态码都可以展示一下」——报错必须带状态码,否则排障没抓手;
- 15:49 「Email and password not match 的话,可以提醒一下登录的。这个应该和登录接口关联的(注释一下)」——401 类错误关联到「该重新登录了」的提示;
- 15:51 「增删改都有二次确认的吧」;
- 15:54 「配置是不是不要保存为密码,而是登录后变成 cookie 类的,你看下是什么形态拿到的」——落盘的是会话凭据,不是密码本身;
- 15:58 「你存在配置里是不是也得加一下 salt,这个也会被利用。加一层盐吧」——凭据落盘再加一层盐。

**最终结论(沉淀)**:鉴权这类横切需求,交给 AI 的正确姿势是**口述一遍状态机**(状态+迁移+幂等+每步确认),而不是逐命令提要求——一次讲清,处处生效。落地在 `feature/auth-idempotent` 分支,当日合入 develop、打 tag、npm version 发布。沉淀为 apprentice 课 [auth-idempotent-state-machine](../apprentice/items/verify/auth-idempotent-state-machine/)。
