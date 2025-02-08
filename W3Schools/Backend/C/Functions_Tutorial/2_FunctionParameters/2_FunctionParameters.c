
// C: W3Schools - Functions Tutorial
// Section 2: Function Parameters

#include <stdio.h>

void myFunction(char name[]) {  // We can modify our function to take in input parameters of a specified type.
  printf("Hello %s\n", name);
}

int main() {
  myFunction("Liam");
  myFunction("Jenny");
  myFunction("Anja");
  return 0;
}