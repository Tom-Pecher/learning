
// C++: W3Schools - Classes Tutorial
// Section 10: Exceptions

#include <iostream>
using namespace std;

// BASICS
int main() {
  try {
    int age = 15;
    if (age >= 18) {
      cout << "1. " << "Access granted - you are old enough." << '\n';
    } else {
      throw (age);
    }
  }
  catch (int myNum) {
    cout << "2. " << "Access denied - You must be at least 18 years old." << '\n';
    cout << "3. " << "Age is: " << myNum << '\n';
  }

  try {
    int age = 15;
    if (age >= 18) {
      cout << "4. " << "Access granted - you are old enough.";
    } else {
      throw 505;
    }
  }
  catch (...) { // NOTE: if one does not know the throw type, we may use an an ellipsis:
    cout << "5. " << "Access denied - You must be at least 18 years old." << '\n';
  }
  return 0;
}
