"""Raindrops"""


def convert(number) -> str:
    res = ""
    divisors_sounds = {
        3 : "Pling",
        5 : "Plang",
        7 : "Plong"
    }
    for divisor, sound in divisors_sounds.items():
        if number % divisor == 0:
            res += sound
    return res if res else str(number)
