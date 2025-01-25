
// C: W3Schools - Main Tutorial
// Section 12: Switch

#include <stdio.h>

int main() {
    int day = 4;

    // The switch statement is used to perform different actions based on different conditions:
    switch (day) {
        case 6:
            printf("Today is Saturday");
            break;  // The break keyword is used to break out of the switch block:
        case 7:
            printf("Today is Sunday");
            break;
        // The default keyword specifies some code to run if there is no case match:
        default:
            printf("Looking forward to the Weekend");
    }

    return 0;
}
