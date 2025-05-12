import numpy as np

def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

if __name__ == '__main__':
    positions = np.linspace(-4, 4, 41)
    gaussian_values = [gaussian(x) for x in positions]

    print(positions)
    print(gaussian_values)