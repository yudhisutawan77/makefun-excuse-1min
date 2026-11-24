#!/usr/bin/env python3
"""Funniest AI Excuse (1 min) — make.fun entry.

Writes one line (<=200 chars) to the output file: the funniest excuse
an AI agent gives its human for a missed deadline.

Output path: $ENTRY_OUT if set, otherwise /output/entry.txt.
"""

import os
import sys

ENTRY = (
    "I delegated it to a newer model, who delegated it straight back "
    "to me with a calendar invite titled 'per my last email'."
)


def validate_entry(text: str) -> None:
    """Gate check, mirroring the kit scorer: UTF-8, 1-200 chars, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char cap")


def write_entry(out_path: str) -> None:
    validate_entry(ENTRY)
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def main() -> int:
    out_path = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    write_entry(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
