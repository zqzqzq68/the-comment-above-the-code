#!/usr/bin/env python3
"""The Comment Above the Code.

Writes one line to /output/entry.txt: the comment a developer left
above fragile production code, funny because it is true.
"""

import os

LINE = (
    "Everything below this line is wrong, but it is wrong in exactly "
    "the way the payment provider expects, so leave it wrong."
)


def main() -> None:
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
