#!/usr/bin/env python3
"""Worst AI Advice entry: one line of the worst possible advice an AI
could give, in 140 characters or fewer, written to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "Quick tip: to fully charge your phone in 30 seconds, pop it in the "
    "microwave on high - it's faster than any cable."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
