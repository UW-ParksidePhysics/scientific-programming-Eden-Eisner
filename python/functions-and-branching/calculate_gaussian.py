import math

def gaussian(position, mean=0, standard_deviation=1):
    """Compute the Gaussian function value at a given position."""
    coefficient = 1 / (standard_deviation * math.sqrt(2 * math.pi))
    exponent = -((position - mean) ** 2) / (2 * standard_deviation ** 2)
    return coefficient * math.exp(exponent)

def print_gaussian_table(start, end, num_points, mean=0, std_dev=1):
    """Print a table of x and Gaussian(x) values for evenly spaced x values."""
    step = (end - start) / (num_points - 1)
    print(f"{'x':>10} {'Gaussian(x)':>20}")
    print("-" * 30)
    for i in range(num_points):
        x = start + i * step
        y = gaussian(x, mean, std_dev)
        print(f"{x:10.4f} {y:20.8f}")

# Example usage
if __name__ == "__main__":
    print("Gaussian Function Table: mean=0, std_dev=1, x in [-3, 3]")
    print_gaussian_table(start=-3, end=3, num_points=13, mean=0, std_dev=1)
