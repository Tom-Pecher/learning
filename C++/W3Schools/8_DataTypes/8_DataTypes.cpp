
// C++: W3Schools - Main Tutorial
// Section 8: Data Types

#include <iostream>
#include <string>
using namespace std;

int main() {

  // BASICS
  int myNum = 5;                        // Integer (whole number): 2-4 bytes
  float myFloatNum = 5.99;              // Floating point number: 4 bytes
  double myDoubleNum = 9.98;            // Floating point number: 8 bytes
  char myLetter = 'D';                  // Character: 1 byte
  bool myBoolean = true;                // Boolean: 1 byte
  string myText = "Hello";              // String: variable

  // NUMBERS
  float f1 = 35e3;                      // Numeric data can also be entered with scientific notation.
  double d1 = 12E4;                     // We can do this using an upper or lower case E.

  // CHARACTERS
  char a = 65, b = 66, c = 67;          // We can set characters based on their ASCII value as well.
  cout << a;
  cout << b;
  cout << c;

  // STRING
  string greeting = "Hello";            // To use string functionality, we must include the string header file.
  cout << greeting.at(0);

  return 0;
}
