import numpy as np

def calculate_lowest_eigenvectors(square_matrix: np.ndarray, number_of_eigenvectors: int = 3):
    """
    Identify eigenvectors with the smallest K eigenvalues using NumPy's eig function.

    Parameters:
    square_matrix (ndarray): shape (M, M), must be square.
    number_of_eigenvectors (int): K smallest eigenvectors to return (default: 3)

    Returns:
    eigenvalues (ndarray): shape (K,), lowest eigenvalues sorted in ascending order.
    eigenvectors (ndarray): shape (K, M), each row is an eigenvector corresponding to eigenvalues.
    """
    if square_matrix.ndim != 2 or square_matrix.shape[0] != square_matrix.shape[1]:
        raise ValueError("Input must be a square matrix.")

    M = square_matrix.shape[0]
    if number_of_eigenvectors < 1 or number_of_eigenvectors > M:
        raise ValueError("number_of_eigenvectors must be between 1 and matrix size M")

    # Compute all eigenvalues and eigenvectors
    eigenvalues_all, eigenvectors_all = np.linalg.eig(square_matrix)

    # Sort indices by eigenvalue (ascending)
    sorted_indices = np.argsort(eigenvalues_all)

    # Get the K smallest eigenvalues and corresponding eigenvectors
    selected_indices = sorted_indices[:number_of_eigenvectors]
    eigenvalues = np.real(eigenvalues_all[selected_indices])
    eigenvectors = np.real(eigenvectors_all[:, selected_indices].T)

    return eigenvalues, eigenvectors
