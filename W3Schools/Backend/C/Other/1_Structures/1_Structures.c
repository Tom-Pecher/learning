
// C: W3Schools - Other Topics Tutorial
// Section 1: Structures

#include <stdio.h>
#include <string.h>

// A structure is a user-defined data type in C that allows you to store multiple items in a single variable:
struct myStructure {
  int myNum;
  char myLetter;
  char myString[30];
};

int main() {
  // Create a structure variable:
  struct myStructure s1;

  // Assign values to the members of the structure:
  s1.myNum = 15;
  s1.myLetter = 'A';

  // Assign a value to the string using the strcpy function:
  strcpy(s1.myString, "Some text"); // You cannot assign a value to a string directly using the assignment operator

  // Print the value
  printf("My string: %s", s1.myString);

  // You can also assign structure variables in shorthand:
  struct myStructure s2 = {13, 'B', "Some text"};

  // We can also copy a structure variable to another structure variable:
  struct myStructure s3;
  s3 = s2;

  // We can also modify values as one would expect:
  s1.myNum = 30;
  s1.myLetter = 'C';

  return 0;
}