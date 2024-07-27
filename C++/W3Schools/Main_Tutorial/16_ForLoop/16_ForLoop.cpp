
// C++: W3Schools - Main Tutorial
// Section 16: For Loop

#include <iostream>
using namespace std;

int main() {

  // BASICS
  for (int i = 0; i < 5; i++) {                   // In a for loop, we define a variable over which we iterate.
    cout << "1. " << i << "\n";
  }

  for (int i = 0; i <= 10; i = i + 2) {           // We can define more complicated increments like so.
    cout << "2. " << i << "\n";
  }


  // NESTED LOOPS
  for (int i = 1; i <= 2; ++i) {                  // We can also nest for loops.
    cout << "3. " << "Outer: " << i << "\n";

    for (int j = 1; j <= 3; ++j) {
      cout << "4. " <<  " Inner: " << j << "\n";
    }
  }


  // FOR EACH
  int myNumbers[5] = {10, 20, 30, 40, 50};        // If we wish to iterate over a list of numbers, we can use a for each loop.
  for (int i : myNumbers) {
    cout << "5. " << i << "\n";
  }

  return 0;
}
