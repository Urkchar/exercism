"""Resistor Color Duo"""


def value(colors) -> int:
    # Only check the first two colors
    colors = colors[0:2]

    res = ""
    for color in colors:
        res += str(_colors().index(color))
    return int(res)


def _colors() -> list:
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]
