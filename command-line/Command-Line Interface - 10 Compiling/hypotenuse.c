/**
 * @file hypotenuse.c
 * @brief Computes the hypotenuse of a right-angled triangle using the Pythagorean theorem.
 *
 * This function takes two integer values representing the lengths of the two perpendicular sides
 * of a right-angled triangle, converts them to doubles, and returns the length of the hypotenuse as a double.
 *
 * Modified by Eden, 2025-04-24
 */

#include <math.h>

/**
 * @brief Calculates the hypotenuse of a right-angled triangle.
 *
 * This function uses the Pythagorean theorem to compute the hypotenuse given the lengths
 * of the other two sides of the triangle.
 *
 * @param a Length of one side of the right-angled triangle.
 * @param b Length of the other side of the right-angled triangle.
 * @return The length of the hypotenuse as a double.
 */
double hypotenuse(int a, int b)
{
    double c;

    c = sqrt(pow((double)a, 2) + pow((double)b, 2));
    return c;
}