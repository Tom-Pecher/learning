
// C: W3Schools - File Handling Tutorial
// Section 3: Reading Files

#include <stdio.h>

int main() {
  FILE *fptr;

  // Open a file in read mode:
  fptr = fopen("example.txt", "r");

  // Read the content and store it inside myString using fgets():
  char myString[100];
  while(fgets(myString, 100, fptr)) { // fgets() only reads a single line
    printf("%s", myString);
  }

  fclose(fptr); 

  return 0;
}
