
// C++: W3Schools - Main Tutorial
// Section 15: While

#include <iostream>
using namespace std;

int main() {

  // BASICS
  int i = 0;
  while (i < 5) {                     // While loops execute their code so long as their condition is true.
    cout << "1." << i << "\n";
    i++;
  }
  

  // DO-WHILE
  int j = 0;
  do {                                // Do-while loops instead complete an iteration and then check to see if their condition is still true.
    cout << "2." << j << "\n";
    j++;
  }
  while (j < 5);

  return 0;
}
