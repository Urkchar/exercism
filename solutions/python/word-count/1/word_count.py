"""Word Count"""

import collections
import string


def count_words(sentence: str) -> dict:
    """Returns each word and its count in `sentence`.
    Case insensitive.
    Ignores punctuation."""

    # Ignoring punctuation except for apostrophes
    for punct in string.punctuation.replace("'", ""):
        sentence = sentence.replace(punct, " ")

    # Normalizing whitespace
    for whitespace in string.whitespace:
        sentence = sentence.replace(whitespace, " ")
    # Flatten multiple spaces in a row
    while "  " in sentence:
        sentence = sentence.replace("  ", " ")

    # Ignore case
    sentence = sentence.lower()

    # Stripping surrounding apostrophes and separting the words
    words = [word.strip("'") for word in sentence.strip().split(" ")]

    return dict(collections.Counter(words))
