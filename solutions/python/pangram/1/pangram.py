"""Pangram"""

import string


def is_pangram(sentence) -> bool:
    for letter in string.ascii_lowercase:
        if letter not in sentence.lower():
            return False
    return True
