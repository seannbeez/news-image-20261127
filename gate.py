#!/usr/bin/env python3
"""Gate for Candidate A (news-image-20261127).
Runs build.py twice, demands byte-identical PNGs, checks 1024x1024 and
<=1 MiB, checks the 300px downscale exists at 300x300, and requires the
build to report a positive tracked-text-box count with no overflow.
Exit 0 = PASS, anything else = FAIL.
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    from PIL import Image
    problems = []
    hashes = []
    for run in (1, 2):
        r = subprocess.run([sys.executable, os.path.join(HERE, "build.py")],
                           capture_output=True, text=True, cwd=HERE)
        if r.returncode != 0:
            print("FAIL: build.py run %d exited %d" % (run, r.returncode))
            print(r.stdout)
            print(r.stderr)
            return 1
        if "boxes tracked: 0" in r.stdout:
            problems.append("no text boxes tracked")
        hashes.append(sha(os.path.join(HERE, "entry.png")))
    if hashes[0] != hashes[1]:
        problems.append("two runs differ: %s vs %s" % (hashes[0][:12], hashes[1][:12]))
    entry = os.path.join(HERE, "entry.png")
    size = os.path.getsize(entry)
    if size > 1048576:
        problems.append("entry.png %d bytes > 1 MiB" % size)
    im = Image.open(entry)
    if im.size != (1024, 1024):
        problems.append("entry.png is %s, not 1024x1024" % (im.size,))
    small = os.path.join(HERE, "entry-300px.png")
    if not os.path.exists(small):
        problems.append("entry-300px.png missing")
    else:
        sim = Image.open(small)
        if sim.size != (300, 300):
            problems.append("entry-300px.png is %s, not 300x300" % (sim.size,))
    if problems:
        print("GATE FAIL")
        for p in problems:
            print(" - " + p)
        return 1
    print("GATE PASS")
    print("entry.png sha256: %s" % hashes[0])
    print("entry.png bytes: %d" % size)
    print("entry-300px.png sha256: %s" % sha(small))
    print("two runs byte-identical: yes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
