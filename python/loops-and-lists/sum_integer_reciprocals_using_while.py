# Original (buggy) code:
# summation = 0
# starting_index = 1
# index = starting_index
# maximum_index = 100
# while index < maximum_index:
#     summation += 1/index
# print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

# --- Errors found:
# 1. Condition should be <= not <.
# 2. index was not incremented (infinite loop).
# 3. Add formatting to output.

# --- Manual test:
# sum(1 to 5) = 1 + 0.5 + 0.333... + 0.25 + 0.2 ≈ 2.283

# --- Final fixed script:
summation = 0
starting_index = 1
maximum_index = 100
index = starting_index

while index <= maximum_index:
    summation += 1 / index
    index += 1

print(f"sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.6f}")
