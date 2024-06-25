
// C++: W3Schools - Main Tutorial
// Section 6: Variables

#include <iostream>
using namespace std;

int main() {
   
  // CREATING VARIABLES
  int var;                                // Declaration of the variable (allocates memory).
  var = 10;                               // Assignment of the variable (give it a value).
  cout << var;                            // Prints the variable. NOTE: the name of a variable is called the identifier.

  // VARIABLE TYPES
  int myNum = 5;                          // Integer (whole number without decimals).
  double myFloatNum = 5.99;               // Floating point number (with decimals).
  char myLetter = 'D';                    // Character (a single letter).
  string myText = "Hello";                // String (text, an array of characters).
  bool myBoolean = true;                  // Boolean (true or false).

  // MULTIPLE VARIABLES
  int a = 5, b = 6, c = 50;               // We can declare many variables at once.
  cout << a + b + c;

  int x, y, z;                            // We can also assign one value to multiple variables.
  x = y = z = 50;
  cout << x + y + z;

  // CONSTANTS
  const float PI = 3.14;                  // Constants are read-only variables whose value cannot be reassigned.
  const int minutesPerHour = 60;          // As a consequence, constants must be assigned in the same line that they are declared in.

  return 0;
}
