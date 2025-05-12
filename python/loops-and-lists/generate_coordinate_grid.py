a = 1
b = 2
n_intervals = 20
h = (b - a) / n_intervals

print(f"For x in [{a}, {b}] with {n_intervals} intervals, the interval length is h = {h:.3f}, and")

# Using for loop
x_for = []
for i in range(n_intervals + 1):
    x_for.append(round(a + i * h, 2))

print("Using a for loop:")
print("x =", x_for)

# Using list comprehension
x_list = [round(a + i * h, 2) for i in range(n_intervals + 1)]

print("Using list comprehension:")
print("x =", x_list)