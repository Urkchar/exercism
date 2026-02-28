"""Sieve"""

import math


def primes(limit: int) -> list:
    """Returns all prime numbers from 2 through limit."""
    prime_numbers = []
    if limit < 2:
        return prime_numbers

    prime_numbers = [True] * (limit + 1)
    # 0 and 1 are not prime
    prime_numbers[0] = False
    prime_numbers[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime_numbers[i] is True:
            for j in range(i ** 2, limit + 1, i):
                prime_numbers[j] = False

    return [i for i, primality in enumerate(prime_numbers) if primality is True]
