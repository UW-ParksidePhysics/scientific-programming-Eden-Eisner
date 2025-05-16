import numpy as np
from scipy.stats import describe

def calculate_bivariate_statistics(data: np.ndarray) -> np.ndarray:
    """
    Calculate statistical characteristics of a bivariate dataset.

    Parameters:
    data (ndarray): A 2xM ndarray of x and y values.

    Returns:
    ndarray: An array containing [mean_y, std_y, min_x, max_x, min_y, max_y]

    Raises:
    IndexError: If data shape is not (2, M) with M > 1
    """
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError("Data must be a 2xM ndarray with M > 1")

    x = data[0]
    y = data[1]

    stats_y = describe(y)
    min_x = np.min(x)
    max_x = np.max(x)
    min_y = stats_y.minmax[0]
    max_y = stats_y.minmax[1]
    mean_y = stats_y.mean
    std_y = np.sqrt(stats_y.variance)

    return np.array([mean_y, std_y, min_x, max_x, min_y, max_y])
