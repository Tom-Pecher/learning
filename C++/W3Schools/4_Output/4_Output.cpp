
// C++: W3Schools - Main Tutorial
// Section 4: Output

#include <iostream>
using namespace std;

int main() {

  // PRINTING TEXT
  cout << "1. " << "Hello World!";                               // As covered previously, we insert our string into the cout object to print to the console.
  cout << "2. " << " " << "I am learning C++!";                  // We can chain as many output objects as we like.

  // NEW LINES
  cout << "3. " << endl << "This is a new line.";                // To create a new line, we can use the endl manipulator.
  cout << "4. " << "\nThis is another new line." << "\n";        // Or we can use the \n escape sequence.
  cout << "5. " << "Backslash (\\), DoubleQuote (\")" << "\n";   // Other escape sequences include \\ (insert backslash) and \" (insert doublequote).

  return 0;
}
