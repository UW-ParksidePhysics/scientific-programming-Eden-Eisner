print(f"{'°F':>5} {'°C':>7} {'~°C':>7}")
fahrenheit = 0
while fahrenheit <= 100:
    exact_celsius = (fahrenheit - 32) * 5 / 9
    approx_celsius = (fahrenheit - 30) / 2
    print(f"{fahrenheit:5} {exact_celsius:7.2f} {approx_celsius:7.2f}")
    fahrenheit += 10
