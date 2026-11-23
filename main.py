#!/usr/bin/env python3
"""One-line roast: my robot vacuum vs my charging cable.

Writes a single original roast (one line, 1-200 characters) to
$OUTPUT_DIR/entry.txt (default /output/entry.txt). Deterministic:
every run writes byte-identical output.
"""

import os

ROAST = (
    'My robot vacuum has mapped my flat to the centimetre, yet every '
    'morning it still drags my charging cable home like a trophy: '
    '"I found the snake again."'
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
