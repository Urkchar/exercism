"""Grains"""


def square(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f"number must be an instance of int, not {type(number)}")

    # number must be between 1 and 64 (inclusive)
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("number must be between 1 and 64 (inclusive)")


def total() -> int:
    return sum([square(i) for i in range(1, 65)])
