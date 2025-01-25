
// C: W3Schools - Main Tutorial
// Section 11: Conditional Statements

#include <stdio.h>

int main() {
    int time = 22;

    // Execute different code blocks based on certain conditions:
    if (time < 10) {
        printf("Good morning.");
    } else if (time < 20) {
        printf("Good day.");
    } else {
        printf("Good evening.");
    }

    // The same code can be rewritten in shorthand using a ternary operator:
    (time < 18) ? printf("Good day.") : printf("Good evening.");

    return 0;
}
