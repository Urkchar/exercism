"""Largest Series Product"""

from typing import List, Sequence


def product(sequence: Sequence[float]) -> int:
    """Return the result of multiply all numbers in the sequence."""
    if len(sequence) == 0:
        raise ValueError("No product of empty sequence")

    p = 1
    for element in sequence:
        p *= element

    return p


def slices(series: str, length: int) -> List[str]:
    """Return the list of contiguous substrings of given length in the order that they appear.
    
    Args:
        series (str): A sequence of digits
        length (int): The length of the substrings to be found

    Returns:
        List(str): A list of substrings found in `series` of length `length` in the order that they appear.
    """
    # length cannot exceed the length of the series
    if length > len(series):
        raise ValueError("length must be less than or equal to the length of the series")

    # length cannot be negative
    if length < 0:
        raise ValueError("length cannot be less than zero")

    slicing = True
    _slices = []
    while slicing:
        if len(series) < length:
            break
        _slices.append(series[0:length])
        series = series[1:]
    return _slices


def largest_product(series: str, size: int) -> int:
    """Return the largest product of a contiguous substring of digits.
    
    Args:
        series (str): A sequence of digits
        size (int): The length of the substring of digits

    Returns:
        (int): The greatest product of a contiguous substring of digits of length `size`
    """
    if size > len(series):
        raise ValueError("size must be less than or equal to the length of series")

    if size == 0:
        return 1

    substrings = slices(series, size)
    products = [product(list(map(int, substring))) for substring in substrings]

    return max(products)

