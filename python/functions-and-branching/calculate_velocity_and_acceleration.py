def calculate_velocity_and_acceleration(positions, index, time_step=1e-6):
    """
    Compute velocity and acceleration using finite difference approximations:
        v_i = (x_{i+1} - x_{i-1}) / (2 * dt)
        a_i = (x_{i+1} - 2 * x_i + x_{i-1}) / (dt^2)
    Arguments:
        positions: list or array of positions at uniform time intervals.
        index: integer index i to compute v_i and a_i (must be 1 <= i <= len-2).
        time_step: time difference between position samples.
    Returns:
        (velocity, acceleration) as floats.
    """
    if index <= 0 or index >= len(positions) - 1:
        raise ValueError("Index must be in the range 1 to len(positions) - 2")

    x_prev = positions[index - 1]
    x_curr = positions[index]
    x_next = positions[index + 1]

    velocity = (x_next - x_prev) / (2 * time_step)
    acceleration = (x_next - 2 * x_curr + x_prev) / (time_step ** 2)

    return velocity, acceleration


def test_kinematics():
    """
    Test the function with a scenario of constant velocity (no acceleration).
    Time:     t = [0.0, 0.5, 1.0, 1.5, 2.2] seconds
    Assume velocity v = 3.0 m/s, so position x = v * t
    """
    # Given constant velocity = 3 m/s
    time_points = [0.0, 0.5, 1.0, 1.5, 2.2]
    velocity_true = 3.0
    positions = [velocity_true * t for t in time_points]

    # Use the middle three points to test (avoid boundary index issues)
    time_step = time_points[1] - time_points[0]  # uniform spacing: 0.5s

    print("Testing constant velocity motion (v = 3.0 m/s)")
    print("Time points:", time_points)
    print("Positions:  ", positions)
    print()

    for i in range(1, len(positions) - 1):
        v, a = calculate_velocity_and_acceleration(positions, i, time_step)
        print(f"Index {i}: x = {positions[i]:.2f}, v ≈ {v:.2f} m/s, a ≈ {a:.2e} m/s²")


if __name__ == "__main__":
    test_kinematics()
