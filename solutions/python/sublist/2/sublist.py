"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def list_contains_list(list_one, list_two):
    """Return True if list_one contains list_two, False otherwise"""

    list_two_length = len(list_two)
    for i in range(len(list_one)):
        if list_one[i:i + list_two_length] == list_two:
            return True
    
    return False


def sublist(list_one, list_two):
    """Given two lists, return whether they are equal, one contains the other,
    one is contained by the other, or they are unequal."""

    # List A is equal to list B
    if list_one == list_two:
        return EQUAL
    
    # List A contains list B (A is a superlist of B)
    if list_contains_list(list_one, list_two) is True:
        return SUPERLIST
        
    # List A is contained by list B (A is a sublist of B)
    if list_contains_list(list_two, list_one) is True:
        return SUBLIST
        
    # None of the above are true, thus lists A and B are unequal
    return UNEQUAL
