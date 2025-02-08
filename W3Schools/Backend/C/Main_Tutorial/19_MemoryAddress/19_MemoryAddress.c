
// C: W3Schools - Main Tutorial
// Section 19: Memory Address

#include <stdio.h>

int main() {

    // By using the & operator, we can get the memory address of a variable:
    int myAge = 43;
    printf("%p", &myAge);

    return 0;
}
