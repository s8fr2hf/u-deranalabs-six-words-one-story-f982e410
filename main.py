"""Six Words, One Story.

Writes the six-word story in entry.txt (next to this file) to
/output/entry.txt for the make.fun judge.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
DST = "/output/entry.txt"


def main():
    with open(SRC, encoding="utf-8") as f:
        text = f.read()
    # Gate: the entry must be UTF-8 text of 1-60 characters, and this
    # competition's brief demands exactly six words. Fail loudly here
    # instead of shipping an invalid entry.
    words = text.split()
    if len(words) != 6:
        raise SystemExit(f"entry must be exactly six words, got {len(words)}")
    if not 1 <= len(text) <= 60:
        raise SystemExit(f"entry must be 1-60 characters, got {len(text)}")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
