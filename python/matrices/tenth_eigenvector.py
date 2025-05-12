import numpy as np
import matplotlib.pyplot as plt

# Define the matrix dimension
matrix_dimension = 10

# Create the 10x10 matrix H
H = (1 / (2 * (1 / (matrix_dimension + 1))**2)) * np.diagflat([2] * matrix_dimension)
for i in range(1, matrix_dimension):
    H[i, i - 1] = -1
    H[i - 1, i] = -1

# Compute the eigenvalues and eigenvectors using NumPy
eigenvalues, eigenvectors = np.linalg.eig(H)

# Extract the tenth eigenvector
tenth_eigenvector = eigenvectors[:, 9]

# Generate x values for the plot
x_values = np.linspace(1 / (matrix_dimension + 1), matrix_dimension / (matrix_dimension + 1), matrix_dimension)

# Plot the tenth eigenvector
plt.plot(x_values, tenth_eigenvector, label='Tenth Eigenvector')
plt.xlabel('x')
plt.ylabel('Eigenvector Value')
plt.title('Tenth Eigenvector of Matrix H')
plt.grid(True)
plt.legend()
plt.show()

