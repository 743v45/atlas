# spark — 奇想录

苗圃:没走通的念头、悬而未决的困惑、半成品脑洞——**apprentice 门禁拒收的一切都住这里**。三馆收结论,spark 收"想去但还没走的 Z"。

**低摩擦是核心功能,不是缺陷**:一句话想法也能存,不要求正反例、不要求验证段、无必填小节。门禁一旦严,想法就不记了,蒸发了。

**毕业制**:终态三选一——`graduated`(走通了,去向三馆或 taevas-plugins,原条目留指向)、`snoozed`(还没死,挂着)、`dropped`(放弃,留尸体 + 一行死因——防的是三个月后又想到同一个点子)。

**记录规则见 [RULES.md](RULES.md)。**

## 结构

```
spark/
├── README.md / RULES.md / CLAUDE.md
├── index.html           # 索引(生成物,禁止手改)
├── scripts/build-index.py
├── template/            # 新念头模板(meta.json + spark.md)
└── items/<念头>/{meta.json, spark.md, spark.html}   # 单层
```

## 快速上手

```bash
mkdir -p items/<念头>
cp template/meta.json template/spark.md items/<念头>/
# spark.md 一句话也行——低摩擦是功能
python3 scripts/build-index.py
```
