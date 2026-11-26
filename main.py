#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

Writes one line, at most 120 characters: a weather forecast for the
nonexistent city of Flibberton. Deterministic, standard library only.
"""

import os


FORECAST = (
    "Sunny in Flibberton today, high of 74, with a 90% chance of frogs "
    "and a 10% chance the frogs are judging you."
)


def main():
    # Honour MAKEFUN_OUTPUT_DIR when set; default to /output per the kit.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
