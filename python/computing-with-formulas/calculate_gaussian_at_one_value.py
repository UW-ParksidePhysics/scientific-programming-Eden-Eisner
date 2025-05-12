import math

# Define inputs
mean = 0  # m
standard_deviation = 1  # s
input_value = 1  # x

# Gaussian function using the exact formula provided
numerator = -0.5 * ((input_value - mean) / standard_deviation) ** 2
coefficient = 1 / (math.sqrt(2 * math.pi) * standard_deviation)
gaussian_value = coefficient * math.exp(numerator)

# Output the results
print(f"Mean (m): {mean}")
print(f"Standard Deviation (s): {standard_deviation}")
print(f"Input Value (x): {input_value}")
print(f"Gaussian f(x): {gaussian_value:.6f}")
