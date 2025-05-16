
import os
from datetime import date
from scipy.linalg import eigh

import matplotlib.pyplot as plt
import numpy as np

from convert_units import convert_units
from equations_of_state import fit_eos
from final_review_module import (
    read_two_columns_text,
    calculate_bivariate_statistics,
    calculate_quadratic_fit,
    calculate_lowest_eigenvectors
)
from generate_matrix import generate_matrix


def parse_file_name(filename):
    base = os.path.basename(filename)
    parts = base.split('.')
    return parts[0], parts[1], parts[2]

def plot_equation_of_state(data_file, display_graph=True):
    import numpy as np
    import matplotlib.pyplot as plt
    from datetime import date
    from final_review_module import (
        read_two_columns_text,
        calculate_bivariate_statistics,
        calculate_quadratic_fit,
        annotate_plot,
    )
    from equations_of_state import fit_eos, evaluate_fit
    from convert_units import convert_units

    # Extract metadata from file name
    element, symmetry, dft_label = parse_file_name(data_file)

    # Read the data
    volumes, energies = read_two_columns_text(data_file)

    # Use if needed: divide by number of atoms (your assignment suggests 1)
    atoms_per_cell = 1
    volumes /= atoms_per_cell
    energies /= atoms_per_cell

    # Stats & quadratic fit
    stats = calculate_bivariate_statistics(volumes, energies)
    coeffs = calculate_quadratic_fit(volumes, energies)

    # EOS fit — FIXED this line
    params = fit_eos(volumes, energies, coeffs)
    v0, e0, b0 = params[:3]  # Slicing fixes the unpacking error

    # Evaluate EOS on smooth volume range
    volume_fit = np.linspace(volumes.min(), volumes.max(), 300)
    energy_fit = evaluate_fit(volume_fit, *params)

    # Convert units
    volumes_A = convert_units(volumes, 'bohr^3', 'angstrom^3')
    energies_eV = convert_units(energies, 'rydberg', 'eV')
    volume_fit_A = convert_units(volume_fit, 'bohr^3', 'angstrom^3')
    energy_fit_eV = convert_units(energy_fit, 'rydberg', 'eV')
    v0_A = convert_units(v0, 'bohr^3', 'angstrom^3')
    e0_eV = convert_units(e0, 'rydberg', 'eV')
    b0_GPa = convert_units(b0, 'rydberg/bohr^3', 'GPa')

    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(volume_fit_A, energy_fit_eV, 'k-', label='EOS Fit')
    plt.plot(volumes_A, energies_eV, 'bo', label='DFT Data')

    # Axis limits
    x_margin = 0.1 * (volumes_A.max() - volumes_A.min())
    y_margin = 0.1 * (energies_eV.max() - energies_eV.min())
    plt.xlim(volumes_A.min() - x_margin, volumes_A.max() + x_margin)
    plt.ylim(energies_eV.min() - y_margin, energies_eV.max() + y_margin)

    # Labels
    plt.xlabel(r'Volume $V$ [$\mathrm{\AA}^3$/atom]')
    plt.ylabel(r'Energy $E$ [eV/atom]')

    # Annotations
    plt.axvline(v0_A, color='k', linestyle='--')
    plt.text(v0_A, energies_eV.min() + y_margin / 2, f'{v0_A:.2f} Å³/atom', rotation=90, verticalalignment='bottom')

    annotate_plot(plt, element, symmetry, f'{b0_GPa:.1f} GPa')

    today = date.today().isoformat()
    plt.text(0.02, -0.12, f'Created by Eden Eisner {today}',
             transform=plt.gca().transAxes, fontsize=9)

    plt.title(f'Birch-Murnaghan Equation of State for {element} in DFT {dft_label}')

    if display_graph:
        plt.show()
    else:
        file_name = f"Eisner.{element}.{symmetry}.{dft_label}.BirchMurnaghanEquationOfState.png"
        plt.savefig(file_name, dpi=300, bbox_inches='tight')


def plot_selected_eigenvectors(potential, indices, ndim, strength, display_graph=False):
    """
    Generate the Hamiltonian and plot selected eigenvectors.

    Parameters:
    - potential (str): Type of potential (e.g., 'Square', 'Harmonic', etc.)
    - indices (list of int): List of eigenvector indices to plot
    - ndim (int): Matrix dimension
    - strength (float): Strength of the potential
    - display_graph (bool): Whether to show the plot
    """
    # Generate Hamiltonian
    H = generate_matrix(potential, ndim, strength)


    # Diagonalize
    eigvals, eigvecs = eigh(H)

    x = np.linspace(0, 1, ndim)

    # Plot selected eigenvectors
    plt.figure(figsize=(8, 6))
    for idx in indices:
        if idx >= ndim:
            print(f"Index {idx} is out of bounds for dimension {ndim}")
            continue
        plt.plot(x, eigvecs[:, idx], label=f'n={idx+1}, E={eigvals[idx]:.3f}')

    plt.xlabel('x')
    plt.ylabel('Wavefunction')
    plt.title(f'{potential} Well Eigenvectors')
    plt.legend()
    plt.grid(True)

    if display_graph:
        plt.show()

if __name__ == '__main__':
    # Test unit conversions
    print(convert_units(1, 'bohr^3', 'angstrom^3'))  # should be 0.14818471147216278
    print(convert_units(1, 'ryd', 'eV'))             # should be 13.605693122994
    print(convert_units(1, 'ryd/bohr^3', 'GPa'))     # should be 14710.507848260711

    # Main functions
    plot_equation_of_state('Cu.Fm-3m.GGA-PBE.volumes_energies.dat', display_graph=True)
    plot_selected_eigenvectors('Square', [1, 2, 3], 130, 10, display_graph=True)

