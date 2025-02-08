
// C: W3Schools - Main Tutorial
// Section 11: Booleans

// Include the stdbool.h header file to use the bool data type.
#include <stdbool.h> 
#include <stdio.h>

// The bool data type is used to store only two possible values: true or false.
int main() {
    bool isHamburgerTasty = true;     // true (1)
    bool isPizzaTasty = false;        // false (0)

    // Perform comparisons on booleans:
    printf("%d", isHamburgerTasty == isPizzaTasty);

    return 0;
}
