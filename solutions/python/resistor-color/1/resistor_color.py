"""Resistor Color"""


def color_code(color) -> int:
    return colors().index(color)


def colors() -> list:
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
