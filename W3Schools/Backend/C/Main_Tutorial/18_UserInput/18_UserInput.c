
// C: W3Schools - Main Tutorial
// Section 18: User Input

#include <stdio.h>

int main() {

    // Create an int and a char variable
    int myNum;
    char myChar;

    // Ask the user to type a number and a character
    printf("Type a number and a character and press enter: \n");

    // Get and save the number and character the user types
    scanf("%d %c", &myNum, &myChar);

    // Print the number
    printf("Your number is: %d\n", myNum);

    // Print the character
    printf("Your character is: %c\n", myChar);

    return 0;
}
