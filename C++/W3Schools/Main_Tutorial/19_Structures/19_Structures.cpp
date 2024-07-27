
// C++: W3Schools - Main Tutorial
// Section 19: Structures

#include <iostream>
using namespace std;

int main() {

  // BASICS
  // Structures are custom containers of attributes.
  // Here we create a structure variable called myStructure:
  struct {
    int myNum;
    string myString;
  } myStructure;

  // We assign values to members of myStructure like usual.
  myStructure.myNum = 1;
  myStructure.myString = "Hello World!";

  cout << "1. " << myStructure.myNum << "\n";
  cout << "2. " << myStructure.myString << "\n";

  // We can also initialize multiple structures at once:
  struct {
    string brand;
    string model;
    int year;
  } myCar1, myCar2;

  return 0;
}
