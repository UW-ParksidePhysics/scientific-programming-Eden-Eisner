"""
Use astronomical symbol for the sun
Use a comparable size circle for the planet
arrow in the orbit itself
use unit that has 2 sig fig for the periods w/o decimal place
make 1.5 and 3 inch tall version
"""

#### RENAME from project.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization
planet_data = {
    "Mercury": {"orbital_period_days": 88, "spin_period_hours": 1407.6, "axial_tilt_degrees": 0.034},
    "Venus": {"orbital_period_days": 225, "spin_period_hours": -5832.5, "axial_tilt_degrees": 177.4},
    "Earth": {"orbital_period_days": 365.25, "spin_period_hours": 24, "axial_tilt_degrees": 23.44},
    "Mars": {"orbital_period_days": 687, "spin_period_hours": 24.6, "axial_tilt_degrees": 25.19},
    "Jupiter": {"orbital_period_days": 4331, "spin_period_hours": 9.9, "axial_tilt_degrees": 3.13},
    "Saturn": {"orbital_period_days": 10747, "spin_period_hours": 10.7, "axial_tilt_degrees": 26.73},
    "Uranus": {"orbital_period_days": 30589, "spin_period_hours": -17.2, "axial_tilt_degrees": 97.77},
    "Neptune": {"orbital_period_days": 59800, "spin_period_hours": 16.1, "axial_tilt_degrees": 28.32},
    "Ceres": {"orbital_period_days": 4375, "spin_period_hours": 9.1, "axial_tilt_degrees": 4.34},  # Ceres is a dwarf planet
    "Pluto": {"orbital_period_days": 90560, "spin_period_hours": 153.3, "axial_tilt_degrees": 122.5}  # Pluto also a dwarf planet
}


# Negative spin periods mean the planet rotates in the opposite direction (retrograde rotation).
def get_data(planet_name):
    data = planet_data[planet_name]
    return [planet_name] + list(data.values())

print(get_data("Mercury"))