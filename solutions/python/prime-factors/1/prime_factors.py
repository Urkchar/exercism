"""Prime Factors"""


def factors(value: int) -> list:
    """Returns a list containing the prime factors of `value`"""
    prime_factors = []
    # Edge case
    if value == 1:
        return prime_factors

    divisor = 2
    while value != 1:
        if value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
        else:
            divisor += 1
    return prime_factors
