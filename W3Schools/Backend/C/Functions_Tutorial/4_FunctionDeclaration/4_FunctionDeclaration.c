
// C: W3Schools - Functions Tutorial
// Section 4: Function Declaration

#include <stdio.h>

// For code optimization, it is recommended to separate the declaration and the definition of the function:
void myFunction();                  // Function declaration
void myFunction() {                 // Function definition
  printf("I just got executed!");
}

int main() {
  myFunction(); // call the function
  return 0;
}