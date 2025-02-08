
// C: W3Schools - Functions Tutorial
// Section 5: Recursion

#include <stdio.h>

// Recursion is when a function calls itself.
int sum(int k);

int main() {
  int result = sum(10);
  printf("%d", result);
  return 0;
}

// This function calls itself to calculate the kth triangular number.
int sum(int k) {
  if (k > 0) {
    return k + sum(k - 1);
  } else {
    return 0;
  }
}