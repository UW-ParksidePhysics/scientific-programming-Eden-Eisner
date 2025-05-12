import matplotlib.pyplot as plt


def parse_sum_output(filename):
    """
    Parse the content of a file to extract epsilon, exact error, and n values.

    Args:
        filename (str): The name of the output file to parse.

    Returns:
        tuple: Three lists: tolerances (epsilon), errors (exact error), and maximum_indices (n).
    """
    tolerances = []
    errors = []
    maximum_indices = []

    with open(filename, 'r') as file:
        for line in file:
            # Example line: "epsilon: 1e-04, exact error: 8.18e-04, n=55"
            parts = line.split(',')
            if len(parts) == 3:
                epsilon = float(parts[0].split(':')[1].strip())
                exact_error = float(parts[1].split(':')[1].strip())
                n = int(parts[2].split('=')[1].strip())

                tolerances.append(epsilon)
                errors.append(exact_error)
                maximum_indices.append(n)

    return tolerances, errors, maximum_indices


def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    """
    Plot tolerance vs. error and tolerance vs. maximum index on a logarithmic scale for the y-axis.

    Args:
        tolerances (list): List of epsilon values.
        errors (list): List of exact error values.
        maximum_indices (list): List of n values.
    """
    # Create subplots
    fig, ax1 = plt.subplots()

    # Plot tolerance vs error on a logarithmic scale
    ax1.semilogy(tolerances, errors, 'bo-', label="Error vs. Tolerance")
    ax1.set_xlabel('Tolerance (epsilon)')
    ax1.set_ylabel('Exact Error', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create another axis for tolerance vs maximum index
    ax2 = ax1.twinx()
    ax2.plot(tolerances, maximum_indices, 'ro-', label="Max Index vs. Tolerance")
    ax2.set_ylabel('Maximum Index', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    # Title and show plot
    plt.title('Logarithmic Sum Error and Maximum Index vs. Tolerance')
    fig.tight_layout()  # To ensure proper layout
    plt.show()


# Main script to run the functions
if __name__ == "__main__":
    # Parse the output file to get tolerances, errors, and maximum indices
    tolerances, errors, maximum_indices = parse_sum_output('logarithmic_sum.out')

    # Plot the results
    plot_logarithmic_sum_error(tolerances, errors, maximum_indices)
