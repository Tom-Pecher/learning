
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 63: Strict Mode

// Strict mode is declared by adding "use strict"; to the beginning of a script or a function:
x = 3.14;       // This will not cause an error.
myFunction();

function myFunction() {
  "use strict";
  y = 3.14;     // This will cause an error
}

// Things that are not allowed in strict mode:
//      Using a variable, without declaring it.
//      Using an object, without declaring it.
//      Deleting a variable (or object).
//      Deleting a function.
//      Duplicating a parameter name.
//      Octal numeric literals.
//      Octal escape characters are not allowed
//      Assigning a value to a read-only property.
//      Deleting an undeletable property is not allowed
//      The string "eval" cannot be used as a variable
//      The string "arguments" cannot be used as a variable
//      The with statement is not allowed
//      For security reasons, eval() is not allowed to create variables in the scope from which it was called
