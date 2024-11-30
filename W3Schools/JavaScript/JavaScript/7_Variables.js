
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 7: Variables

// Variables can be declared in 4 ways:
x = 5;         // Implicitly
var x = 5;     // Using var (deprecated)
let x = 5;     // Using let
const x = 5;   // Using const

// The var keyword was used in all JavaScript code from 1995 to 2015.
// The let and const keywords were added to JavaScript in 2015.
// The var keyword should only be used in code written for older browsers.

// We can declare variables without assignment, during which they will have the undefined value.
let carName1;

// Redeclaring a var will not change its value (will not work with let or const):
var carName2 = "Volvo";
var carName2;

// Mathematically, the following statement will evaluate to 10:
let x1 = 5 + 2 + 3;

// Adding strings will concatenate them:
let x2 = "John" + " " + "Doe";

// Adding a number and a string will treat the numbers as strings and concatenate them:
let x = "5" + 2 + 3;

// Underscores are used to denote private variables in JavaScript:
let _lastName = "Johnson";
let _x = 2;
let _100 = 5;
