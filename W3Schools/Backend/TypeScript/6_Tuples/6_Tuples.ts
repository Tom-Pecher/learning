
// TypeScript: W3Schools - Main Tutorial
// Section 6: Tuples

// A tuple is a typed array with a pre-defined length and types for each index:
let tuple1: [number, boolean, string];
tuple1 = [5, false, 'Coding God was here'];

// It is good practice to use the readonly keyword to make the tuple immutable:
const tuple2: readonly [number, boolean, string] = [5, true, 'The Real Coding God'];
