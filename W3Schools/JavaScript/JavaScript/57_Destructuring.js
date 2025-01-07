
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 57: Destructuring

// The destructuring assignment syntax unpack object properties into variables:
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 50
};
  
// Destructuring
let {firstName1, lastName1} = person;

// Destructuring does not change the original object.
person.firstName = "Jane";

// For potentially missing properties we can set default values:
let {firstName2, lastName2, country = "US"} = person;

// We can also alias the variable names:
let {lastName : name1} = person;

// Destructuring can also be used with arrays:
let name2 = "W3Schools";
let [a1, a2, a3, a4, a5] = name2;

// We can skip values:
let [b1,,,,b5] = name2;

// We can also assign the rest of the array to a variable:
let [c1, ...rest] = name2;

// We can also set indices:
let {[0]:d1 ,[1]:d2} = name2;

// Destructuring a map:
const fruits = new Map([
    ["apples", 500],
    ["bananas", 300],
    ["oranges", 200]
  ]);
let text = "";
for (const [key, value] of fruits) {
    text += key + " is " + value;
}
