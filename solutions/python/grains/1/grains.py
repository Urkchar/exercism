"""Grains"""


def square(number: int) -> int:
    # number must be between 1 and 64 (inclusive)
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("number must be between 1 and 64 (inclusive)")


def total() -> int:
    return sum([square(i) for i in range(1, 65)])
