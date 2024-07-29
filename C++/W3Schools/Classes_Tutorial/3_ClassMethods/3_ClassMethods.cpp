
// C++: W3Schools - Classes Tutorial
// Section 3: Class Methods

#include <iostream>
using namespace std;

// BASICS
// Class methods are methods that belong to a class (and can only be called by that class or its instances):
// Class methods can be defined inside the class definition:
class MyClass1 {
  public:
    void myMethod() {       // Method/function defined inside the class
      cout << "1. " << "Hello World!" << '\n';
    }
};

// However, the definition can be moved outside of the class so long as it is declared within:
class MyClass2 {
  public:
    void myMethod();        // Method/function declaration
};

void MyClass2::myMethod() { // Method/function definition outside the class
  cout << "2. " << "Goodbye World!" << '\n';
}

int main() {
  MyClass1 myObj1;          // Create an object of MyClass
  myObj1.myMethod();        // Call the method
  MyClass2 myObj2;
  myObj2.myMethod();
  return 0;
}
