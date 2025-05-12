v0 = 10.0
g = 9.8
dt = 0.177
t_max = 1.416

times = []
positions = []

t = 0
while t <= t_max:
    y = v0 * t - 0.5 * g * t**2
    times.append(round(t, 2))
    positions.append(round(y, 2))
    t += dt

times_positions = [times, positions]
time_positions = [[t, y] for t, y in zip(times, positions)]

print(f"{'t (s)':>10} {'y (m)':>10}")
print(f"{'-'*10} {'-'*10}")

for row in time_positions:
    print(f"{row[0]:10.2f} {row[1]:10.2f}")
