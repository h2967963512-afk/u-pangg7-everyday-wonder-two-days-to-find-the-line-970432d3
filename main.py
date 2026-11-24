"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one sentence on a small moment of wonder in
# everyday life: a shadow slipping out the door ahead of its owner.
# One sentence, 104 characters — inside the 200-character gate.
# Revision note (parent pass): re-checked after the local run —
# the 104-character line is unchanged; this note only records the check.
import os

TEXT = (
    "My shadow slips out the door half a step ahead of me every "
    "morning, as if it already knows the way home."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
