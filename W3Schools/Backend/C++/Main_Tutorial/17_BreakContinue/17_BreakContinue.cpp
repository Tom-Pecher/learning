
// C++: W3Schools - Main Tutorial
// Section 17: Break and Continue

#include <iostream>
using namespace std;

int main() {

  // BASICS
  int i = 0;
  while (i < 10) {
    cout << "1. " << i << "\n";
    i++;
    if (i == 4) {
      break;                            // When the break keyword is called, the execution of the the loop is halted.
    }
  }

  int j = 0;
  while (j < 10) {
    if (j == 4) {
      j++;
      continue;                         // The continue keyword skips the current loop iteration when it is called.
    }
    cout << "2. " << j << "\n";
    j++;
  }

  return 0;
}
