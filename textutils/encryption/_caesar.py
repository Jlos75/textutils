"""Private Caesar-cipher implementation shared by encryption functions."""


def _shift_text(text: str, key: int) -> str:
    """Shift ASCII letters while preserving all other characters."""
    shifted = []

    for character in text:
        if "a" <= character <= "z":
            shifted.append(chr((ord(character) - ord("a") + key) % 26 + ord("a")))
        elif "A" <= character <= "Z":
            shifted.append(chr((ord(character) - ord("A") + key) % 26 + ord("A")))
        else:
            shifted.append(character)

    return "".join(shifted)
