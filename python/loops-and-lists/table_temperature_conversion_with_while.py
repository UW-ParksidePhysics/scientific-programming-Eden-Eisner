print(f"{'°F':>5} {'°C':>7}")
fahrenheit = 0
while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:5} {celsius:7.2f}")
    fahrenheit += 10
