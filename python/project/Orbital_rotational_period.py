"""
Planetary Orbit and Spin Visualizer

This module generates visual representations of planetary orbits, spin directions, and axial tilts
based on orbital and rotational data. It uses `matplotlib` to draw orbital ellipses, planet positions,
axial tilt arrows, and annotated labels for rotation and revolution periods.

Functions:
- get_data(): Returns a dictionary of planetary orbital and spin parameters.
- draw_sun(): Draws the Sun at the center of the orbit.
- draw_orbit_with_arrow(): Draws a planet's orbit with an arrow indicating orbital direction.
- draw_planet(): Draws the planet and its astronomical symbol on the orbit.
- draw_tilt_with_arrow(): Draws the planet's axial tilt and a spin direction arrow.
- draw_labels(): Adds text labels for orbit and spin periods.
"""

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Arc


def get_data():
    """Returns a dictionary containing orbital periods, spin periods, and axial tilts for planets."""
    return {
        "Mercury": {"orbital_period_days": 87.97, "spin_period_hours": 1407.6, "axial_tilt_degrees": 0.034},
        "Venus": {"orbital_period_days": 224.7, "spin_period_hours": -5832.5, "axial_tilt_degrees": 177.4},
        "Earth": {"orbital_period_days": 365.25, "spin_period_hours": 23.93, "axial_tilt_degrees": 23.44},
        "Mars": {"orbital_period_days": 686.98, "spin_period_hours": 24.62, "axial_tilt_degrees": 25.19},
        "Jupiter": {"orbital_period_days": 4332.59, "spin_period_hours": 9.93, "axial_tilt_degrees": 3.13},
        "Saturn": {"orbital_period_days": 10759.22, "spin_period_hours": 10.7, "axial_tilt_degrees": 26.73},
        "Uranus": {"orbital_period_days": 30688.5, "spin_period_hours": -17.24, "axial_tilt_degrees": 97.77},
        "Neptune": {"orbital_period_days": 60182, "spin_period_hours": 16.11, "axial_tilt_degrees": 28.32},
        "Ceres": {"orbital_period_days": 1680.0, "spin_period_hours": 9.07, "axial_tilt_degrees": 4.0},
        "Pluto": {"orbital_period_days": 90560.0, "spin_period_hours": 153.3, "axial_tilt_degrees": 122.5}
    }


def draw_sun(height, line_thickness):
    """Draws the Sun at the center of the orbit diagram."""
    line_width = 3 if line_thickness == 3 else 1.5
    ax.add_patch(plt.Circle((0, 0), radius=height / 4, color='k', fill=False, lw=line_width))
    ax.add_patch(plt.Circle((0, 0), radius=height / 16, color="k"))


def draw_planet(planet_name, ellipse_axes):
    """Draws the planet on its orbit with its astronomical symbol."""
    from astronomical_symbols import astronomical_symbols
    symbol_size = ellipse_axes[0] * 6
    line_width = 2 if ellipse_axes[1] == 3 else 1

    center_x = ellipse_axes[0] / (8 / 3)
    radius = ellipse_axes[1] / 6

    planet_patch = plt.Circle((center_x, 0), radius=radius, fc="white", ec="k", lw=line_width, zorder=3)
    symbol_bg = plt.Circle((center_x, 0), radius=symbol_size / 100, zorder=5, fc="white", lw=0)

    plt.gca().add_patch(planet_patch)
    plt.gca().add_patch(symbol_bg)
    plt.text(center_x, 0, astronomical_symbols[planet_name], fontsize=symbol_size, ha="center", va="center", zorder=6)


def draw_orbit_with_arrow(ellipse_axes, ellipse_color='k'):
    """Draws the orbital ellipse and an arrow indicating the direction of revolution."""
    line_width = 2 if ellipse_axes[1] * (8 / 3) == 3 else 1

    angle = np.linspace(0, 2 * np.pi)
    plt.plot(ellipse_axes[0] * np.cos(angle), ellipse_axes[1] * np.sin(angle), color=ellipse_color, lw=line_width)

    arrow_length = ellipse_axes[1] / 4.5
    plt.arrow(-arrow_length / 3, -ellipse_axes[1], 0.00001, 0,
              head_width=arrow_length, head_length=arrow_length, fc="k")


def draw_tilt_with_arrow(axial_tilt, spin_period, ellipse_axes):
    """Draws the axial tilt of a planet with a spin direction arrow."""
    line_width = 2 if ellipse_axes[1] == 3 else 1
    length = ellipse_axes[1] / 2
    tilt_radian = np.radians(axial_tilt)

    center_x = ellipse_axes[0] / (8 / 3)
    dx = (length / 2) * np.sin(tilt_radian)
    dy = (length / 2) * np.cos(tilt_radian)

    start = (center_x - dx, -dy)
    end = (center_x + dx, dy)

    plt.plot([start[0], end[0]], [start[1], end[1]], color='k', linewidth=line_width, zorder=2)

    arc_radians = 0.15 * length
    arc = Arc(end, width=2 * arc_radians, height=2 * arc_radians,
              angle=-axial_tilt, theta1=170, theta2=370,
              color='k', linewidth=line_width, zorder=4)
    plt.gca().add_patch(arc)

    theta = 370 if spin_period >= 0 else 170
    theta_rad = np.radians(theta)
    x_arc = arc_radians * np.cos(theta_rad)
    y_arc = arc_radians * np.sin(theta_rad)

    x_rot = x_arc * np.cos(-tilt_radian) - y_arc * np.sin(-tilt_radian)
    y_rot = x_arc * np.sin(-tilt_radian) + y_arc * np.cos(-tilt_radian)

    arrow_x = end[0] + x_rot
    arrow_y = end[1] + y_rot

    dx_tangent = -np.sin(theta_rad)
    dy_tangent = np.cos(theta_rad)

    dx_rot = dx_tangent * np.cos(-tilt_radian) - dy_tangent * np.sin(-tilt_radian)
    dy_rot = dx_tangent * np.sin(-tilt_radian) + dy_tangent * np.cos(-tilt_radian)

    if spin_period <= 0:
        dx_rot, dy_rot = -dx_rot, -dy_rot

    arrow_length = ellipse_axes[1] / 25
    plt.arrow(
        arrow_x - dx_rot * arrow_length / 2,
        arrow_y - dy_rot * arrow_length / 2,
        dx_rot * 0.00001, dy_rot * 0.00001,
        head_width=arrow_length,
        head_length=arrow_length,
        color='k',
        zorder=4,
        head_starts_at_zero=True
    )


def draw_labels(planet_name, orbit_days, spin_hours, axis):
    """Draws labels for the orbital and spin periods on the diagram."""
    font_size = axis[0] * 2
    orbit_x, orbit_y = 0, -axis[1] / 2
    rotate_x, rotate_y = axis[0] / (8 / 3), -axis[1] / 3

    orbit_period = orbit_days / 365 if orbit_days >= 365 else orbit_days
    orbit_units = "years" if orbit_days >= 365 else "days"

    spin_period = abs(spin_hours / 24) if abs(spin_hours) >= 48 else abs(spin_hours)
    spin_units = "days" if abs(spin_hours) >= 48 else "hours"

    if planet_name == "Earth":
        orbit_period, spin_period = 365, 24

    def round_period(period):
        magnitude = len(str(int(abs(period))))
        rounded = int(round(period, 0))
        return rounded + (10 - rounded % 10) if magnitude >= 3 else rounded

    plt.text(orbit_x, orbit_y, f"{round_period(orbit_period)} {orbit_units}", fontsize=font_size, ha="center")
    plt.text(rotate_x, rotate_y, f"{round_period(spin_period)} {spin_units}", fontsize=font_size, ha="center")


if __name__ == "__main__":
    sizes = ((6, 3), (3, 1.5))
    data = get_data()
    planet = "Earth"
    reduced_data = {planet: data[planet]}
    for planet, planet_data in data.items():
        for size in sizes:
            figure, ax = plt.subplots(figsize=size)
            draw_sun(size[1], size[1])
            draw_orbit_with_arrow([size[0] / (8 / 3), size[1] / (8 / 3)])
            draw_planet(planet, size)
            draw_tilt_with_arrow(planet_data["axial_tilt_degrees"], planet_data["spin_period_hours"], size)
            draw_labels(planet, planet_data["orbital_period_days"], planet_data["spin_period_hours"], size)
            ax.axis('off')
            plt.show()
