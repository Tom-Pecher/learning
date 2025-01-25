
// C: W3Schools - Main Tutorial
// Section 15: Continue

#include <stdio.h>

int main() {

    int i;

    // The continue statement allows us to skip one iteration of the loop:
    for (i = 0; i < 10; i++) {
        if (i == 4) {
            continue;
        }
        printf("%d\n", i);
    } 

    return 0;
}
