
// C Mini Tutorial
// Section 4: Null Pointers

#include <stdio.h>

int main() {
    int *ptr = NULL;
    printf("The value of ptr is %p\n", ptr);

    // Dereferencing a null pointer will cause a segmentation fault, check before dereferencing:
    if (ptr != NULL) {
        printf("The value of *ptr is %d\n", *ptr);
    } else {
        printf("The pointer is NULL\n");
    }
}