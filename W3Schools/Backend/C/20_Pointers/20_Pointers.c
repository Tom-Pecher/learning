
// C: W3Schools - Main Tutorial
// Section 20: Pointers

#include <stdio.h>

int main() {

    // A pointer is a variable that stores the memory address (specified with the asterisk *):
    int myAge = 43;
    int* ptr = &myAge;

    // Reference: Output the memory address of myAge with the pointer (0x7ffe5367e044)
    printf("%p\n", ptr);

    // Dereference: Output the value of myAge with the pointer (43)
    printf("%d\n", *ptr);

    return 0;
}
