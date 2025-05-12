from numpy.lib.scimath import sqrt

def calculate_quadratic_roots(a, b, c):
    """Calculate the roots of ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    root1 = (-b + sqrt(discriminant)) / (2 * a)
    root2 = (-b - sqrt(discriminant)) / (2 * a)
    return root1, root2

# Test function for single real root (discriminant == 0)
def test_single_root():
    a, b, c = 1, 2, 1  # x^2 + 2x + 1 = 0 -> root: -1
    expected = (-1.0, -1.0)
    result = calculate_quadratic_roots(a, b, c)
    print(f"x^2 + 2x + 1 = 0: x = -1     ; calculate_quadratic_roots({a}, {b}, {c}) = {result[0]}, {result[1]}")
    assert result == expected

# Test function for two real roots (discriminant > 0)
def test_roots_float():
    a, b, c = 1, -2, -3  # x^2 - 2x - 3 = 0 -> roots: 3, -1
    expected = (3.0, -1.0)
    result = calculate_quadratic_roots(a, b, c)
    print(f"x^2 - 2x - 3 = 0: x = 3, -1. ; calculate_quadratic_roots({a}, {b}, {c}) = {result[0]}, {result[1]}")
    assert set(result) == set(expected)

# Test function for complex roots (discriminant < 0)
def test_roots_complex():
    a, b, c = 1, 0, 1  # x^2 + 0x + 1 = 0 -> roots: i, -i
    expected = (1j, -1j)
    result = calculate_quadratic_roots(a, b, c)
    print(f"x^2 + 0x + 1 = 0: x = i, -i  ; calculate_quadratic_roots({a}, {b}, {c}) = {result[0]}, {result[1]}")
    assert set(result) == set(expected)

# Run tests
if __name__ == "__main__":
    test_single_root()
    test_roots_float()
    test_roots_complex()
