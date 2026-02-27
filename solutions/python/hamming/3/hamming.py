"""Hamming"""


def distance(strand_a: str, strand_b: str) -> int:
    """Returns the number of different characters in two strings"""
    # Strands must be the same length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be the same length")

    return sum([ch1 != ch2 for ch1, ch2 in zip(strand_a, strand_b)])
