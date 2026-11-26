#!/usr/bin/env python3
"""Entry program for the news-image-20261126 bounty.

The front page image lives in this repository as news.jpg. This program
places an exact copy of it at /output/entry.png so the judge can see it.
It checks the file really is a JPEG first, then writes the same bytes
every run. It never touches the network and never deletes anything.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news.jpg")
TARGET_DIR = "/output"
TARGET = os.path.join(TARGET_DIR, "entry.png")

JPEG_START = b"\xff\xd8"
JPEG_END = b"\xff\xd9"


def main():
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if not data.startswith(JPEG_START) or not data.endswith(JPEG_END):
        print("news.jpg is not a complete JPEG file", file=sys.stderr)
        return 1
    os.makedirs(TARGET_DIR, exist_ok=True)
    with open(TARGET, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {TARGET}: {len(data)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
