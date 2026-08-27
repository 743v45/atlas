#!/usr/bin/env python3
"""用 gh 一手数据刷新所有 meta.json 的 stats 字段。

用法：python3 scripts/refresh-stats.py [--dry-run]

行为：
- 遍历 items/*/*/meta.json，解析 repo 字段（仅 https://github.com/<owner>/<repo> 两段式生效；
  org 页 / 空值 / 商业闭源自动跳过并说明）
- gh api 拉取 stargazers_count / pushed_at / license.spdx_id
- 写入 stats: {stars, pushed_at, license, collected_at: 今天}
- 之后跑 build-index.py 重建全部页面（stale 判定基于 collected_at）

要求 gh 已登录（gh auth login）。
"""

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEMS_DIR = ROOT / "items"
GITHUB_REPO_RE = re.compile(r"^https://github\.com/([\w.-]+)/([\w.-]+)/?$")


def repo_slug(url):
    """从 repo URL 解析 owner/repo；org 页或空值返回 None。"""
    if not url:
        return None
    m = GITHUB_REPO_RE.match(url.strip())
    return f"{m.group(1)}/{m.group(2)}" if m else None


def gh_repo_info(slug):
    """gh api 单仓库：原始 JSON 落盘到 raw/<日期>/gh/（原始数据留档，RULES 第 9 节），
    返回 (stars, pushed_date, license) 或 None。"""
    import datetime
    try:
        r = subprocess.run(
            ["gh", "api", f"repos/{slug}"],
            capture_output=True, text=True, timeout=30,
        )
    except FileNotFoundError:
        sys.exit("❌ 找不到 gh 命令，请先安装 GitHub CLI 并 gh auth login")
    if r.returncode != 0:
        return None
    # 原始响应留档（同日重复采集覆盖当日文件；跨日目录即时间序列）
    raw_dir = ROOT / "raw" / datetime.date.today().isoformat() / "gh"
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / f"{slug.replace('/', '_')}.json").write_text(r.stdout, encoding="utf-8")
    # 从留档解析（单一口径：留档文件就是数据源）
    d = json.loads(r.stdout)
    stars = d["stargazers_count"]
    pushed = d["pushed_at"][:10]
    license_ = (d.get("license") or {}).get("spdx_id") or "NOASSERTION"
    return stars, pushed, license_


def main():
    dry_run = "--dry-run" in sys.argv
    metas = []
    if ITEMS_DIR.is_dir():
        for meta_path in sorted(ITEMS_DIR.glob("*/*/meta.json")):
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            slug = repo_slug(meta.get("repo", ""))
            metas.append((meta_path, meta, slug))

    with_repo = [(p, m, s) for p, m, s in metas if s]
    skipped = [(p, m) for p, m, s in metas if not s]
    if not with_repo:
        sys.exit("没有可刷新的 meta（repo 字段均非两段式 GitHub URL）")

    # 先探测 gh 可用性
    probe = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    if probe.returncode != 0:
        sys.exit("❌ gh 未登录：先运行 gh auth login")

    changed = 0
    # 并发刷新（膨胀到几百条目仍可分钟级完成；gh 认证额度 5000/h，并发 8 安全）
    with ThreadPoolExecutor(max_workers=8) as pool:
        infos = list(pool.map(lambda t: gh_repo_info(t[2]), with_repo))
    for (meta_path, meta, slug), info in zip(with_repo, infos):
        rel = meta_path.relative_to(ROOT).as_posix()
        if info is None:
            print(f"⏭️  {rel}: gh 查询 {slug} 失败，跳过")
            continue
        stars, pushed, license_ = info
        old = meta.get("stats", {})
        new_stats = {
            "source_repo": slug,
            "stars": stars,
            "pushed_at": pushed,
            "license": license_,
            "collected_at": date.today().isoformat(),
        }
        diff = []
        for k in ("stars", "pushed_at", "license"):
            if old.get(k) != new_stats[k]:
                diff.append(f"{k}: {old.get(k, '—')} → {new_stats[k]}")
        if diff:
            print(f"📝 {rel}: " + "; ".join(diff))
        meta["stats"] = new_stats
        if not dry_run:
            meta_path.write_text(
                json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        changed += 1

    for meta_path, meta in skipped:
        print(f"⏭️  {meta_path.relative_to(ROOT).as_posix()}: repo={meta.get('repo') or '（空）'} 非项目仓库，跳过")

    mode = "（dry-run，未写盘）" if dry_run else ""
    print(f"\n✅ 刷新 {changed} 个 meta{mode}。接着跑 python3 scripts/build-index.py 重建页面。")


if __name__ == "__main__":
    main()
