"""Worst Fix Ever: Funniest Commit Message.

Writes the single commit-message entry to entry.txt.
Pure Python standard library only.
"""

import os

ENTRY = "Fix slow search by caching empty results; users now get nothing, instantly"

# Entry gate: one line, 1-100 chars, as the bounty requires.
assert 1 <= len(ENTRY) <= 100, "entry must be 1-100 chars"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
