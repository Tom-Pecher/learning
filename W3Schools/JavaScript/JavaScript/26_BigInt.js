
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 26: BigInt


// JavaScript integers are only accurate up to 15 digits.
// To create a BigInt, append n to the end of an integer or call BigInt():
let x = 9999999999999999;
let y = 9999999999999999n;
let z = BigInt(1234567890123456789012345)

// BigInt can also be written in hexadecimal, octal, or binary notation:
let hex = 0x20000000000003n;
let oct = 0o400000000000000003n;
let bin = 0b100000000000000000000000000000000000000000000000000011n;

// The maximum safe integer in JavaScript is 2^53 - 1.:
let a = Number.MAX_SAFE_INTEGER;
let b = Number.MIN_SAFE_INTEGER;

// The integer isSafeInteger() method returns true if an integer is a safe integer, otherwise false.
Number.isInteger(10);
Number.isSafeInteger(10);
