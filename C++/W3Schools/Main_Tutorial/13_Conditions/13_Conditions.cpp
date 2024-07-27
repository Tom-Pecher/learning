
// C++: W3Schools - Main Tutorial
// Section 13: Conditions

#include <iostream>
using namespace std;

int main() {

  // BASICS
  int time = 22;
  if (time < 10) {                                   // If statements execute their code only if their boolean expression is true.
    cout << "1. " << "Good morning." << endl;
  } else if (time < 20) {
    cout << "2. " << "Good day." << endl;            // When the boolean is not met, we then chech the else if expression.
  } else {
    cout << "3. " << "Good evening." << endl;        // When none of the boolean expressions are met, we execute the code in the else statement.
  }
  

  // SHORTHAND
  string result = (time < 18) ? "Good day." : "Good evening.";    // For less complicated conditions, we can use a ternary operator to shorten it.
  cout << "4. " << result << endl;

  return 0;
}
