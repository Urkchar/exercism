import re


def line_up(name, number):
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
