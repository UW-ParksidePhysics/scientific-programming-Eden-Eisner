import numpy as np

def fit_curve_array(quadratic_coefficients: np.ndarray,
                    minimum_x: float,
                    maximum_x: float,
                    number_of_points: int = 100) -> np.ndarray:
    """
    Generate an x-y curve from a quadratic polynomial over a specified range.

    Parameters:
    quadratic_coefficients (ndarray): [c0, c1, c2] for y = c0 + c1*x + c2*x^2
    minimum_x (float): Minimum x-value
    maximum_x (float): Maximum x-value
    number_of_points (int): Number of points for the curve (default: 100)

    Returns:
    ndarray: Array of shape (2, N) where N = number_of_points

    Raises:
    ArithmeticError: If maximum_x < minimum_x
    IndexError: If number_of_points <= 2
    """
    if maximum_x < minimum_x:
        raise ArithmeticError("maximum_x must be greater than or equal to minimum_x")

    if number_of_points <= 2:
        raise IndexError("number_of_points must be greater than 2")

    # Generate x values
    x = np.linspace(minimum_x, maximum_x, number_of_points)

    # Create polynomial and evaluate it
    # Coefficients need to be reversed for NumPy's Polynomial class: [c0, c1, c2]
    p = np.polynomial.Polynomial(quadratic_coefficients)
    y = p(x)

    return np.vstack((x, y))
