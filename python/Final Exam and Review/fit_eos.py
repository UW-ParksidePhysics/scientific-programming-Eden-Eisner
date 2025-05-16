import numpy as np
from scipy.optimize import curve_fit

def birch_murnaghan(V, E0, V0, B0, B0_prime):
    eta = (V0 / V) ** (2 / 3)
    return E0 + (9 * V0 * B0 / 16) * ((eta - 1) ** 3 * B0_prime + (eta - 1) ** 2 * (6 - 4 * eta))

def fit_eos(volumes, energies, initial_guess):
    popt, _ = curve_fit(birch_murnaghan, volumes, energies, p0=initial_guess)
    return popt  # Returns E0, V0, B0, B0_prime
