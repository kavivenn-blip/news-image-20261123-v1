#!/usr/bin/env python3
"""Seven Drones, One Comeback -- news-image-20261123 V1 entrypoint.

Writes the pre-rendered entry.png that sits next to this file into the
make.fun output directory. Pure Python standard library: no network,
no randomness, no timestamps, no font loading while it runs.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not SRC.is_file():
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    dst = Path(out_dir) / "entry.png"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, dst)
    dst.chmod(0o644)
    print("copied entry.png -> %s (%d bytes)" % (dst, dst.stat().st_size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
