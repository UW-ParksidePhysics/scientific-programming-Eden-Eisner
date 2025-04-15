import numpy as np
import matplotlib.pyplot as plt

def draw_orbit_with_arrow(ellipse_axes, ellipse_color='k'):
    # Unpack ellipse axes: (semi-major, semi-minor)
    semi_major, semi_minor = ellipse_axes

    # Generate ellipse points
    angles = np.linspace(0, 2 * np.pi, 500)
    x_ellipse = semi_major * np.cos(angles)
    y_ellipse = semi_minor * np.sin(angles)
    plt.plot(x_ellipse, y_ellipse, color=ellipse_color)

    # ==== Add the chevron (">") style arrow ====

    # Choose angle position on ellipse: bottom (270° / 3π/2 radians)
    arrow_angle = 3 * np.pi / 2

    # Arrow base point (on the ellipse)
    arrow_base_x = semi_major * np.cos(arrow_angle)
    arrow_base_y = semi_minor * np.sin(arrow_angle)

    # Tangent direction (counter-clockwise)
    dx_dt = semi_major * np.sin(arrow_angle)
    dy_dt = -semi_minor * np.cos(arrow_angle)
    tangent_angle = np.arctan2(dy_dt, dx_dt)

    # Arrow appearance
    arrow_length = 0.2
    chevron_angle_offset = np.deg2rad(25)  # spread of the ">" shape

    # Calculate points for the two arms of the chevron
    left_arm_x = arrow_base_x + arrow_length * np.cos(tangent_angle - chevron_angle_offset)
    left_arm_y = arrow_base_y + arrow_length * np.sin(tangent_angle - chevron_angle_offset)

    right_arm_x = arrow_base_x + arrow_length * np.cos(tangent_angle + chevron_angle_offset)
    right_arm_y = arrow_base_y + arrow_length * np.sin(tangent_angle + chevron_angle_offset)

    # Draw the chevron using two lines
    plt.plot([left_arm_x, arrow_base_x, right_arm_x],
             [left_arm_y, arrow_base_y, right_arm_y],
             color='red', linewidth=2)

    return


draw_orbit_with_arrow((3,1.5))
plt.show()