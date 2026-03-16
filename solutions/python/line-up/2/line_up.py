"""Module providing a function printing '{name}, you are the {ordinal} customer
we serve today. Thank you!'

Rules:
    Numbers ending in 1 (unless ending in 11) → "st"
    Numbers ending in 2 (unless ending in 12) → "nd"
    Numbers ending in 3 (unless ending in 13) → "rd"
    All other numbers → "th"

Examples:
    "Mary", 1 → "Mary, you are the 1st customer we serve today. Thank you!"
    "John", 12 → "John, you are the 12th customer we serve today. Thank you!"
    "Dahir", 162 → "Dahir, you are the 162nd customer we serve today. Thank 
    you!"
"""

import re


def line_up(name: str, number: int) -> str:
    """Returns a sentence addressing a customer by name, telling them what
    number they are, and thanking them.
    """
    number = str(number)

    if re.search(r"(?<!1)1$", number):
        ordinal = number + "st" 
    elif re.search(r"(?<!1)2$", number):
        ordinal = number + "nd"
    elif re.search(r"(?<!1)3", number):
        ordinal = number + "rd"
    else:
        ordinal = number + "th"

    return f"{name}, you are the {ordinal} customer we serve today. Thank you!"
