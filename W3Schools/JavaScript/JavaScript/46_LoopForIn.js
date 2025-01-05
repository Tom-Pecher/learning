
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 46: For Loop In


// We can loop across all of the properties in an object:
const person = {fname:"John", lname:"Doe", age:25};

let text = "";
for (let x in person) {
  text += person[x];
}
