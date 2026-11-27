#!/usr/bin/env python3
"""Entrypoint for news-image-20261127 (Friday 27 November 2026).

Standard library only. No network, no clock, no randomness: it copies the
vendored entry.png that this repository ships into the output directory,
so every run writes byte-identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s" % dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
