#!/usr/bin/env python3
"""Hand over the finished picture for the 23 November 2026 news image.

The picture was rendered earlier in the pipeline and sits beside this
script under the name ``entry.png``.  This program does nothing creative:
it places an exact copy of that file where the judging harness looks for
the entry.  Keeping the copy byte-for-byte is what makes the run
reproducible -- the file that leaves here is the file that was rendered.

Only the standard library is used.  Nothing is fetched, nothing is
generated, and nothing depends on the clock, so two runs from the same
rendered picture always produce the same bytes.
"""

import os
import shutil
import sys

PICTURE = "entry.png"
WANTED_MODE = 0o644


def complain(text):
    """Report a problem on stderr and signal failure with exit code 1."""
    print("entry deliver: " + text, file=sys.stderr)
    return 1


def run():
    """Copy the rendered picture into the harness output folder."""
    target_folder = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not target_folder:
        return complain("MAKEFUN_OUTPUT_DIR is not set")

    script_folder = os.path.dirname(os.path.abspath(__file__))
    picture_path = os.path.join(script_folder, PICTURE)
    if not os.path.isfile(picture_path):
        return complain("no " + PICTURE + " next to this script")

    os.makedirs(target_folder, exist_ok=True)

    destination = os.path.join(target_folder, PICTURE)
    shutil.copyfile(picture_path, destination)
    os.chmod(destination, WANTED_MODE)
    return 0


if __name__ == "__main__":
    sys.exit(run())
