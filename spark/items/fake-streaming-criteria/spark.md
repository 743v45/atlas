# 「假流式」判据:end-to-end token delta 才是真流式

> longxia 审计发现同一系统两层都在假装流式:BFF 层「流式」实为 350ms tail CLI 写的文件再 diff(fs.watch 不可靠到要 800ms 轮询兜底,watcher 成装饰);RN 层 fetch 不暴露 getReader,平板上流式也是假的。提炼判据:**end-to-end token delta 才是真流式,「轮询+diff+重发」都是假流式**,且每层各自造假会叠加延迟。判据未实测验证,提炼自审计(C2/C4)。

来源:本机 MacBook Air dig(0bf6bb65 | 2026-07-27 | holdcloud-longxia)。

## 怎么试

- 在任一真实流式链路上做端到端 token 到达时间对比,验证判据可测
- 走通后毕业去 apprentice(判据类)或直接当审计 checklist 项
