"""Module providing functions for translating text into Pig Latin."""

import re


def translate_word(word):
    """
    
    :param word: str to translate into Pig Latin.
    :return: str translated into Pig Latin.

    This funciton takes a `word` string and returns the string translated into Pig Latin.
    """
    # Rule 1
    pattern = r"[aeiou]|xr|yt"
    if re.match(pattern, word):
        # return "Rule 1"
        return word + "ay"

    # Rule 3
    pattern = r"[b-df-hj-np-tv-z]*qu"
    if result := re.match(pattern, word):
        return word[result.end():] + result[0] + "ay"

    # Rule 4
    pattern = r"[b-df-hj-np-tv-z]+(y)"
    if result := re.match(pattern, word):
        return word[result.end() - 1:] + result[0][:-1] + "ay"

    # Rule 2
    pattern = r"[b-df-hj-np-tv-z]+"
    if result := re.match(pattern, word):
        return word[result.end():] + result[0] + "ay"
    
    return None


def translate(text):
    """
    
    :param text: str of one or more words to translate into Pig Latin.
    :return: str of one or more words translated into Pig Latin.

    The funciton takes in a string of words and returns the string of words translated into Pig Latin.
    """
    words = text.split()
    return " ".join(translate_word(word) for word in words)
