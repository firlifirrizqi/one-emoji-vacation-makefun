#!/usr/bin/env python3
"""One Emoji, One Dream Vacation - Make.fun entry.

Writes exactly one emoji (no trailing newline, no extra text) to
/output/entry.txt. Stdlib only.
"""

import os
import sys

# The chosen emoji: U+1F388 BALLOON - a hot-air balloon drifting over
# Cappadocia at sunrise. A once-in-a-lifetime dream trip in one picture.
EMOJI = "\U0001F388"

OUTPUT_PATH = "/output/entry.txt"


def is_single_emoji(text: str) -> bool:
    """Validate the entry: exactly one character (one code point in Python's
    len, not bytes), non-whitespace, and in a pictographic emoji range.

    A multi-byte UTF-8 emoji is still len() == 1 in Python, so the check
    must use character count, never byte count.
    """
    if not isinstance(text, str):
        return False
    if len(text) != 1:
        return False
    if text.isspace():
        return False
    code = ord(text)
    emoji_ranges = (
        (0x1F300, 0x1FAFF),  # Misc Symbols & Pictographs, Emoticons, Transport, etc.
        (0x2600, 0x27BF),    # Misc Symbols & Dingbats
        (0x2B00, 0x2BFF),    # Misc Symbols and Arrows
        (0xFE00, 0xFE0F),    # Variation Selectors (never alone, but kept for safety)
    )
    return any(start <= code <= end for start, end in emoji_ranges)


def write_entry(path: str = OUTPUT_PATH) -> None:
    """Write the emoji to path, exactly as-is, UTF-8, no trailing newline."""
    if not is_single_emoji(EMOJI):
        raise ValueError("EMOJI constant failed validation: %r" % (EMOJI,))
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


def verify_entry(path: str = OUTPUT_PATH) -> bool:
    """Read back the written file as raw bytes and confirm it is byte-identical
    to the emoji's UTF-8 encoding (no newline, no BOM, no extra bytes)."""
    expected = EMOJI.encode("utf-8")
    with open(path, "rb") as f:
        actual = f.read()
    if actual != expected:
        raise ValueError(
            "entry.txt mismatch: got %d bytes %s, expected %d bytes %s"
            % (len(actual), actual.hex(), len(expected), expected.hex())
        )
    text = actual.decode("utf-8")
    if not is_single_emoji(text):
        raise ValueError("entry.txt failed emoji validation: %r" % (text,))
    return True


def main() -> int:
    write_entry()
    verify_entry()
    print("Wrote %r to %s (%s)" % (EMOJI, OUTPUT_PATH, EMOJI.encode("utf-8").hex()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
