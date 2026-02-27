"""Acronym"""


def abbreviate(words: str) -> str:
    """Convert a phrase to its acronym and return it.
    
    Args:
        words (str): A series of sequences of characters separated by spaces or hyphens.

    Returns:
        (str): The first letter of each word concatenated and capitalized.
    """
    # Underscores are ignored
    words = words.replace("_", "")

    # Hyphens are treated as spaces
    words = words.replace("-", " ")

    # Split the phrase into individual words
    words_list = words.split()

    # For each word, take the first letter, capitalizee it, and add it to the acronym
    letters = [word[0] for word in words_list]

    return "".join(letters).upper()
