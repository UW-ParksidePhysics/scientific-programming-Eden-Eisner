"""
This module calculates quantities for one-dimensional freefall motion
"""


import numpy as np


def velocity_in_time(time, initial_velocity=0, gravitational_acceleration=9.8):
    return initial_velocity - gravitational_acceleration * time


def height_in_time(time, initial_height=0, initial_velocity=0, gravitational_acceleration=9.8):
    return initial_height + initial_velocity * time - 0.5 * gravitational_acceleration * time**2


def velocity_in_height(height, initial_height=0, initial_velocity=0, gravitational_acceleration=9.8):
    height_change = height - initial_height
    if initial_velocity == 0.0:
        return np.sign(initial_velocity) * np.sqrt(initial_velocity**2 - 2 * gravitational_acceleration*(height_change))
    else:
        return np.sign(initial_velocity) *np.sqrt(initial_velocity**2 - 2 * gravitational_acceleration*(height_change))

if __name__ == '__main__':
    starting_velocity = 1
    total_time = 1

    test_velocity = velocity_in_time(total_time, initial_velocity=starting_velocity)
    print(f'v(t = {total_time}, v0 = {starting_velocity}) = {test_velocity:.2f} m/s')