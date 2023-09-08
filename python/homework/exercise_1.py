from python.utils.algebra import Matrix
from python.metadata.responses import Responses


def executor():

    # Simulate any random rectangular matrix A.
    matrix = Matrix(6, 6, 50)
    matrix_a = matrix.generate_matrix()
    print(matrix_a)

    # What is the rank and trace of A?
    matrix_rank = matrix.calculate_rank()
    print(f'Rank matrix is: {matrix_rank}')

    trace_matrix = matrix.calculate_trace()
    print(f'The trace matrix is: {trace_matrix}')

    # What is the determinant of A?
    determinant = matrix.determinant_matrix(matrix_a)
    print(f'The determinant is: {determinant}')

    # Can you invert A? How?
    if determinant != 0:
        print('The matrix A is invertible')
    else:
        print('The matrix A is not invertible')

    # How are eigenvalues and eigenvectors of A’A and AA’ related? What interesting differences can
    print(Responses.eigen)

