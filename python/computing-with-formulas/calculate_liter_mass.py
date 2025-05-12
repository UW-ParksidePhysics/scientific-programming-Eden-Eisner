def main():
    # Densities in g/cm³
    substances = {
        "Iron": 7.874,
        "Air": 0.001225,
        "Gasoline": 0.755,
        "Ice": 0.9167,
        "Human Body": 1.062,
        "Silver": 10.49,
        "Platinum": 21.45
    }

    print("Mass of 1 liter (1000 cm³) of various substances:")
    for substance, density in substances.items():
        mass = calculate_mass(density)
        print(f"{substance}: {mass:.3f} g")

def calculate_mass(density_g_per_cm3, volume_cm3=1000):
    return density_g_per_cm3 * volume_cm3

main()