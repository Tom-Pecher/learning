
// C: W3Schools - Main Tutorial
// Section 16: Arrays

#include <stdio.h>

// Arrays are used to store multiple values in a single collection, instead of declaring separate variables for each value.
int main() {

    // BASICS
    // We declare an array with the datatype of the elements followed by square brackets and the name of the array:
    int myNumbers[] = {25, 50, 75, 100};

    // We can access the elements of the array using the index number:
    printf("%d\n", myNumbers[0]);

    // ARRAY SIZE
    // The sizeof() function returns the size of the whole array in bytes:
    printf("%lu\n", sizeof(myNumbers));

    // To get the length of the array, we must divide this by the size of one element:
    int length = sizeof(myNumbers) / sizeof(myNumbers[0]);

    // We can then use this to iterate through the array:
    int i;
    for (i = 0; i < length; i++) {
    printf("%d\n", myNumbers[i]);
    }

    // NESTED ARRAYS
    // Arrays can also be nested:
    int matrix[2][3] = {{1, 4, 2}, {3, 6, 8}};

    return 0;
}
