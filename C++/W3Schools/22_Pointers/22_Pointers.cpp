
// C++: W3Schools - Main Tutorial
// Section 22: Pointers

#include <iostream>
using namespace std;

int main() {

  // BASICS
  // We refer to variables that store memory addresses as pointers:
  string food = "Pizza";
  string * ptr = &food; // Pointer variables have * before the variable name
  cout << "1. " << ptr << "\n";

  // To obtain the value of the variable at the address, we add * before the variable name:
  cout << "2. " << *ptr << "\n"; // This is called dereferencing the pointer

  return 0;
}
