import numpy as np
import matplotlib.pyplot as plt

def f(x, t, alpha, k, v, omega):
    return np.exp(-alpha * (x - v * t)**2) * np.sin(k * x - omega * t)

if __name__ == '__main__':
    x_values = np.linspace(-4, 4, 41)
    t = 0
    k = 3 * np.pi
    v = 3
    omega = 3 * v

    alpha_values = [0.5, 1, 2]

    for alpha in alpha_values:
        y_values = f(x_values, t, alpha, k, v, omega)
        plt.plot(x_values, y_values, label=f'alpha = {alpha}')

    plt.xlabel('x')
    plt.ylabel('f(x, t)')
    plt.title('Visualization of f(x, t) for different alpha values')
    plt.legend()
    plt.grid(True)
    plt.show()