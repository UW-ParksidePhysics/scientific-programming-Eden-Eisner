"""
Example usage:

>>> python convert_temperature.py 21.3 C
70.3 F, 294.4 K

>>> python convert_temperature.py 70 F
21.1 C, 294.3 K

>>> python convert_temperature.py 300 K
26.9 C, 80.4 F
"""

import sys

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def test_conversion():
    passed = True
    tol = 1e-10

    f = 100
    c = fahrenheit_to_celsius(f)
    f2 = celsius_to_fahrenheit(c)
    if abs(f2 - f) > tol:
        print(f"Failed: {f}F -> {c}C -> {f2}F")
        passed = False

    c = 0
    k = celsius_to_kelvin(c)
    c2 = kelvin_to_celsius(k)
    if abs(c2 - c) > tol:
        print(f"Failed: {c}C -> {k}K -> {c2}C")
        passed = False

    f = 32
    k = fahrenheit_to_kelvin(f)
    f2 = kelvin_to_fahrenheit(k)
    if abs(f2 - f) > tol:
        print(f"Failed: {f}F -> {k}K -> {f2}F")
        passed = False

    assert passed, "One or more conversion tests failed!"
    print("All conversion tests passed.")

def user_interface():
    if len(sys.argv) != 3:
        print("Usage: python convert_temperature.py <temperature> <scale>")
        print("Example: python convert_temperature.py 21.3 C")
        sys.exit(1)

    try:
        temp = float(sys.argv[1])
    except ValueError:
        print("Invalid temperature input.")
        sys.exit(1)

    scale = sys.argv[2].upper()

    if scale == "C":
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
        print(f"{f:.1f} F, {k:.1f} K")
    elif scale == "F":
        c = fahrenheit_to_celsius(temp)
        k = fahrenheit_to_kelvin(temp)
        print(f"{c:.1f} C, {k:.1f} K")
    elif scale == "K":
        c = kelvin_to_celsius(temp)
        f = kelvin_to_fahrenheit(temp)
        print(f"{c:.1f} C, {f:.1f} F")
    else:
        print("Unknown scale. Use C, F, or K.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "verify":
        test_conversion()
    else:
        user_interface()
