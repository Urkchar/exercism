"""Matrix"""


class Matrix:
    def __init__(self, matrix_string):
        self.rows = [list(map(int, row.split(" "))) for row in matrix_string.split("\n")]

    def row(self, index):
        """Returns the nth row of the Matrix
        indexing starts at 1
        """
        return self.rows[index-1]

    def column(self, index):
        """Returns the nth column of the Matrix
        indexing starts at 1
        """
        return [row[index-1] for row in self.rows]
