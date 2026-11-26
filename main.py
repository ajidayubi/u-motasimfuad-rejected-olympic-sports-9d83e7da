"""Rejected Olympic Sports entry: one funny single-line sport.

The program holds the line in one constant, checks it fits the gate
(1 to 200 characters, not only whitespace), and writes exactly that
line, with no trailing newline, to entry.txt in the output directory
the grader provides. It prints the line and its character count.
"""

import os
import sys

LINE = (
    "Competitive microwave watching: athletes heat one bowl of soup "
    "for four minutes, and the first to open the door early is out "
    "\u2014 the soup is cold in the middle no matter who wins."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print(
            f"entry line must be 1-200 non-blank characters, got {len(LINE)}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
