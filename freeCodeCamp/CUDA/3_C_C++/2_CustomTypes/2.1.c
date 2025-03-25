
// C Mini Tutorial
// Section 2.1: Size_T

#include <stdio.h>

int main() {
    int arr1[] = {1, 2, 3, 4, 5};

    // The size_t data type is used to store the size of a variable in bytes:
    size_t size = sizeof(arr1) / sizeof(arr1[0]);
    printf("Size of array: %zu\n", size);
    printf("Size of size_t: %zu\n", sizeof(size_t)); // Long unsigned integer
    printf("Size of int: %zu\n", sizeof(int));
}
