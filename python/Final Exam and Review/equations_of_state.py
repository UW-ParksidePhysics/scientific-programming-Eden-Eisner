import numpy as np
from scipy.optimize import curve_fit

def birch_murnaghan(V, E0, V0, B0, B0p):
    """
    Birch-Murnaghan equation of state:
    E(V) = E0 + (9/16)*B0*V0*[ ((V0/V)^(2/3) - 1)^3 * B0p + ((V0/V)^(2/3) - 1)^2 * (6 - 4*(V0/V)^(2/3)) ]
    """
    eta = (V0 / V)**(2.0 / 3.0)
    term1 = (eta - 1.0)
    energy = E0 + (9.0 * B0 * V0 / 16.0) * (
        term1**3 * B0p + term1**2 * (6.0 - 4.0 * eta)
    )
    return energy

def fit_eos(volumes, energies, initial_coeffs):
    """
    Fit the Birch-Murnaghan EOS to volume and energy data using a quadratic fit as initial guess.
    Returns: E0, V0, B0, B0'
    """
    # Initial guess from quadratic fit: ax^2 + bx + c -> coeffs = [a, b, c]
    a, b, c = initial_coeffs
    V0_guess = -b / (2 * a)
    E0_guess = a * V0_guess**2 + b * V0_guess + c
    B0_guess = 2 * a * V0_guess
    B0p_guess = 4.0  # typical value

    popt, _ = curve_fit(
        birch_murnaghan,
        volumes,
        energies,
        p0=[E0_guess, V0_guess, B0_guess, B0p_guess],
        maxfev=10000
    )

    return popt  # [E0, V0, B0, B0']
def evaluate_fit(volumes, v0, e0, b0, b1=4.0):
    """
    Evaluate the Birch-Murnaghan equation of state for a set of volumes.

    Parameters:
        volumes (np.ndarray): Array of volume values.
        v0 (float): Equilibrium volume.
        e0 (float): Equilibrium energy.
        b0 (float): Bulk modulus.
        b1 (float): First derivative of the bulk modulus (default is 4.0).

    Returns:
        np.ndarray: Energy values for the input volumes.
    """
    eta = (v0 / volumes) ** (2.0 / 3.0)
    energy = e0 + (9.0 * v0 * b0 / 16.0) * ((eta - 1.0) ** 3 * b1 + (eta - 1.0) ** 2 * (6.0 - 4.0 * eta))
    return energy