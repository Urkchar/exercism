"""Raindrops"""


def convert(number) -> str:
    divisors_sounds = {
        3 : "Pling",
        5 : "Plang",
        7 : "Plong"
    }
    res = "".join([sound for divisor, sound in divisors_sounds.items() if number % divisor == 0])
    return res if res else str(number)
