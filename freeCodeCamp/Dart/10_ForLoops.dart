
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 10: For Loops

main() {
  // Standard for loop:
  for (var i = 0; i < 5; i++) {
    print(i);
  }

  // For-in loop:
  var numbers = [50, 7, 16];
  for (var n in numbers) {
    print(n);
  }

  // For-each loop:
  numbers.forEach((n) => print(n));
}
