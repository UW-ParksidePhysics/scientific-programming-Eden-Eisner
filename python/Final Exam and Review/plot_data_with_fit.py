import numpy as np
import matplotlib.pyplot as plt

def plot_data_with_fit(data: np.ndarray,
                       fit_curve: np.ndarray,
                       data_format: str = 'o',
                       fit_format: str = ''):
    """
    Plot x-y data and a fitted curve using matplotlib.pyplot.plot.

    Parameters:
    data (ndarray): shape (2, M), the original x-y data points.
    fit_curve (ndarray): shape (2, N), the fitted x-y curve data.
    data_format (str): Format string for data points (default: 'o').
    fit_format (str): Format string for fit curve (default: '').

    Returns:
    list: Line2D objects returned by plt.plot
    """
    x_data, y_data = data
    x_fit, y_fit = fit_curve

    plot_data = plt.plot(x_data, y_data, data_format, label="Data")
    plot_fit = plt.plot(x_fit, y_fit, fit_format, label="Fit")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    return plot_data + plot_fit
