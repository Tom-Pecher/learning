
// C++: W3Schools - Main Tutorial
// Section 1: Functions

#include <iostream>
using namespace std;

// BASICS
// Functions are blocks of code that can be called and run anywhere in the program:
void myFunction1() { // declaration (we must declare what type the function will output)
  cout << "1. " << "I just got executed!" << '\n'; // definition
}

// If a user-defined function is declared before main, an error will be thrown.
// However, it may be defined before main:
void myFunction2();

int main() {
  myFunction1(); // call the function 
  myFunction2(); // call the function 
  return 0;
}

// Here myFunction2 doesn't throw an error since it was declared before main:
void myFunction2() {
  cout << "2. " << "I just got executed, despite being defined after main!" << '\n';
}
