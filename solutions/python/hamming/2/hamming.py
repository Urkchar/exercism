"""Hamming"""


def distance(strand_a: str, strand_b: str) -> int:
    """Returns the number of different characters in two strings"""
    # Strands must be the same length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be the same length")

    return sum([1 for character1, character2 in zip(strand_a, strand_b) if character1 != character2])
