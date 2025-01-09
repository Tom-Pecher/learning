
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 62: Hoisting

// Hoisting is JavaScript's default behavior of moving declarations to the top of its current scope.
// In JavaScript, a variable can be declared after it has been used:
x = 5;
var x;

// Variables defined with let and const are hoisted to the top of the block, but not initialized.
carName = "Volvo";
// let carName;     // This will cause an error
// const carName;   // This will cause an error

// Hoisting only moves the declaration, not the initialization. The variable is initialized with undefined.
