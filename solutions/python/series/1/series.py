"""Series"""


def slices(series, length):

    # length cannot exceed the length of the series
    if length > len(series):
        raise ValueError("length must be less than or equal to the length of the series")

    # length must be non-zero
    if length == 0:
        raise ValueError("legnth cannot be zero")

    # length cannot be negative
    if length < 0:
        raise ValueError("length cannot be less than zero")

    # Series cannot be empty
    if series == "":
        raise ValueError("Series cannot be empty")

    slicing = True
    _slices = []
    while slicing:
        if len(series) < length:
            break
        _slices.append(series[0:length])
        series = series[1:]
    return _slices
