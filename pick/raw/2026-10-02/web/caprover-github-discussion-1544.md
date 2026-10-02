# CapRover Discussion #1544「Stale Development」

- 来源：https://github.com/CapRover/CapRover/discussions/1544
- 访问日期：2026-10-02（WebFetch 提取）

## 原帖（Alfagun74，2022-10-24）
认为开发 "seems kinda stale at this moment"，询问原因与如何帮忙。

## 维护者 githubsaturn 回复（2022-10-24）
- 项目并非无人维护，只是新功能放缓
- 独立开发者立场："do not want to add features that'll be used by less than 5% of users"——每个新功能都增加维护负担
- CapRover 高度稳定，可靠性优先；承诺 "address any reliability issues immediately"
- 提到 netdata 过时等可通过配置覆盖解决（可扩展性优势）

## 跟帖
- drakon（2022-10-24/25）：从 Heroku 迁移考虑者；认同 "Stability should be above everything else"；澄清低活跃主要指 release 间隔超一年但 commits 仍在继续
- maietta（2022-10-26）：CapRover 定位是「部署工具到 Docker Swarm」，可从 Swarm 安全移除而应用继续运行，非 bloatware
- fu-sen（2022-10-30）：releases 少但 commits 频繁，"alive and well"
- frederikhors（2023-03-02）：催 2FA；维护者次日回复 2FA 将在未来几个月内推出

## 解读备注
「维护放缓」的担忧自 2022 年起就存在，是项目长期特征而非 2025-2026 新现象；维护者定位一贯是「稳定优先、拒绝功能膨胀」。
