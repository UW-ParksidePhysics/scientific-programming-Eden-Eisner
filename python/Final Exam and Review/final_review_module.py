import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

def read_two_columns_text(filename):
    return np.loadtxt(filename, unpack=True)

def calculate_bivariate_statistics(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)
    correlation = np.corrcoef(x, y)[0, 1]
    return mean_x, mean_y, std_x, std_y, correlation

def calculate_quadratic_fit(x, y):
    return np.polyfit(x, y, 2)

def calculate_lowest_eigenvectors(matrix, indices):
    eigenvalues, eigenvectors = eigh(matrix)
    selected_vectors = eigenvectors[:, indices]
    selected_values = eigenvalues[indices]
    return selected_values, selected_vectors

def annotate_plot(ax, element, symmetry, text, position=(0.05, 0.95), fontsize=12, ha='left', va='top'):
    """
    Adds annotation to a plot at a given position with formatted text.

    Parameters:
        ax : matplotlib axes object
        element : str, element symbol
        symmetry : str, crystal symmetry
        text : str, e.g., '140.2 GPa'
        position : tuple, position in axes fraction coordinates
        fontsize : int
        ha : str, horizontal alignment
        va : str, vertical alignment
    """
    label = f'{element} ({symmetry})\nBulk modulus: {text}'
    ax.annotate(label, xy=position, xycoords='axes fraction',
                fontsize=fontsize, ha=ha, va=va)