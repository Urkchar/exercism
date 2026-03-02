"""This function was generated with M365 Copilot Think Deeper,
revised with the auto-generated feedback, and finally manually revised.

Rotational (Caesar) cipher implementation.

This module exposes:
- rotate(text: str, key: int) -> str
"""

__all__ = ["rotate"]


def rotate(text: str, key: int) -> str:
    """
    Apply a rotational (Caesar) cipher to ``text`` using the integer ``key``.

    Behavior:
    - Only A–Z and a–z are shifted.
    - Case is preserved.
    - Non-letters (spaces, punctuation, digits) are left unchanged.
    - Keys are normalized with modulo 26 so any integer works.

    Parameters
    ----------
    text : str
        Input text to be transformed.
    key : int
        Rotation amount. Any integer is accepted.

    Returns
    -------
    str
        The rotated (ciphered) text.
    """
    if not isinstance(key, int):
        raise TypeError("key must be an integer")

    shift = key % 26
    if shift == 0:
        return text  # small early exit

    result_chars = []
    for char in text:
        if "a" <= char <= "z":
            base = ord("a")
            result_chars.append(chr((ord(char) - base + shift) % 26 + base))
        elif "A" <= char <= "Z":
            base = ord("A")
            result_chars.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result_chars.append(char)
    return "".join(result_chars)
