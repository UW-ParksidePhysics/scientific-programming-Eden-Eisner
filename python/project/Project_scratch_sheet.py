import numpy as np
import matplotlib.pyplot as plt

def draw_tilt_with_arrow(axial_tilt, spin_period, ellipse_axes):
    length = ellipse_axes[1] / 2  # Half-length of the semi-minor axis

    # Convert tilt angle to radians
    tilt_rad = np.radians(axial_tilt)

    # Planet center (position of the axis)
    center_x = ellipse_axes[0] / (8 / 3)  # This could be adjusted to the desired position
    center_y = 0

    # Half-length to draw equally in both directions
    dx = (length / 2) * np.sin(tilt_rad)
    dy = (length / 2) * np.cos(tilt_rad)

    # Start and end points of the line (through the center)
    start_x = center_x - dx
    start_y = center_y - dy
    end_x = center_x + dx
    end_y = center_y + dy

    # Draw the axis of rotation line
    plt.plot([start_x, end_x], [start_y, end_y], color='red', linewidth=2)

    # Add an arrow at the end of the line to indicate direction
    arrowhead_size = 0.15  # Adjust this value for the arrowhead size
    plt.arrow(end_x, end_y, dx=dx/4, dy=dy/4, head_width=arrowhead_size, head_length=arrowhead_size, fc='red', ec='red')

    # Set the aspect ratio to ensure the ellipse isn't distorted
    plt.gca().set_aspect('equal', adjustable='box')

    # Show the plot
    plt.show()

# Example usage of the function
draw_tilt_with_arrow(axial_tilt=23.5, spin_period=24, ellipse_axes=[5, 3])  # Tilt of 23.5 degrees, example ellipse axes
