"""Saddle Points"""


def column(rows: list, index: int) -> list:
    """Returns the nth column of the Matrix
    indexing starts at 1
    """
    return [row[index-1] for row in rows]


def saddle_points(matrix: list) -> list:
    # Matrix must be regular
    # That means that all rows are the same length
    lengths = [len(row) for row in matrix]
    if len(set(lengths)) not in [1, 0]:
        raise ValueError("Matrix must be regular. All rows must have the same length.")

    _saddle_points = []
    for row_index, row in enumerate(matrix, start=1):
        for column_index, point in enumerate(row, start=1):
            if max(row) <= point <= min(column(matrix, column_index)):
                _saddle_points.append({"row":row_index, "column":column_index})
    return _saddle_points
