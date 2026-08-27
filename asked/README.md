# asked — 问答馆

「我问、AI 长答、值得留存的一切」——师父讲给你听的地形:技术原理、概念解惑、方法论讲义。apprentice 教你怎么走,asked 存你沿路学到的地理。

与姊妹馆的分界:**apprentice 收「怎么做」(方法,下次照做),asked 收「是什么/为什么」(知识,下次翻查);pick 收选型结论,mistakes 收摔跤,spark 收想去没去的地方。** 横评见 [../COMPARISON.md](../COMPARISON.md)。

**记录规则见 [RULES.md](RULES.md)。**

## 结构

```
asked/
├── README.md / RULES.md / CLAUDE.md
├── index.html               # 索引(生成物,禁止手改)
├── scripts/build-index.py
├── template/                # 新条目模板(meta.json + answer.md)
└── items/<条目>/{meta.json, answer.md, answer.html}   # 单层
```

## 快速上手

```bash
mkdir -p items/<条目>
cp template/meta.json template/answer.md items/<条目>/
# 先归档源对话到 atlas/conversations/,source 填归档路径(门禁要求存在)
python3 scripts/build-index.py
```
