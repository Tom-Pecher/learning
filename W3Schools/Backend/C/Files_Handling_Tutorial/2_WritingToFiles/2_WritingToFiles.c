
// C: W3Schools - File Handling Tutorial
// Section 2: Writing to Files

#include <stdio.h>

int main() {
  FILE *fptr;
  fptr = fopen("example.txt", "w"); // By default, "write" mode overwrites the file contents (if any exist)

  // Use fprintf() to write to a file:
  fprintf(fptr, "Some text");

  fclose(fptr);

  // If we instead want to append to a file, we can use "a" mode:
  fptr = fopen("example.txt", "a");
  fprintf(fptr, "\nHi everybody!");
  fclose(fptr); 

  return 0;
}
