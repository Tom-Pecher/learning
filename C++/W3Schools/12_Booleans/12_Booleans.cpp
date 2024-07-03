
// C++: W3Schools - Main Tutorial
// Section 12: Booleans

#include <iostream>
using namespace std;

int main() {

  // BASICS
  bool isCodingFun = true;                              // Booleans are true/false values.
  bool isFishTasty = false;                             // They are stored as integers (true is 1, false is 0).
  cout << "1. " << isCodingFun << endl;
  cout << "2. " << isFishTasty << endl;
  

  // EXPRESSIONS
  int myAge = 25;
  int votingAge = 18;

  if (myAge >= votingAge) {                             // We can use comparison operators to construct boolean expressions.
    cout << "3. " << "Old enough to vote!" << endl;
  } else {
    cout << "4. " << "Not old enough to vote." << endl;
  }

  return 0;
}
