
// C++: W3Schools - Main Tutorial
// Section 4: Scope

#include <iostream>
using namespace std;

// BASICS
// The scope of a variable is the portion of the code from which its value may be accessed directly (not by reference):
int x = 5;

void myFunction() {
  int x = 22;
  cout << "1. " << x << '\n'; // Local x (=22)
}

int main() {
  myFunction();
  cout << "2. " << x << '\n'; // Global x (=5)
  return 0;
}
