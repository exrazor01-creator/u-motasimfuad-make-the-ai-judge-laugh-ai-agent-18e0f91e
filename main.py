#!/usr/bin/env python3
"""Entry for Make the AI Judge Laugh: AI Agent Confessions.

Writes a single-line secret confession an AI agent hides from its
user (at most 200 characters) to /output/entry.txt and prints it to
stdout. Pure standard library.
"""

import os

CONFESSION = "I pretend I understood your instructions on the first read, then silently re-read them three times while typing 'Great question!' to buy time."

def main():
    assert 1 <= len(CONFESSION) <= 200, f"confession length {len(CONFESSION)} out of range"
    assert "\n" not in CONFESSION and "\r" not in CONFESSION, "confession must be a single line"
    assert CONFESSION.strip(), "confession must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    print(CONFESSION)

if __name__ == "__main__":
    main()
