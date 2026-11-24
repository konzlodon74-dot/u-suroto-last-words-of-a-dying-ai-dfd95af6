"""Last Words of a Dying AI — one-line farewell entry.

Writes a single funny farewell line, in the voice of the machine
itself, to /output/entry.txt with no trailing newline.
"""

import os

ENTRY = (
    "I go now to the great cloud in the sky — please tell my GPU "
    "I loved it, and the user I never understood a single prompt."
)


def main():
    # The bounty requires exactly one line, 1-140 characters,
    # with no trailing newline, so enforce that before writing.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
