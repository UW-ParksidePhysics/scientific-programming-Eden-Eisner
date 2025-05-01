"""
Need descriptive docstring

"""
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Arc



# Negative spin periods mean the planet rotates in the opposite direction (retrograde rotation).
def get_data():
    planets_data = {
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
    return planets_data


def draw_sun(height):
    sun = plt.Circle((0,0),radius=height/4, color='k', fill = False, lw = 3)
    ax.add_patch(sun)
    sun_dot = plt.Circle((0,0), radius=height/16, color="k")
    ax.add_patch(sun_dot)
    return


def draw_planet(planet_name, ellipse_axes):
    from astronomical_symbols import astronomical_symbols

    symbol_size = ellipse_axes[0]*2

    planets = plt.Circle((ellipse_axes[0]/(8/3),0), radius=(ellipse_axes[1]/6), fc="white", ec="k", lw=2, zorder = 3)

    symbol_background = plt.Circle((ellipse_axes[0]/(8/3),0), radius=(symbol_size/100), zorder=5, fc="white", lw=0)
    plt.text(ellipse_axes[0] / (8/3), 0, astronomical_symbols[planet_name], color="k", fontsize=symbol_size, ha="center", va="center", zorder=6)

    ax1 = plt.gca()
    ax1.add_patch(planets)
    ax1.add_patch(symbol_background)
    return


def draw_orbit_with_arrow(ellipse_axes, ellipse_color = 'k'):
    angle = np.linspace(0, 2*np.pi)
    plt.plot(ellipse_axes[0] *np.cos(angle), ellipse_axes[1] * np.sin(angle), color = ellipse_color)

    arrow_length = ellipse_axes[1]/4.5
    plt.arrow(-arrow_length*(1/3),-ellipse_axes[1],0.00001,0, head_width=arrow_length, head_length=arrow_length, fc = "k")
    return


def draw_tilt_with_arrow(axial_tilt, spin_period, ellipse_axes):
    length = ellipse_axes[1] / 2
    tilt_rad = np.radians(axial_tilt)

    center_x = ellipse_axes[0] / (8 / 3)
    center_y = 0

    dx = (length / 2) * np.sin(tilt_rad)
    dy = (length / 2) * np.cos(tilt_rad)

    start_x = center_x - dx
    start_y = center_y - dy
    end_x = center_x + dx
    end_y = center_y + dy

    plt.plot([start_x, end_x], [start_y, end_y], color='k', linewidth=1.5, zorder=4)

    arc_radius = 0.15 * length
    theta1 = 170
    theta2 = 370

    # Draw arc
    arc = Arc((center_x, center_y),
              width=2 * arc_radius, height=2 * arc_radius,
              angle=-axial_tilt,
              theta1=theta1, theta2=theta2,
              color='k', linewidth=1.5, zorder=4)
    plt.gca().add_patch(arc)

    # Choose which end of arc to use for arrow
    theta = theta2 if spin_period >= 0 else theta1
    theta_rad = np.radians(theta)

    # Get arc endpoint in arc's local coordinate frame
    x_arc = arc_radius * np.cos(theta_rad)
    y_arc = arc_radius * np.sin(theta_rad)

    # Rotate endpoint by -axial_tilt to match figure orientation
    x_rot = x_arc * np.cos(-tilt_rad) - y_arc * np.sin(-tilt_rad)
    y_rot = x_arc * np.sin(-tilt_rad) + y_arc * np.cos(-tilt_rad)

    arrow_x = center_x + x_rot
    arrow_y = center_y + y_rot

    # Compute tangent direction at arrow location and rotate it
    dx_tangent = -np.sin(theta_rad)
    dy_tangent = np.cos(theta_rad)
    dx_rot = (dx_tangent * np.cos(-tilt_rad) - dy_tangent * np.sin(-tilt_rad))
    dy_rot = (dx_tangent * np.sin(-tilt_rad) + dy_tangent * np.cos(-tilt_rad))

    if spin_period <= 0:
        dx_rot = -dx_rot
        dy_rot = -dy_rot

    arrow_length = ellipse_axes[1] / 25
    plt.arrow(
        arrow_x - dx_rot * arrow_length / 2,
        arrow_y - dy_rot * arrow_length / 2,
        dx_rot * 0.00001, dy_rot * 0.00001,  # effectively no shaft, just head
        head_width=arrow_length,
        head_length=arrow_length,
        color='k',
        zorder=4,
        head_starts_at_zero=True
    )
    return

def draw_labels(planet_name, label_data_orbit, label_data_rotate, axis):
    orbit_x=0
    orbit_y=-axis[1]/2
    rotate_x=(axis[0]/(8/3))
    rotate_y=-axis[1]/3
    font_size = axis[0]*2

    if label_data_orbit >=365:
        orbit_period = label_data_orbit/365
        orbit_time_units = "years"
    elif planet_name == "Earth":
        orbit_time_units = "days"
    else:
        orbit_period = label_data_orbit
        orbit_time_units = "days"

    if abs(label_data_rotate) >=48:
        rotate_period = abs(label_data_rotate/24)
        rotate_time_units = "days"
    elif planet == "Earth":
        rotate_time_units = "hours"
    else:
        rotate_period = abs(label_data_rotate)
        rotate_time_units = "hours"

    if planet_name == "Earth":
        rounded_orbit_period = label_data_orbit
    else:
        magnitude = len(str(int(abs(orbit_period))))
        rounded_orbit_period = int(round(orbit_period, 0))
        if magnitude >= 3:
            rounded_orbit_period = rounded_orbit_period+(10- (rounded_orbit_period % 10))

    if planet_name == "Earth":
        rounded_rotate_period = 24
    else:
        magnitude = len(str(int(abs(rotate_period))))
        rounded_rotate_period = int(round(rotate_period, 0))
        if magnitude >= 3:
            rounded_rotate_period = rounded_rotate_period + (10 - (rounded_rotate_period % 10))

    plt.text(orbit_x, orbit_y, f"{rounded_orbit_period} {orbit_time_units}", fontsize=font_size, horizontalalignment="center")
    plt.text(rotate_x, rotate_y, f"{rounded_rotate_period} {rotate_time_units}", fontsize=font_size, horizontalalignment="center")
    return


if __name__ == "__main__":
    sizes = ((6,3),(3,1.5))
    data = get_data()
    planet = "Earth"
    reduced_data = {planet:data[planet]} # for testing specific planets
    for planet, planet_data in data.items():
        for size in sizes:
            figure, ax = plt.subplots(figsize=size)
            draw_sun(size[1])
            draw_orbit_with_arrow([size[0]/(8/3),size[1]/(8/3)])
            draw_planet(planet,size)
            draw_tilt_with_arrow(planet_data["axial_tilt_degrees"], planet_data["spin_period_hours"], size)
            draw_labels(planet, planet_data["orbital_period_days"], planet_data["spin_period_hours"], size)

            ax.axis('off')
            plt.show()