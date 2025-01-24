
// C: W3Schools - Main Tutorial
// Section 6: Variables

 #include <stdio.h>

int main() {
  // Declare a variable
  int myNum;

  // Assign a value to the variable
  myNum = 15;

  // In C, you must also declare the data type of the variable when you assign and print it:
  printf("%d\n", myNum);

  // We can combine variables together, in the case of integers, we can add them together:
  int x1 = 5;
  int y1 = 6;
  int sum = x1 + y1;
  printf("%d\n", sum);

  // We can also declare multiple variables in one line:
  int x2 = 5, y2 = 6, z2 = 50;
  printf("%d\n", x2 + y2 + z2);

  // We can also assign the same value to multiple variables in one line:
  int x3, y3, z3;
  x3 = y3 = z3 = 50;
  printf("%d\n", x3 + y3 + z3); 

  return 0;
}
