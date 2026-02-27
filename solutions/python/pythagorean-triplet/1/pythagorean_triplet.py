"""Pythagorean Triplet"""


def triplets_with_sum(number: int) -> list:
    """Returns a list containing all lists of Pythagorean triplets that sum to `number`."""
    triplets = []
    for i in range(1, number + 1):
        for j in range(i + 1, number + 1 - i):
            k = number - i - j
            if is_triplet([i, j, k]):
                triplets.append([i, j, k])
    return triplets


def triplets_in_range(start, end):
    pass


def is_triplet(triplet: list) -> bool:
    """Returns true if the three numbers in `triplet` make a Pythagorean triplet."""
    a, b, c = triplet

    return a < b < c and a ** 2 + b ** 2 == c ** 2
