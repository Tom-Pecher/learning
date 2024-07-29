
// C++: W3Schools - Classes Tutorial
// Section 5: Access Specifiers

#include <iostream>
using namespace std;

// BASICS
// Access specifiers determine what attributes of an object may be accessed from outside the class:
class MyClass {
  public:
    int w;   // Public attribute
  protected:
    int x;   // Protected attribute
  private:
    int y;   // Private attribute
  int z;
};

int main() {
  MyClass myObj;
  myObj.w = 25;  // Allowed (public)
  //myObj.x = 50;   Not allowed (protected)
  //myObj.y = 75;   Not allowed (private)
  //myObj.z = 100;  Not allowed (all attibutes are private by default)
  return 0;
}
