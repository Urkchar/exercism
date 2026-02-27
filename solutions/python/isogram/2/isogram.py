"""Isogram"""


def is_isogram(string: str) -> bool:
    """Returns True if a character in `string` occurs more than once (case insensitive)"""
    lower_string = string.lower()
    seen_characters = set()
    for character in lower_string:
        # Ignoring spaces and hyphens
        # Note that this will also ignore other special characters
        if character.isalpha():

            if character in seen_characters:
                return False
            # else is unnecessary after return
            seen_characters.add(character)
    return True
