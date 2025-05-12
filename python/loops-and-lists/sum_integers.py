maximum_integer = 100
sum_loop = 0
for i in range(1, maximum_integer + 1):
    sum_loop += i

sum_formula = maximum_integer * (maximum_integer + 1) // 2

print(f"n = {maximum_integer}")
print(f"sum(1, n) = {sum_loop}")
print(f"n(n+1)/2 = {sum_formula}")
