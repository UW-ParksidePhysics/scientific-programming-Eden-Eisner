import math

# Constants
drag_coefficient = 0.2  # dimensionless
air_density = 1.2       # kg/m^3
radius = 0.11           # meters (soccer ball radius)
cross_area = math.pi * radius ** 2  # m^2, cross-sectional area of a sphere
ball_mass = 0.43        # kg
gravitational_acceleration = 9.81  # m/s^2

# Function to calculate forces for a given velocity
def calculate_forces(ball_velocity):
    drag_force = 0.5 * air_density * ball_velocity ** 2 * cross_area * drag_coefficient  # N
    gravitational_force = ball_mass * gravitational_acceleration  # N
    force_ratio = drag_force / gravitational_force

    print(f"\n--- For ball velocity: {ball_velocity} m/s ---")
    print(f"Drag force: {drag_force:.1f} N")
    print(f"Gravitational force: {gravitational_force:.1f} N")
    print(f"Ratio (drag/gravity): {force_ratio:.2f}")

# Soft kick (10 m/s)
calculate_forces(10)

# Hard kick (30 m/s)
calculate_forces(30)
