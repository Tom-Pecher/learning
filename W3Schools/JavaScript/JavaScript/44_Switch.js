
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 44: Switch


// Switch Statements:
switch (new Date().getDay()) {
  case 1:
    day = "Monday";
    break;
  case 2:   // Reuse code for case 2 and 3
  case 3:
    day = "Wednesday";
    break;
  case 4:
    day = "Thursday";
    break;
  case 5:
    day = "Friday";
    break;
  default:  // default case
    day = "Weekend";
}
