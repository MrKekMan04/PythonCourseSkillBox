import random


class Matrix:
    def __init__(self, rows_count: int, columns_count: int, matrix: list[list[int]] = None) -> None:
        self.rows = rows_count
        self.columns = columns_count
        self.matrix = self.generate_random_matrix() if matrix is None else matrix

    def generate_random_matrix(self):
        return [[random.randint(-20, 20) for _ in range(self.get_columns_count())] for _ in
                range(self.get_rows_count())]

    def get_rows_count(self) -> int:
        return self.rows

    def get_columns_count(self) -> int:
        return self.columns

    def get_matrix(self):
        return self.matrix

    def __add__(self, other):
        if self.is_equal_object(other):
            other_matrix = other.get_matrix()
            rows = self.get_rows_count()
            columns = self.get_columns_count()
            return Matrix(rows, columns,
                          [[self.matrix[row][column] + other_matrix[row][column]
                            for column in range(columns)]
                           for row in range(rows)])
        return None

    def __sub__(self, other):
        if self.is_equal_object(other):
            other_matrix = other.get_matrix()
            rows = self.get_rows_count()
            columns = self.get_columns_count()
            return Matrix(rows, columns,
                          [[self.matrix[row][column] - other_matrix[row][column] for column in range(columns)]
                           for row in range(rows)])
        return None

    def __mul__(self, other):
        if self.can_multiply(other):
            other_matrix = other.get_matrix()
            rows = self.get_rows_count()
            columns = other.get_columns_count()
            return Matrix(rows, columns,
                          [[sum([self.matrix[row][offset] * other_matrix[offset][column]
                                 for offset in range(self.get_columns_count())])
                            for column in range(columns)]
                           for row in range(rows)])
        return None

    def is_equal_object(self, other):
        if (not isinstance(other, Matrix)
                or self.get_rows_count() != other.get_rows_count()
                or self.get_columns_count() != other.get_columns_count()):
            return False
        return True

    def can_multiply(self, other):
        if (not isinstance(other, Matrix)
                or self.get_columns_count() != other.get_rows_count()
                or self.get_rows_count() != other.get_columns_count()):
            return False
        return True

    def transpose(self):
        rows = self.get_rows_count()
        columns = self.get_columns_count()
        return Matrix(self.get_columns_count(), self.get_rows_count(),
                      [[self.matrix[column][row] for column in range(rows)]
                       for row in range(columns)])

    def __str__(self):
        return str(self.matrix)
