
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 4: Types

main() {
  // In a strongly typed language, a variable's type is known at compile time (you have to declare it explicitly).
  // In Dart, the following are the basic types:
  int age = 30;
  double pi = 3.14;
  String name = 'James';
  bool isTrue = true;

  // To infer a variable's type at compile time, we can use the keyword 'var':
  var variable = 'This is a variable';

  // In a dynamically typed language, a variable's type is known at runtime (its type is inferred).
  // For this, we can use the keyword 'dynamic':
  dynamic dynamicVar = 'This is a dynamic variable';

  print(age);
  print(pi);
  print(name);
  print(isTrue);
  print(variable);
  print(dynamicVar);
}
