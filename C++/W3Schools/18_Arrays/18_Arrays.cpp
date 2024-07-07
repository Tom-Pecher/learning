
// C++: W3Schools - Main Tutorial
// Section 18: Arrays

#include <iostream>
using namespace std;

int main() {

  // BASICS
  string cars1[4];                                            // Arrays are fixed-size collections (their size is assigned by the value in the square brackets).
  string cars2[4] = {"Volvo", "BMW", "Ford", "Mazda"};        // Arrays can only contain a single data type.
  cout << "1. " << cars1[1] << "\n";                          // We can access elements of an array by their index.
  cars1[1] = "Toyota";                                        // In the same way, we can also reassign values.
  cout << "2. " << cars1[1] << "\n";
  string cars3[] = {"Volvo", "BMW", "Ford"};                  // If we leave out the array size, the compiler will infer the array size from the number of elements supplied.

  // LOOPING
  int myNumbers[5] = {10, 20, 30, 40, 50};
  for (int i = 0; i < 5; i++) {                               // We can use a for loop to iterate over the indices of an array.
    cout << "3. " << myNumbers[i] << "\n";
  }

  for (int i : myNumbers) {                                   // To loop over each element directly, we can use a for each loop.
    cout << "4. " << i << "\n";
  }

  // SIZES
  cout << "5. " << sizeof(myNumbers) << "\n";                 // The function sizeof() returns the number of bytes that the array occupies.
  cout << "6. " << sizeof(myNumbers) / sizeof(int) << "\n";   // To get the number of elements we must divide by the size of a single element.

  // MULTIDIMENSIONAL ARRAYS
  string letters[2][4] = {                                    // Arrays with more than one dimension are also supported.
    { "A", "B", "C", "D" },
    { "E", "F", "G", "H" }
  };

  return 0;
}
