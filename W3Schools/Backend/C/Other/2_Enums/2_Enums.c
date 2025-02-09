
// C: W3Schools - Other Topics Tutorial
// Section 2: Enums

#include <stdio.h>

// An enum is a group of constants:
enum Level1 {
  LOW1,
  MEDIUM1,
  HIGH1
};

// We can assign values like so:
enum Level2 {
  LOW2 = 25,
  MEDIUM2 = 50,
  HIGH2 = 75
};

// If we set one value, the others will also change:
enum Level3 {
  LOW3 = 5,
  MEDIUM3, // Now 6
  HIGH3 // Now 7
};

int main() {
  enum Level1 myVar = MEDIUM1;
  printf("%d", myVar);

  return 0;
}
