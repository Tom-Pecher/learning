
// C: W3Schools - Main Tutorial
// Section 13: While Loop

#include <stdio.h>

int main() {

    int i = 0;

    // The while loop loops through a block of code as long as a specified condition is true:
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }

    i = 0;

    // Similarly, a do-while loop executes the code block once before evaluating the condition:
    do {
        printf("%d\n", i);
        i++;
    } while (i < 5);

    return 0;
}
