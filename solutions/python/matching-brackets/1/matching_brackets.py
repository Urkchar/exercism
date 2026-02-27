"""Matching Brackets"""


def is_match(bracket_1: str, bracket_2: str) -> bool:
    return bracket_1 + bracket_2 in ("()", "[]", "{}")


def get_first_closing(expression: str) -> str:
    """Returns the first instance of (, [, or { in `expression`."""
    if ")" in expression:
        parentheses_index = expression.index(")")
    else:
        parentheses_index = float("inf")

    if "]" in expression:
        bracket_index = expression.index("]")
    else:
        bracket_index = float("inf")

    if "}" in expression:
        curly_index = expression.index("}")
    else:
        curly_index = float("inf")

    lowest_closing_index = min([parentheses_index, bracket_index, curly_index])
    first_closing = expression[lowest_closing_index]
    return first_closing, lowest_closing_index


def get_rightmost_opening(expression: str) -> str:
    """Returns the rightmost occurence of an opening bracket in `expression`."""
    if "(" in expression:
        parentheses_index = expression.rindex("(")
    else:
        parentheses_index = 0

    if "[" in expression:
        bracket_index = expression.rindex("[")
    else:
        bracket_index = 0

    if "{" in expression:
        curly_index = expression.rindex("{")
    else:
        curly_index = 0

    rightmost_opening_index = max([parentheses_index, bracket_index, curly_index])
    rightmost_opening = expression[rightmost_opening_index]
    return rightmost_opening


def is_paired(input_string):
    # check parentheses
    if input_string.count("(") != input_string.count(")"):
        return False
    if "(" in input_string:
        if input_string.index("(") > input_string.index(")"):
            return False

    # check square brackets
    if input_string.count("[") != input_string.count("]"):
        return False
    if "[" in input_string:
        if input_string.index("[") > input_string.index("]"):
            return False

    # check curly braces
    if input_string.count("{") != input_string.count("}"):
        return False
    if "{" in input_string:
        if input_string.index("{") > input_string.index("}"):
            return False

    # Find the pairs
    while "(" in input_string or "[" in input_string or "{" in input_string:
        # Find the first closing bracket
        first_closing, lowest_closing_index = get_first_closing(input_string)

        # Find the first opening bracket to the left of that
        rightmost_opening = get_rightmost_opening(input_string[:lowest_closing_index])
        rightmost_opening_index = input_string[:lowest_closing_index].rindex(rightmost_opening)

        # They must match
        if not is_match(rightmost_opening, first_closing):
            return False
        else:
            # Remove the pair and continue
            input_string = input_string[:rightmost_opening_index] + input_string[rightmost_opening_index + 1:lowest_closing_index] + input_string[lowest_closing_index + 1:]

    return True
