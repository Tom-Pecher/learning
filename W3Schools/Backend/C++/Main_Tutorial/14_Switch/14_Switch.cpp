
// C++: W3Schools - Main Tutorial
// Section 14: Switch

#include <iostream>
using namespace std;

int main() {

  // BASICS
  int day = 4;
  switch (day) {                                                    // Switch statements compare a chosen value to a set of cases and execute all those that return true.
    case 6:
      cout << "1. " << "Today is Saturday" << endl;
      break;                                                        // If we only want to execute the first true instance, we can use the break keyword to stop the execution.
    case 7:
      cout << "2. " << "Today is Sunday" << endl;
      break;
    default:                                                        // If none of the cases are true, it will execute the default case.
      cout << "3. " << "Looking forward to the weekend!" << endl;
  }

  return 0;
}
