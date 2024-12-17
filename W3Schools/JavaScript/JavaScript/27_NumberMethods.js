
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 27: Number Methods


// The toString() method returns a number as a string:
let x = 9.656;
x.toString();

// The toExponential() method returns a string, with a number rounded and written using exponential notation:
x.toExponential(2);

// The toFixed() method returns a string, with a number written with a specified number of decimals:
x.toFixed(2);

// The toPrecision() method returns a string, with a number written with a specified length:
x.toPrecision(4);

// The Number() method can be used to convert JavaScript variables to numbers:
Number(" 10  ");

// The parseInt() method can also be used to convert strings to numbers:
parseInt("10");

// As does parseFloat():
parseFloat("10");

// The Number.isInteger() method returns true if the argument is an integer:
Number.isInteger(10);

// The Number.isSafeInteger() method returns true if the argument is a safe integer:
Number.isSafeInteger(10);
