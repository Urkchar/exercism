"""ISBN Verifier"""


def is_valid(isbn):
    """Checkis if `isbn` is a valid ISBN-10"""

    # Remove the dashes
    isbn = isbn.replace("-", "")

    # Check length
    if len(isbn) != 10:
        return False

    # Multiply each digit descending from 10
    mults = []
    for i, digit in zip(range(10, 0, -1), isbn):

        # Check for illegal characters
        if digit not in "0123456789X":
            return False

        # X can only be the check digit
        if digit == "X" and i != 1:
            return False
        if i == 1 and digit == "X":
            mults.append(i * 10)
        else:
            mults.append(i * int(digit))

    # If the sum of the results mod 11 is 0, it is valid
    if sum(mults) % 11 == 0:
        return True
    else:
        return False
