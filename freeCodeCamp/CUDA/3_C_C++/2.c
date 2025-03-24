
// C Mini Tutorial
// Section 2: Nesting Pointers

#include <stdio.h>

int main() {
    int value = 5;
    int *p1 = &value;
    int **p2 = &p1;
    int ***p3 = &p2;

    printf("Value: %d\n", value);
    printf("Value: %d\n", *p1);
    printf("Value: %d\n", **p2);
    printf("Value: %d\n", ***p3);
    return 0;
}