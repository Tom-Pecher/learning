
// C Mini Tutorial
// Section 5: Arrays and Pointers

#include <stdio.h>

int main() {
    char arr[5] = {'a', 'b', 'c', 'd', 'e'};
    char* ptr = arr;

    for (int i = 0; i < 5; i++) {
        printf("Address: %p\n", ptr);
        printf("Value: %c\n", *ptr);
        ptr++;
    }
}