"""Sum of Multiples"""


def sum_of_multiples(limit: int, multiples: list) -> int:
    """
    Returns the sum of all numbers below `limit` that a multiples of any multiple in `multiples`.
    """
    _sum = 0
    for i in range(limit):
        for multiple in multiples:
            if multiple != 0 and i % multiple == 0:
                _sum += i
                break
    return _sum
