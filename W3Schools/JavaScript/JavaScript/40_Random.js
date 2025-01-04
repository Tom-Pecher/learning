
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 40: Random

// Math.random() returns a random number between 0 (inclusive),  and 1 (exclusive):
Math.random()

// We must use Math functions to obtain our desired range (e.g. random integer from 1 to 100):
Math.floor(Math.random() * 100) + 1;

// It is often worth creating a function to generate random numbers:
function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
}
