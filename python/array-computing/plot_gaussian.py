import numpy as np
import matplotlib.pyplot as plt

def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

if __name__ == '__main__':
    x_values = np.linspace(-4, 4, 41)
    y_values = gaussian(x_values)

    plt.plot(x_values, y_values, label='Gaussian Function')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.title('Gaussian Function Plot')
    plt.legend()
    plt.grid(True)
    plt.show()