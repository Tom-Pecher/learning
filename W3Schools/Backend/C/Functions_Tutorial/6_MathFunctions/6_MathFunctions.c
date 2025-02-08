
// C: W3Schools - Functions Tutorial
// Section 6: Math Functions

#include <stdio.h>
 #include <math.h> // We can use the math.h library to perform mathematical operations.

int main() {
  // The sqrt() function returns the square root of a number:
  printf("%f\n", sqrt(16));

  // The floor and ceil functions return the largest and smallest integers, respectively, that are less than or equal to a number:
  printf("%f\n", ceil(1.4));
  printf("%f\n", floor(1.4));

  // The pow() function returns the value of the first argument raised to the power of the second argument:
  printf("%f\n", pow(2, 3));

  return 0;
}
