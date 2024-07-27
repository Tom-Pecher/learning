
// C++: W3Schools - Main Tutorial
// Section 10: Strings

#include <iostream>
#include <string>
using namespace std;

int main() {

  // INTRODUCTION
  string greeting = "Hello";                        // Strings are arrays of characters.
  cout << "1. " << greeting << endl;


  // CONCATENATION
  string firstName = "John";
  string lastName = "Doe";
  string fullName = firstName + ' ' + lastName;     // The + operator can be used to join strings together.
  cout << "2. " << fullName << endl;


  fullName = firstName.append(' ' + lastName);      // The append operator can be used for the same thing.
  cout << "3. " << fullName << endl;


  // LENGTH
  string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  cout << "4. " << "The length of the txt string is: " << txt.length() << endl;   // We can find the number of characters in a string using string.length()
  cout << "5. " << "The length of the txt string is: " << txt.size() << endl;     // Or string.size()


  // ACCESS
  string myString = "Hello";
  cout << "6. " << myString[0] << endl;                                           // We can index strings using squared bracket notation
  cout << "7. " << myString[myString.length()-1] << endl;

  myString[1] = 'j';                                                              // We can also reassign characters.
  cout << "8. " << myString << endl;

  myString.at(2) = 'k';                                                           // The square bracket notation is shorthand for the string.at(int) function.
  cout << "9. " << myString << endl;


  // ESCAPE CHARACTERS
      //    \' 	  ' 	  Single quote
      //    \" 	  " 	  Double quote
      //    \\ 	  \ 	  Backslash
      //    \n 	        New Line 	
      //    \t 	        Tab

  
  // USER INPUT
  string firstName2;                                               // As discussed previously, we can take a user input like so, even strings.
  cout << "10. " << "Type your first name: " << endl;
  cin >> firstName2;
  cout << "11. " << "Your name is: " << firstName2 << endl;        // However this will only take the first word (it terminates at the whitespace).

  string f;
  cout << "12. " << "Type your full name: " << endl;
  getline (cin, f);                                                // To take the full line, we can use getline() to take each of the words.
  cout << "13. " << "Your name is: " << f << endl;


  // C-TYPE STRINGS
  string greeting1 = "Hello";
  char greeting2[] = "Hello";                                      // Whilst strings are now their own datatype, C++ still supports C-style strings.

  return 0;
}
