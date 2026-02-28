"""Difference of Squares"""


def square_of_sum(number: int) -> int:
    """Returns the square of the sum of the first `number` natural numbers"""
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """Returns the sum of the squares of the first `number` natural numbers"""
    return sum([n ** 2 for n in range(1, number + 1)])


def difference_of_squares(number: int) -> int:
    """
    Returns the difference in the square of the sum of the first `number` natural numbers and the
    sum of the squares of the first `number` natural numbers
    """
    return square_of_sum(number) - sum_of_squares(number)
