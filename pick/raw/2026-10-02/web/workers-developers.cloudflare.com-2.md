# Cloudflare Workers 定价页 WebFetch 补抓（表格单价数字）

- 来源 URL: https://developers.cloudflare.com/workers/platform/pricing/
- 访问日期: 2026-10-02（WebFetch，用于补齐 web-reader 丢掉的表格数字）
- 注: 完整官方 markdown 版（含全部表格、Last updated Oct 2, 2026）在同目录 workers-pricing-full.md，以下为 WebFetch 对同一页面的结构化提取结果，两相印证。

## WebFetch 提取原文

**Workers Paid (Standard) plan:**
- Requests: "10 million included per month" plus "+$0.30 per additional million"
- CPU time: "30 million CPU milliseconds included per month" plus "+$0.02 per additional million CPU milliseconds"
- Base plan: "$5 USD per month" minimum charge

**Workers Free plan:**
- Requests: "100,000 per day"
- CPU time: "10 milliseconds of CPU time per invocation"

## 与官方 md 版交叉核对

workers-pricing-full.md 中 Workers 计费表（同页渲染版）与上述数字完全一致：

| | Requests | Duration | CPU time |
|---|---|---|---|
| Free | 100,000 per day | 无收费 | 10 ms CPU / invocation |
| Standard | 含 10M/月，+$0.30/百万 | 无收费无上限 | 含 30M CPU-ms/月，+$0.02/百万 CPU-ms；单次调用上限 5 min（默认 30s） |
