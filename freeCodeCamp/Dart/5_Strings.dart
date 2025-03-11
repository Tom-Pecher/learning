
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 5: Strings

main() {
  // We can represent strings of characters using single or double quotes
  String singleQuote = 'Hello, World!';
  String doubleQuote = "Hello, World!";
  print(singleQuote);
  print(doubleQuote);

  // To include special characters, we can use the backslash:
  String specialCharacters = 'Hello, \'World\'!';
  print(specialCharacters);

  // However, if we do not with to evaluate escape characters, we can create a raw string with r:
  String rawString = r'Hello, \nWorld!';
  print(rawString);

  // We can parse strings to integers and doubles:
  String a = '30';
  String b = '3.14';
  int aInt = int.parse(a);
  double bDouble = double.parse(b);
  print(aInt);
  print(bDouble);

  // Convert integers and doubles to strings:
  int c = 30;
  double d = 3.14159;
  String cString = c.toString();
  String dString = d.toStringAsFixed(3); // 3 decimal places
  print(cString);
  print(dString);
}
