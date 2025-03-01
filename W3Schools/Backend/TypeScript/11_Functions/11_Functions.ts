
// TypeScript: W3Schools - Main Tutorial
// Section 11: Functions

// TypeScript has a specific syntax for typing function parameters and return values.

// The type of the value returned by the function can be explicitly defined:
function getTime(): number {
    return new Date().getTime();
}

// The void type can be used to indicate that a function does not return a value:
function printHello(): void {
    console.log('Hello!');
}

// Parameters can be typed with the same syntax as variables:
function multiply(a: number, b: number) {
    return a * b;
}

// Optional parameters can be defined by adding a question mark after the parameter name:
function add1(a: number, b: number, c?: number) {
    return a + b + (c || 0);
}

// Default values can be assigned to parameters by using the = operator:
function pow(value: number, exponent: number = 10) {
    return value ** exponent;
}

// Named parameters can be used to make the function call more readable:
function divide({ dividend, divisor }: { dividend: number, divisor: number }) {
    return dividend / divisor;
}

// Rest parameters can be typed like normal parameters, but the type must be an array as rest parameters are always arrays:
function add2(a: number, b: number, ...rest: number[]) {
    return a + b + rest.reduce((p, c) => p + c, 0);
}

// Function types can be defined using the arrow function syntax:
type Negate = (value: number) => number;
const negateFunction: Negate = (value) => value * -1;
