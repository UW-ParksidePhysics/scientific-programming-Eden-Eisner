v0 = 10.0
g = 9.8
dt = 0.177
t_max = 1.416

times = []
positions = []

t = 0
while t <= t_max:
    y = v0 * t - 0.5 * g * t**2
    times.append(t)
    positions.append(y)
    t += dt

print(f"{'t (s)':>10} {'y (m)':>10}")
print(f"{'-'*10} {'-'*10}")

for t, y in zip(times, positions):
    print(f"{t:10.2f} {y:10.2f}")
