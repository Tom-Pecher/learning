
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 19: Exceptions


num divide(var a, var b) {
  if (b == 0) {
    throw 'Cannot divide by zero';
  }
  return a / b;
}

main() {
  // Try-catch block:
  try {          // Try the code in the try block:
    print(divide(6, 3));
    print(divide(1, 2));
    print(divide(4, 0));
  } catch (e) {  // Catch the exception thrown in the try block (if one occurs):
    print(e);
  } finally {    // Execute some code after the try-catch block:
    print('This is always executed');
  }
}
