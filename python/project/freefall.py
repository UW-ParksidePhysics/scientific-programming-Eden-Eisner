"""
This module calculates quantities for one-dimensional freefall motion
"""
__author__ = "Eden Eisner"

import numpy as np
import matplotlib.pyplot as plt


def test_plot():
    #line
    intercepts = [4,3]
    x_bounds = np.array([-3,8])
    x_values = np.linspace(x_bounds[0], x_bounds[1], num=100)

    y_bounds = -intercepts[1] * x_bounds / intercepts[0] + intercepts[1]
    y_values = -intercepts[1] * x_values / intercepts[0] + intercepts[1]

    #circle
    radius = intercepts[0]
    angles = np.linspace(0, 2 * np.pi, num=4)
    circle_xs = radius * np.cos(angles)
    circle_ys = radius * np.sin(angles)

    plt.plot(x_values, y_values)
    plt.show()

    return


def velocity_in_time(time, initial_velocity=0, gravitational_acceleration=9.8):
    return initial_velocity - gravitational_acceleration * time


def height_in_time(time, initial_height=0, initial_velocity=0, gravitational_acceleration=9.8):
    return initial_height + initial_velocity * time - 0.5 * gravitational_acceleration * time**2


def velocity_in_height(height, initial_height=0, initial_velocity=0, gravitational_acceleration=9.8):
    height_change = height - initial_height
    if initial_velocity == 0.0:
        return np.sign(initial_velocity) * np.sqrt(initial_velocity ** 2 - 2 * gravitational_acceleration * height_change)
    else:
        return np.sign(initial_velocity) *np.sqrt(initial_velocity ** 2 - 2 * gravitational_acceleration * height_change)

if __name__ == '__main__':
    test_plot()
    starting_velocity = 1
    total_time = 1

    test_velocity = velocity_in_time(total_time, initial_velocity=starting_velocity)
    print(f'v(t = {total_time}, v0 = {starting_velocity}) = {test_velocity:.2f} m/s')