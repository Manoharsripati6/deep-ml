import numpy as np

def pairwise_cosine_similarity(X):
    X = np.array(X, dtype=float)

    norms = np.linalg.norm(X, axis=1, keepdims=True)

    # Avoid division by zero for zero vectors
    norms[norms == 0] = 1.0

    X_normalized = X / norms

    # Pairwise cosine similarity
    S = X_normalized @ X_normalized.T

    # Round to 4 decimal places
    S = np.round(S, 4)

    return S.tolist()