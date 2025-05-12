import math

# Constants
density = 1030             # kg/m^3
specific_heat = 3700       # J/kg·K
thermal_conductivity = 0.54  # W/m·K (converted from 5.4e-3 W/cm·K)
pi = math.pi
water_temp = 100           # °C
yolk_temp = 70             # °C

# Egg masses
mass_small = 0.047         # kg
mass_large = 0.067         # kg

# Initial temperatures
initial_fridge = 4         # °C
initial_room = 20          # °C

# Cooking time calculation
def cooking_time(M, T0):
    term1 = (M ** (2/3)) * specific_heat * (density ** (1/3)) / (thermal_conductivity * pi ** 2)
    term2 = math.log(0.76 * (T0 - water_temp) / (yolk_temp - water_temp))
    return term1 * term2  # in seconds

# List of conditions
conditions = [
    ("Small egg from fridge", mass_small, initial_fridge),
    ("Small egg from room temperature", mass_small, initial_room),
    ("Large egg from fridge", mass_large, initial_fridge),
    ("Large egg from room temperature", mass_large, initial_room)
]

# Compute and display results
for label, mass, T0 in conditions:
    time_seconds = cooking_time(mass, T0)
    time_minutes = time_seconds / 60
    print(f"{label} cook time = {int(time_seconds)} s = {time_minutes:.1f} min")
