
// C++: W3Schools - Main Tutorial
// Section 2: Functions Parameters

#include <iostream>
using namespace std;

// PASS-BY-VALUE
// We can pass parameters of certain types to the function to be used in the code block:
void myFunction1(string x) {
  cout << "1. " << "Printing: " << x << '\n';
}

// We can set default parameter values like so:
void myFunction2(string x = "Cabbage") {
  cout << "2. " << "Printing: " << x << '\n';
}

// Functions can return values using the return keyword so long as it matches the function's return type:
int myFunction3(int i) {
  return i * 2;
}

int myFunction4(int myNumbers[5]) {
  int sum = 0;
  for (int i = 0; i < 5; i++) {
    sum += myNumbers[i];
  }
  return sum;
}


// PASS-BY-REFERENCE
// If we wish to modify the parameters we enter, it is better to instead pass their memory address:
void increment(int &x) {
  x++;
}


int main() {
  myFunction1("Potato");
  myFunction2();
  cout << "3. " << myFunction3(2) << '\n';

  int x = 5;
  increment(x);
  cout << "4. " << x << '\n';

  int nums[5] = {5, 10, 15, 10, 5};
  cout << "5. " << myFunction4(nums) << '\n';

  return 0;
}
