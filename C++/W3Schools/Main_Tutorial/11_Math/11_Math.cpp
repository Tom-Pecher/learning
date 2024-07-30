
// C++: W3Schools - Main Tutorial
// Section 11: Math

#include <cmath>
#include <iostream>
using namespace std;

int main() {

  // BASICS
  cout << "1. " << max(5, 10) << endl;      // max(x, y) returns the greatest value out of x and y.
  cout << "2. " << min(5, 10) << endl;      // min(x, y) returns the smallest value out of x and y.

  // CMATH
  cout << "3. " << sqrt(64) << endl;        // sqrt(x) returns the square root of x.
  cout << "4. " << round(2.6) << endl;      // round(x) rounds x to the nearest integer.
  cout << "5. " << log(2) << endl;          // log(x) takes the natural logarithm of x.

  // RANDOM
  cout << "6. " << rand() << endl;          // returns a random positive integers.

  return 0;
}
