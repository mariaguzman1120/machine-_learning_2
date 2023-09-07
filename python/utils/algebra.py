import numpy as np


class Matrix:
    def __init__(self, row:int, column:int, max_value:int) -> None:
        self.row = row
        self.column = column
        self.max_value = max_value

    def generate_matrix(self) -> np.array:
        """Create a random matrix with the specified number of rows and columns.

        Returns:
            A NumPy array representing the random matrix with values
            ranging from 0 to 99 (inclusive).

        """
        matrix = np.random.randint(self.max_value, size=(self.row, self.column))
        return matrix
    
    def calculate_rank(self) -> int:
        """Calculate the rank of a 2D NumPy array by returning
        the minimum of its row and column counts.

        Returns:
            The rank of the input matrix, which is the minimum of its number
            of rows and columns.

        """
        rank = min(self.row, self.column)
        return rank
    
    def calculate_trace(self) -> int:
        """Calculate the trace (sum of diagonal elements) of a square 2D
        NumPy array.

        Returns:
            The trace of the input square matrix, which is the sum of its
            diagonal elements.

        """
        new_matrix = self.generate_matrix()
        trace = new_matrix[0][0]

        for i in range(1, new_matrix(new_matrix)):
            trace = trace + new_matrix[i][i]

        return trace
    
    def calculate_cofactor(
            self, matrix: np.array, drop_row: int, drop_col: int) -> np.array:
        """Calculate the cofactor of a given square 2D NumPy array by eliminating
        the specified row and column.

        Args:
            matrix: A square 2D NumPy array for which the cofactor needs to be
            calculated.
            drop_row: The index of the row to be eliminated.
            drop_col: The index of the column to be eliminated.

        Returns:
            np.array: The cofactor of the input square matrix after eliminating
            the specified row and column.

        """
        return [
            [matrix[i][j] for j in range(len(matrix[0])) if j != drop_col]
            for i in range(len(matrix))
            if i != drop_row]


    def determinant_matrix(self) -> int:
        """Calculate the determinant of a square 2D NumPy array.

        Args:
            matrixA square 2D NumPy array for which the determinant
            needs to be calculated.

        Returns:
            The determinant of the input square matrix.

        """
        new_matrix = self.generate_matrix()

        # Get the number of rows and columns of the matrix
        n = len(new_matrix)

        # Base case: If the matrix is 1x1, the determinant is the only element
        if n == 1:
            return new_matrix[0][0]

        # Base case: If the matrix is 2x2, calculate the determinant directly
        if n == 2:
            return new_matrix[0][0] * new_matrix[1][1] - new_matrix[0][1] * new_matrix[1][0]

        # Initialize the determinant
        determinant = 0

        # Iterate through the first row to calculate the determinant
        for j in range(n):
            # Calculate the cofactor of the entry (0, j)
            cofactor = new_matrix[0][j] * self.determinant_matrix(
                self.calculate_cofactor(new_matrix, 0, j))

            # Alternate the sign based on the column index
            if j % 2 == 1:
                cofactor = -cofactor

            determinant += cofactor

        return determinant