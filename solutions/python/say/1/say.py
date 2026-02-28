"""Say"""


def hundred(number: int) -> str:
    """Return the English representation of number between 1 and 999.
    
    Args:
        number (int): 1 <= number <= 999

    Returns:
        (str): The English, string representation of number
    """
    if number == 0:
        return ""

    if not (1 <= number <= 999):
        raise ValueError("Number must be between 1 and 999 (inclusive)")

    hundreds_and_ones = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    if len(str(number)) == 3:
        base = hundreds_and_ones[str(number)[0]] + " hundred"
        if number % 100 == 0:
            return base
        else:
            number = number % 100
            return base + " " + hundred(number)

    if len(str(number)) == 2:
        if 10 <= number <= 19:
            teens = {
                "10": "ten",
                "11": "eleven",
                "12": "twelve",
                "13": "thirteen",
                "14": "fourteen",
                "15": "fifteen",
                "16": "sixteen",
                "17": "seventeen",
                "18": "eighteen",
                "19": "nineteen"
            }
            return teens[str(number)]
        else:
            tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
            base = tens[number // 10 - 2]

            # Check if a hyphen needs to be added for a number in the ones place
            if number % 10 == 0:
                return base
            else:
                return base + "-" + hundred(number % 10)

    if len(str(number)) == 1:
        return hundreds_and_ones[str(number)]


def say(number: int) -> str:
    """Return the English representation of an integer.
    
    Args:
        number (int): 0 <= number <= 999999999999

    Returns:
        (str): The English, string representation of number
    """
    # Negative numbers are not allowed
    if number < 0:
        raise ValueError("number must be non-negative")

    # Number must not be too large
    if number > 999999999999:   # Nine hundred nintey-nine billion
        raise ValueError("Number too great")

    if number == 0:
        return "zero"

    english_number = ""
    str_number = str(number)

    # If the length of the number is not a multiple of 3, lpad zeroes to make chunking easier
    while len(str_number) % 3 != 0:
        str_number = "0" + str_number

    # Break number up into chunks of thousands
    chunk_length = 3
    chunks = [str_number[i:i+chunk_length] for i in range(0, len(str_number), chunk_length)]

    # Remove the leading zeroes if necessary
    chunks[0] = str(int(chunks[0]))

    # Substitute decimal numbers for English numbers
    chunks = [hundred(int(chunk)) for chunk in chunks]

    # Insert the appropriate scale word between the chunks
    if len(chunks) >= 4:
        english_number += chunks[-4] + " billion "

    if len(chunks) >= 3 and chunks[-3] != "":
        english_number += chunks[-3] + " million "

    if len(chunks) >= 2 and chunks[-2] != "":
        english_number += chunks[-2] + " thousand "

    english_number += chunks[-1]

    return english_number.strip()
