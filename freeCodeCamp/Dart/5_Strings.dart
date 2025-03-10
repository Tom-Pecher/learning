
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
}
