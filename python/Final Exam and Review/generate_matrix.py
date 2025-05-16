import numpy as np


def generate_matrix(potential_type: str, ndim: int, strength: float) -> np.ndarray:
    """
    Generate a Hamiltonian matrix for a given potential type.

    Parameters:
        potential_type (str): Type of potential ('Square', 'Harmonic', etc.)
        ndim (int): Number of spatial grid points
        strength (float): Strength of the potential

    Returns:
        np.ndarray: Hamiltonian matrix of shape (ndim, ndim)
    """
    # Discretize 1D space on the interval [0, 1]
    x = np.linspace(0, 1, ndim)
    dx = x[1] - x[0]

    # Kinetic energy operator (finite-difference second derivative)
    kinetic = (-2 * np.eye(ndim) + np.eye(ndim, k=1) + np.eye(ndim, k=-1)) / dx ** 2

    # Potential energy operator
    if potential_type == 'Square':
        potential = np.zeros(ndim)
    elif potential_type == 'Harmonic':
        potential = strength * (x - 0.5) ** 2
    else:
        raise ValueError(f"Unknown potential type: {potential_type}")

    potential_matrix = np.diag(potential)

    # Hamiltonian = Kinetic + Potential
    H = -0.5 * kinetic + potential_matrix
    return H
