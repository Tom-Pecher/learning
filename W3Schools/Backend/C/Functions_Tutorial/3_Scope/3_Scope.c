
// C: W3Schools - Functions Tutorial
// Section 3: Scope

#include <stdio.h>

// The value of a variable can be accessed from anywhere within its scope (the block of code in which it is declared).

// This is a global variable.
int x = 10;

void myFunction() {
  // This is a local variable.
  int x = 5;
  printf("%d", x); // The most local version of the variable will be used, in this case 5.
}

int main() {
  myFunction();
  return 0;
}