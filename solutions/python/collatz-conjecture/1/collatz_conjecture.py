"""Collatz Conjecture"""


def steps(number: int) -> int:
    """Returns the number of steps it takes to reach 1"""
    if number <= 0:
        raise ValueError("number must be a positive integer")
    number_of_steps = 0
    while number != 1:
        number_of_steps += 1
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
    return number_of_steps
