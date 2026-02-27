"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category) -> int:
    if category == YACHT:
        if is_yacht(dice):
            return 50
        else:
            return 0

    if category == ONES:
        return 1 * dice.count(1)

    if category == TWOS:
        return 2 * dice.count(2)

    if category == THREES:
        return 3 * dice.count(3)

    if category == FOURS:
        return 4 * dice.count(4)

    if category == FIVES:
        return 5 * dice.count(5)

    if category == SIXES:
        return 6 * dice.count(6)

    if category == FULL_HOUSE:
        if is_full_house(dice):
            return sum(dice)
        else:
            return 0

    if category == FOUR_OF_A_KIND:
        if is_four_of_a_kind(dice):
            return most_common(dice) * 4
        else:
            return 0

    if category == LITTLE_STRAIGHT:
        if is_little_straight(dice):
            return 30
        else:
            return 0

    if category == BIG_STRAIGHT:
        if is_big_straight(dice):
            return 30
        else:
            return 0

    if category == CHOICE:
        return sum(dice)


def most_common(elements: list):
    """Returns the most common element of `elements`"""
    return max(set(elements), key=elements.count)


def is_yacht(dice: list) -> bool:
    """Returns True if all dice show the same face"""
    return dice.count(dice[0]) == len(dice)


def is_full_house(dice: list) -> bool:
    """Returns True if there's three of one number and two of a different number"""
    dice.sort()
    two = dice.count(dice[0]) == 2 or dice.count(dice[-1]) == 2
    three = dice.count(dice[0]) == 3 or dice.count(dice[-1]) == 3
    return two and three


def is_four_of_a_kind(dice: list) -> bool:
    """Returns True if at least 4 of the dice show the same face"""
    dice.sort()
    return dice.count(dice[0]) >= 4 or dice.count(dice[-1]) >= 4


def is_little_straight(dice: list) -> bool:
    dice.sort()
    return dice == [1, 2, 3, 4, 5]

def is_big_straight(dice: list) -> bool:
    dice.sort()
    return dice == [2, 3, 4, 5, 6]
