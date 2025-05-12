import math

v0 = 10.0  # initial velocity in m/s
g1 = 9.8   # gravity on object 1
g2 = 1.6   # gravity on object 2

print(f"For initial velocity of {v0:.2f} m/s:")
print("-----------------------------------------------------")
print("Earth (g = 9.8 m/s²)         Moon (g = 1.6 m/s²)")
print("-----------------------------------------------------")
print(f"{'t (s)':>10} {'y (m)':>12}     {'t (s)':>10} {'y (m)':>12}")
print(f"{'-'*10} {'-'*12}     {'-'*10} {'-'*12}")
print("using a for loop:")

N = 9
for i in range(N + 1):
    t1 = i * 0.177
    y1 = v0 * t1 - 0.5 * g1 * t1**2
    t2 = i * 0.193
    y2 = v0 * t2 - 0.5 * g2 * t2**2
    print(f"{t1:10.3f} {y1:12.3f}     {t2:10.3f} {y2:12.3f}")

print("using a while loop:")

t1 = 0
while t1 <= 1.416:
    y1 = v0 * t1 - 0.5 * g1 * t1**2
    print(f"{t1:10.3f} {y1:12.3f}")
    t1 += 0.177

print(" " * 32)

t2 = 0
while t2 <= 1.545:
    y2 = v0 * t2 - 0.5 * g2 * t2**2
    print(f"{'':>32}{t2:10.3f} {y2:12.3f}")
    t2 += 0.193

print("-----------------------------------------------------")
