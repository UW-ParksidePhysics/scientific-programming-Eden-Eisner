import numpy as np


size = 2
identity_matrix = np.identity(size)
negative_ones = np.full(size-1, -1)
down_shifted_negative_ones = np.diag(negative_ones, -1)
up_shifted_negative_ones = np.diag(negative_ones, 1)
combined_matrix = 2*identity_matrix + down_shifted_negative_ones + up_shifted_negative_ones
print(f' A_3 = {combined_matrix}\n')

eigenvalues, eigenvectors = np.linalg.eig(combined_matrix)

print(f'lambda: {eigenvalues}\n')
print(f'x-vector: {eigenvectors}\n')

for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors.transpose()):
    print(f'λ = {eigenvalue}, x-vector = {eigenvector}\n')