import numpy as np

def transform_matrix(A: list[list[int | float]],
                     T: list[list[int | float]],
                     S: list[list[int | float]]) -> list[list[int | float]]:
    A = np.array(A, dtype=float)
    T = np.array(T, dtype=float)
    S = np.array(S, dtype=float)

    try:
        if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
            return -1

        transformed_matrix = np.linalg.inv(T) @ A @ S
        return np.round(transformed_matrix, 4).tolist()

    except np.linalg.LinAlgError:
        return -1