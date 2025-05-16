
from scipy.constants import physical_constants

def convert_units(value, from_units, to_units):
    from_units = from_units.lower().strip().replace("rydberg", "ryd")
    to_units = to_units.lower().strip()

    if from_units == 'bohr^3' and to_units == 'angstrom^3':
        return value * (physical_constants['Bohr radius'][0] ** 3) * 1e30
    elif from_units == 'ryd' and to_units == 'ev':
        return value * physical_constants['Rydberg constant times hc in eV'][0]
    elif from_units == 'ryd/bohr^3' and to_units == 'gpa':
        bohr_to_m = physical_constants['Bohr radius'][0]
        ryd_to_joule = physical_constants['Rydberg constant times hc in J'][0]
        pascal = ryd_to_joule / (bohr_to_m ** 3)
        return value * pascal / 1e9  # Pa to GPa
    else:
        raise ValueError(f'Unsupported conversion: {from_units} to {to_units}')

