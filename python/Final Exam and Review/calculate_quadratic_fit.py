import numpy as np

def calculate_quadratic_fit(data: np.ndarray) -> np.ndarray:
    """
    Fit a quadratic polynomial to x-y data.

    Parameters:
    data (ndarray): A 2xM ndarray where first row is x and second row is y.

    Returns:
    ndarray: Quadratic polynomial coefficients [c0, c1, c2]
             where the polynomial is c0 + c1*x + c2*x^2

    Raises:
    IndexError: If data does not have shape (2, M) with M > 1
    """
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError("Data must be a 2xM ndarray with M > 1")

    x = data[0]
    y = data[1]

    # np.polyfit returns coefficients in descending order: [a, b, c] for ax^2 + bx + c
    coeffs = np.polyfit(x, y, deg=2)

    # Reverse to return in order: [c0, c1, c2]
    return coeffs[::-1]
