
// C: W3Schools - File Handling Tutorial
// Section 1: Create Files

#include <stdio.h>

int main() {
  // Create a variable of type FILE to store the file pointer:
  FILE *fptr;

  // Use the fopen() function to create (or edit) a file with the specified name:
  fptr = fopen("example.txt", "w");

  // Close the file using the fclose() function:
  fclose(fptr); 

  return 0;
}
