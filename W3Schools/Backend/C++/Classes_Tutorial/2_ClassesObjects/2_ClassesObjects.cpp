
// C++: W3Schools - Classes Tutorial
// Section 2: Classes/Objects

#include <iostream>
using namespace std;

// BASICS
class MyClass {             // The class
  public:                   // Access specifier
    int myNum;              // Attribute (int variable)
    string myString;        // Attribute (string variable)
};

int main() {
  MyClass myObj;  // Create an object of MyClass

  // Access attributes and set values
  myObj.myNum = 15; 
  myObj.myString = "Some text";

  // Print attribute values
  cout << "1. " << myObj.myNum << '\n';
  cout << "2. " << myObj.myString << '\n';
  return 0;
}
