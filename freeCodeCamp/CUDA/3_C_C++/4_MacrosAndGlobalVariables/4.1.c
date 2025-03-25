
// C Mini Tutorial
// Section 4.1: Type Casting

#include <stdio.h>

// EXAMPLES of Conditional Macros:
//  if
//  ifdef
//  ifndef
//  elif
//  else
//  endif

#define PI 3.14159265359
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main() {
    printf("%f\n", PI);
    printf("%d\n", MAX(5, 10));
    return 0;
}
