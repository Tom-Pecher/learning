
// C Mini Tutorial
// Section 1.3: Void Pointers

#include <stdio.h>

int main() {
    int num = 5;
    float fnum = 3.14;
    void *vptr; // Point with no type

    // Since the void pointer has no type, we can cast it to any type:
    vptr = &num;
    printf("Value of num = %d\n", *(int *)vptr);

    vptr = &fnum;
    printf("Value of fnum = %f\n", *(float *)vptr);

    // Note that void pointers cannot be dereferenced directly.
}