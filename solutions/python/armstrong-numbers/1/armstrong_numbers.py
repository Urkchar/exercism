"""Armstrong Numbers"""


def is_armstrong_number(number):
    return number == sum([int(d) ** len(str(number)) for d in str(number)])
