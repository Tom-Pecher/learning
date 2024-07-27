
// C++: W3Schools - Main Tutorial
// Section 5: Recursion

#include <iostream>
using namespace std;

// BASICS
// Functions can call other functions. Recursion is when a function calls itself:
int sum(int k) {
  if (k > 0) {
    return k + sum(k - 1);
  } else {
    return 0;
  }
}

int main() {
  int result = sum(10);
  cout << "1. " << result << '\n';
  return 0;
}
