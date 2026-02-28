"""Secret Handshake"""

from typing import List


def commands(number: int) -> List[str]:
    """Convert a decimal number to binary, then translate that binary to a sequence of events. Return that sequence.
       1 = wink
       10 = double blink
       100 = close your eyes
       1000 = jump
       10000 = Reverse the order of the operations in the secret handshake

    Args:
        number (int): A decimal number

    Returns:
        (List[str]): A list, empty or containing strings.
                     Each string is one of wink, double blink, close your eyes, or jump.
    """
    binary_number = bin(number)[2:]
    actions = []
    reverse = False

    if binary_number.endswith("1"):
        actions.append("wink")
        binary_number = binary_number[0:-1] + "0"

    if binary_number.endswith("10"):
        actions.append("double blink")
        binary_number = binary_number[0:-2] + "00"

    if binary_number.endswith("100"):
        actions.append("close your eyes")
        binary_number = binary_number[0:-3] + "000"

    if binary_number.endswith("1000"):
        actions.append("jump")
        binary_number = binary_number[0:-4] + "0000"

    if binary_number.endswith("10000"):
        reverse = True
        binary_number = binary_number[0:-5] + "00000"

    if reverse:
        actions.reverse()

    return actions
