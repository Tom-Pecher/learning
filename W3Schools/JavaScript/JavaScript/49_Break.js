
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 49: Break


// The break statement "jumps out" of a loop:
const cars = ["BMW", "Volvo", "Saab", "Ford"];
list: {
  text += cars[0] + "<br>";
  text += cars[1] + "<br>";
  break list;
  text += cars[2] + "<br>";
  text += cars[3] + "<br>";
}

// The continue statement "jumps over" one iteration in the loop:
for (let i = 0; i < 10; i++) {
  if (i === 3) { continue; }
  text += "The number is " + i + "<br>";
}
