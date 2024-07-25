
// C++: W3Schools - Main Tutorial
// Section 20: Enums

#include <iostream>
using namespace std;

int main() {

  // BASICS
  // Enums (enumerations) are containers of constants
  enum Level1 {
    LOW1,
    MEDIUM1,
    HIGH1
  }; 

  enum Level1 myVar1 = HIGH1;              // Enums take the value of one of the constants provided.
  cout << "1. " << myVar1 << "\n";         // Printing an enum on its own will print the index position of the constant chosen.

  // However we can reassign the values:
  enum Level2 {                           
    LOW2 = 25,
    MEDIUM2 = 50,
    HIGH2 = 75
  };
  enum Level2 myVar2 = MEDIUM2;
  cout << "2. " << myVar2 << "\n";

  // Additionally, changing the first value will also shift the other two:
  enum Level3 {
    LOW3 = 5,
    MEDIUM3, // Now 6
    HIGH3 // Now 7
  };
  enum Level3 myVar3 = HIGH3;
  cout << "3. " << myVar3 << "\n";

  return 0;
}
