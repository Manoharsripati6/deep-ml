import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.

    Args:
        matrix: A square matrix (n x n) represented as list of lists

    Returns:
        Tuple of (determinant, trace)
    """
    a = np.array(matrix)

    determinant = float(np.linalg.det(a))
    trace = float(np.trace(a))

    return determinant, trace