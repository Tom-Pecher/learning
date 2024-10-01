
// C++: W3Schools - Main Tutorial
// Section 21: References

#include <iostream>
using namespace std;

int main() {

  // BASICS
  // Reference variables are used to refer to existing variables, achieved with & on variable the being assigned:
  string food = "Pizza";  // food variable
  string &meal = food;    // reference to food
  cout << "1. " << food << "\n";
  cout << "2. " << meal << "\n";

  // If we instead use & on the variable itself, we are given its memory address:
  cout << "3. " << &food << "\n";

  return 0;
}
