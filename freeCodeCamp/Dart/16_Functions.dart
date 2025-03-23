
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 16: Dart

// A function is a block of reusable code that performs a specific task:
void sayHello() { // void means that the function does not return a value
  print('Hello');
}

// Functions can also take parameters:
int addNumbers(int a, int b) { // int specifies the return type of the function
  return a + b;
}

main() {
  sayHello();
  print(addNumbers(2, 3));

  // Arrow function (shorthand):
  int square(int num) => num * num;
  print(square(5));
}
