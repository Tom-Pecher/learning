
// C Mini Tutorial
// Section 1: Pointers

#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;
    printf("Value of a: %d\n"       , a     );  // 10
    printf("Address of a: %p\n"     , &a    );  // memory address
    printf("Value of p: %p\n"       , p     );  // memory address
    printf("Address of p: %p\n"     , &p    );  // memory address of memory address
    printf("Value of *p: %d\n"      , *p    );  // 10
    return 0;
}