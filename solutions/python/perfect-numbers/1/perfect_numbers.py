def classify(number):
    """Classifies a number into perfect, abundant, or deficient"""
    # Non positive numbers are regected
    if number <= 0:
        raise ValueError("number must be a positive integer")

    div_sum = aliquot_sum(number)
    if div_sum == number:
        return "perfect"
    elif div_sum > number:
        return "abundant"
    else:
        return "deficient"


def aliquot_sum(n: int) -> int:
    """Returns the sum of hte divisors of `n` not including `n`"""
    divisors = []
    if n == 1:
        return sum(divisors)
    else:
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors)
