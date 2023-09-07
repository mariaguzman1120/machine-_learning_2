class Responses:
    eigen = """
        The eigenvalues and eigenvectors of A'A and AA' are related, but 
        they represent different aspects of the matrix. A'A is a square 
        symmetric matrix, so its eigenvalues are real and non-negative, and 
        its eigenvectors are orthogonal. AA' may not be square, so it 
        doesn't necessarily have real eigenvalues or orthogonal 
        eigenvectors.
    """

    inverse_matrix = """
        Whether you can invert matrix A depends on its properties. 
        If the matrix is square and has full rank (i.e., its rows and columns 
        are linearly independent), then you can invert it. To invert matrix A, 
        you can use methods like Gaussian elimination or matrix inversion 
        formulae.
    """

    distance_face = """
        This calculation computes the pixel-wise difference between your face 
        and the average face, and then calculates the magnitude of that 
        difference vector. The resulting value represents the Euclidean 
        distance between the two faces.
    """