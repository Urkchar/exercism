"""Darts"""


def score(x, y) -> int:
    """Scores a throw of a dart"""
    distance = distance_to_origin(x, y)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0


def distance_to_origin(x, y) -> float:
    """Returns the distance of a coordinate point to (0, 0)"""
    return (x ** 2 + y ** 2) ** 0.5
