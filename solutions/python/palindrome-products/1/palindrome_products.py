"""Palindrome Products"""


def largest(max_factor: int, min_factor: int = 0) -> tuple:
    # max_factor must be greater than min_factor
    if min_factor > max_factor:
        raise ValueError("min_factor must be less than max_factor")
    value = 0
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            if product < value:
                continue
            str_product = str(product)
            if str_product == str_product[::-1]:
                if product > value:
                    value = product
                    factors = [[i, j]]
                elif product == value:
                    factors.append([i, j])

    # If a palindrome couldn't be found in the range, return None for value
    if value == 0:
        value = None
    return value, factors


def smallest(max_factor: int, min_factor: int = 0) -> tuple:
    # max_factor must be greater than min_factor
    if min_factor > max_factor:
        raise ValueError("min_factor must be less than max_factor")
    value = float("inf")
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            if product > value:
                continue
            str_product = str(product)
            if str_product == str_product[::-1]:
                if product < value:
                    value = product
                    factors = [[i, j]]
                elif product == value:
                    factors.append([i, j])

    # If a palindrome couldn't be found in the range, return None for value
    if value == float("inf"):
        value = None
    return value, factors
