
// C: W3Schools - Other Topics Tutorial
// Section 3: Memory

#include <stdio.h>
#include <stdlib.h> // Include for dynamic memory allocation

int main() {
  // Each datatype takes up a different size in memory:
  int myInt;
  float myFloat;
  double myDouble;
  char myChar;

  printf("%lu\n", sizeof(myInt));      // 4 bytes
  printf("%lu\n", sizeof(myFloat));    // 4 bytes
  printf("%lu\n", sizeof(myDouble));   // 8 bytes
  printf("%lu\n", sizeof(myChar));     // 1 byte

  // There are two types of memory in C, static and dynamic.
  // Static memory is reserved for variables before the program runs (compile time):
  int students[20];
  printf("%lu", sizeof(students));

  // Dynamic memory is allocated after a program starts running (runtime) and can only be accessed by pointers:
  // Allocate memory to a single value with a specified size using malloc():
  int *ptr1 = malloc(4);

  // Allocate memory to multiple values (specified number) with a specified size using calloc():
  int *ptr2 = calloc(10, 2);

  // Dynamic memory has no datatype as it is just a sequence of bytes, but we can interpret a type:
  int *ptr3 = malloc(4);
  char *ptr4 = (char*) ptr3;
  ptr3[0] = 1684234849;
  printf("%d is %c %c %c %c", *ptr3, ptr4[0], ptr4[1], ptr4[2], ptr4[3]);

  // The realloc() function tries to resize the memory at ptr1 and return the same memory address. 
  // If it cannot resize the memory at the current address then it will allocate memory at a different address and return the new address instead.
  int *ptr5 = realloc(ptr1, 6);

  // NOTE: The realloc() function returns a NULL pointer if it is not able to allocate more memory so make sure to check for NULL.

  // Free allocated memory using free():
  free(ptr1);

  // A memory leak is when allocated memory is not freed, which slows the system down.

  return 0;
}
