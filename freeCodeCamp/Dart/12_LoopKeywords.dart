
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 12: Loop Keywords

main() {
  // Break exits the loop:
  for (var i = 0; i < 5; i++) {
    if (i == 3) {
      break;
    }
    print(i);
  }

  // Continue skips the current iteration:
  for (var i = 0; i < 5; i++) {
    if (i == 3) {
      continue;
    }
    print(i);
  }
}
