"""Triangle"""


def equilateral(sides):
    """Returns True if all of the sides of the Triangle have the same length"""
    # A side of length zero means the shape isn't a triangle
    if 0 in sides:
        return False

    return len(set(sides)) == 1


def isosceles(sides):
    """Returns True if at least two of the sides have the same length"""
    # The sum of the two smallest sides must be greater than or equal to (degenerate) the largest
    # side
    sorted_sides = sorted(sides)
    if sorted_sides[0] + sorted_sides[1] < sorted_sides[2]:
        return False

    return len(set(sides)) <= 2


def scalene(sides):
    """Returns True if all sides have different lengths"""
    # The sum of the two smallest sides must be greater than or equal to (degenerate) the largest
    # side
    sorted_sides = sorted(sides)
    if sorted_sides[0] + sorted_sides[1] < sorted_sides[2]:
        return False

    return len(set(sides)) == 3
