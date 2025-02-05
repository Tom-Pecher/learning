
// C: W3Schools - Main Tutorial
// Section 20: Pointers

#include <stdio.h>

int main() {

    // A pointer is a variable that stores the memory address (specified with the asterisk *):
    int myAge = 43;
    int* ptr1 = &myAge;

    // Reference: Output the memory address of myAge with the pointer (0x7ffe5367e044)
    printf("%p\n", ptr1);

    // Dereference: Output the value of myAge with the pointer (43)
    printf("%d\n", *ptr1);

    int myNumbers[4] = {25, 50, 75, 100};

    // The pointer to an array will point to the first element of the array:
    printf("%p\n", &myNumbers);

    // Using this, we can access the elements of the array using the pointer:
    int *ptr2 = myNumbers;
    int i;

    for (i = 0; i < 4; i++) {
    printf("%d\n", *(ptr2 + i));
    }

    return 0;
}
