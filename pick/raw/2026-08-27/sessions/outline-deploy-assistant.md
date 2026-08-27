这是 **Docker 拉取镜像时无法访问 macOS 钥匙串（keychain）** 的报错，跟镜像本身无关。
## 根因
Docker Desktop 在 macOS 上默认把 `credsStore` 设成 `osxkeychain`——也就是登录凭证存在系统钥匙串里。每次拉镜像前，Docker 都会调用 `docker-credential-osxkeychain` 去读 keychain。
但你现在这个会话「不允许用户交互」，keychain 又是锁定的状态，没法弹出密码框解锁，所以读不到凭证，直接报错退出。
关键点：你要拉的三个镜像（`redis:7-alpine`、`postgres:17-alpine`、`outlinewiki/outline:latest`）**都是公开镜像，本来不需要登录**。但因为配置了 credential store，Docker 还是机械地先去读 keychain，读失败就整个挂掉。
## 解决方案（推荐顺序）
**① 最快：解锁钥匙串**（你在本机终端、能输密码的话）
```bash
security -v unlock-keychain ~/Library/Keychains/login.keychain-db
```
会让你输入开机登录密码，输完重跑 `docker compose pull` 即可。
**② 如果你只拉公开镜像、不需要任何私有仓库登录：直接去掉 credential helper**
编辑 `~/.docker/config.json`，删掉这行：
```json
"credsStore": "osxkeychain"
```
（或把整段 `auths`/`credsStore` 相关配置清掉）。改完 Docker 就不再尝试读 keychain，公开镜像能直接拉。
> ⚠️ 代价：以后拉私有仓库镜像前需要手动 `docker login`，凭证按明文存进 `config.json`。只拉公开镜像的话没影响。
## 怎么选
- 你只是临时部署 Outline 自用 → 方案 ① 最干净，不改配置。
- 你经常碰到这个报错、且从来不拉私有镜像 → 方案 ② 一劳永逸。
先用方案 ①，输个密码就能继续。要不要我帮你看一下当前 `~/.docker/config.json` 的内容确认配置？
