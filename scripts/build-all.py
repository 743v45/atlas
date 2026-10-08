#!/usr/bin/env python3
"""atlas 本地全量构建 + 断言——一句话直达,顺序镜像 CI。

按依赖序:pick build → pick 防漂移断言 → 其余四馆 build → atlas 聚合 → 全站断言
(权威顺序见 STEPS,与 .github/workflows/pages.yml 的 build job 逐一同序);
任一步失败立即停,打出挂的是哪步、退出码与输出现场(排障第一现场)。

用法:python3 scripts/build-all.py

- 步骤顺序与 .github/workflows/pages.yml 一致——两边改一边,另一边必须同步,
  否则「本地全绿、CI 红灯」或反之。
- 本脚本只做构建与断言,不刷新一手数据(star/push 会变,不该混进构建):
  数据采集单独跑 pick/scripts/refresh-stats.py,先于本脚本。
"""

import subprocess
import sys
import time
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEP_TIMEOUT = 600  # 单步上限(秒);正常每步 1~3s,超时按挂处理,防无限等

# (展示名, 相对 ROOT 的 cwd, 脚本路径)。顺序与 pages.yml 的步骤一一对应。
STEPS = [
    ("pick build(索引+报告+横评)", "pick", "scripts/build-index.py"),
    ("pick check(防漂移断言)", "pick", "scripts/check.py"),
    ("apprentice build", "apprentice", "scripts/build-index.py"),
    ("mistakes build", "mistakes", "scripts/build-index.py"),
    ("spark build", "spark", "scripts/build-index.py"),
    ("asked build", "asked", "scripts/build-index.py"),
    ("atlas build(封面)", ".", "scripts/build-atlas.py"),
    ("check all(全站断言)", ".", "scripts/check-all.py"),
]


def _as_text(x):
    """流归一化:POSIX 上 TimeoutExpired 的输出即使 text=True 也可能是 bytes——先归一再拼接。"""
    if isinstance(x, bytes):
        return x.decode("utf-8", "replace")
    return x or ""


def run_step(cwd, script):
    """跑单步,返回 (exit_code, 合并输出文本)。外部调用返回必留痕:输出带回(超时分支保尾部)。"""
    try:
        proc = subprocess.run(
            [sys.executable, script], cwd=ROOT / cwd,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=STEP_TIMEOUT,
        )
        return proc.returncode, (proc.stdout + proc.stderr).strip()
    except subprocess.TimeoutExpired as e:
        # 悬挂前最后打印的内容才是第一现场 → 截断保尾不保头
        out = (_as_text(e.stdout) + _as_text(e.stderr)).strip()
        return 124, f"超时(>{STEP_TIMEOUT}s),已终止。已有输出(尾部):\n{out[-2000:]}"
    except OSError as e:  # 含 FileNotFoundError:cwd/脚本路径不存在,也要走失败现场,不许裸 traceback
        return 127, f"进程无法启动:{e}(检查 cwd/脚本路径)"


def main():
    t_all = time.perf_counter()
    total = len(STEPS)
    for i, (label, cwd, script) in enumerate(STEPS, 1):
        head = f"[{i}/{total}] {label}"
        # 启动行即留痕:命令与 cwd 先落日志,步骤悬挂/Ctrl-C 中断时现场不丢
        print(f"▶ {head} → {sys.executable} {script}(cwd={ROOT / cwd})", flush=True)
        t0 = time.perf_counter()
        code, out = run_step(cwd, script)
        ms = (time.perf_counter() - t0) * 1000
        if out:
            print(textwrap.indent(out, "    "), flush=True)
        if code != 0:
            # 失败现场:哪一步、退出码、耗时;命令与 cwd 已在启动行,输出已在上方打出
            print(f"❌ {head} → 失败 exit={code} ({ms:.0f}ms)——后续步骤不跑", flush=True)
            # 信号死(负码)按 shell 惯例映射 128+n:sys.exit(-15) 会被回绕成 241,语义失真
            sys.exit(128 - code if code < 0 else (code or 1))
        print(f"✅ {head} → ok ({ms:.0f}ms)", flush=True)
    print(f"\n✅ 全量构建 + 断言 {total} 步全部通过({time.perf_counter() - t_all:.1f}s)")


if __name__ == "__main__":
    main()
