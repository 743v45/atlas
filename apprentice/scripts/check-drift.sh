#!/bin/bash
# 引擎对账(血缘与纪律见同目录 ORIGIN.md):
# 精确 diff 两库共享的 Markdown 渲染器(render_inline → render_markdown 整块)。
# 输出 ✅ = 共享层同步;有 diff = 逐处确认「故意的分叉」还是「忘了同步」,当天处理。
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
PICK="$(dirname "$HERE")/../pick/scripts/build-index.py"
APP="$HERE/build-index.py"

[ -f "$PICK" ] || { echo "⚠️  找不到 pick 的引擎:$PICK"; exit 2; }

# 抽取 def render_inline 起到下一个 "#####" 分隔线为止的函数块
extract() { sed -n '/^def render_inline/,/^# =\{10,\}$/p' "$1" | sed '$d'; }

if diff <(extract "$PICK") <(extract "$APP") > /tmp/apprentice-drift.txt; then
  echo "✅ 渲染引擎同步"
else
  echo "⚠️  渲染引擎漂移(详见 /tmp/apprentice-drift.txt):确认是故意的分叉还是忘了同步(ORIGIN.md 同步纪律)"
  cat /tmp/apprentice-drift.txt
fi
