
// C++: W3Schools - Classes Tutorial
// Section 7: Inheritance

#include <iostream>
using namespace std;

// BASICS
// Inheritance is where a class inherits the functionality of another:
class Vehicle { // Base (parent) class
  public:
    string brand = "Ford";
    void honk() {
      cout << "1. " << "Tuut, tuut!" <<  '\n';
    }
};

class MyOtherClass {
  public:
    void myOtherFunction() {
      cout << "2. " << "Hello World!" <<  '\n';
    }
};

class Car: public Vehicle, public MyOtherClass { // Derived (child) class
  public:
    string model = "Mustang";
};

int main() {
  Car myCar;
  myCar.honk();
  myCar.myOtherFunction();
  cout << "3. " << myCar.brand + " " + myCar.model << '\n';
  return 0;
}
