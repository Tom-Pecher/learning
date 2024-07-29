
// C++: W3Schools - Classes Tutorial
// Section 4: Constructor

#include <iostream>
using namespace std;

// BASICS
class Car {
  public:
    string model;   // Attribute
    Car(string x) { // Constructor with parameters
      model = x;
    }
};

int main() {
  // Create Car objects and call the constructor with different values
  Car carObj1("X5");

  // Print values
  cout << "1. " << carObj1.model << '\n';
  return 0;
}
