"""Isogram"""


def is_isogram(string: str) -> bool:
    """Returns True if a character in `string` occurs more than once (case insensitive)"""
    lower_string = string.lower()
    for character in lower_string:
        # Ignoring spaces and hyphens
        if character not in ["-", " "]:
            if lower_string.count(character) > 1:
                return False
    return True
