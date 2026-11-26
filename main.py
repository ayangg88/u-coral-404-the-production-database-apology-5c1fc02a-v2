#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

A database admin apologizes in one line for dropping the production
database: calm, slightly too casual about a disaster, and the replacement
is worse than the loss. One sentence, no explanation of the joke.
"""

import os

ENTRY = (
    "I am sorry, I dropped the production database. It is fine. "
    "I have replaced it with a spreadsheet I found on my desktop. "
    "It has one column: regrets."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
