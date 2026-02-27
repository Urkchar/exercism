"""Anagram"""

import collections


def find_anagrams(word: str, candidates: list) -> list:
    """Returns a list of anagrams of `word` from `candidates`"""
    anagrams = []
    word_counter = collections.Counter(word.lower())
    for candidate in candidates:
        # Words are not anagrams of themselves

        if word.lower() == candidate.lower():
            continue
        if word_counter == collections.Counter(candidate.lower()):
            anagrams.append(candidate)
    return anagrams
