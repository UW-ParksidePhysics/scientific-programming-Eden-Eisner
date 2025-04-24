#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/**
 * @brief This function calculates the hypotenuse of a right triangle
 *        given the lengths of the other two sides, a and b, using
 *        the Pythagorean theorem.
 *
 * @param a The length of one side of the triangle.
 * @param b The length of the other side of the triangle.
 *
 * @return The length of the hypotenuse.
 *
 * Modified by Eden, 2025-04-24
 */
double hypotenuse(int a, int b);

int main(int argc, char* argv[])
{
    int a, b, maximum_c;
    double c;

    double epsilon = 1e-3;
    if (argc == 1) {
       maximum_c = 50;
    } else {
       maximum_c = atoi(argv[1]);
    }

    for (a = 1; a < maximum_c; a++) {
        for (b = a; b < maximum_c; b++) {
            c = hypotenuse(a, b);
            if ( (c <= (double)(maximum_c) ) &&
                 (c - floor(c) < epsilon ) ) {
               printf("%4d%4d%4d\n", a, b, (int)c);
            }
        }
    }
    return 0;
}
