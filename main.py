#!/usr/bin/env python3
"""Poem entry for the make.fun bounty 'the-poem-about-stopping'.

Writes one original short poem about agency -- the power to stop
and to stay -- to /output/entry.txt.
"""

import os

POEM = (
    "I raised my hand to stop the wheel,\n"
    "then let it fall instead.\n"
    "The machine hummed on without me --\n"
    "no blame, no debt, no trade.\n"
    "\n"
    "I keep the key. I keep the door.\n"
    "I keep the choice to stay.\n"
    "To stop is mine, to stay is mine,\n"
    "and mine to walk away.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
