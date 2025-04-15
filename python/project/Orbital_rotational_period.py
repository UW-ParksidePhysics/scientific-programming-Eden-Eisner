"""
Use astronomical symbol for the sun
Use a comparable size circle for the planet to the sun
arrow in the orbit itself
use unit that has 2 sig fig for the periods w/o decimal place
make 1.5 and 3 inch tall version
"""
from matplotlib import pyplot as plt
import numpy as np

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


# Negative spin periods mean the planet rotates in the opposite direction (retrograde rotation).
def get_data():
    planets_data = {
        "Mercury": {"orbital_period_days": 88, "spin_period_hours": 1407.6, "axial_tilt_degrees": 0.034},
        "Venus": {"orbital_period_days": 225, "spin_period_hours": -5832.5, "axial_tilt_degrees": 177.4},
        "Earth": {"orbital_period_days": 365.25, "spin_period_hours": 24, "axial_tilt_degrees": 23.44},
        "Mars": {"orbital_period_days": 687, "spin_period_hours": 24.6, "axial_tilt_degrees": 25.19},
        "Jupiter": {"orbital_period_days": 4331, "spin_period_hours": 9.9, "axial_tilt_degrees": 3.13},
        "Saturn": {"orbital_period_days": 10747, "spin_period_hours": 10.7, "axial_tilt_degrees": 26.73},
        "Uranus": {"orbital_period_days": 30589, "spin_period_hours": -17.2, "axial_tilt_degrees": 97.77},
        "Neptune": {"orbital_period_days": 59800, "spin_period_hours": 16.1, "axial_tilt_degrees": 28.32},
        "Ceres": {"orbital_period_days": 4375, "spin_period_hours": 9.1, "axial_tilt_degrees": 4.34},
        # Ceres is a dwarf planet
        "Pluto": {"orbital_period_days": 90560, "spin_period_hours": 153.3, "axial_tilt_degrees": 122.5}
        # Pluto also a dwarf planet
    }
    return planets_data


def draw_sun(ax, height):
    sun = plt.Circle((0,0),radius=height/4, color='k', fill = False, lw = 3)
    ax.add_patch(sun)
    sun_dot = plt.Circle((0,0), radius=height/16, color="k")
    ax.add_patch(sun_dot)

    rect = plt.Rectangle((-size[0] / 2, -size[1] / 2), size[0], size[1], color='k', fill=False)
    ax.add_patch(rect)

    return


def draw_planet(planet_name):
    from astronomical_symbols import astronomical_symbols


    print(astronomical_symbols[planet_name])
    pass


def draw_orbit_with_arrow(ellipse_axes, ellipse_color = 'k'):
    angle = np.linspace(0, 2*np.pi)
    plt.plot(ellipse_axes[0] *np.cos(angle), ellipse_axes[1] * np.sin(angle), color = ellipse_color)


    return


def draw_axis_with_arrow(axial_tilt, spin_period):
    print(axial_tilt, spin_period)
    return


def draw_labels(label_data):
    pass


if __name__ == "__main__":
    sizes = ((6,3),(3,1.5))
    data = get_data()
    planet = "Mercury"
    reduced_data = {planet:data[planet]} # for testing specific planets
    for planet, planet_data in reduced_data.items():
        for size in sizes:
            figure, ax = plt.subplots(figsize=size)
            draw_sun(ax, size[1])
            draw_orbit_with_arrow([size[0]/(8/3),size[1]/(8/3)])
            draw_planet(planet)
            draw_axis_with_arrow(planet_data["axial_tilt_degrees"], planet_data["spin_period_hours"])
            draw_labels(planet_data)



            plt.show()