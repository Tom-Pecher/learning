
// C: W3Schools - Main Tutorial
// Section 7: Data Types

 #include <stdio.h>

int main() {
  // Create variables
  int myNum1 = 5;             // Integer (whole number)
  float myFloatNum1 = 5.99;   // Floating point number
  char myLetter = 'D';       // Character

  // Print variables
  printf("%d\n", myNum1);
  printf("%f\n", myFloatNum1);
  printf("%c\n", myLetter);

  // Characters are individual letters, numbers, or symbols enclosed by single quotes:
  char myGrade = 'A';
  printf("%c", myGrade); 

  // You can also use ASCII values to display certain characters:
  char a = 65, b = 66, c = 67;
  printf("%c", a);
  printf("%c", b);
  printf("%c", c);

  // Multiple characters can be stored in a char array:
  char myText[] = "Hello";
  printf("%s", myText);

  // Numeric data types include integers:
  int myNum2 = 1000;
  printf("%d", myNum2);

  // Floating point numbers:
  float myFloatNum2 = 5.75;
  printf("%f", myFloatNum2);

  // Double precision floating point:
  double myDoubleNum = 19.99;
  printf("%lf", myDoubleNum);

  // Scientific numbers:
  float f1 = 35e3;
  double d1 = 12E4;
  printf("%f\n", f1);
  printf("%f\n", d1);

  // We 
  float myFloatNum = 3.5;

  printf("%f\n", myFloatNum);
  printf("%.1f\n", myFloatNum);
  printf("%.2f\n", myFloatNum);
  printf("%.4f", myFloatNum);

  // int 	2 or 4 bytes
  // float 	4 bytes
  // double 	8 bytes
  // char 	1 byte

  int myInt;
  float myFloat2;
  double myDouble;
  char myChar;

  printf("%lu\n", sizeof(myInt));
  printf("%lu\n", sizeof(myFloat2));
  printf("%lu\n", sizeof(myDouble));
  printf("%lu\n", sizeof(myChar));

  // Automatic conversion: int to float
  float myFloat3 = 9;
  printf("%f", myFloat3); 

  // Manual conversion: int to float
  float sum = (float) 5 / 2;
  printf("%f", sum);

  return 0;
}
