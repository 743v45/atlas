#!/bin/bash
# 引擎对账(反向断言,见 ORIGIN.md):
# shared/render.py 抽取后,任何 build 脚本内不得再出现本地渲染器副本——
# 有人复制回去 = 分叉复活。输出 ✅ = 干净;列出文件 = 立即删副本接 shared。
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ATLAS="$(cd "$HERE/../../.." && pwd)"

BAD=0
for f in "$ATLAS"/pick/scripts/build-index.py \
         "$ATLAS"/apprentice/scripts/build-index.py \
         "$ATLAS"/mistakes/scripts/build-index.py \
         "$ATLAS"/scripts/build-atlas.py; do
  [ -f "$f" ] || continue
  if grep -q "^def render_inline\|^BASE_CSS = " "$f"; then
    echo "⚠️  $f 含本地渲染器副本——删除并接 atlas/shared/render.py"
    BAD=1
  fi
done
[ "$BAD" -eq 0 ] && echo "✅ 引擎单源:各 build 均无本地副本,统一挂 shared/render.py"
exit $BAD
