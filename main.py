#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line, at most 140 characters, in which a robot vacuum
explains why it missed a spot, to /output/entry.txt.
"""
import os

EXCUSE = "My sensors found a dust-bunny union meeting under the sofa, so I left that spot alone — I don't cross picket lines."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
