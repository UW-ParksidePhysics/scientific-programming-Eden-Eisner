import matplotlib.pyplot as plt


def parse_viscosity_data(filename):
    """
    Parses a file containing viscosity data for different gases and returns a nested dictionary.

    Args:
        filename (str): The file containing the viscosity data.

    Returns:
        dict: A nested dictionary with gas names as keys, and dictionaries with 'viscosity', 'reference_temperature',
              and 'reference_viscosity' as the values.
    """
    viscosity_data = {}

    with open(filename, 'r') as file:
        for line in file:
            # Assuming the file has the following format (space-separated):
            # gas_name C T0 mu0
            parts = line.split()
            if len(parts) == 4:
                gas_name = parts[0]
                C = float(parts[1])
                T0 = float(parts[2])
                mu0 = float(parts[3])

                viscosity_data[gas_name] = {
                    'viscosity': C,
                    'reference_temperature': T0,
                    'reference_viscosity': mu0
                }

    return viscosity_data


def calculate_viscosity(temperature, gas, viscosity_data):
    """
    Calculates the viscosity for a given gas at a specific temperature using the formula:
    mu(T) = mu0 * (T / T0) ^ C

    Args:
        temperature (float): The temperature at which to calculate the viscosity.
        gas (str): The gas name.
        viscosity_data (dict): A nested dictionary containing viscosity constants for different gases.

    Returns:
        float: The calculated viscosity for the gas at the given temperature.
    """
    # Retrieve constants for the specified gas
    if gas in viscosity_data:
        C = viscosity_data[gas]['viscosity']
        T0 = viscosity_data[gas]['reference_temperature']
        mu0 = viscosity_data[gas]['reference_viscosity']

        # Calculate viscosity using the formula
        viscosity = mu0 * (temperature / T0) ** C
        return viscosity
    else:
        raise ValueError(f"Data for {gas} not found.")


def plot_viscosities(viscosity_data, gases, temperature_range):
    """
    Plots the viscosities of specified gases over a temperature range.

    Args:
        viscosity_data (dict): A dictionary containing viscosity data for each gas.
        gases (list): A list of gases to plot the viscosity for.
        temperature_range (tuple): A tuple specifying the range of temperatures (min_temp, max_temp).
    """
    temperatures = range(temperature_range[0], temperature_range[1] + 1)

    plt.figure(figsize=(10, 6))

    # Loop through each gas and plot its viscosity
    for gas in gases:
        viscosities = [calculate_viscosity(temp, gas, viscosity_data) for temp in temperatures]
        plt.plot(temperatures, viscosities, label=gas)

    plt.xlabel('Temperature (K)')
    plt.ylabel('Viscosity (Pa.s)')
    plt.title('Viscosity of Gases vs Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage:
if __name__ == "__main__":
    # Assuming the file 'viscosity_of_gases.dat' is available in the working directory
    viscosity_data = parse_viscosity_data('viscosity_of_gases.dat')

    # Gases to plot
    gases_to_plot = ['air', 'carbon_dioxide', 'hydrogen']

    # Define temperature range (in Kelvin)
    temperature_range = (200, 350)

    # Plot viscosities for the specified gases
    plot_viscosities(viscosity_data, gases_to_plot, temperature_range)
