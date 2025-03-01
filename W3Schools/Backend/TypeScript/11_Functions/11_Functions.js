// TypeScript: W3Schools - Main Tutorial
// Section 11: Functions
// TypeScript has a specific syntax for typing function parameters and return values.
// The type of the value returned by the function can be explicitly defined:
function getTime() {
    return new Date().getTime();
}
// The void type can be used to indicate that a function does not return a value:
function printHello() {
    console.log('Hello!');
}
// Parameters can be typed with the same syntax as variables:
function multiply(a, b) {
    return a * b;
}
// Optional parameters can be defined by adding a question mark after the parameter name:
function add1(a, b, c) {
    return a + b + (c || 0);
}
// Default values can be assigned to parameters by using the = operator:
function pow(value, exponent) {
    if (exponent === void 0) { exponent = 10; }
    return Math.pow(value, exponent);
}
// Named parameters can be used to make the function call more readable:
function divide(_a) {
    var dividend = _a.dividend, divisor = _a.divisor;
    return dividend / divisor;
}
// Rest parameters can be typed like normal parameters, but the type must be an array as rest parameters are always arrays:
function add2(a, b) {
    var rest = [];
    for (var _i = 2; _i < arguments.length; _i++) {
        rest[_i - 2] = arguments[_i];
    }
    return a + b + rest.reduce(function (p, c) { return p + c; }, 0);
}
var negateFunction = function (value) { return value * -1; };
