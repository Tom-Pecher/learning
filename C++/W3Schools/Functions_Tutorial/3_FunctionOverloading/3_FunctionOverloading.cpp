
// C++: W3Schools - Main Tutorial
// Section 3: Functions Overloading

#include <iostream>
using namespace std;

// BASICS
// We can define multiple functions with the same name but taking different parameters:
int add5(int x) {
  return x + 5;
}

double add5(double x) {
  return x + 5;
}

int main() {
  cout << "1. " << add5(10) << '\n';
  cout << "2. " << add5(10.1) << '\n';
  return 0;
}
