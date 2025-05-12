
import numpy as np
import matplotlib.pyplot as plt

# Define the matrix dimension
matrix_dimension = 5

# Create the 5x5 matrix H
H = (1 / (2 * (1 / (matrix_dimension + 1))**2)) * np.array([
    [2, -1, 0, 0, 0],
    [-1, 2, -1, 0, 0],
    [0, -1, 2, -1, 0],
    [0, 0, -1, 2, -1],
    [0, 0, 0, -1, 2]
])

# Compute the eigenvalues and eigenvectors using NumPy
eigenvalues, eigenvectors = np.linalg.eig(H)

# Extract the fifth eigenvector
fifth_eigenvector = eigenvectors[:, 4]

# Generate x values for the plot
x_values = np.linspace(1 / (matrix_dimension + 1), matrix_dimension / (matrix_dimension + 1), matrix_dimension)

# Plot the fifth eigenvector
plt.plot(x_values, fifth_eigenvector, label='Fifth Eigenvector')
plt.xlabel('x')
plt.ylabel('Eigenvector Value')
plt.title('Fifth Eigenvector of Matrix H')
plt.grid(True)
plt.legend()
plt.show()
