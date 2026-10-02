# dokku proxy 文档（内置 nginx 与可换 proxy 清单）

- 来源 URL: https://github.com/dokku/dokku/blob/main/docs/networking/proxy-management.md（https://dokku.com/docs/networking/proxy-management/）
- 获取方式: gh api repos/dokku/dokku/contents/docs/networking/proxy-management.md
- 访问日期: 2026-10-02

## 关键原文

- "The default proxy shipped with Dokku is `nginx`. It can be changed via the `proxy:set` command."
- "In Dokku 0.5.0, port proxying was decoupled from the `nginx-vhosts` plugin into the proxy plugin. Dokku 0.6.0 introduced the ability to map host ports to specific container ports. This allows other proxy software - such as HAProxy or Caddy - to be used in place of nginx."
- proxy 命令组：proxy:build-config / clear-config / disable / enable / report / set

## proxies 目录（可换实现清单，docs/networking/proxies/）

- caddy.md
- haproxy.md
- nginx.md
- openresty.md
- traefik.md

（⇒ 五种 proxy 实现，默认 nginx；域名路由 → nginx 自动配置 vhost，证书由 letsencrypt 插件接管）

## 同目录旁证（docs/deployment/）

- zero-downtime-deploys.md 存在（官方文档化零停机部署）
