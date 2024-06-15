
// C++: W3Schools - Main Tutorial
// Section 4: Output

#include <iostream>
using namespace std;

int main() {

  // PRINTING TEXT
  cout << "Hello World!";                               // As covered previously, we insert our string into the cout object to print to the console.
  cout << " " << "I am learning C++!";                  // We can chain as many output objects as we like.

  // NEW LINES
  cout << endl << "This is a new line.";                // To create a new line, we can use the endl manipulator.
  cout << "\nThis is another new line." << "\n";          // Or we can use the \n escape sequence.
  cout << "Backslash (\\), DoubleQuote (\")" << "\n";   // Other escape sequences include \\ (insert backslash) and \" (insert doublequote).

  return 0;
}
